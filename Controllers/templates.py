
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from Controllers import templateController

class Template(Gtk.Window):
	def __init__(self):
		self.builder = Gtk.Builder()
		self.builder.add_from_file('UI/templates.glade')
		self.next = []

	def Next(self): # Chama o próximo template da lista
		if(len(self.next[0]) > self.next[1]):
			templateController.load(*self.next)

class Template1(Template):
	def __init__(self):
		Template.__init__(self)
		self.window = self.builder.get_object('1')
		self.options = []
		for x in range(1,5):
			self.options.append(self.builder.get_object('op' + str(x)))
			self.options[x - 1].id = x
		self.image = self.builder.get_object('image')
		self.resposta = ''
		self.builder.connect_signals(self)

	def onButtonClicked(self, widget): # Checa se o botão pressionado corresponde à resposta configurada como correta
		if(str(widget.id) == self.resposta):
			print("Correta")
		else:
			print("Errada")
		self.Next()
		self.window.destroy()

class Template2(Template):
	def __init__(self):
		Template.__init__(self)
		self.window = self.builder.get_object('2')
		self.image = self.builder.get_object('image2')
		self.text = self.builder.get_object('text')
		self.builder.connect_signals(self)

	def	onButtonClicked(self, widget):
			self.Next()
			self.window.destroy()

class Template3(Template):
	def __init__(self):
		Template.__init__(self)
		self.window = self.builder.get_object('3')
		self.images = []
		self.texts = []
		for x in range(1,9):
			self.images.append(self.builder.get_object('img' + str(x)))
		for x in range(1, 9):
			self.texts.append(self.builder.get_object('text' + str(x)))
		self.builder.connect_signals(self)

	def onButtonClicked(self, widget):
		self.Next()
		self.window.destroy()
