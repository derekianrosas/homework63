#kwargs stand for key word arguments outputs a dictionary. Real magic is in the **
def greeting(**kwargs):
  print(kwargs)


greeting()
greeting(first = 'Kristine', last = 'Hudgens')

def greeting(**kwargs):
  if kwargs:
    print(f"Hi {kwargs['first']} {kwargs['last']}, have a great day!")
  else:
    print('Hi Guest!')


greeting()
greeting(first = 'Kristine', last = 'Hudgens')