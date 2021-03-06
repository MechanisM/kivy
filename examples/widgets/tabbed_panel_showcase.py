'''
TabbedPanel
============

Test of the widget TabbedPanel showing all capabilities.
'''

from kivy.app import App
from kivy.animation import Animation
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelHeader
from kivy.factory import Factory


class StandingHeader(TabbedPanelHeader):
    pass


class ClosableHeader(TabbedPanelHeader):
    pass


Factory.register('StandingHeader', cls = StandingHeader)
Factory.register('ClosableHeader', cls = ClosableHeader)

from kivy.lang import Builder

Builder.load_string('''
<TabShowcase>
    but: _but
    Button:
        id: _but
        text: 'Press to show Tabbed Panel'
        on_release: root.show_tab()

<StandingHeader>
    color: 0,0,0,0
    Scatter:
        do_translation: False
        do_scale: False
        do_rotation: False
        auto_bring_to_front: False
        rotation: 70
        size_hint: None, None
        size: lbl.size
        center_x: root.center_x
        center_y: root.center_y + (lbl.height/4)
        Label:
            id: lbl
            text: root.text
            size: root.size
            pos: 0,0

<PanelLeft>
    size_hint: (.45, .45)
    pos_hint: {'center_x': .25, 'y': .55}
    #replace the default tab with our custom tab
    default_tab: def_tab
    tab_width: 40
    tab_height: 70
    FloatLayout:
        RstDocument:
            id: default_content
            text: '\\n'.join(("Standing tabs", "-------------",\
                "Tabs in \\'%s\\' position" %root.tab_pos))
        Image:
            id: tab_2_content
            pos:self.parent.pos
            size: self.parent.size
            source: 'data/images/defaulttheme-0.png'
        Image:
            id: tab_3_content
            pos:self.parent.pos
            size: self.parent.size
            source: 'data/images/image-loading.gif'
    StandingHeader:
        id: def_tab
        content: default_content
        text: 'Default tab'
    StandingHeader:
        content: tab_2_content
        text: 'tab 2'
    StandingHeader:
        content: tab_3_content
        text: 'tab 3'

<ClosableHeader>
    color: 0,0,0,0
    # variable tab_width
    text: 'tabx'
    size_hint_x: None
    width: self.texture_size[0] + 40
    BoxLayout:
        pos: root.pos
        size_hint: None, None
        size: root.size
        padding: 3
        Label:
            id: lbl
            text: root.text
        BoxLayout:
            size_hint: None, 1
            width: 22
            orientation: 'vertical'
            Widget:
            Button:
                border: 0,0,0,0
                background_normal: 'tools/theming/defaulttheme/close.png'
                on_release: root.panel.remove_widget(root)
            Widget:


<PanelRight>
    tab_pos: 'top_right'
    size_hint: (.45, .45)
    pos_hint: {'center_x': .75, 'y': .55}
    default_tab: def_tab
    #allow variable tab width
    tab_width: None
    FloatLayout:
        RstDocument:
            id: default_content
            text: '\\n'.join(("Closable tabs", "-------------",\
                "- The tabs above are also scrollable",\
                "- Tabs in \\'%s\\' position" %root.tab_pos))
        Image:
            id: tab_2_content
            pos:self.parent.pos
            size: self.parent.size
            source: 'data/images/defaulttheme-0.png'
        BoxLayout:
            id: tab_3_content
            pos:self.parent.pos
            size: self.parent.size
            BubbleButton:
                text: 'Press to add new tab'
                on_release: root.add_header()
            BubbleButton:
                text: 'Press set this tab as default'
                on_release: root.default_tab = tab3
    ClosableHeader:
        id: def_tab
        text: 'default tab'
        content:default_content
        panel: root
    ClosableHeader:
        text: 'tab2'
        content: tab_2_content
        panel: root
    ClosableHeader:
        id: tab3
        text: 'tab3'
        content: tab_3_content
        panel: root
    ClosableHeader:
        panel: root
    ClosableHeader:
        panel: root
    ClosableHeader:
        panel: root
    ClosableHeader:
        panel: root
    ClosableHeader:
        panel: root
    ClosableHeader:
        panel: root
    ClosableHeader:
        panel: root

<PanelbLeft>
    tab_pos: 'bottom_left'
    size_hint: (.45, .45)
    pos_hint: {'center_x': .25, 'y': .02}
    default_tab_text: 'Settings'
    default_tab_content: default_content
    FloatLayout:
        RstDocument:
            id: default_content
            text: '\\n'.join(("Normal tabs", "-------------",\
                "Tabs in \\'%s\\' position" %root.tab_pos))
        Image:
            id: tab_2_content
            pos: self.parent.pos
            size: self.parent.size
            source: 'data/images/defaulttheme-0.png'
        Image:
            id: tab_3_content
            pos:self.parent.pos
            size: self.parent.size
            source: 'data/images/image-loading.gif'
    TabbedPanelHeader:
        text: 'tab2'
        content: tab_2_content
    TabbedPanelHeader:
        text: 'tab3'
        content: tab_3_content

<PanelbRight>
    tab_pos: 'right_top'
    size_hint: (.45, .45)
    pos_hint: {'center_x': .75, 'y': .02}
    default_tab: def_tab
    tab_height: img.width
    FloatLayout:
        RstDocument:
            id: default_content
            text: '\\n'.join(("Image tabs","-------------",\
                "1. Normal image tab","2. Image with Text","3. Rotated Image",\
                "4. Tabs in \\'%s\\' position" %root.tab_pos))
        Image:
            id: tab_2_content
            pos:self.parent.pos
            size: self.parent.size
            source: 'data/images/defaulttheme-0.png'
        VideoPlayer:
            id: tab_3_content
            pos:self.parent.pos
            size: self.parent.size
            source: 'softboy.avi'
    TabbedPanelHeader:
        id: def_tab
        content:default_content
        border: 0, 0, 0, 0
        background_down: 'softboy.png'
        background_normal:'sequenced_images/data/images/info.png'
    TabbedPanelHeader:
        id: tph
        content: tab_2_content
        BoxLayout:
            pos: tph.pos
            size: tph.size
            orientation: 'vertical'
            Image:
                source: 'sequenced_images/data/images/info.png'\
                    if tph.state == 'normal' else 'softboy.png'
            Label:
                text: 'text & img'
    TabbedPanelHeader:
        id: my_header
        content: tab_3_content
        Scatter:
            do_translation: False
            do_scale: False
            do_rotation: False
            auto_bring_to_front: False
            rotation: 90
            size_hint: None, None
            size: img.size
            center: my_header.center
            Image:
                id: img
                source: 'sequenced_images/data/images/info.png'\
                    if my_header.state == 'normal' else 'softboy.png'
                size: my_header.size
                allow_stretch: True
                keep_ratio: False
''')


