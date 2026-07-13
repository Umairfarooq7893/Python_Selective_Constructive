### Range( )
# range functions returns a sequence of numbers, starting from 0 by default , 
# and increments by 1 (by default), and ends at a specified number.


### range(4) will return a sequence of numbers from 0 to 3
#range(stop)
r1 = range(4)
print(r1[0])                                                                      
print(r1[1])
print(r1[2])
print(r1[3])
# r1[4] will not be printed because it is out of range
# now same sequence can be printed using a loop
for el in r1:
    print(el)


###range(1,11) will return a sequence of numbers from 1 to 10
#range(start,stop)
r2 = range(1,11)
# print(r2)
print(r2[0])
print(r2[1])
print(r2[2])
print(r2[3])
print(r2[4])
print(r2[5])
print(r2[6])
print(r2[7])
print(r2[8])
print(r2[9])
# now using a loop
for el in r2:
    print(el)


### range((1,12,2) ,will return a sequuence of numbers from 1 to 11 ,with a step increment of 2
#range(start,stop,step)
r3 =range(1,12,2)
print(r3)
print(r3[0])
print(r3[1])
print(r3[3])
print(r3[4])
print(r3[5])
#now using loop
for el in r3:
    print(el)


### Pass statement
#pass is a null statement that does nothing.
#it is used when a statement is required syntacically but you do not want any command or code to excute.

# example of pass statement
# r4 = range(1,11)
# for el in r4:
    
# print("hello world")       #It will show an error 
#because uper ka kaam , abi excute nahi huwa,
#hence ,we need to use pass statement
r4 = range(1,11)
for el in r4:
    pass
print("hello world")          #It will not show an error









