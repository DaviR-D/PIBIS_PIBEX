
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from Controllers import templateController

class Template1(Gtk.Window):
	def __init__(self):
		builder = Gtk.Builder()
		builder.add_from_file('UI/templates.glade')
		self.window = builder.get_object('1')
		self.options = []
		for x in range(1,5):
			self.options.append(builder.get_object('op' + str(x)))
			self.options[x - 1].id = x
		self.image = builder.get_object('image')
		self.resposta = ''
		self.next = []
		builder.connect_signals(self)

	def onButtonClicked(self, widget): # Checa se o botão pressionado corresponde à resposta configurada como correta
		if(str(widget.id) == self.resposta):
			print("Correta")
		else:
			print("Errada")
		if(len(self.next[0]) > self.next[1]):
			templateController.load(self.next[0], self.next[1])
		self.window.destroy()

class Template2(Gtk.Window):
	def __init__(self):
		builder = Gtk.Builder()
		builder.add_from_file('UI/templates.glade')
		self.window = builder.get_object('2')
		self.image = builder.get_object('image2')
		self.text = builder.get_object('text')
		self.next = []
		builder.connect_signals(self)

	def	onButtonClicked(self, widget):
			if(len(self.next[0]) > self.next[1]):
				templateController.load(self.next[0], self.next[1])
			self.window.destroy()

class Template3(Gtk.Window):
	def __init__(self):
		builder = Gtk.Builder()
		builder.add_from_file('UI/templates.glade')
		self.window = builder.get_object('3')
		self.images = []
		self.texts = []
		for x in range(1,9):
			self.images.append(builder.get_object('img' + str(x)))
		for x in range(1, 9):
			self.texts.append(builder.get_object('text' + str(x)))
		self.next = []
		builder.connect_signals(self)

	def onButtonClicked(self, widget):
		if(len(self.next[0]) > self.next[1]):
			templateController.load(self.next[0], self.next[1])
		self.window.destroy()
