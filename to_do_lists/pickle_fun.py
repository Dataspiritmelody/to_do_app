import pickle
class ToDo:
	def __init__(self, title, important, category = "Normal"):
		self.title = title
		self.important = important
		self.category = category

todos = [ToDo("Walk Dog", True), ToDo("Eat Cheese", False), ToDo("Learn Python", True, category = "Work")]
print(todos)
# age = [34,45,56,6,67]
file = open("hare.txt","wb")
pickle.dump(todos, file)
file.close()

file = open("hare.txt","rb" )
new_todos = pickle.load(file)
file.close()
print(new_todos)