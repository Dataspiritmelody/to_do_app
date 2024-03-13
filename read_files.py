# file = open("cheese.txt","r")
# file_text = file.read()
# print(file_text)file
# getting all the lines from
#  the and ()put it into list
# lines = file.readlines()
# print(lines)
# for line in file:
#     print(line)
# file.close()

# create a file numbers.txt that has a few lines of nuumbers 
# multiply all the number and print the result.
num = open("number.txt" , "r")
result = 1
try:
    for line in num:
        result *= float(line) 
except Exception as e:
    pass 
print(result)
num.close()