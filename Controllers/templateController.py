import gi
import json
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf, Gio
from Controllers import templates

def load(config, index): # Carrega uma janela vazia do template e a configura de acordo com a configuração recebida
    if (config[index]['template'] == '1'):
        win = templates.Template1()
        for x in range(1, 5):
            win.options[x - 1].set_label(config[index]['op' + str(x)])
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(config[index]['imagem'], width=500, height=300, preserve_aspect_ratio=False)
        win.image.set_from_pixbuf(pixbuf)
        win.resposta = config[index]['correta']
        win.next = [config, index + 1]
        win.window.show()
