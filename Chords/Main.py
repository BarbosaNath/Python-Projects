from kivymd.app import MDApp
from kivy.lang  import Builder

#from my_colors   import*
#from my_str_inst import*


#f = Fret_board()
#f.print()

screen_helper = """
Screen:
    NavigationLayout:



        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'Chord App'
                        left_action_items: [["menu", lambda x: nav_drawer.set_state()]]
                        elevation: 8
                    Widget:
                        id: m_scr


                        BoxLayout:
                            orientation: 'horizontal'
                            canvas.after:
                                Color:
                                    rgba: 0,0,0,1
                                Line:
                                    points: ( m_scr.width / 2, m_scr.height -50 ), ( m_scr.width / 2, 50 )





        MDNavigationDrawer:
            id: nav_drawer
            BoxLayout:
                orientation: 'vertical'

                MDLabel:
                    text: 'Nath'
                    font_style: 'Subtitle1'
                    size_hint_y: None
                    height: self.texture_size[1]

"""




class ChordApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Purple'
        screen = Builder.load_string(screen_helper)
        return screen

    def navigation_draw(self):
        print("bah che")
        exit()

        
ChordApp().run()