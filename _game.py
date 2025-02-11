from abc import ABC, abstractmethod

class Profile:
    def __init__(self, health):
        self.health = health

    def heal(self, health_points):
        self.health += health_points
        if self.health > 100:
            self.health = 100
        print(f"You have healed. Your health is now {self.health}.")

    def damage(self, health_points):
        self.health -= health_points
        print(f"You have taken damage. Your health is now {self.health}.")

class Interact():
    def __init__(self, health_points):
        self.health_points = health_points

    def execute(self, profile):
        pass

class Heal_Interact(Interact):
    def execute(self, profile):
        profile.heal(self.health_points)

class Damage_Interact(Interact):
    def execute(self, profile):
        profile.damage(self.health_points)

class GameSystem(ABC):
    @abstractmethod

    def processhealth(self, health_points):
        pass

class MyGameSystem(GameSystem):
    def processhealth(self, health_points):
        print(f"Health points: {health_points}")

obj = MyGameSystem()

user1 = Profile(100)

heal = Heal_Interact(50)
damage = Damage_Interact(20)

heal.execute(user1)
damage.execute(user1)