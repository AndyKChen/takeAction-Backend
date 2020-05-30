import unittest
from getURL import getURL


class TestStringMethods(unittest.TestCase):

    def test_getURL(self):
        self.assertEqual(getURL("https://google.com"), 'https://google.com')

        def sample_getURL(self):
            PLACEHOLDER_INPUT_URL = 'https://google.com'
            PLACEHOLDER_OUTPUT_URL = 'https://google.com'
            self.assertEqual(getURL(PLACEHOLDER_INPUT_URL),
                             PLACEHOLDER_OUTPUT_URL)


if __name__ == "__main__":
    unittest.main()

# cd in to utils directory
# python -m unittest getURLtest.py
