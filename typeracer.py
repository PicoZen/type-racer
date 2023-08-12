from kivy.core.text import LabelBase
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import ListProperty
import keyboard
from kivy.clock import Clock
from kivymd.uix.behaviors import CommonElevationBehavior, FakeRectangularElevationBehavior
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.floatlayout import MDFloatLayout
from paragraphs import which_para

Window.maximize()


kv = '''
MDFloatLayout:
    ScreenManager:
        id: scr
        Screen: 
            name: "select"
            SplashBar:
                size_hint: .85, .9
                pos_hint: {"center_x": 0.5, "center_y": 0.5}
                elevation : 3
                md_bg_color: 1,1,1,1
                radius:  [18]
                
                MDLabel:
                    text: "VELOCITY - TYPE RACER"
                    pos_hint: {"center_x": .5,"center_y": .80}
                    halign: "center" 
                    font_name: "BPoppins"
                    font_size: "50sp"
                    theme_text_color: "Custom"
                    text_color: 60/255, 43/255, 117/255, 1
                
                Image:
                    id: app_logo
                    source: 'fast.png'
                    pos_hint: {"center_x": 0.48, "center_y": 0.65}
                    size_hint: .36, .4
                    allow_stretch: False
                    keep_ratio: True
                
                MDFloatLayout:  
                    MDLabel:
                        text: "Set Timer :" 
                        pos_hint: {"x": 0.25, "center_y": .54}
                        font_name: "Poppins"
                        font_size: "20sp"
                        theme_text_color: "Custom"
                        text_color: 60/255, 43/255, 117/255, 1
                
                MDFloatLayout:
                    size_hint: .15, .08
                    pos_hint: {"center_x": 0.33, "center_y": .479}
                    canvas:
                        Color:
                            rgb: (238/255, 238/255, 238/255, 1)
                        RoundedRectangle:
                            size: self.size
                            pos: self.pos
                            radius: [25]
                    TextInput:
                        id: timer
                        hint_text: "in seconds"
                        size_hint: 1, None
                        pos_hint: {"center_x": .5, "center_y":.5}
                        height: self.minimum_height
                        cursor_color: 96/255, 74/255, 215/255, 1
                        cursor_width: "2sp"
                        foreground_color: 96/255, 74/255, 215/255, 1
                        background_color: 0, 0, 0, 0
                        padding: 15
                        font_name: "Poppins"
                        font_size: "15sp"        
                MDFloatLayout:
                    MDLabel:
                        id: click
                        text: "Choose the paragraph : "
                        pos_hint: {"x": 0.61, "center_y": .54}
                        font_name: "Poppins"
                        font_size: "20sp"
                        theme_text_color: "Custom"
                        text_color: 60/255, 43/255, 117/255, 1
                        
                    MDFloatLayout:
                        size_hint: .09, .08
                        pos_hint: {"center_x": 0.858, "center_y": .5}
                        Spinner:
                            id: spinner
                            text: "Paragraphs"
                            font_name: "Poppins"
                            font_size: "15sp"
                            pos_hint: {"center_x": .55, "center_y": .9}
                            values: ["para1", "para2", "para3", "para4", "para5" , "para6", "para7", "para8", "para9", "para10"]
                            on_text:
                                app.spinner_click(spinner.text)
                            background_color: 0,0,0,0
                            canvas.before:
                                Color: 
                                    rgb: (60/255, 43/255, 117/255, 1)
                                RoundedRectangle:
                                    size: self.size
                                    pos: self.pos
                                    radius: [25]
                
                MDFloatLayout:
                    size_hint: .9, .08
                    pos_hint: {"center_x": 0.5, "center_y": .31}
                    canvas.before:
                        Color:
                            rgb: (238/255, 238/255, 238/255, 1)
                        RoundedRectangle:
                            size: self.size
                            pos: self.pos
                            radius: [25]
                    TextInput:
                        id: para_content
                        hint_text: "Paragraph Content ....." 
                        pos_hint: {"center_x": .5, "center_y":.5}
                        height: self.minimum_height
                        cursor_color: 96/255, 74/255, 215/255, 1
                        cursor_width: "2sp"
                        foreground_color: 96/255, 74/255, 215/255, 1
                        background_color: 0, 0, 0, 0
                        padding: 15
                        font_name: "Poppins"
                        font_size: "15sp"
                        readonly: True
                        multiline: False
                
                Button:
                    id: enter 
                    text: "Enter"
                    font_name: "BPoppins"
                    font_size: "20sp"
                    size_hint: .3, .09
                    pos_hint: {"center_x": .48 , "center_y": .15}
                    background_color: 0,0,0,0
                    canvas.before:
                        Color: 
                            rgb: (60/255, 43/255, 117/255, 1)
                        RoundedRectangle:
                            size: self.size
                            pos: self.pos
                            radius: [25]
                    on_release:
                        scr.current= "start"       
        Screen:
            name: "start"
            StartBar:
                size_hint: .85, .9
                pos_hint: {"center_x": 0.5, "center_y": 0.5}
                elevation : 3
                md_bg_color: 1,1,1,1
                radius:  [16]
                
                MDLabel:
                    text: "VELOCITY - TYPE RACER"
                    pos_hint: {"center_x": .5,"center_y": .65}
                    halign: "center" 
                    font_name: "BPoppins"
                    font_size: "50sp"
                    theme_text_color: "Custom"
                    text_color: 60/255, 43/255, 117/255, 1
                
                Image:
                    id: app_logo
                    source: 'fast.png'
                    pos_hint: {"center_x": 0.48, "center_y": 0.49}
                    size_hint: .36, .4
                    allow_stretch: False
                    keep_ratio: True
                
                Button:
                    id: start_game 
                    text: "Start"
                    font_name: "BPoppins"
                    font_size: "20sp"
                    size_hint: .3, .09
                    pos_hint: {"center_x": .48 , "center_y": .25}
                    background_color: 0,0,0,0
                    canvas.before:
                        Color: 
                            rgb: (60/255, 43/255, 117/255, 1)
                        RoundedRectangle:
                            size: self.size
                            pos: self.pos
                            radius: [25]
                    on_release:
                        app.set_time()
                        scr.current= "main"
                        
                    
        Screen:
            name: "main"
            MDFloatLayout:
                md_bg_color: 1, 1, 1, 1
                MDLabel:
                    text: "VELOCITY - TYPE RACER"
                    pos_hint: {"center_x": .5,"center_y": .96}
                    halign: "center" 
                    font_name: "BPoppins"
                    font_size: "30sp"
                    theme_text_color: "Custom"
                    text_color: 60/255, 43/255, 117/255, 1
                MDLabel:
                    id: para_area
                    text: ""
                    size_hint_x: .9
                    pos_hint: {"center_x": .5, "center_y": .7}
                    font_name: 'Poppins'
                    font_size: "23sp"
                    multiline: False
            
                MDFloatLayout
                    size_hint: .9, .15
                    pos_hint: {"center_x": .5, "center_y": .35}
                    canvas.before:
                        Color:
                            rgb: 230/255, 230/255, 230/255 ,255
                        Line:
                            width: 1.5
                            rounded_rectangle: self.x, self.y, self.width, self.height, 6, 6, 6, 6, 100
                    
                    TextInput:
                        id: typing_area
                        hint_text: "Type Here .........."
                        size_hint: 1, None
                        pos_hint: {"center_x": .5, "center_y": .5}
                        height: "100dp"
                        font_name : "Poppins"
                        font_size: "23sp"
                        background_color: 1, 1, 1, 0
                        foreground_color: app.color
                        padding: 15
                        cursor_color: 0, 0, 0, 1
                        focus: True
                        cursor: 0
                        on_text: app.check(self.text)
                        multiline: False
                        
                MDGridLayout:
                    cols : 3
                    pos_hint : {"center_x": .5, "center_y": .1}
                    size_hint_x : .9
                    MDLabel:
                        id : time_left
                        text: "Time Left : 60"
                        size_hint_x : .85
                        post_hint:   {"center_x": .5, "center_y": .2}
                        halign: "center"
                        font_name : "Poppins"
                        font_size: "20sp"
                    MDLabel:
                        id : mistakes
                        text: "Mistakes : 0"
                        size_hint_x : .85
                        post_hint:   {"center_x": .5, "center_y": .2}
                        halign: "center"
                        font_name : "Poppins"
                        font_size: "20sp" 
                    MDLabel:
                        id : wpm
                        text: "WPM : 0"
                        size_hint_x : .85
                        post_hint:   {"center_x": .5, "center_y": .2}
                        halign: "center"
                        font_name : "Poppins"
                        font_size: "20sp"  

'''


