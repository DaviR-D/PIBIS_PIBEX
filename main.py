import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from Controllers import templateController, builderController

class Main(Gtk.Window):
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
		templateController.load('Custom/default.config')

	def newBuild(self, widget):
		builder = Gtk.Builder()
		builder.add_from_file('UI/main.glade')
		self.newWindow = builder.get_object('newWindow')
		self.createButton = builder.get_object('createButton')
		self.templateEntry = builder.get_object('templateEntry')
		builder.connect_signals(self)
		self.newWindow.show()

	def createButtonClicked(self, widget):
		builderController.Build(self.templateEntry.get_text())
		self.newWindow.destroy()




win = Main()
win.window.show()
Gtk.main()
