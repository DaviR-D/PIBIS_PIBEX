import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import json
from Controllers import builderController

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
		self.file = []
		self.next = [[], int()]
		self.window.connect("delete-event", Gtk.main_quit)
		builder.connect_signals(self)

	def salvar(self, widget):
		self.file.append(dict())
		self.file[-1]['imagem'] = self.seletorImagem.get_filename()
		self.file[-1]['template'] = '1'
		for x in range(1, 5):
			self.file[-1]['op' + str(x)] = self.options[x - 1].get_text()

		self.file[-1]['correta'] = self.alternativaCorreta.get_text()
		with open("Custom/default.config", 'w') as config:
			json.dump(self.file, config)
		if(self.next[1] < len(self.next[0])):
			builderController.Build(self.next[0], self.next[1], self.file)
		self.window.destroy()

class Builder2(Gtk.Window):
	def __init__(self):
		builder = Gtk.Builder()
		builder.add_from_file('UI/builder.glade')
		self.window = builder.get_object('2')
		self.seletorImagem = builder.get_object('seletorImagem1')
		self.text = builder.get_object('text')
		self.button = builder.get_object('saveButton1')
		self.file = []
		self.next = [[], int()]
		builder.connect_signals(self)
		self.window.connect("delete-event", Gtk.main_quit)

	def salvar(self, widget):
		self.file.append(dict())
		self.file[-1]['imagem'] = self.seletorImagem.get_filename()
		self.file[-1]['texto'] = self.text.get_text()
		self.file[-1]['template'] = '2'
		with open("Custom/default.config", 'w') as config:
			json.dump(self.file, config)
		if(self.next[1] < len(self.next[0])):
			builderController.Build(self.next[0], self.next[1], self.file)
		self.window.destroy()

class Builder3(Gtk.Window):
	def __init__(self):
		builder = Gtk.Builder()
		builder.add_from_file('UI/builder.glade')
		self.window = builder.get_object('3')
		self.seletoresImagem = []
		self.textInputs = []
		for x in range(1, 9):
			self.seletoresImagem.append(builder.get_object('seletorImagem' + str(x + 1)))
			self.textInputs.append(builder.get_object('textInput' + str(x)))
		self.button = builder.get_object('saveButton2')
		self.file = []
		self.next = [[], int()]
		builder.connect_signals(self)
		self.window.connect("delete-event", Gtk.main_quit)

	def salvar(self, widget):
		self.file.append(dict())
		for x in range(1, 9):
			self.file[-1]['img' + str(x)] = self.seletoresImagem[x - 1].get_filename()
			self.file[-1]['text' + str(x)] = self.textInputs[x - 1].get_text()
		self.file[-1]['template'] = '3'
		with open("Custom/default.config", 'w') as config:
			json.dump(self.file, config)
		if(self.next[1] < len(self.next[0])):
			builderController.Build(self.next[0], self.next[1], self.file)
		self.window.destroy()
