import datetime

class LifePathCalculator:
    @staticmethod
    def calculate_life_path_num(birthday: datetime.date) -> int:
        numbers = [int(digit) for digit in birthday.strftime("%Y%m%d")]
        while sum(numbers) > 9 and sum(numbers) not in [11, 22, 33]:
            numbers = [int(digit) for digit in str(sum(numbers))]
        return sum(numbers)

    @staticmethod
    def is_master_num(life_path_num: int) -> bool:
        return life_path_num in [11, 22, 33]

    @staticmethod
    def compare_life_path_num(birthday1: datetime.date, birthday2: datetime.date) -> bool:
        return (LifePathCalculator.calculate_life_path_num(birthday1) ==
                LifePathCalculator.calculate_life_path_num(birthday2))