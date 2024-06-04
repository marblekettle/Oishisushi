class Tab(object):
	def __init__(self, text, url):
		self.text = text
		self.url = url

tabs = [
	Tab('Home', 'home.home'),
	Tab('Menu', 'menu.menu'),
	Tab('About','home.home')
]
