#DEFINING A FUNCTION IN PYTHON
def greeting(name):
  result=  print("Welcome, " + name)
  print(result)             #NONE OUTPUT COME HERE

    
greeting("Kay")
greeting("Cameron")
greeting("Sekh Zubair")

def goodbye(name):
    print("Bye,"+ name)

goodbye("Pope")
goodbye("francis")

#name = "Kay"
#number = len(name) * 9
#print("Hello " + name + ". Your lucky number is " + str(number))
#name = "Cameron"
#number = len(name) * 9
#print("Hello " + name + ". Your lucky number is " + str(number)) 
#REWRITE THIS CODE USING 'def'

def greeting(name):
   number=len(name)*9
   print("Hello "+name+" . Your lucky number is "+str(number))
   
   
greeting("SRK")
def greeting(friends):
    for friend in friends:
        print("Hi "+friend)
greeting(["Sim","Alex","Zuber"])
#OUTPUTS ARE DIFFERENT FOR THESE TWO CASES
greeting("Sim") 
greeting("Zuber")