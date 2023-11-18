# Front End Source Code
# Import needed libraries/components for the camera/gallery retrieval (and permissions)
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen
from kivymd.uix.filemanager import MDFileManager
import cv2

import ui_screens
import back_end

# Screen Initialization
class MainScreen(Screen):
    pass
class AssessmentScreen(Screen):
    pass
class ResultsScreen(Screen):
    def clear(self):
        self.ids.lb.text = ""

# Main Front End Execution
class front_end_main(MDApp):
    def build(self):
        self.screen = Builder.load_string(ui_screens.screens)
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"
        self.manager_open = False
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path,
            preview=True,
        )

        #Dummy Input Loading
        back_end.dummy()
        self.screen.get_screen(name='result').ids.lb.text = ""

        return self.screen

    ## Gallery Operations ##
    def file_manager_open(self):
        self.file_manager.show('/')  # output manager to the screen

    def select_path(self, path):
        '''It will be called when you click on the file name
        or the catalog selection button.
        :type path: str;
        :param path: path to the selected directory or file;
        '''
        self.exit_manager()

        
        if (self.isEmpty(path)):
            return
        else:
            self.callBackend(path)
            self.screen.current = 'result'

    def exit_manager(self, *args):
        '''Called when the user reaches the root of the directory tree.'''

        self.file_manager.close()

    ## Camera Operations ##
    def open_camera(self, *args):
        '''Called when the user clicks the capture using camera button'''

        # Open the camera
        cap = cv2.VideoCapture(0)

        while(True):
            # Capture frame-by-frame
            ret, frame = cap.read()

            # Display the resulting frame
            cv2.imshow('frame', frame)
            
            # Break the loop on pressing 'q'
            if cv2.waitKey(1) & 0xFF == ord('c'):
                break

        cv2.imwrite('photo.jpg', frame)
        # Release the capture and destroy all windows when done
        cap.release()
        cv2.destroyAllWindows()

        path = 'photo.jpg'
        if (self.isEmpty(path)):
            return
        else:
            self.callBackend(path)
            self.screen.current = 'result'
    
    def callBackend(self, inputData):
        # processinput takes the PATH of the image, and then updates outputData of the results
        outputData = back_end.processInput(inputData)
        self.screen.get_screen(name='result').ids.lb.text = outputData
    
    def isEmpty(self, inputData):
        if (inputData == ""):
            return True
        else:
            return False