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
        text: "Upload Eye Image Using Gallery"
        pos_hint: {"center_x": .5, "center_y": .2}
        on_press: 
            app.file_manager_open()
    MDRectangleFlatButton:
        text: "Upload Eye Image Using Camera"
        pos_hint: {"center_x": .5, "center_y": .1}
        on_press: 
            app.open_camera()
            
"""

result_screen = """
<ResultsScreen>:
    name: 'result'
    MDLabel:
        id: lb
        text: ''
        halign: 'center'
        valgin: 'center'
    MDRectangleFlatButton:
        text: "Assess Again"
        pos_hint: {"center_x": .5, "center_y": .3}
        on_press: 
            root.manager.current = 'assess'
            root.clear()
    MDRectangleFlatButton:
        text: "Back to Main"
        pos_hint: {"center_x": .5, "center_y": .2}
        on_press: 
            root.manager.current = 'main'
            root.clear()
            
"""

screens = screen_manager + main_screen + assessment_screen + result_screen