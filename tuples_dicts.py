first_tuple = (1, 2, 3, 4)
second_tuple = ('A', 'b', 'r', 'a', 'k', 'a', 'd', 'a', 'b', 'r', 'a')
third_tuple = tuple("Maciej")

print("1st tuple: ", first_tuple)
print("2nd tuple: ", second_tuple)
print("3rd tuple: ", third_tuple)

tuple_1_and_2 = first_tuple + second_tuple
print("1 and 2 tuple: ", tuple_1_and_2, "Length: ", len(tuple_1_and_2))
print("4th element of 2nd tuple: ", second_tuple[3])
print("Sliced tuple 1 and 2 from 4:6: ", tuple_1_and_2[4:6])

coordinates = 4.21, 9.29
x, y = coordinates
print(f'x = {x}')
print(f'y = {y}')

name, age, occupation = "Tomek", 41, "programmer"
print(f"Name : {name}")

age2 = (22, 34, 56, 41)
if 41 in age2:
    print("Old programmer found!")

list1 = ["Ania", "Zosia", "Kasia"]
if "Ania" in list1:
    print("Ania found")

list1[0] = "Monia"
print(list1[0:1])

list1.insert(2, "Aga")
print(list1)

list1.insert(-1, "Bogus")  # insert one element before last
print(list1)

popping = list1.pop(0)  # pop element 0
print(list1)

list1.append("Jola")  # append to the end of list
print(list1)

dict1 = {'a': "1", 'b': "2"}
print(dict1)

print(dict1['a'])

dict2 = {'first': {'a': '1'}, 'second': {'b': '2'}}
print(dict2['second']['b'])

dict3 = dict()
dict3['Enterprise'] = 'Picard'
dict3['Voyager'] = 'Janeway'
dict3['Defiant'] = 'Sisko'

print(dict3)

del dict3['Enterprise']
print(dict3.items())

capitals_dict = {'Alabama': 'Montgomery',
                 'Alaska': 'Juneau',
                 'Arizona': 'Phoenix',
                 'Arkansas': 'Little Rock',
                 'California': 'Sacramento',
                 'Colorado': 'Denver',
                 'Connecticut': 'Hartford',
                 'Delaware': 'Dover',
                 'Florida': 'Tallahassee',
                 'Georgia': 'Atlanta',
                 }

for item in capitals_dict:
    print(f'Capital of {item} is {capitals_dict[item]}')

# Cat has hats
# 9.9 Challenge: Cats With Hats
# You have 100 cats.
# One day you decide to arrange all your cats in a giant circle. Initially,
# none of your cats have any hats on. You walk around the circle 100
# times, always starting at the same spot, with the first cat (cat # 1).
# Every time you stop at a cat, you either put a hat on it if it doesn’t have
# one on, or you take its hat off if it has one on.
# 1. The first round, you stop at every cat, placing a hat on each one.
# 2. The second round, you only stop at every second cat (#2, #4, #6,
# #8, etc.).
# 3. The third round, you only stop at every third cat (#3, #6, #9, #12,
# etc.).
# 4. You continue this process until you’ve made 100 rounds around
# the cats (e.g., you only visit the 100th cat).
# Write a program that simply outputs which cats have hats at the end.

cats = []
for i in range(0, 100):
    cats.append(0)

for a in range(1, 101):
    print('Round: ', a)
    for i in range(a-1, 100, a):
        if cats[i] == 0:
            cats[i] = 1
        else:
            cats[i] = 0

for b in range(0, 100):
    if cats[b] == 1:
        print(f'Cat {b+1} has hat')