class SplashBar (CommonElevationBehavior, MDFloatLayout):
    pass


class StartBar (CommonElevationBehavior, MDFloatLayout):
    pass




class Velocity(MDApp):
    # para = "Sir Tristram, violer d'amores, fr'over the short sea, had passencore rearrived from North Armorica on this side the scraggy isthmus of Europe Minor to wielderfight his penisolate war: nor had topsawyer's rocks by the stream Oconee exaggerated themselse to Laurens County's gorgios while they went doublin their mumper all the time: nor avoice from afire bellowsed mishe mishe to tauftauf thuartpeatrick: not yet, though venissoon after, had a kidscad buttended a bland old isaac: not yet, though all's fair in vanessy, were sosie sesthers wroth with twone nathandjoe."
    para = ""
    # para = "Computer science is a field of study that involves the design, development, and analysis of computer systems and software. It is a broad and rapidly evolving field that encompasses a wide range of topics, including programming languages, algorithms, data structures, artificial intelligence, databases, networks, securitymore."
    color = ListProperty((86 / 225, 150 / 255, 79 / 255, 1))
    index = 1
    incorrect = []
    mistakes = 0
    time = 60
    timeleft = 60
    isTyped = False
    typed =[]
    #count =0

    def build(self):
        self.icon = "fast.png"
        return Builder.load_string(kv)

    def set_time(self):
        self.time = int(self.root.ids.timer.text)
        self.timeleft = int(self.root.ids.timer.text)
        self.root.ids.time_left.text = f"Time Left : {self.timeleft}"

    def spinner_click(self, value):
        parag = which_para(value)
        self.para = parag
        self.root.ids.para_area.text = parag
        self.root.ids.para_content.text = parag
        self.root.ids.para_content.cursor = (0, 0)

    def check(self, text):
        count = 0
        if self.timeleft != 0:
            if not self.isTyped:
                self.start_time()
                self.isTyped = True

            if keyboard.is_pressed("backspace"):
                self.index = self.root.ids.typing_area.cursor[0]

                if self.index > 0:
                    print(f"index{self.index}, typed{self.typed}")
                    try:
                        self.typed.pop()
                    except IndexError:
                        self.typed.clear()
                    self.index -= 1

                else:
                    self.index = 0
                    self.typed.clear()

                if self.index in self.incorrect:
                    self.incorrect.remove(self.index)
                    self.mistakes -= 1
                print(f"Index{self.index}")  
                print(f"len(typed){len(self.typed)}")
                print(f"typed){self.typed}")     

                if self.index < (len(self.typed)-1):
                    print(f"cursor{self.index}, length{len(self.typed)}")
                    print(f"mistakes{self.mistakes}, incorrect{self.incorrect}")
                    print(f"mistakes{self.mistakes}, incorrect{self.incorrect}")
                    print("antada select akkano nenekk?outside")

                    def on_ok_3(button_widget):
                        self.index = 0
                        self.typed.clear()
                        self.mistakes = 0
                        self.incorrect.clear()
                        self.root.ids.typing_area.text = ""
                        area = self.root.ids.typing_area
                        area.cursor = 0
                        alert_t.dismiss()

                    alert_t = MDDialog(title="Error", text="Mouse movement identified",
                                       buttons=[MDFlatButton(text="OK", theme_text_color="Custom",
                                                             text_color=self.theme_cls.primary_color,
                                                             on_release=on_ok_3)])
                    alert_t.open()

            else:
                keyboard.block_key("left")
                keyboard.block_key("up")
                keyboard.block_key("down")
                keyboard.block_key("ctrl")
                keyboard.block_key("enter")

                self.index = self.root.ids.typing_area.cursor[0]

                for i in text:
                    if count == 0:
                        count = 1
                        self.typed.clear()

                    self.typed.append(i)
                    #print(f"typed){self.typed}")
                count = 0    

                if self.index < (len(self.typed)-1):
                    print(f"cursor{self.index}, length{len(self.typed)}")
                    print("antada select akkano nenekk?")

                    def on_ok_1(button_widget):
                        self.index = 0
                        self.typed.clear()
                        self.mistakes = 0
                        self.incorrect.clear()
                        self.root.ids.typing_area.text = ""
                        alert_n.dismiss()

                    alert_n = MDDialog(title="Error", text="Mouse movement identified!",
                                       buttons=[MDFlatButton(text="OK", theme_text_color="Custom",
                                                             text_color=self.theme_cls.primary_color,
                                                             on_release=on_ok_1)])
                    alert_n.open()

                try:
                    if self.para[self.index] == self.typed[self.index]:
                        #print(f"Para: {self.para[self.index]}, Type: {typed[self.index]}")
                        #print(f"Incorrect{self.incorrect}")
                        if not self.incorrect:
                            self.color = (86 / 225, 150 / 255, 79 / 255, 1)
                    else:
                        self.color = (203 / 225, 52 / 255, 57 / 255, 1)
                        self.mistakes += 1
                        self.incorrect.append(self.index)

                    self.index += 1

                    # while keyboard.is_pressed("backspace"):
                    #     self.index = self.root.ids.typing_area.cursor[0]
                    #
                    #     if self.index > 0:
                    #         self.index -= 1
                    #
                    #     else:
                    #         self.index = 0
                    #
                    #     if self.index in self.incorrect:
                    #         self.incorrect.remove(self.index)
                    #         self.mistakes -= 1
                    #
                    #     print(f"Index{self.index}")
                    #     print(f"len(typed){len(self.typed)}")
                    #
                    #     if self.index < (len(self.typed) - 1):
                    #         print(f"cursor{self.index}, length{len (self.typed)}")
                    #         print("antada select akkano nenekk? inside w")

                except IndexError:
                    self.root.ids.typing_area.disabled = True

                    def on_ok(button_widget):
                        if len(self.para) < len(self.typed):
                            text_input = self.root.ids.typing_area
                            extra = len(text_input.text) - len(self.para)
                            text_input.text = text_input.text[: -extra]

                        self.root.ids.typing_area.disabled = False
                        alert.dismiss()

                    alert = MDDialog(title="Error",
                                     text="Verify your text!(Mouse movement/Above word limit reached)",
                                     buttons=[MDFlatButton(text="OK", theme_text_color="Custom",
                                                           text_color=self.theme_cls.primary_color,
                                                           on_release=on_ok)], auto_dismiss=False)
                    alert.open()

                self.root.ids.mistakes.text = f"Mistake : {self.mistakes}"
                wpm = round((((self.index - self.mistakes) / 5) / (self.time - self.timeleft)) * 60)
                if wpm > 0:
                    self.root.ids.wpm.text = f"WPM : {wpm}"

            if len(self.para) == self.index and self.mistakes == 0:
                self.root.ids.typing_area.disabled = True
                Clock.unschedule(self.start_time)
                clk = self.root.ids.time_left.text
                mist = self.root.ids.mistakes.text
                word_pm = self.root.ids.wpm.text

                thanks = MDDialog(title="Congratulations!", text=f"{clk}        {mist}          {word_pm} ",
                                  auto_dismiss=False)
                thanks.open()
        else:

            self.root.ids.typing_area.disabled = True

            mist = self.root.ids.mistakes.text
            word_pm = self.root.ids.wpm.text

            para_comp = len(self.root.ids.typing_area.text)
            para_left = len(self.para) - para_comp

            def on_time_up(button_widget):
                time_up.dismiss()

            time_up = MDDialog(title="Time Up!", text=f"Data Left:{para_left}     {mist}          {word_pm} ",
                               buttons=[MDFlatButton(text="OK", theme_text_color="Custom",
                                                      text_color=self.theme_cls.primary_color,
                                                      on_release=on_time_up)],
                               auto_dismiss=False)
            time_up.open()
            self.root.ids.time_left.text = f"Data Left: {para_left}"

    def start_time(self, *args):
        self.index = self.root.ids.typing_area.cursor[0]
        if self.timeleft > 0:
            self.timeleft -= 1
            self.root.ids.time_left.text = f"Time Left : {self.timeleft}"
            wpm = round((((self.index - self.mistakes) / 5) / (self.time - self.timeleft)) * 60, 4)
            if wpm > 0:
                self.root.ids.wpm.text = f"WPM : {wpm}"

        else:
            Clock.unschedule(self.start_time)
        Clock.schedule_once(self.start_time, 1)


if __name__ == "__main__":

    LabelBase.register (name="Poppins",
                        fn_regular="Poppins-Regular.ttf")
    LabelBase.register (name="BPoppins",
                        fn_regular="Poppins-SemiBold.ttf")
    Velocity().run ()