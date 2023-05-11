import datetime
from exceptions import *

LOWER_BOUND_DATE = "2022-06-08"
UPPER_BOUND_DATE = datetime.date.today() + datetime.timedelta(15)


def validate_date_format(date_string: str) -> None:
    """Validates if date_string is in valid ISO format (YYYY-MM-DD)"""
    try:
        datetime.date.fromisoformat(date_string)
    except ValueError as exc:
        raise InvalidDateFormat from exc


def validate_start_date(start_date: str):
    """
    Validates if date_string is in valid ISO format (YYYY-MM-DD)
    and not before lower date limit.
    """
    validate_date_format(start_date)
    day = datetime.date.fromisoformat(start_date)
    if day < datetime.date.fromisoformat(LOWER_BOUND_DATE):
        raise LowerBoundDateException


def validate_end_date(start_date, end_date):
    """
    Validates if end_date is in valid ISO format (YYYY-MM-DD)
    and not before start date or after upper date limit.
    """
    validate_date_format(end_date)
    end_date = datetime.date.fromisoformat(end_date)
    if end_date > UPPER_BOUND_DATE:
        raise UpperBoundDateException
    try:
        start_date = datetime.date.fromisoformat(start_date)
        if start_date > end_date:
            raise InvalidEndDateException
    except ValueError as exc:
        raise InvalidDateFormat from exc
