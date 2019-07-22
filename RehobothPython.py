def printList(x):
    m = []

    ## This gets out the numbers in the list passed into the function
    m = [int(s) for s in x if s.isdigit()]
    m.sort()

    ## this block is executed when a string is found in the list
    if(len(x)!= len(m)):
        print("Invalid Input")
        print("Minimum: ",m[0])
        print("Maximum: ",m[len(m)-1])

    ## this block is executed when a string is not in the list
    else:
        print("Minimum: ",m[0])
        print("Maximum: ",m[len(m)-1])




## This function is called when you run the program, it collects user input and processes it
        
def getInput(y):
    user_input = input("Enter a number: ") ## user_input is a variable that collects user input

    ## if the input is 'done' the block below is executed 
    if(user_input.lower()=='done'): 
        printList(list(y))
    ## if the input is not 'done' the block below is executed
    else:
        y.append(user_input)
        getInput(y)


## FUNCTION CALL FOR THE USER INPUT COLLECTION FUNCTION
## This implementation uses recursion in place of a loop
        
getInput([])
        
        
