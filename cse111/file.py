"""Write a set of functions which generates 1 million rows in
 a csv of fake people data and writes the data to a file"""

#imports
import csv
import random
from faker import faker
from datetime import datetime, timedelta


"""function to generate random date of birth"""
def generate_date_of_birth(start_date, end_date=datetime.now()):
    #Generates a random date between two given dates.

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + timedelta(days=random_number_of_days)

    #return the value
    return random_date.strftime("%Y-%m-%d")  # Format as YYYY-MM-DD
    
"""store the value"""
DOB = (generate_date_of_birth)


"""function to generate random phone number"""
def generate_phone_number():
    #Generates a random phone number (basic format).

    area_code = str(random.randiant(200, 999))
    prefix = str(random.randint(200, 999))
    line_number = str(random.randint(1000, 9999))

    #return the value
    return f"{area_code}-{prefix}-{line_number}"

"""store the value"""
pNum = (generate_date_of_birth)
    

"""function to generate random email"""
def generate_email(first_name, last_name, domain=None):
    #Generates a random email address.

    email_provider = random.choice(["gmail.com", "yahoo.com", "outlook.com", "aol.com", "hotmail.com"])
    email = f"{first_name}.{last_name}@{email_provider}"

    #return the value
    return email