import math
import string
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

"""
print("Topic1_Task3") #suma modułów trzech wartości
a = float(input("Podaj wart a: "))
a = abs(a)
b = float(input("Podaj wart b: "))
b = abs(b)
c = float(input("Podaj wart c: "))
c = abs(c)

print(a+b+c)
"""
"""
print("Topic1_Task4") #znajdz wynik równania z x - x podane
x = float(input("Podaj wart x: "))

print(2*x**4-3*x**3+4*x**2-5*x+6)
"""

"""
print("Topic1_Task5") #odległość pomiędzy punktami
x1 = float(input("Podaj wart x1: "))
y1 = float(input("Podaj wart y1: "))
x2 = float(input("Podaj wart x2: "))
y2 = float(input("Podaj wart y2: "))

print (math.sqrt((x2-x1)**2+(y2-y1)**2))
"""
"""
print("Topic1_Task6") #liczenie średniej wartości dla liczby czterocyfowej)
a = (input("Podaj wart a (liczba cztero cyfrowa, naturalna): "))
a1 = a[0]
a2 = a[1]
a3 = a[2]
a4 = a[3]

b1 = int(a1)
b2 = int(a2)
b3 = int(a3)
b4 = int(a4)
print((b1 +b2 + b3 +b4)/4)

#inne rozwiązanie:
a = int(input("Podaj wart a (liczba cztero cyfrowa, naturalna): "))

x1 = a // 1000
x2 = a % 1000 //100     # // - to dzielenie obcięte do liczb całkowitych !!   11//3 = 3
x3 = a % 100 //10       # % - to reszta z dzielenia !!   11//3 = 2
x4 = a % 10

print ((x1+x2+x3+x4)/4)
"""

print("Topic1_Task12") #ile godzin, minut, sekund
s = int(input("Podaj wart a (liczba sekund): "))

godz = (s//3600)
min = (s-godz*3600)//60
sek = s - ((godz*3600) + (min*60))

print("liczna godzin: ", godz)
print("liczba minut: ", min)
print("liczba sekund: ", sek)

