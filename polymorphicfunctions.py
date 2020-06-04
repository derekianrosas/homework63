#how to create write file system
file_builder = open("logger.txt", "w+") #open is a function that allows you to open or create a file in python, if it finds a file then it will open it, but if it does not find it then it will create it on the fly
for i in range(100):
	file_builder.write(f"I will not write bad code {i + 1}\n")
#file_builder.write("Hey, I'm in a file")
file_builder.close()
#if you use this syntax you will overwrite all of that content on the file, you are not adding to it