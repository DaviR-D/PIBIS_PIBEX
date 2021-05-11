import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import json

class Builder1(Gtk.Window):
	def __init__(self):
		builder = Gtk.Builder()
		builder.add_from_file('UI/builder.glade')
		self.window = builder.get_object('1')
		self.options = []
		for x in range(1, 5):
			self.options.append(builder.get_object('op' + str(x)))
		self.alternativaCorreta = builder.get_object('correta')
		self.seletorImagem = builder.get_object('seletorImagem')
		self.build = dict()
		self.window.connect("delete-event", Gtk.main_quit)
		builder.connect_signals(self)

	def salvar(self, widget):
		self.build['imagem'] = self.seletorImagem.get_filename()
		for x in range(1, 5):
			self.build['op' + str(x)] = self.options[x - 1].get_text()

		self.build['correta'] = self.alternativaCorreta.get_text()
		with open("Custom/default.config", 'w') as config:
			json.dump(self.build, config)
		self.window.destroy()
