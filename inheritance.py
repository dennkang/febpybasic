class Dad:
    def football(self):
        print("J'adore Arsenal")

class Mom:
    def cooking(self):
        print("I love Spaghetti")

class Boy(Dad):
    def generation(self):
        print("I am a Gen Z")

class Girl(Mom):
    def hobby(self):
        print("I love Dancing")

my_boy = Boy()
my_girl = Girl()

my_boy.football()
my_boy.generation()
my_girl.cooking()
my_girl.hobby()