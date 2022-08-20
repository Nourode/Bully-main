

from cgi import print_directory


bullying = []
print("Welcome. This is a test to determine if you are a kind, or mean person. Do you think you have what it takes?")

bully = input("Do you consider yourself a bully? yes or no >>> ")
if bully == "yes":
    print("Okay. Next question.")
    bullying.append("yes1")
elif bully == "no":
    print("Okay Next question.")
    
bully2 = input("If you saw an elderly person struggling to cross the street would you help them? yes or no >>> ")
if bully2 == "yes":
    print("Next question")
    bullying.append("yes2")
elif bully2 == "no":
    print("Next question")

bully3 = input("If someone asks you for help on an exam would you help? yes or no? >>> ")
if bully3 == "yes":
    print("NEXT!!!!")
    bullying.append("yes3")
elif bully3 == "no":
    print("NEXT!!!!")

bully4 = input("If you see someone whos struglling with there body image bc of bullying would you help them? yes or no? >>> ")
if bully4 == "yes":
    print("Onwards to the next question.")
    bullying.append("yes4")
elif bully4 == "no":
    print("Onwards to the next question.")

bully5 = input("If an incident occured where someone was getting cyber bullyed, would you help? them yes or no?")

if bully5 == "yes":
    print("Just a few more questions")
elif bully5 == "no":
    print("Just a few more questions")



bully6 = input("If you were dared to do something, knowing it would negatively affect another person, would you do it?")
if bully6 == "yes":
    print("Okay. Next question.")
    bullying.append("yes6")
elif bully6 == "no":
    print("Okay Next question.")
    
bully7 = input("If you saw a sick animal on the streets would you help it? yes or no >>> ")
if bully7 == "yes":
    print("Next question")
    bullying.append("yes7")
elif bully7 == "no":
    print("Next question")

bully8 = input("If someone got injured badly would you help them? yes or no? >>> ")
if bully8 == "yes":
    print("NEXT!!!!")
    bullying.append("yes8")
elif bully8 == "no":
    print("NEXT!!!!")

bully9 = input("If you see someone getting threatend would you help them? yes or no? >>> ")
if bully9 == "yes":
    print("Onwards to the next question.")
    bullying.append("yes9")
elif bully9 == "no":
    print("Onwards to the next question.")

bully10 = input("If you see a person in need would you help them yes or no?")
if bully10 == "yes":
    bullying.append("yes10")
    print("Calculating your results...")
elif bully10 == "no":
    print("Calculating your results")


print(bullying)

if len(bullying) > 5:
    #for the end and to check if user is a bully or not
    print("You aren't a bully")
elif len(bullying) < 5:
    print("You are a bully") 




 

#If you saw an elderly person struggling to cross the street would you help them? yes or no?
#if someone asks you for help on a exam would you help? yes or no?
#if you see someone whos struglling with there body image bc of bullying would you help them? yes or no?
# if you see someone getting bullied would you help them? yes or no?
# if you see someone getting cyber bullying would you help? them yes or no?
# 
 