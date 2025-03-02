class Person:
    """a representation of a person
        
        Attributes: 
        given_name: (str) the given name of the person
        family_name: (str) the family name of the person
        age: (int) the age of the person
        gender: (str) lowercase fully typed gender of the person

        Example:
        person = Person("","",10,"")
    """
    def __init__(self, given_name, family_name, age, gender):
      
        self.given_name = given_name
        self.family_name = family_name
        #w/put variable it acts as scope variable
        self.age = age
        self.gender = gender
    
    def get_full_name(self):
        """gets the full name of the person"""
        return f"{self.given_name} {self.family_name}"

person1 = Person("John", "Doe", 22, "male")
person2 = Person("Jane", "Doe", 21, "female")

print(person1.get_full_name())
print(person2.get_full_name())