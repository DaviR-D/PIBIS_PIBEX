
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Template1(Gtk.Window):
	def __init__(self):
		builder = Gtk.Builder()
		builder.add_from_file('UI/templates.glade')
		self.window = builder.get_object('1')
		self.window.connect("delete-event", Gtk.main_quit)
		builder.connect_signals(self)

class Template2(Gtk.Window):
	def __init__(self):
		builder = Gtk.Builder()
		builder.add_from_file('templates.glade')
		self.window = builder.get_object('2')
		self.window.connect("delete-event", Gtk.main_quit)
		builder.connect_signals(self)
