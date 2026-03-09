# Half Birthday Calculator (Python)

A robust Python library for calculating half birthdays, ported from the original TypeScript version.

## Installation

```bash
pip install .
```

## Usage

```python
from datetime import datetime, timezone
from half_birthday_calc import get_traditional_half_birthday, get_accurate_half_birthday

birthday = datetime(1992, 2, 29, tzinfo=timezone.utc)

# Traditional returns "none" for Feb 29
traditional = get_traditional_half_birthday(birthday)
# traditional == "none"

# Accurate calculates the halfway point of the 4-year cycle
accurate = get_accurate_half_birthday(birthday)
# accurate == 1994-03-01 12:00:00+00:00
```

## Logic

### 1. Traditional Half Birthday
*   **Standard Rule**: Add exactly six months to the birthday.
*   **Special Case**: For February 29th birthdays, always returns `"none"`.
*   **Special Case**: For August 29th birthdays, returns `"none"` in non-leap years if the corresponding half-birthday would fall on Feb 29th.

### 2. Accurate Half Birthday
*   **Rule**: Calculate the halfway point in time (total microseconds divided by two) between two consecutive birthdays.
*   **Feb 29th Birthday**: Considers the full 4-year leap cycle and returns the halfway point (approximately 2 years later).

## Development

Run tests using pytest:

```bash
pytest
```
