numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

sum_of_even = 0
sum_of_odd = 0
sum_of_trio = 0
sum_of_quad = 0
sum_of_quin = 0
sum_of_all = 0

for enumber in numbers:
    if enumber % 2 == 0:
        sum_of_even += enumber

for onumber in numbers:
    if onumber % 2 != 0:
        sum_of_odd += onumber

for tnumber in numbers:
    if tnumber % 3 == 0:
        sum_of_trio += tnumber

for qdnumber in numbers:
    if qdnumber % 4 == 0:
        sum_of_quad += qdnumber

for qtnumber in numbers:
    if qtnumber % 5 == 0:
        sum_of_quin += qtnumber

for anumber in numbers:
    sum_of_all += anumber

print(f"The sum of even numbers is {sum_of_even}")
print(f"The sum of odd numbers is {sum_of_odd}")
print(f"The sum of threes is {sum_of_trio}")
print(f"The sum of fours is {sum_of_quad}")
print(f"The sum of fives is {sum_of_quin}")
print("")
print(f"The sum of all numbers is {sum_of_all}")