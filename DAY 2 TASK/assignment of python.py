# Python Assignment
# Name:Dharti
# Enroll. No:230470107152

# -------- LIST (5 methods) ------------

fruits = ["apple", "banana", "mango"]
print(fruits)

fruits.append("orange")
print(fruits)

fruits.insert(1, "grapes")
print(fruits)

fruits.remove("banana")
print(fruits)

fruits.pop()
print(fruits)

fruits.sort()
print(fruits)


# --------- DICTIONARY (5 methods) -----------

student = {
    "name": "Rahul",
    "age": 20,
    "course": "Python"
}

print(student)

print(student.keys())

print(student.values())

print(student.items())

print(student.get("name"))

student.update({"age": 21})
print(student)


# -------- TUPLE ----------

colors = ("red", "green", "blue", "green")

print(colors)

print(colors.count("green"))

print(colors.index("blue"))

print(len(colors))

print(max(colors))

print(min(colors))


# ------ SET (5 methods) -----

numbers = {1, 2, 3}

print(numbers)

numbers.add(4)
print(numbers)

numbers.remove(2)
print(numbers)

numbers.discard(10)
print(numbers)

numbers.pop()
print(numbers)

numbers.clear()
print(numbers)


# ------ IF --------

age = 18

if age >= 18:
    print("You can vote")


# ------ IF ELSE ----------

marks = 45

if marks >= 35:
    print("Pass")
else:
    print("Fail")


# --------- IF ELIF ELSE -------------

score = 80

if score >= 90:
    print("Grade A")
elif score >= 60:
    print("Grade B")
else:
    print("Grade C")


# ----- NESTED IF ELSE -------------

age = 20
citizen = True

if age >= 18:
    if citizen:
        print("Eligible to vote")
    else:
        print("Not eligible")
else:
    print("Too young")


# ---------------- BREAK ----------------

for i in range(1, 6):
    if i == 3:
        break
    print(i)


# ------- CONTINUE --------

for i in range(1, 6):
    if i == 3:
        continue
    print(i)


# -------- PASS ----------------

for i in range(1, 6):
    if i == 3:
        pass
    print(i)


# ----- INPUT -----------

name = input("Enter your name: ")
print("Hello", name)


# ----- RANGE ---

for i in range(5):
    print(i)


# ----- LEN -----------

names = ["Amit", "Rahul", "Priya"]
print(len(names))


# ---- TYPE -----

x = 10
print(type(x))


# ------ FOR LOOP ------

for i in range(1, 6):
    print(i)


# ------- WHILE LOOP -------

i = 1

while i <= 5:
    print(i)
    i = i + 1