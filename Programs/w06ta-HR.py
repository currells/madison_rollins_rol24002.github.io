"""
    Madison Rollins Team Activity

    Download the file and save it to your computer. In VS Code, open the folder that contains this file. Then, create a new Python script in that folder.

Have your program open the HR System file, read through it line by line, and at this point, simply display the line to the screen.

Split the line into parts and change your display, so that it shows only the names (instead of the whole line).

For each line, get the name and the job title for each person, and display those to the screen.


"""
#open
with open("hr_system.txt") as hr_file:
    print(f'{hr_file}')
    #for line
    for line in hr_file:
        line = line.strip()
        #split for name
        parts=line.split(" ")
        names= parts[0]
        ID = int(parts[1])
        titles= parts[2]
        salary = int(parts[3])
        #Salary Doubled
        salary2 = salary / 24
        #enginer bonus
        if titles == 'Engineer':
            salary2 += 1000
        #print   Alexia (ID: 1913), Engineer - $4500.00
        print(f' {names} (ID: {ID}), {titles} - ${salary2:.2f}')
        
