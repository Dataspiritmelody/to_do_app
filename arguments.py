# allow us to work with system level things 
import sys
#all the arguments that are passed into the script 
total = 1
del(sys.argv[0])
for argument in sys.argv:    
    # arguments are the things that you provide after the name of your file 
    try:
        number = float(argument)
        total = total * number 
    except Exception as e:
        print(e)
        print("only numbers can be provided.")
        sys.exit(1)
        

print(total)

# make a script that multiples all the number
# arguments passed into it
