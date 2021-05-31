import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf, Gio
from Controllers import templateController, builderController
import json

class Main(Gtk.Window): # Carrega elementos UI
	def __init__(self):
		self.builder = Gtk.Builder()
		self.builder.add_from_file('UI/main.glade')
		self.window = self.builder.get_object('mainWindow')
		self.newButton = self.builder.get_object('new')
		self.loadButton = self.builder.get_object('load')
		self.deleteButton = self.builder.get_object('delete')
		self.randomButton = self.builder.get_object('random')
		self.defaultButton = self.builder.get_object('default')
		self.window.connect("delete-event", Gtk.main_quit)
		self.builder.connect_signals(self)

	def defaultBuild(self, widget):
		pass

	def newBuild(self, widget): # Carrega e apresenta a janela de seleção de templates e nome para a nova configuração
		self.newWindow = self.builder.get_object('newWindow')
		self.createButton = self.builder.get_object('createButton')
		self.templateEntry = self.builder.get_object('templateEntry')
		self.nameChooser = self.builder.get_object('nameChooser')
		self.img = []
		for x in range(1, 7):
			self.img.append(self.builder.get_object('img' + str(x)))
			pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale('Imagens/t' + str(x) + '.png', width=250, height=400, preserve_aspect_ratio=False)
			self.img[x - 1].set_from_pixbuf(pixbuf)
		self.builder.connect_signals(self)
		self.newWindow.show()

	def createButtonClicked(self, widget): # Passa a lista de templates selecionados e o nome do arquivo para o builderController
		builderController.Build(self.templateEntry.get_text().split(), 'Custom/' + self.nameChooser.get_text() + '.config')
		self.newWindow.destroy()

	def load(self, wiget):
		with open (self.loadButton.get_filename()) as conf:
			build = json.load(conf)
		templateController.load(build)




win = Main()
win.window.show()
Gtk.main()
