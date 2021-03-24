from robot.libraries.BuiltIn import BuiltIn
from _ast import keyword


class SeleniumLibraryExt:

    @classmethod
    def _driver(cls):
        return BuiltIn().get_library_instance('SeleniumLibrary').driver


