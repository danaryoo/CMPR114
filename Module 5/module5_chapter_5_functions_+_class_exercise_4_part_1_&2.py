# -*- coding: utf-8 -*-
"""Module5_Chapter 5 functions + class exercise #4 Part 1 &2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zSMF8hagVHyhTyNghSdUMn9KaRj2sVYj

---


Chapter 5 Functions + Class exercise #4 Part 1
"""

#Challenge #1
def main():
  texas()
  california()
def texas():
	birds_tx = float(input('How many birds are in Texas?: '))
	print(f'Texas has {birds_tx:,.0f} birds.')
def california():
	birds_ca = float(input('How many birds are in California?: '))
	print(f'California has {birds_ca:,.0f} birds.')

main()

#Challenge #2
def info():
  first_name = input('Enter your first name: ')
  last_name = input('Enter your last name: ')
  address = input('What is your addres?: ')
  city = input('What is your city?: ')
  state = input('What is the state?: ')
  zipcode = input('What is the zip code?: ')
  print(f'Your name is {first_name} {last_name}. \nYour address is {address}, {city} {state} {zipcode}.')

info()

#Challenge #3
def add(num1,num2, num3):
	global total
	total = num1 + num2 + num3
	return total 

add(3,4,5)
print(total)

#Challenge #4
def numbers(num1,num2, num3):
  global total, avg
  num1 = int(input('What is the 1st number?: '))
  num2 = int(input('What is the 2nd number?: '))
  num3 = int(input('What is the 3rd number?: '))
  total = num1 + num2 + num3
  avg = total / 3
  return total
  return avg 

numbers(3,4,5)
print(f'the total of 3 numbers is: {total:,.0f} and the average is {avg:,.0f}')

#Challenge #5
#user inputs hours worked and hourly pay
#output in print statement

def wage():
  hr = int(input('Please enter the number of hours you\'ve worked: '))
  pay = int(input('How much do you get paid per hour?: $'))
  show_total(hr,pay)

def show_total(hr, pay):
  total = hr * pay
  print(f'The total wage is ${total:,.2f}')

wage()

"""

---

Chapter 5 functions + class exercise #4 Part 2"""

#Challenge #1
#user inputs distance in kilometers
#program calculates it in miles

conversion = 0.6214

def distance():
  km = float(input('Enter the kilometer(s) traveled: ')) 
  mi = km * conversion
  print(f'{km} km = {mi} mi.')

distance()

#Challenge #2
#users enter (1) loan payment (2) insurance (3) gas (4) oil (5) tires (6) maintenance per month
#program calculates total monthly cost and total annaul costs

def expense(annual):
  loan = int(input('How much do you pay for loan on a monthly basis? '))
  insurance = int(input('How much do you pay for insurance on a monthly basis? '))
  gas = int(input('How much do you pay for gas on a monthly basis? '))
  oil = int(input('How much do you pay for oil on a monthly basis? '))
  tires = int(input('How much do you pay for tires on a monthly basis? '))
  maintenance = int(input('How much do you pay for maintenance on a monthly basis? '))
  monthly = loan + insurance + gas + oil + tires + maintenance
  annually = monthly * annual
  return monthly, annually

annual = 12
monthly, annually = expense(annual)
print(f'Monthly payment: ${monthly:,.2f} \nAnnual payment: ${annually:,.2f}')