post = ('Python Basics', 'Intro guide to python', 'Some cool python content') #the tuple list
#post = post + ('published',) #adding to tuples with new variable
#title, sub_headering, content, status = post #unpacking tuple by assigning every string a variable
#print(title)
#print(sub_headering)
#print(content)
#print(status)
#leveraged reassignment and used a variable to create a new list and add on to the list
#concatenating them
#tuple
#tuple with nested string and a list inside of that identical for when we added a new string element
# tags = ['python', 'coding', 'tutorial']
# post += (tags,)  #comma is needed, python thinks we are overiding order of operations
# print(post[-1][1]) #you can traverse this tuple the same way as a nested list
# guide to slices in tuples
#print(post[1::2]) #key difference is it prints out a tuple all of the same rules apply
# three ways to remove elements from the tuple by definition cannot be changed
# removing elements from end
#post = post[:-1]
#print(post)
#removing from beginning
#post = post[1:]
#print(post)
#removing specific element(messy/not recommended)
post = list(post) #bad idea that at some point you dont change it back, it causes bugs since you expected tuple instead of list
post.remove('Python Basics')
post = tuple(post)
print(post)