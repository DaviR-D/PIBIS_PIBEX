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
		self.build = {'imagem':'', 'op1':'', 'op2':'', 'op3':'', 'op4':'', 'correta':''}
		self.window.connect("delete-event", Gtk.main_quit)
		builder.connect_signals(self)

	def salvar(self, widget):
		self.build['imagem'] = self.seletorImagem.get_filename()
		self.build['op1'] = self.op1.get_text()
		self.build['op2'] = self.op2.get_text()
		self.build['op3'] = self.op3.get_text()
		self.build['op4'] = self.op4.get_text()
		self.build['correta'] = self.alternativaCorreta.get_text()
		with open("Custom/default.config", 'w') as config:
			json.dump(self.build, config)
