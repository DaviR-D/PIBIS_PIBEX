import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from Controllers import templates, builder

win = builder.Builder1()
win.window.show()
