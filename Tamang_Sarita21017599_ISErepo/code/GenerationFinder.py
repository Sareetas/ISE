import datetime
class GenerationFinder:
    @staticmethod
    def find_generation(birthday: datetime.date) -> str:
        year = birthday.year
        if year < 1946:
            return "The Silent Generation. "
        elif year < 1965:
            return "The Baby Boomer."
        elif year < 1980:
            return "The Generation X."
        elif year < 1995:
            return "The Millennial."
        elif year < 2010:
            return "The Generation Z. "
        else:
            return "The Generation Alpha."