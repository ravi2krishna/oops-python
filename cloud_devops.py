#!/usr/bin/env python3
"""
Simple EC2 Manager CLI (boto3)
Prereqs:
 - pip install boto3
 - Configure AWS credentials (aws configure) or env vars
 - IAM permissions for EC2 actions
"""

# export AWS_ACCESS_KEY_ID="YOUR_ACCESS_KEY"
# export AWS_SECRET_ACCESS_KEY="YOUR_SECRET_KEY"
# export AWS_DEFAULT_REGION="ap-south-1"
# ami-0d9a665f802ae6227
# sg-0afa441c618b286a3

import boto3
import botocore
import sys

# Configure region here or rely on AWS_DEFAULT_REGION
DEFAULT_REGION = "us-east-2"   # change if you want (ap-south-1 = Mumbai)

# Create boto3 EC2 client & resource
session = boto3.Session(region_name=DEFAULT_REGION)
ec2_client = session.client("ec2")
ec2_resource = session.resource("ec2")


def add_instance():
    """Launch a new EC2 instance (very basic)."""
    print("\n-- Add Instance --")
    try:
        ami = input("Enter AMI id (e.g. ami-0abcdef1234567890) [required]: ").strip()
        if not ami:
            print("AMI id is required. Aborting.")
            return

        instance_type = input("Instance type (default t3.micro): ").strip() or "t3.micro"
        key_name = input("Key pair name (leave empty for none): ").strip() or None
        sg = input("Security group id (comma-separated) (leave empty for default SG): ").strip()
        sg_list = [s.strip() for s in sg.split(",") if s.strip()] if sg else None

        count_input = input("How many instances? (default 1): ").strip()
        count = int(count_input) if count_input.isdigit() and int(count_input) > 0 else 1

        name_tag = input("Name tag for instance(s) (optional): ").strip() or "ec2-server"

        print(f"\nLaunching {count} instance(s) with AMI={ami}, type={instance_type} in {DEFAULT_REGION} ...")

        run_kwargs = {
            "ImageId": ami,
            "InstanceType": instance_type,
            "MinCount": 1,
            "MaxCount": count,
        }
        if key_name:
            run_kwargs["KeyName"] = key_name
        if sg_list:
            run_kwargs["SecurityGroupIds"] = sg_list

        resp = ec2_client.run_instances(**run_kwargs)

        launched_ids = [inst["InstanceId"] for inst in resp["Instances"]]
        tag_pairs = [{"Key": "Name", "Value": name_tag}]
        ec2_client.create_tags(Resources=launched_ids, Tags=tag_pairs)

        print("Launched instances:", ", ".join(launched_ids))
        print("Note: It may take a short while until instances are in 'running' state.")
    except botocore.exceptions.ClientError as e:
        print("AWS error:", e.response.get("Error", {}).get("Message", str(e)))
    except Exception as ex:
        print("Error:", ex)


def update_instance_name():
    """Update Name tag for an instance."""
    print("\n-- Update Instance Name --")
    instance_id = input("Enter Instance ID (e.g. i-0abcd1234): ").strip()
    if not instance_id:
        print("Instance ID required.")
        return
    new_name = input("Enter new Name tag value: ").strip()
    if not new_name:
        print("New name required.")
        return
    try:
        inst = ec2_resource.Instance(instance_id)
        _ = inst.state
        ec2_client.create_tags(Resources=[instance_id], Tags=[{"Key": "Name", "Value": new_name}])
        print(f"Instance {instance_id} tagged with Name = '{new_name}'")
    except botocore.exceptions.ClientError as e:
        print("AWS error:", e.response.get("Error", {}).get("Message", str(e)))
    except Exception as ex:
        print("Error:", ex)


def delete_instance():
    """Terminate an EC2 instance by ID."""
    print("\n-- Delete (Terminate) Instance --")
    instance_id = input("Enter Instance ID to terminate: ").strip()
    if not instance_id:
        print("Instance ID required.")
        return
    confirm = input(f"Are you sure you want to terminate {instance_id}? (yes/no): ").strip().lower()
    if confirm != "yes":
        print("Termination cancelled.")
        return
    try:
        resp = ec2_client.terminate_instances(InstanceIds=[instance_id])
        print("Terminate API called. Current state transitions:")
        for inst in resp.get("TerminatingInstances", []):
            print(f"  {inst.get('InstanceId')} : {inst.get('PreviousState',{}).get('Name')} -> {inst.get('CurrentState',{}).get('Name')}")
        print("Note: Termination may take some time. Check AWS Console or use 'List Instances' to verify.")
    except botocore.exceptions.ClientError as e:
        print("AWS error:", e.response.get("Error", {}).get("Message", str(e)))
    except Exception as ex:
        print("Error:", ex)


