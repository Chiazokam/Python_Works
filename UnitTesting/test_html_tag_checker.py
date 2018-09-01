import unittest
import html_tag_checker as c

class TestHtmlCheckerMethod(unittest.TestCase):
    def test_read_file(self):
        result = c.read_file('helloworld.html')
        self.assertEqual(result[0].startswith('<'), True)





if __name__ == '__main__':
    unittest.main()
