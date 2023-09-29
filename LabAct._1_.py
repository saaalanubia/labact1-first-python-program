weight = float(input("Weight in pounds (lbs) : "))
weight = weight / 2.205
print (f"Weight converted to kilograms (kg) :{weight}")
print ("===================================")

distance = float(input("Length in Miles (mi) : "))
distance = distance * 1.6093
print (f"Length in Kilometers (km) :  {distance}")
print ("===================================")

temp = float(input("Temperature in Fahrenheit (°F) : "))
temp = ((temp - 32) * 5 ) / 9
print (f"Temperature in Celcius (°C) :  {temp}")
print ("===================================")

age1 = float(input("Age of student 1 : "))
age2 = float(input("Age of student 2 : "))
age3 = float(input("Age of student 3 : "))
age4 = float(input("Age of student 4 : "))
age5 = float(input("Age of student 5 : "))
age6 = float(input("Age of student 6 : "))
age7 = float(input("Age of student 7 : "))
age8 = float(input("Age of student 8 : "))
age9 = float(input("Age of student 9 : "))
age10 = float(input("Age of student 10 : "))
add = age1 + age2 + age3 + age4 + age5 + age6 + age7 + age8 + age9 + age10
average_age = (float (add / 10 ))
print(f"The average age of students is :{average_age}")
print ("===================================")

a = """Aphrodite came out of the sea,with natural charm and beauty."""
b = """But Medusa was once a beauty however taken away, 
replaced with hideousness and a head full of snakes. """
c = """No ordinary man wanted a cerberus as their pet because it has
3 heads ready to bark,its name is Fluffy ."""
d = """No one but one being liked having a Fluffy as a pet and
that being was Hades,god of the underworld. """
e = """But Zeus can manage Fluffy and Hades at the same time with
his powerful thunderbolts and casting of storms."""
print(a + b + c + d + e)



