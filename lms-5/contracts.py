from abc import ABC, abstractmethod

# Contract for entities with personal details
class Personable(ABC):
    @abstractmethod
    def set_personal_details(self, id, name, age, email, mobile):
        """Set personal details for the entity"""
        pass
    
    @abstractmethod
    def person_complete_info(self):
        """Display complete personal information"""
        pass

# Contract for entities involved in payment calculations
class Payables(ABC):
    @abstractmethod
    def calculate_payment(self):
        """Calculate payment for the entity"""
        pass

