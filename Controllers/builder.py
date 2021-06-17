import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import json
from Controllers import builderController
from os import path
from shutil import copy2 as copy

class Builder(Gtk.Window):
	def __init__(self):
		self.builder = Gtk.Builder()
		self.builder.add_from_file('UI/builder.glade')
		self.file = list() # Dicionários contendo a configuração que será salva
		self.fileName = str() # Endereço em que a configuração será salva
		self.index = 0 # Index da lista de templates a serem configurados
		self.templateList = list() # Lista de templates

	def Next(self): # Chama o contrutor do próximo template da lista e salva caso for o último
		if(self.index < len(self.templateList)):
			builderController.Build(self.templateList, self.fileName, self.file, self.index)

		else:
			with open(self.fileName, 'w+') as config:
				json.dump(self.file, config)

		self.window.destroy()

	def addFile(self, file):
		filePath = 'Imagens/' + path.basename(file)
		if(not path.exists(filePath)):
			copy(file, 'Imagens')
		return filePath


class Builder1(Builder):
	def __init__(self):
		Builder.__init__(self)
		self.window = self.builder.get_object('1')
		self.options = list()
		for x in range(1, 5):
			self.options.append(self.builder.get_object('1input' + str(x)))
		self.alternativaCorreta = self.builder.get_object('1inputCorreta')
		self.seletorImagem = self.builder.get_object('1seletorImagem1')
		self.builder.connect_signals(self)

	def salvar(self, widget):
		self.file.append(dict())
		self.file[-1]['imagem'] = self.addFile(self.seletorImagem.get_filename())
		self.file[-1]['template'] = '1'
		for x in range(1, 5):
			self.file[-1]['option' + str(x)] = self.options[x - 1].get_text()
		self.file[-1]['correta'] = self.alternativaCorreta.get_text()
		self.Next()

class Builder2(Builder):
	def __init__(self):
		Builder.__init__(self)
		self.window = self.builder.get_object('2')
		self.seletorImagem = self.builder.get_object('2seletorImagem1')
		self.text = self.builder.get_object('2input1')
		self.button = self.builder.get_object('saveButton2')
		self.builder.connect_signals(self)

	def salvar(self, widget):
		self.file.append(dict())
		self.file[-1]['imagem'] = self.addFile(self.seletorImagem.get_filename())
		self.file[-1]['text'] = self.text.get_text()
		self.file[-1]['template'] = '2'
		self.Next()

class Builder3(Builder):
	def __init__(self):
		Builder.__init__(self)
		self.window = self.builder.get_object('3')
		self.seletoresImagem = list()
		self.textInputs = list()
		for x in range(1, 9):
			self.seletoresImagem.append(self.builder.get_object('3seletorImagem' + str(x)))
			self.textInputs.append(self.builder.get_object('3input' + str(x)))
		self.button = self.builder.get_object('saveButton3')
		self.builder.connect_signals(self)

	def salvar(self, widget):
		self.file.append(dict())
		for x in range(1, 9):
			self.file[-1]['imagem' + str(x)] = self.addFile(self.seletoresImagem[x - 1].get_filename())
			self.file[-1]['text' + str(x)] = self.textInputs[x - 1].get_text()
		self.file[-1]['template'] = '3'
		self.Next()

class Builder4(Builder):
	def __init__(self):
		Builder.__init__(self)
		self.window = self.builder.get_object('4')
		self.seletoresImagem = list()
		self.textInputs = list()
		self.button = self.builder.get_object('saveButton4')
		for x in range(1,5):
			self.seletoresImagem.append(self.builder.get_object('4seletorImagem' + str(x)))
			self.textInputs.append(self.builder.get_object('4input' + str(x)))

		self.builder.connect_signals(self)

	def salvar(self, widget):
		self.file.append(dict())
		for x in range(1, 5):
			self.file[-1]['imagem' + str(x)] = self.addFile(self.seletoresImagem[x - 1].get_filename())
			self.file[-1]['text' + str(x)] = self.textInputs[x - 1].get_text()
		self.file[-1]['template'] = '4'
		self.Next()

class Builder5(Builder):
	def __init__(self):
		Builder.__init__(self)
		self.window = self.builder.get_object('5')
		self.seletoresImagem = list()
		self.textInput = self.builder.get_object('5input1')
		self.button = self.builder.get_object('saveButton5')
		self.alternativaCorreta = self.builder.get_object('5inputCorreta')
		for x in range(1,6):
			self.seletoresImagem.append(self.builder.get_object('5seletorImagem' + str(x)))

		self.builder.connect_signals(self)

	def salvar(self, widget):
		self.file.append(dict())
		for x in range(1, 6):
			self.file[-1]['imagem' + str(x)] = self.addFile(self.seletoresImagem[x - 1].get_filename())
		self.file[-1]['text'] = self.textInput.get_text()
		self.file[-1]['correta'] = self.alternativaCorreta.get_text()
		self.file[-1]['template'] = '5'
		self.Next()

class Builder6(Builder):
	def __init__(self):
		Builder.__init__(self)
		self.window = self.builder.get_object('6')
		self.seletorImagem = self.builder.get_object('6seletorImagem1')
		self.button = self.builder.get_object('saveButton5')
		self.respostaCorreta = self.builder.get_object('6inputCorreta')
		self.builder.connect_signals(self)

	def salvar(self, widget):
		self.file.append(dict())
		self.file[-1]['imagem'] = self.addFile(self.seletorImagem.get_filename())
		self.file[-1]['correta'] = self.respostaCorreta.get_text()
		self.file[-1]['template'] = '6'
		self.Next()
