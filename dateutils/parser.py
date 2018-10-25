import calendar

from word2number.w2n import word_to_num

DAYS_OF_WEEK_MAP = {'sunday': 6, 'tuesday': 1, 'wednesday': 2, 'monday': 0, 'thursday': 3, 'saturday': 5, 'friday': 4}
MONTHS_MAP = {'may': 5, 'september': 9, 'march': 3, 'december': 12, 'november': 11, 'august': 8, 'january': 1, 'february': 2, 'june': 6, 'july': 7, 'october': 10, 'april': 4}


def day_parser(line):
    """
    Parse an event_frequency config line for day information
    :param line:
    :type line: str
    :return:
    :rtype: Dict[str, int]
    """
    day = None
    day_of_week = None
    day_position_in_month = None

    day_part = line.lower().strip().split('of')[0].strip()
    day_parts = day_part.split(' ')
    if len(day_parts) == 1:
        day = word_to_num(day_parts[0])
    elif len(day_parts) == 2:
        if day_parts[0] == 'last':
            day_position_in_month = -1
        else:
            day_position_in_month = word_to_num(day_parts[0])
        day_of_week = DAYS_OF_WEEK_MAP[day_parts[1]]

    return dict(day=day, day_of_week=day_of_week, day_position_in_month=day_position_in_month)

def month_parser(line):
    """
    Parse an event_frequency config line for month information, return -1 for all months
    :param line:
    :type line: str
    :return:
    :rtype: int
    """
    month = None
    month_part =  line.lower().strip().split('of')[1].strip()

    if month_part == 'every month' or month_part == 'month':
        month = -1
    else:
        month = MONTHS_MAP[month_part]
    return month

def year_parser(line):
    year = None
    parts = line.lower().strip().split('of')
    if len(parts) == 3:
        year_part = parts[2].strip()
        year = word_to_num(year_part)
    return year