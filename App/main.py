from sys import _xoptions
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang import Builder

KV = '''
MDScreen:

    MDNavigationLayout:

        MDScreenManager:

            MDScreen:

                MDTopAppBar:
                    elevation: 4
                    pos_hint: {"top": 1}
                    md_bg_color: "#90abe0"
                    specific_text_color: "#4a4939"
                    left_action_items:
                        [['menu', lambda x: nav_drawer.set_state("open")]]


        MDNavigationDrawer:
            id: nav_drawer
            radius: (0, 16, 16, 0)

            ContentNavigationDrawer:
'''

class ContentNavigationDrawer(MDBoxLayout):
    pass

class ISSRA(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        screen = Builder.load_string(KV)
        return screen

if __name__ == '__main__':
    ISSRA().run()