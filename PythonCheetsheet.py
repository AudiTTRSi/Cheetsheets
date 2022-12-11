########################
# List comprehensions  #
# examples             #
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


##############################
#                            #
# Lambda functions examples  #
#                            #
##############################


#adds +2 to the my_input variable
add_two = lambda my_input: my_input + 2


#checking if my_sting is part of 
is_substring = lambda my_string: my_string in "This is the master s

print(is_substring('I'))
print(is_substring('am'))
print(is_substring('the'))
print(is_substring('master'))

# logic operation in lambda function
check_if_A_grade = lambda grade: 'Got an A!' if grade >= 90 else 'Did not get an A...'

print(check_if_A_grade(91))
print(check_if_A_grade(70))
print(check_if_A_grade(20))

#another string check function
contains_a = lambda my_string: "a" in my_string
print(contains_a("banana"))
print(contains_a("apple"))
print(contains_a("cherry"))

#lambda function to check string ending on certain character
#at the moment if ends on a
ends_in_a = lambda my_string: my_string[-1] == "a"

print(ends_in_a("data"))
print(ends_in_a("aardvark"))

#lambda function with if else
even_or_odd = lambda num: "even" if num % 2 == 0 else "odd"

#lambda function that doubles value of num squared
double_square = lambda num: (num ** 2)*2

#lambda function with addup random int between x and y to the input number
add_random = lambda num: num+ random.randint(1,10)