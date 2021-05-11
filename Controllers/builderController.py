import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from Controllers import builder

def Build(templates): # Carrega uma janela de criação de configuração para cada template da lista
    for template in templates:
        if int(template) == 1:
            Builder = builder.Builder1()
            Builder.window.show()
