import datetime
from typing import Union

class InputParser:
    @staticmethod
    def parse_birthday(input_str: str) -> datetime.date:
        formats = ["%B %d, %Y", "%m/%d/%Y"]
        for fmt in formats:
            try:
                return datetime.datetime.strptime(input_str, fmt).date()
            except ValueError:
                continue
        raise ValueError("Invalid Date Format. ")

    @staticmethod
    def validate_birthday(Birthday: datetime.date) -> bool:
        commence_date = datetime.date(1901, 1, 1)
        end_date = datetime.date(2024, 12, 31)
        return commence_date <= Birthday <= end_date

    @staticmethod
    def convert_month(input_str: str) -> int:
        try:
            datetime_obj = datetime.datetime.strptime(input_str, "%B")
            return datetime_obj.month
        except ValueError:
            raise ValueError("Invalid Month Name. ")


class LifePathCalculator:
    @staticmethod
    def calculate_life_path_number(Birthday: datetime.date) -> int:
        numbers = [int(digit) for digit in Birthday.strftime("%Y%m%d")]
        while sum(numbers) > 9 and sum(numbers) not in [11, 22, 33]:
            numbers = [int(digit) for digit in str(sum(numbers))]
        return sum(numbers)

    @staticmethod
    def is_master_number(life_path_number: int) -> bool:
        return life_path_number in [11, 22, 33]

    @staticmethod
    def compare_life_path_numbers(birthday1: datetime.date, birthday2: datetime.date) -> bool:
        return (LifePathCalculator.calculate_life_path_number(birthday1) ==
                LifePathCalculator.calculate_life_path_number(birthday2))


class LuckyColourDetector:
    @staticmethod
    def get_lucky_colour(life_path_number: int) -> str:
        colours = {
            1: "Red",
            2: "Orange",
            3: "Yellow",
            4: "Green",
            5: "Blue",
            6: "Indigo",
            7: "Violet",
            8: "Pink",
            9: "Gold",
            11: "Silver",
            22: "Platinum",
            33: "Diamond"
        }
        return colours.get(life_path_number, "Unknown")


class GenerationIdentifier:
    @staticmethod
    def identify_generation(birthday: datetime.date) -> str:
        year = birthday.year
        if year < 1946:
            return "The Silent Generation."
        elif year < 1965:
            return "The Baby Boomers."
        elif year < 1980:
            return "The Generation X."
        elif year < 1995:
            return "The Millennials."
        elif year < 2010:
            return "The Generation Z."
        else:
            return "The Generation Alpha."


class OutputHandler:
    @staticmethod
    def show_life_path_number(life_path_number: int):
        print(f"Life Path Number: {life_path_number}")

    @staticmethod
    def show_lucky_colour(colour: str):
        print(f"Lucky Colour: {colour}")

    @staticmethod
    def show_comparison_result(same: bool):
        if same:
            print("The Life Path Numbers are the same here.")
        else:
            print("The Life Path Numbers are different.")

    @staticmethod
    def show_generation(generation: str):
        print(f"Generation: {generation}")


def main():
    birthday_str = input("Enter any Birthday (e.g., June 12, 1998 or 06/12/1998): ")
    parser = InputParser()
    try:
        birthday = parser.parse_birthday(birthday_str)
    except ValueError as e:
        print(e)
        return

    if not parser.validate_birthday(birthday):
        print("Invalid birthday. Please enter a date between 1901 and 2024.")
        return

    life_path_calculator = LifePathCalculator()
    life_path_number = life_path_calculator.calculate_life_path_number(birthday)

    lucky_colour_detector = LuckyColourDetector()
    lucky_colour = lucky_colour_detector.get_lucky_colour(life_path_number)

    generation_identifier = GenerationIdentifier()
    generation = generation_identifier.identify_generation(birthday)

    output_handler = OutputHandler()
    output_handler.show_life_path_number(life_path_number)
    output_handler.show_lucky_colour(lucky_colour)
    output_handler.show_generation(generation)

if __name__ == "__main__":
    main()
