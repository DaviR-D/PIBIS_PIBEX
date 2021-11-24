import gi
import json
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf, Gio
from Controllers import templates
import random

def load(config, index=2, questionCount=0, rightAnswer=0, score=0): # Carrega e configura o template recebido

    win = eval('buildTemplate' + str(config[index]['template']))(config, index)
    win.questionCount = questionCount
    win.rightAnswer = rightAnswer
    win.Score = score
    win.config = config
    win.index = index + 1
    win.window.show()

def buildTemplate1(config, index):
    win = templates.Template1()
    for x in range(1, 5):
        win.options[x - 1].set_label(config[index]['option' + str(x)])
    pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(config[index]['imagem'], width=500, height=300, preserve_aspect_ratio=False)
    win.image.set_from_pixbuf(pixbuf)
    win.respostaCorreta = config[index]['correta']
    return win

def buildTemplate2(config, index):
    win = templates.Template2()
    pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(config[index]['imagem'], width=500, height=300, preserve_aspect_ratio=False)
    win.image.set_from_pixbuf(pixbuf)
    win.text.set_label(config[index]['text'])
    return win

def buildTemplate3(config, index):
    win = templates.Template3()
    for x in range(1, 9):
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(config[index]['imagem' + str(x)], width=200, height=150, preserve_aspect_ratio=False)
        win.images[x - 1].set_from_pixbuf(pixbuf)
        win.texts[x - 1].set_label(config[index]['text' + str(x)])
    return win

def buildTemplate4(config, index):
    win = templates.Template4()
    randomindex = list(range(1, 5))
    random.shuffle(randomindex)
    win.respostaCorreta = randomindex

    for x, y in zip(range(1, 5), randomindex):
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(config[index]['imagem' + str(x)], width=100, height=100, preserve_aspect_ratio=False)
        win.images[x - 1].set_from_pixbuf(pixbuf)
        win.texts[x - 1].set_label(config[index]['text' + str(y)])
    win.window.show()
    win.janelaExplic.show()
    return win

def buildTemplate5(config, index):
    win = templates.Template5()
    win.respostaCorreta = config[index]['correta']
    win.text.set_label(config[index]['text'])
    for x in range(1, 6):
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(config[index]['imagem' + str(x)], width=200, height=150, preserve_aspect_ratio=False)
        win.images[x - 1].set_from_pixbuf(pixbuf)
    return win

def buildTemplate6(config, index):
    win = templates.Template6()
    win.respostaCorreta = config[index]['correta'].lower()
    pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(config[index]['imagem'], width=500, height=300, preserve_aspect_ratio=False)
    win.image.set_from_pixbuf(pixbuf)
    return win

#def buildTemplate7(config, index):
#    t1 = buildTemplate1(config, index)
#    t2 = buildTemplate2([{'imagem':config[index][imagem], 'text':config[index]['correta']}], 0)
#    win = templates.Template7()
#    win = t2
#    win.t1 = t1
#    win.t2 = t2
