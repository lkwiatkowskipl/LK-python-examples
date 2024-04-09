print("Hellooo")
print("hahahahah !!!!!")


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


