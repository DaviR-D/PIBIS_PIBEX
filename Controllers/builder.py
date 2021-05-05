import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import json

class Builder1(Gtk.Window):
	def __init__(self):
		builder = Gtk.Builder()
		builder.add_from_file('UI/builder.glade')
		self.window = builder.get_object('1')
		self.op1 = builder.get_object('op1')
		self.op2 = builder.get_object('op2')
		self.op3 = builder.get_object('op3')
		self.op4 = builder.get_object('op4')
		self.alternativaCorreta = builder.get_object('correta')
		self.seletorImagem = builder.get_object('seletorImagem')
		self.build = dict()
		self.window.connect("delete-event", Gtk.main_quit)
		builder.connect_signals(self)

	def salvar(self, widget):
		with open("Custom/default.config", 'w') as config:
			json.dump(self.build, config)
