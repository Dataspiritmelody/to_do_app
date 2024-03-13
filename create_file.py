# this create only if the file doesnot exist
file = open("cheese.txt" , "x") 
file.write("X marks the spot!")
file.close()

# # overwrite
# file = open("cheese.txt" , "w") 
# file.write("for the W!")
# # file.close()
# # append
# file = open("cheese.txt" , "a") 
# file.write("A+ work ")
# file.close()
# create the file name after an argumrnt passed to the script
# import sys
# file = sys.argv[1]
# file = open(file,"w")
# file.close()

    