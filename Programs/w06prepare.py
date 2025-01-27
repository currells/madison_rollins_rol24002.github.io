"""
    Madison Rollins

    W06 Prepare - Working with files

I got my code to work except it's not registering Michles age, only Jacob as the youngest.



For this assignment, you'll download the file books.txt that contains the names of the books in the Book of Mormon, and save it to your computer.

Once you have the file saved to your computer, in VS Code, open the folder that contains it and create a new Python script.

Have your program open the file, read through it line by line, strip off leading and trailing whitespace and display each book to the screen.

The following shows the expected output:


1 Nephi
2 Nephi
Jacob
Enos
Jarom
Omni
Words of Mormon
Mosiah
Alma
Helaman
3 Nephi
4 Nephi
Mormon
Ether
Moroni
"""

"""
with open("programs/books.txt") as books_file:
    for line in books_file:
        line = line.strip()
        print(line)
"""


#the list
people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 02",
    "Jacob 10"
]
#printing peeps
print(f'DA PEEPS:')
for item in people:
    print(f'{item}')
ages = []
names = []

print()
print('IN NUMBER, NAME ORDER')
#split numbers and peeps
for person in people:
    name, age = person.split()
    names.append(name)
    ages.append(int(age))
    print()
    print(f'{age}, {name}')
#if age bbig
print()
print('THE YOUNGEST PERSON')
min_age = int(100)
min_name = name
if 00 <= int(age) < min_age:
       #new max
        #people
    print(f'The Youngest age is {age}')
    print(f'The Youngest person is {min_name}')