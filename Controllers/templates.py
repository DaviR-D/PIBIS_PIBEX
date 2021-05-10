
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Template1(Gtk.Window):
	def __init__(self):
		builder = Gtk.Builder()
		builder.add_from_file('UI/templates.glade')
		self.window = builder.get_object('1')
		self.op1 = builder.get_object('op1')
		self.op1.id = '1'
		self.op2 = builder.get_object('op2')
		self.op2.id = '2'
		self.op3 = builder.get_object('op3')
		self.op3.id = '3'
		self.op4 = builder.get_object('op4')
		self.op4.id = '4'
		self.image = builder.get_object('image')
		self.resposta = ''
		builder.connect_signals(self)

	def onButtonClicked(self, widget):
		if(widget.id == self.resposta):
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
