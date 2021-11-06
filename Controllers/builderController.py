import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from Controllers import builder

def Build(templates, fileName, file=[], index=0): # Carrega uma janela de criação de configuração para cada template da lista
    Builder = eval('builder.Builder' + str(templates[index]))()
    Builder.templateList = templates
    Builder.index = index + 1
    Builder.file = file
    Builder.fileName = fileName
    Builder.window.show()
