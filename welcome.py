from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.card import MDCard

Window.size = (360,640)

KV = '''
MDScreen:
    MDFloatLayout:
        md_bg_color: 255/255,244/255,231/255
    BoxLayout:
        orientation: 'vertical'
        Image:
            source: 'images/applogo.png'
            size: "500dp","500dp"

'''

class Demo(MDApp):
    def build(self):
        self.icon = "images/applogo.png"
        # self.theme_cls.theme_style = "Light"
        return Builder.load_string(KV)
Demo().run()