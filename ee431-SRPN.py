'''
SRPN CALCULATOR
AUTHOR: TuringMach1ne


'''
#initiating the stack
stack = []

#random numbers are found to be the same list in legacy SRPN calculator.This list copies it.
RANDOMS = [1804289383, 846930886, 1681692777, 1714636915, 1957747793,
                  424238335, 719885386,1649760492,596516649,1189641421,1025202362,
                  1350490027,783368690,1102520059,2044897763,1967513926,1365180540,
                  1540383426,304089172,1303455736,35005211,521595368,1804289383]
#how many randoms requested so far for the reference of index of random numbers in the list
rand_count = 0

#max length of the stack
LEN_STACK = 22
#max value of a variable
MAX = 2147483647
# min value of a variable
MIN = -2147483648


def process_command(s):
    '''
    Function to execute all operations

    '''
    if len(stack) > LEN_STACK: #Max size of stack is 22 and if 23rd item gets into the stack, 
        del stack[-1] # 1)the last item from stack is removed
        raise Exception("Stack overflow.") # 2) 'Stack overflow' exception is printed
    if user_input == "+":
        x = stack.pop()
        y = stack.pop()
        result = x+y # basic addition operation
        stack.append(result)
    elif user_input == "-":
        x = stack.pop() # basic substraction operation
        y = stack.pop()
        result = y-x
        stack.append(result)
    elif user_input == "*":
        x = stack.pop() # basic multiplication operation
        y = stack.pop()
        result = x*y
        stack.append(result) 
    elif user_input == "%":
        x = stack.pop() # modulo operation.The remainder of y/x
        y = stack.pop()
        result = y%x
        stack.append(result)
    elif user_input == "/":
        x = stack.pop()# division operation that ony returns integers
        y = stack.pop()
        result = y//x
    elif user_input == "^": # power base. returns y to the power of x
        x = stack.pop()
        y = stack.pop()
        result = pow(y, x)
        stack.append(result)
    elif user_input == "r": # each time 'r' is pressed, a random number from RAND_LIST is given, with an order
        global rand_count # because the random numbers were ordered in the legacy SRPN, 
        stack.append(RANDOMS[rand_count]) # each iteration of random gives another random 
        rand_count+=1
    elif user_input == "d": # pressing 'd' prints out the entire stack
        for i in range(len(stack)):
            print(stack[i])
    elif user_input[0] == "#": # if '#' is pressed, the program ignores the input
            pass
    elif user_input == "=": # when '=' is pressed, the program prints the result of prior calculation(s)
        if stack[-1] <= MIN : # saturation check for minimum value
            stack.pop()
            result = MIN
            stack.append(result)
        if stack [-1] > MAX: # saturation check for maximum value
            stack.pop()
            result = MAX
            stack.append(result)
            print(stack[-1])
        else:
            print(stack[-1])
       
    else:
        stack.append(int(user_input)) # pushes user input inside stack

        
        
        
while True:
    user_input = input() # constantly gets user input
    
    try:
        process_command(user_input) # operations function runs
    except ValueError:
        if user_input == "": # if the input is blank, the program ignores it
            pass
        else:
            for i in user_input:
                print("Unrecognised operator or operand \"" + i + "\"") # unrecognised input raises exception
            pass
    except IndexError:
        print("Stack underflow.") # if number of operators are equal or more than operands. stack underflow happens
        pass
    except ZeroDivisionError:
        print("Divide by 0.") # division by zero is possible, but prints out exception
        stack.append(0)
        pass
    except Exception as e : # in case there is any other exceptions.
        print(e)
    finally:
        pass

