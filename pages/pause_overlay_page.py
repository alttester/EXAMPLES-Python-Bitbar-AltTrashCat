from pages.base_page import BasePage
from alttester import By


class PauseOverlayPage(BasePage):
    def __init__(self, altdriver):
        BasePage.__init__(self, altdriver)

    @property
    def resume_button(self):
        return self.altdriver.wait_for_object(By.PATH,
                                              "//Game/PauseMenu/Resume",
                                              timeout=5)

    @property
    def main_menu_button(self):
        return self.altdriver.wait_for_object(By.PATH,
                                              "//Game/PauseMenu/Exit",
                                              timeout=5)

    @property
    def title(self):
        return self.altdriver.wait_for_object(By.PATH,
                                              "//Game/PauseMenu/Text",
                                              timeout=5)

    def is_displayed(self):
        if self.resume_button and self.main_menu_button and self.title:
            return True

    def press_resume(self):
        self.resume_button.tap()

    def press_main_menu(self):
        self.main_menu_button.tap()
