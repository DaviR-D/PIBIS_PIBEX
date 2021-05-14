import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from Controllers import templateController, builderController
import json

class Main(Gtk.Window): # Carrega elementos UI
	def __init__(self):
		builder = Gtk.Builder()
		builder.add_from_file('UI/main.glade')
		self.window = builder.get_object('mainWindow')
		self.newButton = builder.get_object('new')
		self.loadButton = builder.get_object('load')
		self.deleteButton = builder.get_object('delete')
		self.randomButton = builder.get_object('random')
		self.defaultButton = builder.get_object('default')
		self.window.connect("delete-event", Gtk.main_quit)
		builder.connect_signals(self)

	def defaultBuild(self, widget):
		with open ('Custom/default.config') as conf:
			build = json.load(conf)
		templateController.load(build, 0)

	def newBuild(self, widget): # Carrega e apresenta a janela de seleção de templates para a nova configuração
		builder = Gtk.Builder()
		builder.add_from_file('UI/main.glade')
		self.newWindow = builder.get_object('newWindow')
		self.createButton = builder.get_object('createButton')
		self.templateEntry = builder.get_object('templateEntry')
		builder.connect_signals(self)
		self.newWindow.show()

	def createButtonClicked(self, widget): # Passa a lista de templates selecionados e o arquivo para o builderController
		builderController.Build(self.templateEntry.get_text().split(), 0, [], 'Custom/default.config')
		self.newWindow.destroy()




win = Main()
win.window.show()
Gtk.main()
