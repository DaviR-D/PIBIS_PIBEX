import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from UI import templates


win = templates.Template1()
win.window.show()
Gtk.main()
