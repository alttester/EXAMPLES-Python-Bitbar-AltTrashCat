from pages.main_menu_page import MainMenuPage
from tests.base_test import TestBase

class TestMainMenuPage(TestBase):
    
    def setUp(self):
        self.main_menu_page = MainMenuPage(self.altdriver)
        self.main_menu_page.load()

    def test_main_menu_page_loaded_correctly(self):
        assert(self.main_menu_page.is_displayed())

