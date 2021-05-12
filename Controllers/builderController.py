import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from Controllers import builder

def Build(templates, index, file): # Carrega uma janela de criação de configuração para cada template da lista
    if int(templates[index]) == 1:
        Builder = builder.Builder1()
        Builder.next = [templates, index + 1]
        Builder.file = file
        Builder.window.show()
