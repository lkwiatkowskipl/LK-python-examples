import math
from struct import pack



a = None
int_number = 3
float_number = 3.3
complex_number = 3.3 + 2j

a=int_number+2

print(a)

s1 = "Hello,"
s2 = " World!"
joined_string = s1 + s2

print(s1 + s1 + s2)

name = "Oleg"
hello_string = f"Hello, {name}!"    #automatycznie wypełnia {name} na name !

print(hello_string)

#a = input("Invitation string: ")                  input !
a = "HELLLOOOOOOOO"


print(a)

#age = input("How old are you? ")
age = 18
age = int(age)                     #rzutowanie typów ze string na int tutaj !

print(age)

pi = float('3.14')                  #rzutowanie na float
pi_str = str(3.14)  
age_str = str(29)                   #rzutowanie na string

#name = input("What is your name? ")
name = "Stefanek"
print(f"Hello {name}")


#age = input("How old are you? ")
age ="45"

if int(age) >= 18:
    print("You are adult already.")
else:
    print("You are infant yet.")


#x = int(input("X: "))
x = 44
#y = int(input("Y: "))
y = 54354

if x == 0:
    print("X can`t be equal to zero")
    x = int(input("X: "))

result = y / x
print(result)



a = 1
while a <= 5:
    print(a)
    a = a + 1



#age = input("How old are you? ")
age = "krowa"
try:
    age = int(age)
    if age >= 18:
        print("You are adult.")
    else:
        print("You are infant")
except ValueError:
    print(f"{age} is not a number")



def say_hello():
    print('Hello, World!') # block belonging to the function
    # end of function say_hello()

# function call
say_hello()

# another function call
say_hello()



def print_max(a, b):
    if a > b:
        print(a, 'max')
    elif a == b:
        print(a, 'equal to', b)
    else:
        print(b, 'max')

print_max(3, 4)  # direct transfer of values

x = 5
y = 7
print_max(x, y)  # passing variables as arguments


x = 50

def funct():
    x = 2
    print('Changing local x to', x)   # Changing local x to 2

funct()
print('x is still', x)   # x is still 50




x = 50

def func():
    global x
    print('x is equal to', x) # x is equal to 50
    x = 2
    print('Change the global value of x to', x)    # Change the global value of x to 2

func()
print('The value of x is (global)', x)    # The value of x is 2

#############?????????????????????????????????????
def total(a=5, *numbers, **phone_boook):
    print('a (any numbers of params)', a)
    # pass through all elements of the tuple
    for single_item in numbers:
        print('single_item', single_item)

    #pass through all items of the dictionary
    for first_part, second_part in phone_boook.items():
        print(first_part,second_part)

print(total(10, 1, 2, 3, Spack=4, John=2231, Inge=1560))
#############?????????????????????????????????????


def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))   # 120


sin_pi = math.sin(math.pi)
print(sin_pi)

#####################kolekcje!!!#########################

some_iterable = ["a", "b", "c"]
first_letter = some_iterable[0]
middle_one = some_iterable[1]
some_iterable[2] = "X"    #sobie zmieniłem 
last_letter = some_iterable[2]

print(first_letter, middle_one, last_letter)




some_str = "This is awesome string"
first_five = some_str[1:9]

print(first_five)




numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

odd_numbers = numbers[::2]  #od której do której i jaki przyrost
even_numbers = numbers[1::2]
three_numbers = numbers[2:9:3]

print(odd_numbers)
print(even_numbers)
print(three_numbers)



numbers = ['a', 'b']
numbers.append('c')      ### funkcje obiektów !! append = add
print(numbers)  # ['a', 'b', 'c']

print(numbers.count("a"))
numbers.clear()

print(numbers)



chars = {'a': 1, 'b': 2}   #słowniki 
b_num = chars.pop('b')

print(chars)  
print(b_num) 

chars = {
    1: "one",
    2: "two",
    3: "three"
}
b_num = chars.pop(1)

print(chars)  
print(b_num)  


b = set('hi there!')
print(b)    # {'r', ' ', 'i', 'e', '!', 'h', 't'}


t="hahahahaadASDSADASdas!@#@!#@dasdasADSDADSAD"
print(t.capitalize())
print(t.lower())
print(t.upper())

"""
print("Topic1_Task1")
a = float(input("Podaj a: "))
if a != 0:
     b = float(input("Podaj b: "))
     x = -b/a
     print("Wynik wynosi", x)
elif a==0 :
     print("wartość 'a' nie może być zero. Spróbuj jeszcze raz ! ")
"""

"""
print("Topic1_Task2") #pole trójkąta prostokątnego
a = float(input("Podaj bok a: "))
b = float(input("Podaj bok b: "))

p = (a*b)/2
c = math.sqrt(a*a + b*b)
print(f"Pole trójkąta prostokątnego o bokach a={a} i b={b} wynosi p=", p)
print(f"Długość przeciwprostokątnej trójkąta prostokątnego o bokach a={a} i b={b} wynosi c=", c)
"""



