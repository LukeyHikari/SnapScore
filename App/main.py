from sys import _xoptions
import kivy
kivy.require('2.1.0') # replace with your current kivy version !
from kivy.app import App
from kivy.uix.label import Label

class ISSRA(App):
    def build(self):
        x = Label(text= 'Jericho')
        y = Label(text= 'Jericho')
        return y

if __name__ == '__main__':
    ISSRA().run()