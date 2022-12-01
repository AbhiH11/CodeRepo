import unittest
from Crash_course import get_formatted_name

class name_test_case(unittest.TestCase):

    def test_first_last_name(self):

        formatted_name = get_formatted_name('hari','anu')
        self.assertEqual(formatted_name,'Hari Anu')

    def test_first_middle_last_name(self):
        formatted_name = get_formatted_name('hari','h','abhi')
        # print(formatted_name)
        self.assertEqual(formatted_name,'Hari Abhi H')
        
if __name__ == '__main__':
    unittest.main()