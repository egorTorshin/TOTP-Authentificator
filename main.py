from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock
import time
import pyotp

TOTP_SECRET = "YOUR_TOTP_SECRET"

class TOTPWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 20

        self.code_label = Label(text="", font_size='40sp')
        self.timer_label = Label(text="", font_size='30sp')

        self.add_widget(self.code_label)
        self.add_widget(self.timer_label)

        self.totp = pyotp.TOTP(TOTP_SECRET)
        Clock.schedule_interval(self.update, 1)

    def update(self, dt):
        current_code = self.totp.now()
        elapsed = time.time() % 30
        remaining = int(30 - elapsed)
        self.code_label.text = f"TOTP: {current_code}"
        self.timer_label.text = f"Обновление через: {remaining} сек"

class TOTPApp(App):
    def build(self):
        return TOTPWidget()

if __name__ == '__main__':
    TOTPApp().run()
