from kivy.lang import Builder

from kivymd.toast import toast
from kivymd.uix.bottomsheet import MDGridBottomSheet
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

KV = '''
Screen:
    BoxLayout:
        text: "Mobile Number"
        id: box
        orientation: "vertical"
    

    MDToolbar:
        title: 'Own Vehicle'
        pos_hint: {"top": 1}
        elevation: 10

    # MDLabel:
    #     text: "Mobile Number"
    #     
        
    MDRaisedButton:
        text: "OTP"
        # on_release: app.show_example_grid_bottom_sheet()
        pos_hint: {"center_x": .5, "center_y": .7}
        
    MDTextField:
        id: text_field_error
        hint_text: "Enter Your Mobile Number"
        helper_text: "There will always be a mistake"
        helper_text_mode: "on_error"
        pos_hint: {"center_y": .8}
'''


class Example(MDApp):
    def build(self):
        return Builder.load_string(KV)




Example().run()