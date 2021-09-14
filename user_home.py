from kivy.lang import Builder

from kivymd.toast import toast
from kivymd.uix.bottomsheet import MDGridBottomSheet
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.picker import MDDatePicker ,MDTimePicker
from kivymd.uix.navigationdrawer import MDNavigationLayout
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.list import OneLineListItem

KV = '''
Screen:
    MDNavigationLayout:

        ScreenManager:

            Screen:

                BoxLayout:
                    orientation: 'vertical'

                    MDToolbar:
                        title: "Own Vehicle"
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.toggle_nav_drawer()]]

                    Widget: 
    

        MDNavigationDrawer:

            ContentNavigationDrawer:
    
    BoxLayout:
        text: "Mobile Number"
        id: box
        orientation: "vertical"


    # MDToolbar:
    #     title: 'Own Vehicle'
    #     pos_hint: {"top": 1}
    #     elevation: 10


    # MDLabel:
    #     text: "Mobile Number"
    #     

    MDRaisedButton:
        text: "Submit"
        # on_release: app.show_example_grid_bottom_sheet()
        pos_hint: {"center_x": .5, "center_y": .1}

    MDTextField:
        id: text_field_error
        hint_text: "Source"
        helper_text: "There will always be a mistake"
        helper_text_mode: "on_error"
        pos_hint: {"center_y": .8}


    MDTextField:
        id: text_field_error
        hint_text: "Destinamtion"
        helper_text: "There will always be a mistake"
        helper_text_mode: "on_error"
        pos_hint: {"center_y": .7}

    MDRaisedButton:
        text: "Date"
        pos_hint: { "center_y": .6}
        on_release: app.show_date_picker()
        
    MDRaisedButton:
        text: "Time"
        pos_hint: { 'center_y': .5}
        on_release: app.show_time_picker()
        
    MDGridLayout:
        cols: 3
        row_default_height: (self.width - self.cols*self.spacing[0]) / self.cols
        row_force_default: True
        adaptive_height: True
        # padding: dp(4), dp(4)
        # spacing: dp(4)
        pos_hint: { 'center_y': .3}

        SmartTileWithStar:
            source: "car.jpg"

        SmartTileWithStar:
            source: "4-wheeler.jpg"

        SmartTileWithStar:
            source: "truck.jpg"
    
'''

class ContentNavigationDrawer(BoxLayout):
    pass


class Example(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def get_date(self, date):
        '''
        :type date: <class 'datetime.date'>
        '''

    def show_date_picker(self):
        date_dialog = MDDatePicker(
            callback=self.get_date,
            year=2010,
            month=2,
            day=12,
        )
        date_dialog.open()

    def show_time_picker(self):
        '''Open time picker dialog.'''

        time_dialog = MDTimePicker()
        time_dialog.open()

Example().run()