screen_manager = """
ScreenManager:
    MainScreen:
    AssessmentScreen:
    ResultsScreen:
"""

main_screen = """

<MainScreen>:
    name: 'main'
    MDLabel:
        text: 'Welcome!'
        halign: 'center'
    MDRectangleFlatButton:
        text: "Assess Your Eye"
        pos_hint: {"center_x": .5, "center_y": .3}
        on_press: root.manager.current = 'assess'

"""

assessment_screen = """

<AssessmentScreen>:
    name: 'assess'
    MDLabel:
        text: 'Assessment Screen'
        halign: 'center'
    MDRectangleFlatButton:
        text: "Back to Main"
        pos_hint: {"center_x": .5, "center_y": .3}
        on_press: root.manager.current = 'main'
    MDRectangleFlatButton:
        text: "Upload Eye Image"
        pos_hint: {"center_x": .5, "center_y": .2}
        on_press: root.manager.current = 'result'

"""

result_screen = """

<ResultsScreen>:
    name: 'result'
    MDLabel:
        text: 'Results Screen'
        halign: 'center'
        valgin: 'center'
    MDRectangleFlatButton:
        text: "Assess Again"
        pos_hint: {"center_x": .5, "center_y": .3}
        on_press: root.manager.current = 'assess'
    MDRectangleFlatButton:
        text: "Back to Main"
        pos_hint: {"center_x": .5, "center_y": .2}
        on_press: root.manager.current = 'main'

"""

screens = screen_manager + main_screen + assessment_screen + result_screen

"""

<MainScreen>:
    name: 'menu'
    MDRectangleFlatButton:
        text: 'Profile'
        pos_hint: {'center_x':0.5,'center_y':0.6}
        on_press: root.manager.current = 'profile'
    MDRectangleFlatButton:
        text: 'Upload'
        pos_hint: {'center_x':0.5,'center_y':0.5}
        on_press: root.manager.current = 'upload'
    
<ProfileScreen>:
    name: 'profile'
    MDLabel:
        text: 'Profile'
        halign: 'center'
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'menu'
        
<UploadScreen>:
    name: 'upload'
    MDLabel:
        text: 'Upload'
        halign: 'center'
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'menu'

"""