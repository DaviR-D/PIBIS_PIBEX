import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from Controllers import builder

def Build(templates, fileName, file=[], index=0): # Carrega uma janela de criação de configuração para cada template da lista
    Builders = [builder.Builder1,
    builder.Builder2,
    builder.Builder3,
    builder.Builder4,
    builder.Builder5,
    builder.Builder6]

    Builder = Builders[int(templates[index]) - 1]()

    Builder.templateList = templates
    Builder.index = index + 1
    Builder.file = file
    Builder.fileName = fileName
    Builder.window.show()
