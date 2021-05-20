import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import json
from Controllers import builderController

class Builder(Gtk.Window):
	def __init__(self):
		self.builder = Gtk.Builder()
		self.builder.add_from_file('UI/builder.glade')
		self.file = [] # Armazena os dicionários contendo a configuração que será salva
		self.fileName = ''
		self.index = 0
		self.templateList = []

	def Next(self): # Chama o contrutor do próximo template da lista e salva caso for o último
		if(self.index < len(self.templateList)):
			builderController.Build(self.templateList, self.fileName, self.file, self.index)

		else:
			with open(self.fileName, 'w+') as config:
				json.dump(self.file, config)

		self.window.destroy()


class Builder1(Builder):
	def __init__(self):
		Builder.__init__(self)
		self.window = self.builder.get_object('1')
		self.options = []
		for x in range(1, 5):
			self.options.append(self.builder.get_object('op' + str(x)))
		self.alternativaCorreta = self.builder.get_object('correta')
		self.seletorImagem = self.builder.get_object('seletorImagem')
		self.window.connect("delete-event", Gtk.main_quit)
		self.builder.connect_signals(self)

	def salvar(self, widget):
		self.file.append(dict())
		self.file[-1]['imagem'] = self.seletorImagem.get_filename()
		self.file[-1]['template'] = '1'
		for x in range(1, 5):
			self.file[-1]['op' + str(x)] = self.options[x - 1].get_text()
		self.file[-1]['correta'] = self.alternativaCorreta.get_text()
		self.Next()

class Builder2(Builder):
	def __init__(self):
		Builder.__init__(self)
		self.window = self.builder.get_object('2')
		self.seletorImagem = self.builder.get_object('seletorImagem1')
		self.text = self.builder.get_object('text')
		self.button = self.builder.get_object('saveButton1')
		self.builder.connect_signals(self)
		self.window.connect("delete-event", Gtk.main_quit)

	def salvar(self, widget):
		self.file.append(dict())
		self.file[-1]['imagem'] = self.seletorImagem.get_filename()
		self.file[-1]['texto'] = self.text.get_text()
		self.file[-1]['template'] = '2'
		self.Next()

class Builder3(Builder):
	def __init__(self):
		Builder.__init__(self)
		self.window = self.builder.get_object('3')
		self.seletoresImagem = []
		self.textInputs = []
		for x in range(1, 9):
			self.seletoresImagem.append(self.builder.get_object('seletorImagem' + str(x + 1)))
			self.textInputs.append(self.builder.get_object('textInput' + str(x)))
		self.button = self.builder.get_object('saveButton2')
		self.builder.connect_signals(self)
		self.window.connect("delete-event", Gtk.main_quit)

	def salvar(self, widget):
		self.file.append(dict())
		for x in range(1, 9):
			self.file[-1]['img' + str(x)] = self.seletoresImagem[x - 1].get_filename()
			self.file[-1]['text' + str(x)] = self.textInputs[x - 1].get_text()
		self.file[-1]['template'] = '3'
		self.Next()
