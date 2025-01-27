"""
    Madsion Rollins 
    Data Analysis

        I prompted the user to enter a year they would like to search up? 
"""

year_prompt = int(input('What year would you like to search up?  (enter a year betweeen 1950-2010):   '))
with open("life-expectancy.csv") as le_file:
    min_life = float("inf")
    min_country = ""
    min_year = ""
    max_life = float("-inf")
    max_country = ""
    max_year = ""
    past_first_line = False
    #for start
    for line in le_file:
        if past_first_line == False:
            past_first_line = True
            continue
        line = line.strip()
        parts = line.split(",")
        #split values
        country = parts[0]
        shorthand = parts[1]
        year = int(parts[2])
        life_expectancy = float(parts[3])
        #check if year match
        if year != year_prompt:
            continue
        #if max

        if max_life < life_expectancy:
            max_life = life_expectancy
            max_country = country
            max_year = year

        #if min
        if 00 <= life_expectancy < min_life:
            min_life = life_expectancy
            min_year = year
            min_country = country
    print(f'The overall MAX life expectancy is:  {max_life} from {max_country} in {max_year}')
    print(f'The overall MIN life expectancy is:  {min_life} from {min_country} in {min_year}')