def list_instances():
    """List EC2 instances with some useful columns."""
    print("\n-- List Instances --")
    try:
        resp = ec2_client.describe_instances(
            Filters=[{"Name": "instance-state-name", "Values": ["pending", "running", "stopping", "stopped"]}]
        )
        reservations = resp.get("Reservations", [])
        if not reservations:
            print("No instances found in this region (or none in selected states).")
            return

        print(f"{'InstanceId':20} {'State':10} {'Type':10} {'PublicIP':15} {'Name':30}")
        print("-" * 90)
        for res in reservations:
            for inst in res.get("Instances", []):
                iid = inst.get("InstanceId")
                state = inst.get("State", {}).get("Name")
                itype = inst.get("InstanceType")
                pub = inst.get("PublicIpAddress") or "-"
                tags = inst.get("Tags") or []
                name = "-"
                for t in tags:
                    if t.get("Key") == "Name":
                        name = t.get("Value")
                        break
                print(f"{iid:20} {state:10} {itype:10} {str(pub):15} {name:30}")
    except botocore.exceptions.ClientError as e:
        print("AWS error:", e.response.get("Error", {}).get("Message", str(e)))
    except Exception as ex:
        print("Error:", ex)


def start_instances():
    """Start one or more stopped instances."""
    print("\n-- Start Instances --")
    ids_input = input("Enter Instance ID(s) to start (comma-separated): ").strip()
    if not ids_input:
        print("No Instance IDs provided.")
        return
    instance_ids = [iid.strip() for iid in ids_input.split(",") if iid.strip()]
    if not instance_ids:
        print("No valid Instance IDs parsed.")
        return
    try:
        resp = ec2_client.start_instances(InstanceIds=instance_ids)
        print("StartInstances API called. State transitions:")
        for inst in resp.get("StartingInstances", []):
            print(f"  {inst.get('InstanceId')} : {inst.get('PreviousState',{}).get('Name')} -> {inst.get('CurrentState',{}).get('Name')}")
        print("Note: It may take a minute for instances to reach 'running' state.")
    except botocore.exceptions.ClientError as e:
        print("AWS error:", e.response.get("Error", {}).get("Message", str(e)))
    except Exception as ex:
        print("Error:", ex)


def stop_instances():
    """Stop one or more running instances."""
    print("\n-- Stop Instances --")
    ids_input = input("Enter Instance ID(s) to stop (comma-separated): ").strip()
    if not ids_input:
        print("No Instance IDs provided.")
        return
    instance_ids = [iid.strip() for iid in ids_input.split(",") if iid.strip()]
    if not instance_ids:
        print("No valid Instance IDs parsed.")
        return

    confirm = input(f"Are you sure you want to stop {', '.join(instance_ids)}? (yes/no): ").strip().lower()
    if confirm != "yes":
        print("Stop cancelled.")
        return

    try:
        resp = ec2_client.stop_instances(InstanceIds=instance_ids)
        print("StopInstances API called. State transitions:")
        for inst in resp.get("StoppingInstances", []):
            print(f"  {inst.get('InstanceId')} : {inst.get('PreviousState',{}).get('Name')} -> {inst.get('CurrentState',{}).get('Name')}")
        print("Note: It may take a minute for instances to reach 'stopped' state.")
    except botocore.exceptions.ClientError as e:
        print("AWS error:", e.response.get("Error", {}).get("Message", str(e)))
    except Exception as ex:
        print("Error:", ex)


def exit_system():
    print("\nExiting EC2 Manager CLI. Goodbye!")
    sys.exit(0)


def main_menu():
    while True:
        print("\nChoose an option:")
        print("1 - Add Instance")
        print("2 - Update Instance Name")
        print("3 - Delete Instance (Terminate)")
        print("4 - List Instances")
        print("5 - Start Instances")
        print("6 - Stop Instances")
        print("7 - Exit")
        choice = input("Enter Choice (1-7): ").strip()
        if choice == "1":
            add_instance()
        elif choice == "2":
            update_instance_name()
        elif choice == "3":
            delete_instance()
        elif choice == "4":
            list_instances()
        elif choice == "5":
            start_instances()
        elif choice == "6":
            stop_instances()
        elif choice == "7":
            exit_system()
        else:
            print("Invalid option. Please choose 1-7.")


if __name__ == "__main__":
    print("=" * 60)
    print("EC2 Manager CLI (Basic)".center(60))
    print("Region:", DEFAULT_REGION)
    print("Make sure AWS credentials are configured and you have EC2 permissions.")
    print("=" * 60)
    main_menu()
