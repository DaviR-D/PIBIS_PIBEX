import gi
import json
import random
from glob import glob
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf, Gio
from os.path import basename
from Controllers import templateController, builderController

class Main(Gtk.Window): # Carrega elementos UI
	def __init__(self):
		self.builder = Gtk.Builder()
		self.builder.add_from_file('UI/main.glade')
		self.window = self.builder.get_object('mainWindow')
		self.newButton = self.builder.get_object('new')
		self.loadButton = self.builder.get_object('load')
		self.deleteButton = self.builder.get_object('delete')
		self.randomButton = self.builder.get_object('random')
		self.loadButton.set_current_folder('Custom')
		self.window.connect("delete-event", Gtk.main_quit)
		self.builder.connect_signals(self)


	def newBuild(self, widget): # Carrega e apresenta a janela de seleção de templates e nome para a nova configuração
		self.builder = Gtk.Builder()
		self.builder.add_from_file('UI/main.glade')
		self.newWindow = self.builder.get_object('newWindow')
		self.createButton = self.builder.get_object('createButton')
		self.templateEntry = self.builder.get_object('templateEntry')
		self.nameChooser = self.builder.get_object('nameChooser')
		self.categoria = self.builder.get_object('categoria')
		self.dificuldade = self.builder.get_object('dificuldade')
		self.loadTemplateExamples()
		self.builder.connect_signals(self)
		self.newWindow.show()

	def createButtonClicked(self, widget): # Passa a lista de templates selecionados e o nome do arquivo para o builderController
		file = list()
		file.append(self.dificuldade.get_active_id())
		file.append(self.categoria.get_active_id())
		builderController.Build(self.templateEntry.get_text().split(), 'Custom/' + self.nameChooser.get_text() + '.config', file)
		self.newWindow.destroy()

	def random(self, widget): # Carrega a janela de configuração aleatória
		self.builder = Gtk.Builder()
		self.builder.add_from_file('UI/main.glade')
		self.randomWindow = self.builder.get_object('randomWindow')
		self.categoria = self.builder.get_object('categoria1')
		self.dificuldade = self.builder.get_object('dificuldade1')
		self.builder.connect_signals(self)
		self.randomWindow.show()

	def loadButtonSet(self, widget):
		self.loadConfig(self.loadButton.get_filename())

	def loadConfig(self, config):
		with open(config) as conf:
			build = json.load(conf)
		templateController.load(build, basename(config)[:-7:])

	def loadRandom(self, widget):
		categoria = self.categoria.get_active_id()
		dificuldade = self.dificuldade.get_active_id()
		listConfig = glob('Custom/*')
		random.shuffle(listConfig)
		for config in listConfig:
			with open(config) as conf:
				build = json.load(conf)
				if(build[0], build[1] == dificuldade, categoria):
					self.loadConfig(config)
					break

	def loadTemplateExamples(self):
		self.img = []
		for x in range(1, 5):
			self.img.append(self.builder.get_object('img' + str(x)))
			pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale('Imagens/t' + str(x) + '.png', width=250, height=400, preserve_aspect_ratio=False)
			self.img[-1].set_from_pixbuf(pixbuf)
		self.img.append(self.builder.get_object('img5'))
		pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale('Imagens/t5.png', width=400, height=250, preserve_aspect_ratio=False)
		self.img[-1].set_from_pixbuf(pixbuf)
		self.img.append(self.builder.get_object('img6'))
		pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale('Imagens/t6.png', width=250, height=400, preserve_aspect_ratio=False)
		self.img[-1].set_from_pixbuf(pixbuf)
		self.img.append(self.builder.get_object('img7'))
		pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale('Imagens/t7.png', width=400, height=250, preserve_aspect_ratio=False)
		self.img[-1].set_from_pixbuf(pixbuf)
		self.img.append(self.builder.get_object('img8'))
		pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale('Imagens/t8.png', width=250, height=400, preserve_aspect_ratio=True)
		self.img[-1].set_from_pixbuf(pixbuf)


win = Main()
win.window.show()
Gtk.main()
