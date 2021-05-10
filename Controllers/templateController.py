import gi
import json
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf, Gio
from Controllers import templates

def load(config):
    with open(config) as conf:
    	build = json.load(conf)
    win = templates.Template1()
    win.op1.set_label(build['op1'])
    win.op2.set_label(build['op2'])
    win.op3.set_label(build['op3'])
    win.op4.set_label(build['op4'])
    pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(build['imagem'], width=500, height=300, preserve_aspect_ratio=False)
    win.image.set_from_pixbuf(pixbuf)
    win.resposta = build['correta']
    win.window.show()
