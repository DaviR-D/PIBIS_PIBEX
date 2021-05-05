import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from Controllers import builder, controller

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

	def onDefaultClicked(self, widget):
		controller.win.window.show()


win = Main()
win.window.show()
Gtk.main()