class Tp(TabbedPanel):
    #override tab switching method to animate on tab switch
    def switch_to(self, header):
        if header.content is None:
            return
        anim = Animation(color=(1, 1, 1, 0), d =.24, t = 'in_out_quad')

        def start_anim(_anim, child, in_complete, *lt):
            if hasattr(child, 'color'):
                _anim.start(child)
            elif not in_complete:
                _on_complete()

        def _on_complete(*lt):
            if hasattr(header.content, 'color'):
                header.content.color = (0, 0, 0, 0)
                anim = Animation(color =
                    (1, 1, 1, 1), d =.23, t = 'in_out_quad')
                start_anim(anim, header.content, True)
            super(Tp, self).switch_to(header)

        anim.bind(on_complete = _on_complete)
        if self.content:
            start_anim(anim, self.content.children[0], False)
        else:
            _on_complete()


class PanelLeft(Tp):
    pass


class PanelRight(Tp):

    def add_header(self):
        self.add_widget(ClosableHeader(panel = self))


class PanelbLeft(Tp):
    pass


class PanelbRight(Tp):
    pass


class TabShowcase(FloatLayout):

    def show_tab(self):
        if not hasattr(self, 'tab'):
            self.tab = tab = PanelLeft()
            self.add_widget(tab)
            self.tab1 = tab = PanelRight()
            self.add_widget(tab)
            self.tab2 = tab = PanelbRight()
            self.add_widget(tab)
            self.tab3 = tab = PanelbLeft()
            self.add_widget(tab)
            self.but.text = \
                'Tabs in variable positions, press to change to top_left'
        else:
            values = ('left_top', 'left_mid', 'left_bottom', 'top_left',
                'top_mid', 'top_right', 'right_top', 'right_mid',
                'right_bottom', 'bottom_left', 'bottom_mid', 'bottom_right')
            index = values.index(self.tab.tab_pos)
            self.tab.tab_pos = self.tab1.tab_pos = self.tab2.tab_pos\
                = self.tab3.tab_pos = values[(index + 1) % len(values)]
            self.but.text = 'Tabs in \'%s\' position,' %self.tab.tab_pos\
                + '\n press to change to next pos'


class TestTabApp(App):

    def build(self):
        return TabShowcase()

if __name__ in ('__main__', '__android__'):
    TestTabApp().run()
