from sys import _xoptions
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import ScreenManager, FadeTransition  
from kivy.lang import Builder

class ScreenManager(ScreenManager):
    pass

class Opening_Screen(MDScreen):
    pass

class Main_Screen(MDScreen):
    pass

class ISSRA(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        screen = Builder.load_file('mainwindow.kv')
        sm = ScreenManager()
        sm.add_widget(Opening_Screen(name='oscreen'))
        sm.add_widget(Main_Screen(name='mscreen'))
        return sm

if __name__ == '__main__':
    ISSRA().run()