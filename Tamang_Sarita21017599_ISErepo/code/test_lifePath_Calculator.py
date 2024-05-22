import unittest
from Life_Path_Calculator import LifePathCalculator
import datetime

class TestLifePathCalculator(unittest.TestCase):
    def test_calculate_life_path_num(self):
        self.assertEqual(LifePathCalculator.calculate_life_path_num(datetime.date(1990, 10, 12)), 5)
        self.assertEqual(LifePathCalculator.calculate_life_path_num(datetime.date(1981, 11, 11)), 11)
        self.assertEqual(LifePathCalculator.calculate_life_path_num(datetime.date(2023, 12, 31)), 8)

    def test_is_master_num(self):
        self.assertTrue(LifePathCalculator.is_master_num(11))
        self.assertFalse(LifePathCalculator.is_master_num(5))

    def test_compare_life_path_num(self):
        self.assertTrue(LifePathCalculator.compare_life_path_num(datetime.date(1990, 10, 12), datetime.date(1990, 10, 12)))
        self.assertFalse(LifePathCalculator.compare_life_path_num(datetime.date(1990, 10, 12), datetime.date(1991, 10, 12)))

if __name__ == '__main__':
    unittest.main()
