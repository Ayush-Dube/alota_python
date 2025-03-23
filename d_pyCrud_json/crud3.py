import json

with open('learn_json.json','r') as f:
    data = json.load(f)

print(data[0]['name'])
# print(data[0]['service']) 

# different ways of reading a dictionary

print(data[2].get('name'))
print(data[2].get('service'))

# dict unpacking

def display_info(name, age, city):
    print(f"Name: {name}, Age: {age}, City: {city}")

person = {'name': 'Alice', 'age': 25, 'city': 'New York'}
display_info(**person)
# Output: Name: Alice, Age: 25, City: New York

# ternery operator
def plyrDetel(name,age,unit,gender):
    print(f"This individual who is {age} yrs of age,belongs to the {unit} and {'his' if gender.lower()=='male' else 'her' if gender.lower()=='female' else 'their'} name is {name}.")

print(data[3])
# plyrDetel(data[3]) will throw error that 3 arguements missing
plyrDetel(**data[3])
plyrDetel(**data[2])
plyrDetel(**data[4])