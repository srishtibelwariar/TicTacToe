#!/usr/bin/env python
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import Screen

Builder.load_string("""
<MenuScreen>:
    GridLayout:
        cols: 2
        rows: 2
        
        GridLayout:
            rows:2
            Label:
                text: '3x3 Tic Tac Toe'
                font_size: '40sp'
            Label:
                text: 'Please select game type and click start'
                valign: 'middle'
        GridLayout:
            rows:3
            ToggleButton:
                text: 'Human vs Human'
                group: 'player'
                state: 'down'
            ToggleButton:
                text: 'Human vs Random Computer'
                group: 'player'
            ToggleButton:
                text: 'Human vs Smart Computer'
                group: 'player'
        Button:
            text: 'Quit'
            on_press: app.stop()
        Button:
            text: 'Start'
            on_press: root.manager.current = 'game'

<GameScreen>:
    GridLayout:
        canvas:
            Rectangle:
                pos: 2*self.width /9,0
                size: 10, self.height
            Rectangle:
                pos: 4*self.width /9, 0
                size: 10, self.height
            Rectangle:
                pos: 2*self.width /3, 0
                size: 2, self.height
            Rectangle:
                pos: 0, self.height/3
                size: 2*self.width/3, 10
            
            Rectangle:
                pos: 0, 2*self.height/3
                size: 2*self.width/3, 10
    
""")

class MenuScreen(Screen):
    pass

class GameScreen(Screen):
    pass

screens = ScreenManager()
screens.add_widget(MenuScreen(name='menu'))
screens.add_widget(GameScreen(name='game'))

class tttApp(App):

    def build(self):
        return screens

if __name__ == '__main__':
    tttApp().run()
