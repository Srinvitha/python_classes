# Dictionary is a set of key-value pairs.
# It is enclosed in curly braces (or flower brackets).

a = {1:'number one', 22 : 'number twenty-two'}     # Here 1 and 22 are keys and 'number one' and 'number twenty-two' are their values respectively.
print(a)
print(a[1])
print(a[22])

dict_employee = {"Employee_name": "Ravi", "Designation":"Vice President", "Age" : "34"}
print (dict_employee)


# Updating the dictionary.
dict_employee ["Employee_name"] = "Ravi Chandra"
dict_employee ["Designation"] = "CEO"
print (dict_employee)

del dict_employee["Age"]           #  comment this if you want to see "clear" work and then uncomment the clear.
print(dict_employee)

# dict_employee.clear()
# print(dict_employee)
print(dict_employee)


dict_employee.update({"Hometown":"Hyderabad"})
print(dict_employee)

print (dict_employee.keys())
print (dict_employee.values())

