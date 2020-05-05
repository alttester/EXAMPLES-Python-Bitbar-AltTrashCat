from pages.base_page import BasePage


class StartPage(BasePage):
    def __init__(self, altdriver):
        BasePage.__init__(self, altdriver)

    def load(self):
        self.altdriver.load_scene('Start')

    @property
    def start_button(self):
        return self.altdriver.find_element('StartButton')

    @property
    def start_text(self):
        return self.altdriver.find_element('StartText')

    @property
    def logo_image(self):
        return self.altdriver.find_element('LogoImage')

    @property
    def unity_url_button(self):
        return self.altdriver.find_element('UnityURLButton')

    def is_displayed(self):
        if self.start_button and self.start_text and self.logo_image and self.unity_url_button:
            return True

    def press_start(self):
        self.start_button.tap()

    def get_start_button_text(self):
        return self.start_text.get_text()