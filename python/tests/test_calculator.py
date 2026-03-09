import pytest
from datetime import datetime, timezone
from half_birthday_calc import is_leap_year, get_traditional_half_birthday, get_accurate_half_birthday

def test_is_leap_year():
    assert is_leap_year(2024) is True
    assert is_leap_year(2000) is True
    assert is_leap_year(2400) is True
    assert is_leap_year(2023) is False
    assert is_leap_year(1900) is False
    assert is_leap_year(2100) is False

def test_get_traditional_half_birthday_standard():
    # Jan 15 2023
    bday = datetime(2023, 1, 15, tzinfo=timezone.utc)
    half = get_traditional_half_birthday(bday)
    assert isinstance(half, datetime)
    assert half.month == 7 # July
    assert half.day == 15

def test_get_traditional_half_birthday_aug29_non_leap():
    # Aug 29 2022 -> Feb 29 2023 (non-leap) -> none
    bday = datetime(2022, 8, 29, tzinfo=timezone.utc)
    half = get_traditional_half_birthday(bday)
    assert half == "none"

def test_get_traditional_half_birthday_aug29_leap():
    # Aug 29 2023 -> Feb 29 2024 (leap) -> Date
    bday = datetime(2023, 8, 29, tzinfo=timezone.utc)
    half = get_traditional_half_birthday(bday)
    assert isinstance(half, datetime)
    assert half.month == 2
    assert half.day == 29

def test_get_traditional_half_birthday_feb29():
    # Feb 29 2024 -> none
    bday = datetime(2024, 2, 29, tzinfo=timezone.utc)
    half = get_traditional_half_birthday(bday)
    assert half == "none"

def test_get_accurate_half_birthday_standard():
    # Jan 1 2023 00:00:00
    bday = datetime(2023, 1, 1, 0, 0, 0, tzinfo=timezone.utc)
    half = get_accurate_half_birthday(bday)
    # 2023 is non-leap, 365 days. 365 / 2 = 182.5 days.
    # July 2nd 12:00 UTC
    assert half.month == 7
    assert half.day == 2
    assert half.hour == 12

def test_get_accurate_half_birthday_feb29_cycle():
    # Feb 29 2024 00:00:00
    bday = datetime(2024, 2, 29, 0, 0, 0, tzinfo=timezone.utc)
    half = get_accurate_half_birthday(bday)
    assert half.year == 2026
    assert half.month == 2
    assert half.day == 28
    assert half.hour == 12
