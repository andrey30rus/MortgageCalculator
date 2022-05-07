from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class MortgageCalculator(MDApp):
    def build(self):
        return MDLabel(text="MortgageCalculator", halign="center")


MortgageCalculator().run()