class LuckyColourDetector:
    @staticmethod
    def get_lucky_colour(life_path_num: int) -> str:
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
        return colours.get(life_path_num, "Unknown")
