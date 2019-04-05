customer = {
    "name" : "jhon",
    "age" : 30,
    "is_verified": True
}
print(customer["name"])
print(customer.get("bday", "1-2-1985"))


phone = input("phone:")
digit_mapping = {
    "1": "one",
    "2": "two" ,
    "3": "three",
    "4": "four"
}

output = ""
for ch in phone:
    output +=digit_mapping.get(ch,"!") + " "
    print(output)