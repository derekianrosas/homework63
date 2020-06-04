#a tool that allows you to wrap up a functiuon and pass it to other functions
#first class citizen
full_name = lambda first, last: f'{first} {last}'


def greeting(name):
  print(f'Hi there {name}')


greeting(full_name('Kristine', 'Hudgens'))
