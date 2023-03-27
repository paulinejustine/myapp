from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (300,500)

KV = '''
MDScreen:
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            id: top_bar
            elevation: 0
            specific_text_color: 111/255,29/255,27/255
            left_action_items: [["chevron-left"]]
            right_action_items: [["theme-light-dark", lambda x: app.switch_theme_style(), "brightness-4"]]
            md_bg_color: (255/255,244/255,231/255)
            radius: "20dp"
        MDLabel:
            text_size: self.size
            text:"Description"
            bold: True
            theme_text_color: "Custom"
            text_color: app.theme_cls.text_color
            # color: 111/255,29/255,27/255
            font_style: 'H5'
            markup: True
            valign: 'top'
            halign: 'center'
            padding: dp(20), dp(10)
'''

class Demo(MDApp):

    def build(self):
        self.theme_cls.theme_style_switch_animation = True
        self.theme_cls.theme_style = "Light"
        self.toolbar_bg_color = (255/255,244/255,231/255)
        return Builder.load_string(KV)    

    def switch_theme_style(self):
        if self.theme_cls.theme_style == "Dark":
            self.theme_cls.theme_style = "Light"
            self.theme_cls.primary_palette = "Gray"
            self.root.ids.top_bar.md_bg_color = (255/255,244/255,231/255)
        else:
            self.theme_cls.theme_style = "Dark"
            self.theme_cls.primary_palette = "Gray"
            self.root.ids.top_bar.md_bg_color = (153/255, 153/255, 153/255)

Demo().run()