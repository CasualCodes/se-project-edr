# Front End Source Code
# add imports for the camera/gallery retrieval (and permissions)
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRectangleFlatButton

# Main Screen
class aisight_mscreen(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"
    
        return (
            MDScreen (
                MDRectangleFlatButton (
                    text = "Assess",
                    pos_hint={"center_x": 0.5, "center_y": 0.8},
                )
            )
        )