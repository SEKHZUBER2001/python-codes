import re


Object="University"
Name="Michael Jackson"
print(Object[0:5])
print(Name[::5])
print(Name[0:10:2])
print(Name[::-1])
print(Name[-1::])

#concatenation of string
statement=Name + " in " + Object
print(statement)
#OR
print("".join(Name+" in "+Object))

#To print statment multiple times
statement_1=3*"THE BODYGUARD\n"         
print(statement_1)


#UPPERCASE & LOWERCASE
a="Thriller is the sixth studio album"
print(a.upper())
print(a.lower())

#REPLACING STRING PORTION
new_string=a.replace("sixth","seventh")
print(new_string)

#splitting of string
print(a.split())
print(new_string.split())



name = "John"
age = 30
print(f"My name is {name} and I am {age} years old.")
print("My name is {} and I am {} years old.".format(name, age))

x = 10
y = 20
print(f"the sum of x and y is {x+y}.")


#USE OF RAW STRING TO ELIMINATE UNWANTED ESACPES
Regular_string="C:\new_folder\tab.txt"
print(Regular_string)
Raw_String=r"C:\new_folder\tab.txt"
print(Raw_String)


#USING FOR LOOP IN STRING
for i in range(len("KNIGHT RIDERS")):
    print(i)
    

message= "A kong string with a silly typo"
new_message=message.replace("kong","long")
print(new_message)
                #ANOTHER PROCESS(or)

new_message2=message[0:2]+"l"+message[3:]
print(new_message2)


#CREATING A NEW STRING (replace the old domain email id to new domain email id)
def replace(email,old_domain,new_domain):
    if "@"+old_domain in email:
        index=email.index("@")   ##o/p WILL BE WHERE "@" POSITIONED
        new_email=email[:index]+"@"+new_domain
        print(new_email)
replace("sekhzuber@old.com","old.com","new.com")
replace("XYZ@old.com","old.com","new.com")
replace("anonymous_old.com","old.com","new.com")    ##output is nothing here as "if" statement is false here
    
    
#using the .strip() function
My_String="\t \n Hello World  "
My_String2="## Hello Sheikh"
My_new_string=My_String.strip()
My_new_string2=My_String2.strip('#')
print(My_new_string)
print(My_new_string2)