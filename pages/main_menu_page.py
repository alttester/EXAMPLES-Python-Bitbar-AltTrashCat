from pages.base_page import BasePage
from alttester import By


class MainMenuPage(BasePage):

    def __init__(self, altdriver):
        BasePage.__init__(self, altdriver)

    def load(self):
        self.altdriver.load_scene('Main')

    @property
    def store_button(self):
        return self.altdriver.wait_for_object(By.PATH,
                                              "//UICamera/Loadout/StoreButton",
                                              timeout=5)

    @property
    def leader_board_button(self):
        return self.altdriver.wait_for_object(By.PATH,
                                              "//UICamera/Loadout/OpenLeaderboard",
                                              timeout=5)

    @property
    def settings_button(self):
        return self.altdriver.wait_for_object(By.PATH,
                                              "//UICamera/Loadout/SettingButton",
                                              timeout=5)

    @property
    def mission_button(self):
        return self.altdriver.wait_for_object(By.PATH,
                                              "//UICamera/Loadout/MissionButton",
                                              timeout=5)

    @property
    def run_button(self):
        return self.altdriver.wait_for_object(By.PATH,
                                              "//UICamera/Loadout/StartButton",
                                              timeout=5)

    @property
    def character_name(self):
        return self.altdriver.wait_for_object(By.NAME, "CharName", timeout=5)

    @property
    def theme_name(self):
        return self.altdriver.wait_for_object(By.PATH,
                                              "//UICamera/Loadout/ThemeZone",
                                              timeout=5)

    def is_displayed(self):
        if self.store_button and self.leader_board_button \
                and self.settings_button \
                and self.mission_button and self.run_button \
                and self.character_name and self.theme_name:
            return True

    def press_run(self):
        self.run_button.tap()
