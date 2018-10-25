import calendar
from datetime import date, timedelta


def find_day_in_month(day, weekday, position_in_month, month_number, year):
    """
    return a date object based in given parameters
    :param day: Day of month, can be an integer or null
    :type day: int
    :param weekday: Day of week to select
    :type weekday: int
    :param position_in_month: A position for given weekday (second saturday of month for example)
    :type position_in_month: int
    :param month_number:
    :type month_number: int
    :param year:
    :type year: int
    :return: Date representation of given dates values
    :rtype: datetime.date
    """
    if day:
        return date(year, month_number, day)

    cal = calendar.monthcalendar(year, month_number)

    if position_in_month < 0:
        for week in cal[::-1]:
            if week[weekday]:
                day = week[weekday]
                return date(year, month_number, day)
    else:
        pos_counter = 0
        for week in cal:
            if week[weekday]:
                pos_counter += 1
            if pos_counter == position_in_month:
                day = week[weekday]
                return date(year, month_number, day)


def find_days(day, weekday, position_in_month, month, year):
    """

    :param day:
    :type day: int
    :param weekday:
    :type weekday: int
    :param position_in_month:
    :type position_in_month: int
    :param month:
    :type month: str
    :param year:
    :type year: int
    :return:
    :rtype: List[datetime.date]
    """
    # Show every month
    dates = []
    if month < 0:
        for month in range(1, 13):
            dates.append(find_day_in_month(day, weekday, position_in_month, month, year))
    else:
        dates.append(find_day_in_month(day, weekday, position_in_month, month, year))

    return dates


def get_date(year, month, day):
    return date(year, month, day)


def are_days_left(days, check_date):
    """
    Check if there are left `days` days to reach `check_date` date
    :param days:
    :type days: int
    :param check_date:
    :type check_date: datetime.date
    :return:
    :rtype: bool
    """
    now = date.today()
    if check_date - timedelta(days=days) == now:
        return True
    return False


def are_days_left_for_date(days, check_dates):
    """
    Check if there are left `days` days to reach any of `check_date` dates
    :param days:
    :type days: int
    :param check_dates:
    :type check_dates: List[datetime.date]
    :return:
    :rtype: bool
    """
    for check_date in check_dates:
        if are_days_left(days, check_date):
            return True
    return False

def get_date_in(days, check_dates):
    now = date.today()
    for check_date in check_dates:
        if check_date - timedelta(days=days) == now:
            return check_date
    return None