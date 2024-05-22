import unittest
from input_parser import InputParser
import datetime

class TestParserInput(unittest.TestCase):
    def test_parse_birthday_valid_format(self):
        self.assertEqual(InputParser.parse_birthday("June 12, 1999"), datetime.date(1999, 6, 12))
        self.assertEqual(InputParser.parse_birthday("06/12/1999"), datetime.date(1999, 6, 12))

    def test_parse_birthday_invalid_format(self):
        with self.assertRaises(ValueError):
            InputParser.parse_birthday("12 June 1999")
    
    def test_validate_birthday(self):
        self.assertTrue(InputParser.validate_birthday(datetime.date(1999, 6, 12)))
        self.assertFalse(InputParser.validate_birthday(datetime.date(1899, 1, 1)))
        self.assertFalse(InputParser.validate_birthday(datetime.date(2025, 12, 31)))

    def test_convert_month(self):
        self.assertEqual(InputParser.convert_month("January"), 1)
        self.assertEqual(InputParser.convert_month("June"), 6)
        with self.assertRaises(ValueError):
            InputParser.convert_month("Junary")

if __name__ == '__main__':
    unittest.main()