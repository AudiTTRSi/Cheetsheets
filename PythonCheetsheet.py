########################
# List comprehensions  #
########################
temperatures = [-5, 29, 26, -7, 1, 18, 12, 31]
temperatures_new = [temp for temp in temperatures]
# temperatures_new is now [-5, 29, 26, -7, 1, 18, 12, 31]


nums = range(11)
squares = [num**2 for num in nums]
print(squares)

nums = [4, 8, 15, 16, 23, 42]
add_ten = [num+10 for num in nums]
print(add_ten)

nums = [4, 8, 15, 16, 23, 42]
divide_by_two = [num/2 for num in nums]
print(divide_by_two)

nums = [4, 8, 15, 16, 23, 42]
parity = [num%2 for num in nums]
print (parity)

names = ["Elaine", "George", "Jerry", "Cosmo"]
greetings = ["Hello, "+str(name) for name in names ]
print(greetings)

names = ["Elaine", "George", "Jerry", "Cosmo"]
lengths = [len(name) for name in names]
print(lengths)

names = ["Elaine", "George", "Jerry", "Cosmo"]
is_Jerry = [name == "Jerry" for name in names]
print(is_Jerry)

nested_lists = [[4, 8], [16, 15], [23, 42]]
greater_than = [ item1 >item2  for (item1, item2) in nested_lists]
print(greater_than)

nested_lists = [[4, 8], [16, 15], [23, 42]]
first_only = [item1 for (item1, item2) in nested_lists]
print (first_only)


a = [1.0, 2.0, 3.0]
b = [4.0, 5.0, 6.0]
together = zip(a,b)
quotients = [item2 / item1 for (item1,item2) in together]

capitals = ["Santiago", "Paris", "Copenhagen"]
countries = ["Chile", "France", "Denmark"]
joined = zip(capitals, countries)
locations = [item1+", "+item2 for (item1,item2) in joined ]