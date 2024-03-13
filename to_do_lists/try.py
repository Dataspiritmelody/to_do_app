import sys 
del(sys.argv[0])
for argument in sys.argv:
    file = open("hare.txt" , "a") 
    file.write(f"{argument }")
    file.close()
