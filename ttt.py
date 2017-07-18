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
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.current = 'game'

<GameScreen>:
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
        
    GridLayout:
        
        Button:
            text:"0"
            font_size: '50sp'
            size: 2*root.width/9, root.height/3
            pos: 0, 2*root.height/3+10
            id: 0
        Button:
            text:"1"
            font_size: '50sp'
            size: 2*root.width/9 -10, root.height/3
            pos: 2*root.width/9 +10, 2*root.height/3+10
            id: 1
    
        Button:
            text:"2"
            font_size: '50sp'
            size: 2*root.width/9 -10, root.height/3
            pos: 4*root.width/9+10, 2*root.height/3+10
            id: 2
            
        Button:
            text:"3"
            font_size: '50sp'
            size: 2*root.width/9, root.height/3 -10
            pos: 0, 1*root.height/3+10
            id: 3
        Button:
            text:"4"
            font_size: '50sp'
            size: 2*root.width/9 -10, root.height/3 -10
            pos: 2*root.width/9 +10, 1*root.height/3+10
            id: 4
    
        Button:
            text:"5"
            font_size: '50sp'
            size: 2*root.width/9 -10, root.height/3 -10
            pos: 4*root.width/9+10, 1*root.height/3+10
            id: 5
        
        
        Button:
            text:"6"
            font_size: '50sp'
            size: 2*root.width/9 , root.height/3
            pos: 0, 0
            id: 6
        Button:
            text:"7"
            font_size: '50sp'
            size: 2*root.width/9 -10 , root.height/3
            pos: 2*root.width/9 +10, 0
            id: 7
        Button:
            text:"8"
            font_size: '50sp'
            size: 2*root.width/9 -10, root.height/3
            pos: 4*root.width/9+10, 0
            id: 8
        Button:
            text:"Home Menu"
            size: 200, 200
            pos: 7*root.width/9+10, 240
            on_press:
                root.manager.transition.direction = 'right'
                root.manager.current = 'menu'
            
        Button:
            text:"Quit Game"
            size: 200, 200
            pos: 7*root.width/9+10, 20
            on_press: app.stop()
        
        Label:
            text:"Player 1's turn!"
            font_size: '30sp'
            halign: 'right'
            valign: 'middle'
            pos: 7*root.width/9+10, root.height/2
            id: message
            
        
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
