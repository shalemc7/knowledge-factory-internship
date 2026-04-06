fruits = ["apple", "banana", "cherry"]
fruits.append("mango")
fruits.remove("banana")
print(fruits[0:2])   # slicing
fruits.sort()
print(fruits)
fruits.reverse()
print(fruits)

#SETS
a = {1, 2, 3}
b = {2, 3, 4}
print(a | b)   # union
print(a & b)   # intersection
print(a - b)  # difference


#DICTIONARIES
person = [
    {"name": "Alex", "age": 15},
    {"name": "Maria", "age": 45},
    {"name": "Timmy", "age": 8},
    {"name": "Jordan", "age": 17},
    {"name": "Eleanor", "age": 72}
]
for p in person:
    print(p.get("name", "Unknown"))
    for k, v in p.items():
        print(k, "->", v)
d = {k: v*2 for k, v in {"a": 1, "b": 2}.items()}
print(d)  # {'a': 2, 'b': 4}

#JSON R/W
import json

# read (load existing data from contacts.json)
with open("contacts.json", "r") as f:
    contacts = json.load(f)

print("Loaded contacts:", contacts)

# write (save back to file, or modify and save)
with open("contacts.json", "w") as f:
    json.dump(contacts, f, indent=2)
    