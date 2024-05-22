import datetime

class InputParser:
    @staticmethod
    def parse_birthday(input_str: str) -> datetime.date:
        formats = ["%B %d, %Y", "%m/%d/%Y"]
        for fmt in formats:
            try:
                return datetime.datetime.strptime(input_str, fmt).date()
            except ValueError:
                continue
        raise ValueError("Invalid date format! ")

    @staticmethod
    def validate_birthday(birthday: datetime.date) -> bool:
        start_date = datetime.date(1901, 1, 1)
        end_date = datetime.date(2024, 12, 31)
        return start_date <= birthday <= end_date

    @staticmethod
    def convert_month(input_str: str) -> int:
        try:
            datetime_obj = datetime.datetime.strptime(input_str, "%B")
            return datetime_obj.month
        except ValueError:
            raise ValueError("Invalid month name here !")
