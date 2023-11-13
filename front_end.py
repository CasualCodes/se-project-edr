# Front End Source Code
# add imports for the camera/gallery retrieval (and permissions)
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

from kivymd.uix.filemanager import MDFileManager
from kivymd.toast import toast

from kivymd.uix.label import MDLabel
from kivy.properties import StringProperty
import ui_screens
import back_end

inputData = ""
outputData = StringProperty()

# Screen Initialization
class MainScreen(Screen):
    pass

class AssessmentScreen(Screen):
    def callBackEnd(self):
        global inputData
        print("InputData " + inputData)
        # inputData = GET INPUT FROM CAMERA/GALLERY

        #root.callBackEnd()

        global outputData
        # processinput takes the PATH of the image, and then updates outputData of the results
        # outputData = back_end.processInput(inputData)

class ResultsScreen(Screen):
    definition = StringProperty()
    # update is what displays the results in result page
    def update(self):
        global outputData
        self.ids.lb.text = outputData
    def clear(self):
        self.ids.lb.text = ""

# Screen Manager Initializations (Preparation for builder use)
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
        self.manager_open = False
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path,
            preview=True,
        )
    
        return screen

    def file_manager_open(self):
        self.file_manager.show('/')  # output manager to the screen

    def select_path(self, path):
        '''It will be called when you click on the file name
        or the catalog selection button.
        :type path: str;
        :param path: path to the selected directory or file;
        '''

        self.exit_manager()
        # toast(path)
        print(path)
        print("Returned Path" + path)

        global outputData
        # processinput takes the PATH of the image, and then updates outputData of the results
        outputData = back_end.processInput(path)

        global inputData
        inputData = path
        return path

    def exit_manager(self, *args):
        '''Called when the user reaches the root of the directory tree.'''

        self.file_manager.close()