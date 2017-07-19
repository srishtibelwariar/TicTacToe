#!/usr/bin/env python
from kivy.app import App
from kivy.lang import Builder
from kivy.vector import Vector
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import Screen
from kivy.uix.screenmanager import WipeTransition
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.properties import NumericProperty
from kivy.properties import ReferenceListProperty
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty

class TTTTile(Widget):
    name= StringProperty(" ")
    def new(self):
        if self.name==" ":
            self.name= "X"

class TTTGame(Widget):
    T0= ObjectProperty(None)
    T1= ObjectProperty(None)
    T2= ObjectProperty(None)
    T3= ObjectProperty(None)
    T4= ObjectProperty(None)
    T5= ObjectProperty(None)
    T6= ObjectProperty(None)
    T7= ObjectProperty(None)
    T8= ObjectProperty(None)
    
    def update(self):
        pass

class Manager(ScreenManager):
    pass


class TTTApp(App):
    def build(self):
        self.load_kv('ttt.kv')
        return Manager()

if __name__ == '__main__':
    TTTApp().run()
