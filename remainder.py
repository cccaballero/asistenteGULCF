import datetime

from mailproc.transports import SmtpSenderTransport

from configutils.configuration import Configuration
from database import Database
from dateutils.dates import find_days, get_date_in
from dateutils.parser import day_parser, month_parser, year_parser

CONFIG = Configuration()

def get_event_dates():
    event_frequency = CONFIG.get_main_params().event_frequency
    day_info = day_parser(event_frequency)
    month = month_parser(event_frequency)
    year = year_parser(event_frequency) if year_parser(event_frequency) else datetime.datetime.now().year

    return find_days(day_info['day'], day_info['day_of_week'], day_info['day_position_in_month'], month, year)


def notify(days):
    date = datetime.date.today() + datetime.timedelta(days=days)
    sender_transport = SmtpSenderTransport(**CONFIG.get_sender_params())
    sender_transport.connect()
    sender_transport.send_mail(
        CONFIG.get_sender_params().from_address,
        [CONFIG.get_sender_params().to_address],
        CONFIG.get_main_params().remainder_subject,
        CONFIG.config.get('main', 'remainder_message').format(date=date)
    )
    db = Database().db
    db.notification.insert(launched_on=datetime.date.today(), event_date=date)
    db.commit()


def should_notify():
    remainder_days = CONFIG.get_main_params().event_remainder
    remainder_days = remainder_days if type(remainder_days) == list else [remainder_days]
    remainder_days = [int(x) for x in remainder_days]

    event_dates = get_event_dates()

    db = Database().db

    for days in remainder_days:
        date = get_date_in(days, event_dates)
        if date and not db((db.notification.launched_on == datetime.date.today()) & (db.notification.event_date == date)).select().first():
            notify(days)
