
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from Controllers import templateController
from time import sleep

class Template(Gtk.Window):
	def __init__(self):
		self.builder = Gtk.Builder()
		self.builder.add_from_file('UI/templates.glade')
		self.next = []
		self.Score = [0, 0, 0]

	def Next(self, widget): # Chama o próximo template da lista
		self.window.destroy()
		if(len(self.next[0]) > self.next[1]):
			templateController.load(*self.next, self.Score)
		elif(self.Score[0]):
			self.finalWindow = self.builder.get_object('finalWindow')
			self.finalText = self.builder.get_object('finalText')
			self.finalText.set_label('Você acertou ' + str(self.Score[1]) + ' de ' + str(self.Score[0]) + ' questões\n' 'Pontuação:' + str(self.Score[2]))
			self.Score[0] = 0
			self.finalWindow.show()

	def leave(self, widget):
		self.finalWindow.destroy()

	def onButtonClicked():
		pass


class TemplateQuestion(Template):
	def __init__(self):
		Template.__init__(self)
		self.respostaCorreta = ''
		self.resposta = ''

	def Correta(self):
		self.corretaWindow = self.builder.get_object('corretaWindow')
		self.corretaWindow.show()
		for x in range(15):
			while Gtk.events_pending():
				Gtk.main_iteration()
			sleep(0.1)
		self.corretaWindow.destroy()


	def Errada(self):
		self.erradaWindow = self.builder.get_object('erradaWindow')
		self.erradaWindow.show()
		for x in range(15):
			while Gtk.events_pending():
				Gtk.main_iteration()
			sleep(0.1)
		self.erradaWindow.destroy()

	def Check(self, widget): # Checa se a resposta recebida corresponde à resposta configurada como correta
		self.Score[0] += 1

		if(self.resposta == self.respostaCorreta):
			self.Score[2] += 10
			self.Score[1] += 1
			self.Correta()
		else:
			self.Score[2] -= 5
			self.Errada()

		self.Next(widget)


class Template1(TemplateQuestion):
	def __init__(self):
		TemplateQuestion.__init__(self)
		self.window = self.builder.get_object('1')
		self.options = []
		for x in range(1,5):
			self.options.append(self.builder.get_object('op' + str(x)))
			self.options[x - 1].id = x
		self.image = self.builder.get_object('image')
		self.builder.connect_signals(self)

	def onButtonClicked(self, widget):
		self.resposta = str(widget.id)
		self.Check(widget)



class Template2(Template):
	def __init__(self):
		Template.__init__(self)
		self.window = self.builder.get_object('2')
		self.image = self.builder.get_object('image2')
		self.text = self.builder.get_object('text')
		self.builder.connect_signals(self)


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
