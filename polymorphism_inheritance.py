#build out an html class and multiple sub classes, that can render custom versions of that html
class Heading: #subclass
	def __init__(self, content):
		self.content = content
	def render(self):
		return f'<h1>{self.content}</h1>'

class Div: #subclass
	def __init__(self, content):
		self.content = content
	def render(self):
		return f'<div>{self.content}</div>'


div_one = Div('some content')
heading = Heading('some big heading')
div_two = Div('Another Div')

def html_render(tag_object):
	print(tag_object.render())

html_render(div_one)
html_render(div_two)
html_render(heading)

#used functions instead of parent classes
#when to use one or the other, if you have quite a bit shared behavior, then that would be inheritance.
#if not much shared behavior but you want to call the same function, use polymorphism with functions