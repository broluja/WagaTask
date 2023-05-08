import datetime
from exceptions import *

LOWER_BOUND_DATE = "2022-06-08"

def validate_date_format(date_string: str) -> None:
    try:
        datetime.date.fromisoformat(date_string)
    except ValueError as exc:
        raise InvalidDateFormat from exc


def validate_start_date(start_date: str):
    validate_date_format(start_date)
    day = datetime.date.fromisoformat(start_date)
    if day < datetime.date.fromisoformat(LOWER_BOUND_DATE):
        raise LowerBoundDateException


def validate_end_date(start_date, end_date):
    validate_date_format(end_date)
    today = datetime.date.today()
    upper_bound = today + datetime.timedelta(15)
    if datetime.date.fromisoformat(end_date) > upper_bound:
        raise UpperBoundDateException
    try:
        start_date = datetime.date.fromisoformat(start_date)
        end_date = datetime.date.fromisoformat(end_date)
        if start_date > end_date:
            raise InvalidEndDateException
    except ValueError as exc:
        raise InvalidDateFormat from exc
