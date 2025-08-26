#usage of FOR loop
multiplication=1
for i in range(1,10):
    multiplication=multiplication*i
print(multiplication)   #MULTIPLICATION MUST BE FROM 1 to 9--------->[n to (n-1)]


def covert_to_Fahrenheit(temp):
    return (9*temp/5)+32
for temp in range(10,201,15):
    print(temp, covert_to_Fahrenheit(temp))


for mul in range(2,10+2):
    print(mul*3)


greeting="hello world"
for i in greeting:
    print(i)
    
numbers=[2,3,5,10,12,9]
squared_value=[x**2 for x in numbers]
print(squared_value)
