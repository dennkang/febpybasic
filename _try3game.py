class Profile:
    def __init__(self, health, armour, money):
        self.health = health
        self.armour = armour
        self.money = money

    def heal(self, health_points):
        self.health += health_points
        if health_points > 100:
            self.health = 100
        print(f"You have collected a health boost!\nYour health is now {health_points}!")

    def add_armor(self, armor_points):
        self.armour += armor_points
        if armor_points > 100:
            self.armour = 100
        print(f"You have equipped armor!\nYour armour is now {armor_points}!")

    def add_money(self, amount):
        self.money += amount
        print(f"{amount} added to your account. New balance is now {self.money}")

    def spend_money(self, amount):
        if amount < self.money:

