import os
from kivy.config import Config
from kivy.properties import StringProperty
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.anchorlayout import AnchorLayout



KV = """
<MyPopup>:
    title: ''  
    title_height: 0  
    size_hint: 0.8, 0.8

    BoxLayout:
        orientation: 'vertical'

        AnchorLayout:
            anchor_x: 'left'
            anchor_y: 'top'
            size_hint: None, None
            size: '50sp', '-1sp'

            Button:
                size_hint: None, None
                size: '40sp', '40sp'
                background_normal: 'images/krest.png'
                on_press: root.dismiss()

        Image:
            source: root.image_path
            allow_stretch: True
            keep_ratio: False


MyBL:
    orientation: "vertical"
    size_hint: (0.95, 0.95)
    pos_hint: {"center_x": 0.5, "center_y": 0.5}

    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: 'images/sobaka.png'

    Button:
        text: "Лента"
        on_press: root.show_image('lenta.png')

    Button:
        text: "Окей"
        on_press: root.show_image('okey.png')

    Button:
        text: "Домовой"
        on_press: root.show_image('domovoy.png')

    Button:
        text: "Максидом"
        on_press: root.show_image('maksidom.png')

    Button:
        text: "Метро"
        on_press: root.show_image('metro.png')

    Button:
        text: "перекрёстокXпятёрочка"
        on_press: root.show_image('PerekrestokXPaterka.png')

    Button:
        text: "Пловдив"
        on_press: root.show_image('plovdiv.png')

    Button:
        text: "СпортМастер"
        on_press: root.show_image('sportmaster.png')
"""

class MyPopup(Popup):
    image_path = StringProperty('')

    def __init__(self, **kwargs):
        super(MyPopup, self).__init__(**kwargs)

class MyBL(BoxLayout):

    def show_image(self, image_name):
        image_path = os.path.join(os.path.dirname(__file__), "images", image_name)
        popup = MyPopup()
        popup.image_path = image_path
        popup.title = ''  
        popup.open()

class MyApp(App):
    running = True

    def build(self):
        self.title = ''  
        return Builder.load_string(KV)

    def on_stop(self):
        self.running = False


if __name__ == "__main__":
    MyApp().run()
