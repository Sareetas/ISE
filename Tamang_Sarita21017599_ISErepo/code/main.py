import datetime
from input_parser import InputParser
from Life_Path_Calculator import LifePathCalculator
from LuckyColourDetector import LuckyColourDetector
from GenerationFinder import GenerationFinder
from OutputHandler import OutputHandler

def main():
    birthday_str = input("Enter a birthday (e.g., June 12, 1999 or 6/12/1999): ")
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
    life_path_num = life_path_calculator.calculate_life_path_num(birthday)

    lucky_colour_finder = LuckyColourDetector()
    lucky_colour = lucky_colour_finder.get_lucky_colour(life_path_num)

    generation_identifier = GenerationFinder()
    generation = generation_identifier.find_generation(birthday)

    output_handler = OutputHandler()
    output_handler.show_life_path_num(life_path_num)
    output_handler.show_lucky_colour(lucky_colour)
    output_handler.show_generation(generation)

if __name__ == "__main__":
    main()
