from itertools import count
from smtpd import DebuggingServer
from sqlite3 import Cursor
from turtle import circle
from typing import Counter


print("Hello World")
my_dictionary = {}
counties_dict = {}
counties_dict["Arapahoe"] = 422829
counties_dict
counties_dict['Denver'] = 463353
counties_dict['Jefferson'] = 432438
counties_dict
len(counties_dict)
counties_dict.items()
counties_dict.keys()
counties_dict.values()
counties_dict.get("Denver")
counties_dict.get("Jefferson")
print(counties_dict['Arapahoe'])
counties_dict.get('Arapahoe')
counties_dict['Arapahoe']
print(counties_dict.get('Araphoe'))
counties_dict['Arapahoe']
voting_data = []
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({'county':'Denver', 'registered_voters': 463353})
voting_data.append({"county": "Jefferson", "registered_voters": 432438})
voting_data
voting_data.append({'county':'El Paso', 'registered_voters':461149})
voting_data
voting_data[1]= {'county':'El Paso', 'registered_voters':461149}
voting_data.pop(0)
voting_data
voting_data.append({'county':'Denver', 'registered_voters': 463353})
voting_data
voting_data.pop(2)
#Membership operators 'in' 'not in'
counties= ['Arapahoe', 'Denver', 'Jefferson']
if 'El Paso' in counties:
    print("El Paso is in the list of counties.")
if 'El Paso' not in counties:
    print('El Paso is not in the list of counties.')
#Logical operators 'and, or, not'
#and 
if 'Arapahoe' in counties and 'El Paso' in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of countries")
#or
if "Arapahoe" in counties or 'El Paso' in counties:
    print('Arapahoe or El Paso is in the list of counties')
else:
    print('Arapahoe or El Paso are not in the list of counties')
#not 
if 'Arapahoe' in counties and 'El Paso' not in counties:
    print('Only Arapahoe is in the list of counties')
else:
    print('Arapahoe is in the list of counties and El Paso is not in the list of counties')
#Repetition statements 'while, for loops'
#while loop
x = 0
while x <= 5:
    print(x)
    x = x + 1
count = 7 
while count > 1:
    print('El Huevo')
#for loop "can be written as 'if and if-else'""
for Arapahoe in counties:
    print("Arapahoe")
for Denver in counties:
    print('Denver')
for Jefferson in counties:
    print('Jefferson')
counties_tuple = ("Arapahoe","Denver","Jefferson")
for 0 in range(len(counties_tuple)):
    print(counties_tuple[0])
for 1 in range(len(counties_tuple)):
    print(counties_tuple[1])
for 2 in range(len(counties_tuple)):
    print(counties_tuple[1])


    


