import gi
import json
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf, Gio
from Controllers import templates
import random

def load(config, index=0, questionCount=0, rightAnswer=0, score=0): # Carrega uma janela vazia do template e a configura de acordo com a configuração recebida
    if (config[index]['template'] == '1'):
        win = templates.Template1()
        for x in range(1, 5):
            win.options[x - 1].set_label(config[index]['op' + str(x)])
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(config[index]['imagem'], width=500, height=300, preserve_aspect_ratio=False)
        win.image.set_from_pixbuf(pixbuf)
        win.respostaCorreta = config[index]['correta']

    elif(config[index]['template'] == '2'):
        win = templates.Template2()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(config[index]['imagem'], width=500, height=300, preserve_aspect_ratio=False)
        win.image.set_from_pixbuf(pixbuf)
        win.text.set_label(config[index]['texto'])

    elif(config[index]['template'] == '3'):
        win = templates.Template3()
        for x in range(1, 9):
            pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(config[index]['img' + str(x)], width=200, height=150, preserve_aspect_ratio=False)
            win.images[x - 1].set_from_pixbuf(pixbuf)
            win.texts[x - 1].set_label(config[index]['text' + str(x)])

    elif(config[index]['template'] == '4'):
        win = templates.Template4()
        randomindex = list(range(1, 5))
        random.shuffle(randomindex)
        win.respostaCorreta = randomindex

        for x, y in zip(range(1, 5), randomindex):
            pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(config[index]['img' + str(x)], width=100, height=100, preserve_aspect_ratio=False)
            win.images[x - 1].set_from_pixbuf(pixbuf)
            win.texts[x - 1].set_label(config[index]['text' + str(y)])

    elif(config[index]['template'] == '5'):
        win = templates.Template5()
        win.respostaCorreta = config[index]['correta']
        win.text.set_label(config[index]['text'])
        for x in range(1, 6):
            pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(config[index]['img' + str(x)], width=200, height=150, preserve_aspect_ratio=False)
            win.images[x - 1].set_from_pixbuf(pixbuf)

    elif(config[index]['template'] == '6'):
        win = templates.Template6()
        win.respostaCorreta = config[index]['correta']
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(config[index]['img'], width=200, height=150, preserve_aspect_ratio=False)
        win.image.set_from_pixbuf(pixbuf)

    win.questionCount = questionCount
    win.rightAnswer = rightAnswer
    win.Score = score
    win.config = config
    win.index = index + 1
    win.window.show()
