
"""
        Madison Rollins W07 Prove


Write a function to calculate and return the wind chill based on a given temperature and wind speed.

Write a function to convert from Celsius to Fahrenheit and return the converted temperature. The formula for this conversion is to multiply the Celsius temperature by (9/5) and then add 32.

Allow the user to enter the temperature in Celsius or Fahrenheit. If they provide it in Celsius, first convert it to Fahrenheit (using the conversion function created above) before using the formula above.

Loop through wind speeds from 5 to 60 miles per hour, incrementing by 5, and calculate and display the wind chill (using the windchill function created above) for each of these wind speeds.

Display the wind chill value to 2 decimals of precision.
"""
import math

temp = float(input("What is the temperature? "))
unit = input("Fahrenheit or Celsius (F/C)? ")

windChill = ""
wind_speeds = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]

def c_to_F(temp):
    return (temp * (9/5)) + 32 


def windChill_fahrenheit(temp, wind_speed):
    windChill = 35.74 + (0.6215 * temp) - 35.75 * (wind_speed ** 0.16) + (0.4275 * temp) * (wind_speed ** 0.16)
    return windChill 

if unit.upper() == "C":
    temp = c_to_F(temp)
for wind_speed in wind_speeds:
    windChill = windChill_fahrenheit(temp, wind_speed)
    print(f"At temperature {temp:.1f}F, and wind speed {wind_speed} mph, the windchill is: {windChill:.2f}F")
