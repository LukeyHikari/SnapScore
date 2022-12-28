from sys import _xoptions
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, FadeTransition  
from kivy.lang import Builder
from kivy.clock import Clock

Window.size = (480,800)

class SnapScore(MDApp):
    global smanager
    smanager = ScreenManager()

    def build(self):
        self.title = "SnapScore"
        #self.theme_cls.theme_style = "Light"
        smanager.add_widget(Builder.load_file('openscreen.kv'))
        smanager.add_widget(Builder.load_file('snapscore.kv'))   
        return smanager

    def on_start(self): #Function that will be called on start
        Clock.schedule_once(self.change_screen, 5)

    def change_screen(self, dt): #Open->Main Screen Transition function
        smanager.transition = FadeTransition(clearcolor=(0,0,0,0))
        smanager.duration = 3 
        smanager.current = "mscreen"

if __name__ == '__main__':
    SnapScore().run()