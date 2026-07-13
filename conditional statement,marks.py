## If - elif - else 

# if(condition):
#    statement1
# elif(condition):
#    statement2
# elif(condition):
#    statement3
# else:
#    statement N


## traffic light code

light = input("light color: ")

if(light == "red"):
    print("stop")
elif(light == "yellow"):
    print("slow down")
elif(light=="blue"):
    print("gaadi side laga")
else:    
    print("light is broken")


## Grades of students

marks = int(input("marks:"))

if(marks >=95):
    print("student elligible for scholarship")
elif(marks >=80 and marks <95):
    print("student elligible for 50% shloarship")    
elif(marks >=70 and marks < 80):
    print("student elligible for 25 % scholarship")
else:    
    print("student not elligible for scholarship")


### Single line if statement / Ternary                                                                          
# <stt1> if <condition> else <stt2>

food = input("food:")
print("bring that on the table") if food == "pizza" or food == "mango shake" else print("i do not want that")

## Clever If 
# <val> = (false_val,true_val) [condition]

marks = int(input("marks:"))
eligible = ("sorry not this time","welcome to our college ")[marks >= 90]
print(eligible)

salary = float(input("salary:"))
tax = salary*(0.01,0.02) [salary >= 3000] 
print(tax)

