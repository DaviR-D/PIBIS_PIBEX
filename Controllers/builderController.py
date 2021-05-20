import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from Controllers import builder

def Build(templates, fileName, file=[], index=0): # Carrega uma janela de criação de configuração para cada template da lista
    if (int(templates[index]) == 1):
        Builder = builder.Builder1()

    elif (int(templates[index]) == 2):
        Builder = builder.Builder2()

    elif (int(templates[index]) == 3):
        Builder = builder.Builder3()

    Builder.templateList = templates
    Builder.index = index + 1
    Builder.file = file
    Builder.fileName = fileName
    Builder.window.show()
