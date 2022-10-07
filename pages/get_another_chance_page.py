from pages.base_page import BasePage
from altunityrunner import By

class GetAnotherChancePage(BasePage):
    def __init__(self, altdriver):
        BasePage.__init__(self, altdriver)
        
    @property
    def game_over_button(self):
       return self.altdriver.wait_for_object(By.PATH, "//Game/DeathPopup/GameOver", timeout=2)

    @property
    def premium_button(self):
       return self.altdriver.wait_for_object(By.PATH, "//Game/DeathPopup/ButtonLayout/Premium Button", timeout=2)

    @property
    def available_currency(self):
       return int(self.altdriver.wait_for_object(By.PATH, "//Game/DeathPopup/PremiumDisplay/PremiumOwnCount", timeout=2).get_text())

    def is_displayed(self):
        if self.game_over_button and self.premium_button:
            return True

    def press_game_over(self):
        self.game_over_button.tap()

    def press_premium_button(self):
        self.premium_button.tap()
