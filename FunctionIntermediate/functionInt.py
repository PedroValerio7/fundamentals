#1. update values in dictionaries and list
"""
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0]= 15
print(x)
students[0]["last_name"] = "Bryant"
print(students)
sports_directory['soccer'][0]="Andres"
print(sports_directory)
z[0]["y"] =30
print(z)
"""
#2.Iterate Through a List of Dictionaries
"""
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(some_list):
    for i in range(0, len(some_list)):
        print(some_list[i])

iterateDictionary(students)
"""
#3.Get Values From a List of Dictionaries
"""
def iterateDictionary2(key_name, some_list):
    for i in range(0,len(some_list)):
        print(some_list[i][key_name])

iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)
"""
# 4.iterate through a dictionary with list values
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(some_dict):
    print(str(len(some_dict['locations'])) + " LOCATIONS")
    for i in range(0, len(some_dict['locations'])):
        print(some_dict['locations'][i])
    print(str(len(some_dict['instructors']))+ " INSTRUCTORS")
    for i in range(0, len(some_dict['instructors'])):
        print(some_dict['instructors'][i])
printInfo(dojo)
