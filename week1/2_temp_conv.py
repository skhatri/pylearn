"""
Convert the given temparature in Celcius to Farenheit
"""

#your friend came from America. you find temperature for him
#37.5 Celcius is 99.5% Farenheit
C = 37.5
#F = ?

#we know F = 9/5 * C + 32

F = 9 / 5 * C + 32
print F

#89.6
F = 9 * 1.0 / 5 * C + 32

print F


#types of names/variables

print type(5)
print type(4.0)
print type("My name is Suresh")

#convert from one type to next
#using str(), int() or float()

x = 4
y = float(x)
z = str(x)
print x, type(x)
print y, type(y)
print z, type(z)


#Now you go to America.
#Exercise convert a F into Celcius using the above formula. Hint you need to find C this time.

#Find the 6^5 using two different ways. Store the result into 2 different names. Print the result
#29F to C


#rounds down as it looses the decimal part of the number
print int(13.89)
print int(1.9999)

