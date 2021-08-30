num1 = 42 # variable declaration, intialize integer
num2 = 2.3 #variable declaration, initalize float
boolean = True #variable declaration, initialize boolean
string = 'Hello World' #variable declaration, initialize string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #variable declaration, initialize list,
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #variable declaration initialize dictionary
fruit = ('blueberry', 'strawberry', 'banana')#variable declaration intialize tuples
print(type(fruit)) # log statement, acces variable type
print(pizza_toppings[1])# log statment, access value in list
pizza_toppings.append('Mushrooms')# add value to list
print(person['name']) #log statement, acces value in dictionary
person['name'] = 'George' #change value in dictionary
person['eye_color'] = 'blue'#change value in dictionary
print(fruit[2]) #log statement, acces value in tuples

if num1 > 45: #condition if
    print("It's greater") #log statement
else: #condition else
    print("It's lower") #log statement

if len(string) < 5: #condtion if
    print("It's a short word!")#log statement
elif len(string) > 15: # condition elif
    print("It's a long word!")#log statement
else: # codition else
    print("Just right!")#log statement

for x in range(5): # for loop
    print(x) #log variable
for x in range(2,5): # for loop
    print(x) #log variable
for x in range(2,10,3): # for loop
    print(x) #log variable
x = 0 #chagnin value
while(x < 5): #while loop
    print(x) #log variable
    x += 1 #adding 1 to variable

pizza_toppings.pop() #delete value from list
pizza_toppings.pop(1) #delete value from list in index 1

print(person) #log dictionary
person.pop('eye_color') # delete value from dictionary
print(person) # log dictionary

for topping in pizza_toppings: # for loop 
    if topping == 'Pepperoni': #if loop
        continue # continue if loop condition is met
    print('After 1st if statement') #log statement
    if topping == 'Olives':# if loop
        break #break if codition is met

def print_hello_ten_times(): #function delaration
    for num in range(10): # for loop, parameter
        print('Hello')# log statement

print_hello_ten_times() #initilize function

def print_hello_x_times(x): #function delclaration, parameter
    for num in range(x): # for loop, parameter
        print('Hello') #log statement

print_hello_x_times(4) #initialize function, argument

def print_hello_x_or_ten_times(x = 10): #function declaration, parameters
    for num in range(x):# function loop
        print('Hello') #log statement

print_hello_x_or_ten_times() #initialize function
print_hello_x_or_ten_times(4)#initilize funtion


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)