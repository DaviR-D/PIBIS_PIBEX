
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from Controllers import templateController
from time import sleep

class Template(Gtk.Window):
	def __init__(self):
		self.builder = Gtk.Builder()
		self.builder.add_from_file('UI/templates.glade')
		self.config = list()
		self.index = list()

	def Next(self, widget): # Chama o próximo template da lista
		self.window.destroy()
		if(len(self.config) > self.index):
			templateController.load(self.config, self.index, self.questionCount, self.rightAnswer, self.Score)
		elif(self.questionCount):
			self.final()

	def final(self): # Carrega a janela final
		self.finalWindow = self.builder.get_object('finalWindow')
		self.finalText = self.builder.get_object('finalText')
		self.finalText.set_label(
		'Você acertou '
		+ str(self.rightAnswer)
		+ ' de ' + str(self.questionCount)
		+ ' questões\n' 'Pontuação:'
		+ str(self.Score))
		self.finalWindow.show()

	def leave(self, widget):
		self.finalWindow.destroy()
		del self

	def onButtonClicked():
		pass


class TemplateQuestion(Template):
	def __init__(self):
		Template.__init__(self)
		self.respostaCorreta = str()
		self.resposta = str()
		self.questionCount = 0
		self.rightAnswer = 0
		self.Score = 0
		self.mostrarCorreta = True

	def Check(self, widget): # Checa se a resposta recebida corresponde à resposta configurada como correta
		self.questionCount += 1

		if(self.resposta == self.respostaCorreta):
			self.Score += 10
			self.rightAnswer += 1
			self.resultWindow = self.builder.get_object('corretaWindow')

		else:
			self.Score -= 5
			self.resultWindow = self.builder.get_object('erradaWindow')

		self.window.hide()
		self.result()
		self.Next(widget)

		if(self.mostrarCorreta):
			self.showRightAnswer()

	def result(self):
		self.resultWindow.show()
		for x in range(15):
			while Gtk.events_pending():
				Gtk.main_iteration()
			sleep(0.1)
		self.resultWindow.destroy()

	def showRightAnswer(self):
		self.resultWindow = self.builder.get_object('respostaCorreta')
		self.respostaTexto = self.builder.get_object('resposta')
		resposta = self.config[self.index - 1]['option' + str(self.respostaCorreta)]
		self.respostaTexto.set_label('A respsota correta é: ' + resposta)
		self.result()



class Template1(TemplateQuestion):
	def __init__(self):
		TemplateQuestion.__init__(self)
		self.window = self.builder.get_object('1')
		self.options = list()
		for x in range(1,5):
			self.options.append(self.builder.get_object('1option' + str(x)))
			self.options[x - 1].id = x
		self.image = self.builder.get_object('1image1')
		self.builder.connect_signals(self)

	def onButtonClicked(self, widget):
		self.resposta = str(widget.id)
		self.Check(widget)



class Template2(Template):
	def __init__(self):
		Template.__init__(self)
		self.window = self.builder.get_object('2')
		self.image = self.builder.get_object('2image1')
		self.text = self.builder.get_object('2text1')
		self.builder.connect_signals(self)


class Template3(Template):
	def __init__(self):
		Template.__init__(self)
		self.window = self.builder.get_object('3')
		self.images = list()
		self.texts = list()
		for x in range(1,9):
			self.images.append(self.builder.get_object('3image' + str(x)))
		for x in range(1, 9):
			self.texts.append(self.builder.get_object('3text' + str(x)))
		self.builder.connect_signals(self)

class Template4(TemplateQuestion):
	def __init__(self):
		TemplateQuestion.__init__(self)
		self.window = self.builder.get_object('4')
		self.janelaExplic = self.builder.get_object('explicT4')
		self.images = list()
		self.texts = list()
		self.inputs = list()
		for x in range(1,5):
			self.images.append(self.builder.get_object('4image' + str(x)))
			self.texts.append(self.builder.get_object('4text' + str(x)))
			self.inputs.append(self.builder.get_object('4input' + str(x)))

		self.builder.connect_signals(self)

	def onButtonClicked(self, widget):
		self.resposta = list()
		for input in self.inputs:
			self.resposta.append(int(input.get_text()))
		self.Check(widget)
	def okBtn(self, widget):
		self.janelaExplic.hide()

class Template5(TemplateQuestion):
	def __init__(self):
		TemplateQuestion.__init__(self)
		self.window = self.builder.get_object('5')
		self.images = list()
		self.options = list()
		self.text = self.builder.get_object('5text1')
		for x in range(1,6):
			self.images.append(self.builder.get_object('5image' + str(x)))
			self.options.append(self.builder.get_object('5option' + str(x)))
			self.options[x - 1].id = x


		self.builder.connect_signals(self)

	def onButtonClicked(self, widget):
		self.resposta = str(widget.id)
		self.Check(widget)

class Template6(TemplateQuestion):
	def __init__(self):
		TemplateQuestion.__init__(self)
		self.window = self.builder.get_object('6')
		self.image = self.builder.get_object('6image1')
		self.input = self.builder.get_object('6input1')
		self.builder.connect_signals(self)

	def onButtonClicked(self, widget):
		self.resposta = self.input.get_text().lower()
		self.Check(widget)

#class Template7(Template1):
#	def __init__(self):
#		Template1.__init__(self)
#		t2 = ''
#	def onButtonClicked(self, widget):
#		self.questionCount += 1
#
#		if(self.resposta == self.respostaCorreta):
#			self.Score += 10
#			self.rightAnswer += 1
#			self.resultWindow = self.builder.get_object('corretaWindow')
#
#		else:
#			self.Score -= 5
#			self.resultWindow = self.builder.get_object('erradaWindow')
#
