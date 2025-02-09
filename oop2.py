# create a class called "fruits" that has the following attributes:
# 1. name
# 2. color
# 3. price

# implement a constructor method and a method function that prints:
# 1. my favorite fruit is {name}
# 2. it is {color} in color
# 3.it costs {price} shillings

# create 5 instances of that class

# start of code:

class fruits:
    # constructor method
    def __init__(self,name, color, price):
        self.name = name
        self.color = color
        self.price = price

    # method function
    def favfruit(self):
        print(f"My favorite fruit is {self.name}. \nIt is {self.color} in colour. \nTo buy one it costs {self.price} shillings.")
        print("")

# class instances
inst1 = fruits("apple", "red", 40)
inst2 = fruits("banana", "yellow", 10)
inst3 = fruits("watermelon", "green", 50)
inst4 = fruits("orange", "orange", 30)
inst5 = fruits("pear", "green", 15)

inst1.favfruit()
inst2.favfruit()
inst3.favfruit()
inst4.favfruit()
inst5.favfruit()