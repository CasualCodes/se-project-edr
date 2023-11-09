# Front End Source Code
# add imports for the camera/gallery retrieval (and permissions)
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import ui_screens

# Screens
class MainScreen(Screen):
    pass


class AssessmentScreen(Screen):
    pass


class ResultsScreen(Screen):
    pass

# Create the screen manager
screen_manager = ScreenManager()
screen_manager.add_widget(MainScreen(name='main'))
screen_manager.add_widget(AssessmentScreen(name='assess'))
screen_manager.add_widget(ResultsScreen(name='result'))

# Main Front End Execution
class front_end_main(MDApp):
    def build(self):
        screen = Builder.load_string(ui_screens.screens)
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"
    
        return screen