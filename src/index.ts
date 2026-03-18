/**
 * Checks if a year is a leap year.
 */
export function isLeapYear(year: number): boolean {
  return (year % 4 === 0 && year % 100 !== 0) || (year % 400 === 0);
}

/**
 * Calculates the traditional half birthday (six months after the birthday).
 * 
 * - For February 29th birthdays, it always returns "none".
 * - For August 29th, it returns "none" in non-leap years if the half-birthday would fall on Feb 29th.
 * - For all other dates, it adds exactly 6 months.
 */
export function getTraditionalHalfBirthday(birthday: Date): Date | "none" {
  const month = birthday.getUTCMonth(); // 0-indexed (Jan=0, Feb=1, Aug=7)
  const day = birthday.getUTCDate();
  const year = birthday.getUTCFullYear();

  // Special Case: Feb 29 birthday always returns "none" per mandate
  if (month === 1 && day === 29) {
    return "none";
  }

  // Calculate target month (6 months later)
  const targetMonth = (month + 6) % 12;
  const result = new Date(Date.UTC(year, month + 6, day));

  // If the month of the result doesn't match our target, it means the day overflowed
  // (e.g., Aug 30 -> Feb 30 becomes March 1 or 2)
  if (result.getUTCMonth() !== targetMonth) {
    return "none";
  }

  return result;
}

/**
 * Calculates the accurate half birthday.
 * 
 * - Finds the halfway point in time between the current birthday and the next one.
 * - For Feb 29th birthdays, it finds the halfway point of the 4-year cycle.
 */
export function getAccurateHalfBirthday(birthday: Date): Date {
  const month = birthday.getUTCMonth();
  const day = birthday.getUTCDate();
  const year = birthday.getUTCFullYear();

  // Special Case: Feb 29 birthday (4-year cycle)
  if (month === 1 && day === 29 && isLeapYear(year)) {
    const start = Date.UTC(year, 1, 29);
    const nextLeapYear = year + 4;
    const nextBirthday = Date.UTC(nextLeapYear, 1, 29);
    
    const diff = nextBirthday - start;
    return new Date(start + diff / 2);
  }

  const start = Date.UTC(year, month, day, 
                         birthday.getUTCHours(), 
                         birthday.getUTCMinutes(), 
                         birthday.getUTCSeconds(), 
                         birthday.getUTCMilliseconds());

  const nextBirthday = Date.UTC(year + 1, month, day,
                                 birthday.getUTCHours(), 
                                 birthday.getUTCMinutes(), 
                                 birthday.getUTCSeconds(), 
                                 birthday.getUTCMilliseconds());
  
  const diff = nextBirthday - start;
  return new Date(start + diff / 2);
}
