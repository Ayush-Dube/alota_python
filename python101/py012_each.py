data = [
    {'name':'alpha','age':'21','city':'london'},
    {'name':'beta','age':'22','city':'NewYork'},
    {'name':'gamma','age':'23','city':'Paris'},
    {'name':'omega','age':'24','city':'Rome'}
]



for each in data:
    print(f"{each['name']} is {each['age']} years old and hails from {each['city']}")


data.append('abc')

print(data)