# lambda function in python = function written in 1 line using lambda keyword
#                            accepts any number of arguments, but only has one expression
#                           (think of it as a shortcut)
#                            (useful if needed for a short period of time, throw away)
# lambds parameters : expression
"""def double(x):
    return x*2
print(double(5

double = lambda x:x *2
print(double(5))
multiply = lambda x,y : x*y
add = lambda x,y,z : x+y+z
full_name = lambda first_name, last_name:first_name +" "+ last_name
age_check = lambda age: True if age>= 18 else False
print(age_check(18))

#                                 Python Sort()
# sort() method = used with lists
# sort() function = used with iterables
students = ["Dhruv Rathee", "Bill Gates", "Sundar Pichai", "Satya Nadela", "Dipu Singha"]
students.sort(reverse=True)

for i in students:
    print(i)

students = (("Dhruv Rathee ","F",45),
            ("Bill Gates   ","A",73), 
            ("Sundar Pichai","B",49),
            ("Satya Nadela ","D",54),
            ("Dipu Singha  ","A",20))
# grade = lambda grades:grades[1]
age = lambda ages:ages[2]
# students.sort(key = grade,reverse = True)
#students.sort(key = age)
sorted_students = sorted(students,key = age) # for a list of tuple
for i in sorted_students:
    print(i)

#   map () = map function applies a funcion to each item in an iterable (list,tuple,etc.)
#   map (function,iterable)
store = [("shirt", 20.00),
         ("pants",34.54),
         ("shocks",53.34),
         ("jacket",99.43)]
#to_euros = lambda data:(data[0],data[1]*0.86)
to_dollars =lambda data:(data[0],data[1]/0.86)
#store_euros = list(map(to_euros,store))
store_dollars = list(map(to_dollars,store))

for i in store_dollars:
    print(i)

# filter () = creates a collection of elements from an iterable for which a funcion returns True
# filter (funcion,iterable)
friends = [("Pronoy",23),
           ("Sourov",22,),
            ("Amit",22),
            ("Shrabanto",18),
            ("Shimul",22),
            ("Dipu",20)]
age = lambda data:data[1] >= 18

drinking_buddies = list(filter(age, friends))
for i in drinking_buddies:
    print(i)

# Python reduce funcion -62
name = input("Enter your name : ")
age = int(input("Enter your age : "))

age = age +1

print("Your BIO is :")
print(f"Hello {name}")
print(f"You are {age} years old")

# Mad libs game
adjective1 = input("Enter an adjective : ")
noun = input("Enter a noun :")
adjective2 = input("Enter another adjective : ")
verb = input("Enter a verb :")
adjective3 = input("Enter an adjective: ")
print("---------------MAD LIB GAME IS------------")

print(f"Today I went to a  {adjective1} zoo.")
print(f"In an exhibit I saw {noun}")
print(f"{noun} was {adjective2} and {verb}ing")
print(f"I was {adjective3}")

# reduce() = apply a funcion to an iterable and reduce it to a single cumulative value
# performs funcion on first two elements and repeats process until 1 value remains
# reduce(funcion,iterable)
import functools

letters = ["H","T","S","A","D","S","S","W","L","E","A","L"]
word = functools.reduce(lambda x,y:x+y,letters)
print(word)

import functools

factorial = [5,4,3,2,1]
result = functools.reduce(lambda x,y:x*y,factorial)

print(result)

# list comprehension = a way to create a new list with less syntax
#                      can mimic certain lambda funcions, easier to read
#             list = [expression for item in iterable]
#  list = [expression for item in iterable if conditional]
# list = [expression if/else for item in iterable]
squares = []             # create an empty list
for i in range(1,11):    # create a for loop
    squares.append(i*i)  # define what each loop iteration should do
print(squares)                       # this code takes 3 lines of code

squares = [i*i for i in range(1,11)] # this code takes 1 line of code

print(squares)

students = [100,90,84,76,65,50,45,23,10,0]

#passed_students = list(filter(lambda x:x >=60, students))
#passed_students = [i for i in students if i >= 60]
passed_students = [i if i >= 60 else "FAILED" for i in students]
print(passed_students)

# ----------------Python dictionary comprehension = create dictionaries using expression--------------
#                           can replace for loops and certain lambda functions
# dictionary = {key:(expression for key,value) in iterable}
# dictionary = {key:(expression for key,value) in iterable if conditional}
# dictionary = {key: (if/else) for (key,value) in iterable
#---------------------------------------------------------
cities_in_F = {'New York':32,'Los Angeles':76,'Colorado':111,'Boston':96,'California':67}

cities_in_C = {key : round((value-32)*(5/9)) for (key,value) in cities_in_F.items()}
print(cities_in_C)

weather = {'New York':"snowing",'Los Angeles':"cloudy",'Colorado':"sunny",'Boston':"sunny",'California':"sunny"}
sunny_weather = {key:value for (key,value) in weather.items() if value == "sunny"}

print(sunny_weather
print("--------------This line indicates both end and start of a new topic------------------")
cities = {'New York':32,'Los Angeles':76,'Colorado':111,'Boston':96,'California':67}
desc_cities = {key : ("WARM" if value >= 40 else "COLD") for (key,value) in cities.items()}
print(desc_cities)

print("--------------This line indicates both end and start of a new topic------------------")
def ckeck_temp(value):
    if value >= 70:
        return "HOT"
    elif 69>= value >= 40:
        return "WARM"
    else:
        return "COLD"
    
cities = {'New York':32,'Los Angeles':76,'Colorado':111,'Boston':96,'California':67}
desc_cities = {key: ckeck_temp(value) for (key,value) in cities.items()}
print(desc_cities)

# zip function python
# zip(*iterables) = aggregate elements from two or more iterables(list,tuples,sets,etc)
#                  creates a zip object with paired elements stored in tuples for each element
usernames = ["Dude","Bro","Mister"]
passwords = ("p@ssword","abc123","guest")
#users = list(zip(usernames,passwords))
users = dict(zip(usernames,passwords))
print(type(users))
#for i in users:
 #   print(i)
for key,value in users.items():
    print(key +" : "+value)

usernames = ["Dude","Bro","Mister"]
passwords = ("p@ssword","abc123","guest")
login_date = ["1/1/2023","1/2/2023","1/3/2023"]
users = zip(usernames,passwords,login_date) # zip function is really transformational

for i in users:
    print(i)
"""





