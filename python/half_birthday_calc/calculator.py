from __future__ import annotations
from datetime import datetime, timedelta, timezone
from typing import Literal, Union
import calendar

def is_leap_year(year: int) -> bool:
    """Checks if a year is a leap year."""
    return calendar.isleap(year)

def _js_utc_date(year: int, month: int, day: int, hour=0, minute=0, second=0, ms=0) -> datetime:
    """Simulates JS Date.UTC behavior (month is 0-indexed)."""
    # JS Date.UTC handles overflow of months and days.
    # First, handle the year and month overflow to get a valid start of month.
    total_months = month
    final_year = year + total_months // 12
    final_month = total_months % 12 + 1  # 1-indexed for Python datetime
    
    # Python datetime(year, month, 1) is fine as long as year is within [MINYEAR, MAXYEAR]
    base = datetime(final_year, final_month, 1, hour, minute, second, ms * 1000, tzinfo=timezone.utc)
    # Add days (day - 1 because we are already at the 1st)
    return base + timedelta(days=day - 1)

def get_traditional_half_birthday(birthday: datetime) -> Union[datetime, Literal["none"]]:
    """
    Calculates the traditional half birthday (six months after the birthday).
    
    - For February 29th birthdays, it always returns "none".
    - For August 29th, it returns "none" in non-leap years if the half-birthday would fall on Feb 29th.
    - For all other dates, it adds exactly 6 months.
    """
    # Use UTC representation to match JS behavior
    bday_utc = birthday.astimezone(timezone.utc) if birthday.tzinfo else birthday.replace(tzinfo=timezone.utc)
    
    month = bday_utc.month - 1  # 0-indexed for logic matching JS
    day = bday_utc.day
    year = bday_utc.year

    # Special Case: Feb 29 birthday
    if month == 1 and day == 29:
        return "none"

    # Special Case: Aug 29 birthday in non-leap year (next Feb is non-leap)
    if month == 7 and day == 29:
        next_feb_year = year + 1
        if not is_leap_year(next_feb_year):
            return "none"

    # General Case: Add 6 months
    return _js_utc_date(year, month + 6, day, 
                        bday_utc.hour, bday_utc.minute, bday_utc.second, 
                        bday_utc.microsecond // 1000)

def get_accurate_half_birthday(birthday: datetime) -> datetime:
    """
    Calculates the accurate half birthday.
    
    - Finds the halfway point in time between the current birthday and the next one.
    - For Feb 29th birthdays, it finds the halfway point of the 4-year cycle.
    """
    # Use UTC representation to match JS behavior
    bday_utc = birthday.astimezone(timezone.utc) if birthday.tzinfo else birthday.replace(tzinfo=timezone.utc)
    
    month = bday_utc.month - 1
    day = bday_utc.day
    year = bday_utc.year

    # Special Case: Feb 29 birthday (4-year cycle)
    if month == 1 and day == 29 and is_leap_year(year):
        start = _js_utc_date(year, 1, 29, 
                             bday_utc.hour, bday_utc.minute, bday_utc.second,
                             bday_utc.microsecond // 1000)
        
        next_leap_year = year + 4
        # Even if next_leap_year is not actually a leap year (e.g. 2100), 
        # JS Date(2100, 1, 29) is March 1.
        next_birthday = _js_utc_date(next_leap_year, 1, 29,
                                      bday_utc.hour, bday_utc.minute, bday_utc.second,
                                      bday_utc.microsecond // 1000)
        
        diff = next_birthday - start
        return start + diff / 2

    # For accurate calculation, we use the specific timestamp of the birthday
    start = _js_utc_date(year, month, day, 
                         bday_utc.hour, bday_utc.minute, bday_utc.second,
                         bday_utc.microsecond // 1000)
                         
    next_birthday = _js_utc_date(year + 1, month, day,
                                  bday_utc.hour, bday_utc.minute, bday_utc.second,
                                  bday_utc.microsecond // 1000)
    
    diff = next_birthday - start
    return start + diff / 2
