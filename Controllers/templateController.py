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

    elif(config[index]['template'] == '2'):
        win = templates.Template2()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(config[index]['imagem'], width=500, height=300, preserve_aspect_ratio=False)
        win.image.set_from_pixbuf(pixbuf)
        win.text.set_label(config[index]['texto'])

    elif(config[index]['template'] == '3'):
        win = templates.Template3()
        for x in range(1, 9):
            pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(config[index]['img' + str(x)], width=100, height=100, preserve_aspect_ratio=False)
            win.images[x - 1].set_from_pixbuf(pixbuf)
            win.texts[x - 1].set_label(config[index]['text' + str(x)])

    win.next = [config, index + 1]
    win.window.show()
