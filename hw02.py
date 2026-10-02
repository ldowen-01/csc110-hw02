# Task 1.1:
#  Complete the function "read_two_ints" below:
#define function
def read_two_ints():
    #assign variables, cast them as integers, and return
    x = int(input("give me x: "))
    y = int(input("give me y: "))
    return x, y

# Task 2.1:
#  Complete the function "compute_multadd" below:
def compute_multadd(a, b):
    
    #calculate numerator and save as variable(mult_result), then print
    mult_result= (a * b)
    print ("mult result:", mult_result)

    #calculate denominator and save as variable(mult_result), then print
    add_result= (a + b)
    print ("add result:", add_result)
    
    return mult_result/add_result
    

# Task 3.1:
#  Complete the function "print_fancy" below:
def print_fancy(a, b, ab_multadd):
    
    #print statements
    print("****************")
    print("RESULTS:")
    print(f"first number: {a}")
    print(f"second number: {b}")
    print(f"multadd result: {ab_multadd}")
    print("================")
    

def main ():
    # Task 1.2:
    #  Add one line below to call read_two_ints (note that it returns two values)
    #  the call should provide no arguments
    #  store the returned values into two variables: x and y
    x, y = read_two_ints()
    
    # Task 2.2:
    #  Add one line below to call multadd (note that it returns one value)
    #  the call should provide the arguments x, and y you obtained above;
    #  store the returned value in a variable called xy_multadd
    xy_multadd= compute_multadd(x, y) 

    # Task 3.2:
    #  Complete The line below to call print_fancy
    #  the call should provide the arguments x, y, and xy_multadd you obtained above;
    print_fancy(x, y, xy_multadd)


    # Do not modify this final print statement
    print("The End")

# Do not modify these two lines
if __name__ == "__main__":
    main()
