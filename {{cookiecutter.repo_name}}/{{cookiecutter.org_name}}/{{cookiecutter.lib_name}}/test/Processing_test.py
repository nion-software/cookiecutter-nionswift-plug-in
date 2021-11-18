import unittest

from {{cookiecutter.org_name}}.{{cookiecutter.lib_name}} import Processing

class TestLibrary(unittest.TestCase):

    def setUp(self) -> None:
        """Common code for all tests can go here."""
        pass

    def tearDown(self) -> None:
        """Common code for all tests can go here."""
        pass

    def test_processing(self) -> None:
        d = Processing.get_processing_data()
        self.assertEqual((40, 60), d.shape)
