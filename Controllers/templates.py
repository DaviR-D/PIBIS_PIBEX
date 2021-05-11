
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

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
		builder.connect_signals(self)

	def onButtonClicked(self, widget): # Checa se o botão pressionado corresponde à resposta configurada como correta
		if(str(widget.id) == self.resposta):
			print("Correta")
		else:
			print("Errada")

class Template2(Gtk.Window):
	def __init__(self):
		builder = Gtk.Builder()
		builder.add_from_file('templates.glade')
		self.window = builder.get_object('2')
		self.window.connect("delete-event", Gtk.main_quit)
		builder.connect_signals(self)
