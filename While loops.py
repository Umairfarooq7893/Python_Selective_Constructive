# A control flow statement that allows a block of code to be executed repeatedly
# as long as a specified condition is true 

# Syntax
# initialization using iterator
# while condition:
#    print(work)
#    increment

# If we want to print hello 5 times
count = 1                     # initialization
while count <=5:              # condition
    print(  "Hello")
    print("Umair")
    count += 1                #increment


# If we want to print Mir Umair 4 times
i = 1 #iterator              # initialization
while i<=4:                  # condition
    print("Mir Umair")        
    i+=1                     # increment


# If we want to print numbers from 1 to 4
i = 1                 # initialization
while i <= 4:         # condition
    print(i)
    i += 1            # increment
 

#or we can also start from reverse
i = 4             # initialization
while i >= 1:     # condition
    print(i)
    i -=1         # decrement

# Example1; print the multiplication of '5'
i = 1                  # initialization
while i <= 10:         # condition 
    print(5*i)
    i += 1

# Example2; print the multiplication of 'n'
n = int(input("n ka value: "))      
i = 1                # initialization
while i <= 10:       # condition
    print(n*i)
    i += 1

# Example3; Print the elements of the following list using a loop
lists = [1,4,9,16,25,36,49,64,81,100]
index = 0
while index < len(lists):  # "=" cannot be used here, as index starts from 0 to 9 and len(lists) is 10
    print(lists[index])    # lists[0], lists[1], lists[2], lists[3]
    index += 1

tuple = (1,2,9,2,25,36,2,64,2,100)
x = int(input("Enter the number to search: "))

i = 0      #interator  , initialisation
while i < len(tuple):
    if tuple[i] == x:
        print("Number found at index",i)
    else:
        print("Number not found")
    i += 1 

### If the counter is incremented before the print
# the output will be
i = 1
while i<=4:
    print("MY Abu Farooq Ah Mir")        
    i+=1
i = 1
while i <= 4 :
    i += 1
    print("MY Abu Farooq Ah Mir")
#both give same output
# but the first one is more readable







    

