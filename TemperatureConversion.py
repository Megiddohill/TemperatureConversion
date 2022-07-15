#David Prato CIS276 Wk2Lab2 Temperature conversion

def fahrenheit_to_celsius(num):
    cel = (5/9) * (num - 32)
    return cel


def celsius_to_fahrenheit(num):
    fah = (num * 9/5 ) +32
    return fah

for num in range(0,212,40):
    print(f'{num} Fahrenheit = {round(fahrenheit_to_celsius(num),2)} Celsius')


for num in range(0,100,20): #start, stop, increments
    print(f'{num} Celsius = {round(celsius_to_fahrenheit(num),2)} Fahrenheit')
