from kivy.app import App
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition

from kivy.graphics import Color,Rectangle

import time
import random

class FirstScreen(Screen):
    pass
class SecondScreen(Screen):
    pass
class ColourScreen(Screen):
    colour = ListProperty([1.,0.,0.,1.])
    pass
class ContentBoxLayout(BoxLayout):
    pass
class ButtonShort(Button):
    pass
class MyScreenManager(ScreenManager):

    def new_colour_screen(self):
        name = str(time.time())
        s =ColourScreen(name=name,
                        colour=[random.random() for _ in range(3)] + [1])
        self.add_widget(s)
        self.current = name

root_widget = Builder.load_file("screenmanager.kv")

class ScreenManagerApp(App):
    def build(self):
        return root_widget




if __name__ == '__main__':
    # Window.fullscreen = True
    
    ScreenManagerApp().run()