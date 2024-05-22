class OutputHandler:
    @staticmethod
    def show_life_path_num(life_path_num: int):
        print(f"The Life Path Number: {life_path_num}")

    @staticmethod
    def show_lucky_colour(colour: str):
        print(f"The Lucky Colour: {colour}")

    @staticmethod
    def show_comparison_result(same: bool):
        if same:
            print("The Life Path Numbers are the same.")
        else:
            print("The Life Path Numbers are different from each other.")

    @staticmethod
    def show_generation(generation: str):
        print(f"Generation: {generation}")