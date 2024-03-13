# editing a file means we're essentially 
# reading an existing file
# and making changes to that file 
# and  saving the file 
# both reading and writing 
# read
#  file = open("cheese.txt", "r")
# lines = file.readlines()
# file.close()

# edit
# lines.insert(0,"I like cheese\n")

# lines[1] = "Hello friend!\n"
# lines[-1] = lines[-1] + "\n"
# lines.append("Goodbye")


# write
# file = open("cheese.txt","w")
# file.writelines(lines)
# file.close()

# multiply each of the number by 2 
file = open("number.txt", "r")
lines = file.readlines()
file.close()

for line in file:
    num = float(line)
    print(2*num)

file = open("number.txt","w")
file.writelines(lines)
file.close()
