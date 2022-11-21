import os
import sys

sys.path.append(os.path.dirname(__file__))


class BasePage:

    def __init__(self, altdriver):
        self.altdriver = altdriver
