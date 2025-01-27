""" Create a ID Badge that looks like so..
----------------------------------------
[LAST NAME], [first name]
[Job title]
ID: [id number]

[email address]
[phone number]
----------------------------------------
Write a program to prompt the user for the following:

First name

Last name

Email Address

Phone Number

Job Title

ID Number


"""
#Questions
print('Hello!  Please Answer the Following Questions!')
first = input('What is your first name?')
last = input('What is your last name?')
email = input('What is your email?')
phone = input('What is your phone number?')
job = input('What is your job title?')
id = input('What is your ID?')
#additional info
hair = input('What is your hair color?')
eye = input('What is your eye color?')
month = input('When did you start?')
train = input('Did you complete the additional training?')

#I card
print (f"""
Your ID card is...
----------------------------------------
{last.capitalize()}, {first.capitalize()}
{job.title()}
ID: {id}

{email}
{phone}

Hair: {hair:15} Eyes: {eye}
Month: {month:14} Training: {train}
----------------------------------------
""")