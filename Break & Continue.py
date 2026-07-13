# Simple case
i = 0                       #initialization step
while i <= 5:               #condition
     print(i)               #print
     i += 1                 # increment

# BREAK, 
# used to terminate the loop when a certain condition is met

# Simple Break case            
i = 0                       #initialization
while i <= 5:               #condition
    print(i)                #print
    if(i == 3):             #condition for breakdown of loop
        break               #break
    i += 1                  #increment

# CONTINUE,
# used to skip the execution in the current iteration and continues execution in the next iteration
# print the numbers from 0 to 4,but skip the number 3
i = 0                      #initialistaion
while i <= 4:              #condition
    if(i == 3):            #condition  for skipping
        i += 1             #skip
        continue           #loop continues
    print(i)
    i += 1                 #increment

#Example :print odd numbers from 0 to 10
i = 0
while i <= 10:             #condition for a loop
    if(i%2 == 0):          #condition for an even number
        i += 1             #skip
        continue           #continue
    print(i)               #print
    i += 1                 #increment        
#Example :print even numbers from 0 t0 10
i = 0
while i <= 10:
    if(i % 2 != 0):
        i += 1
        continue
    print(i)
    i += 1













