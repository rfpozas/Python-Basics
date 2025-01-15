class Monster: # class definition
    # next is our Constructor function, called when we instantiate an object
    # self keyword is very important, because it allows us to bind parameters to itself
    def __init__(self, name, given_age):
        self.name = name
        self.age = given_age

    def speak(self):
        return "Generic Monster Voice"

    def __str__(self): # to_string method such as in java
        return f"{self.name}, {self.age}"

class Vampire(Monster): # inheritance to create a child class
    def __init__(self, name, age, amt_blood):
        super().__init__(name, age) # calls a super constructor
        self.amt_blood = amt_blood
        # super constructor lets us superpose and add new elements

    def speak(self): # override functionality in parent class
        return "I drink blood."

monsters = [Monster("Bob", 10),
            Vampire("Edward", 10, 40)]

for m in monsters:
    print(m.speak())

c = None
print(c is None)
# is keyword is more reliable to check whether something is non-type, null-type.