import { describe, it, expect } from 'vitest';
import { getTraditionalHalfBirthday, getAccurateHalfBirthday, isLeapYear } from './index.js';

describe('Half Birthday Library', () => {
  describe('isLeapYear', () => {
    it('returns true for leap years', () => {
      expect(isLeapYear(2024)).toBe(true);
      expect(isLeapYear(2000)).toBe(true);
      expect(isLeapYear(2400)).toBe(true);
    });

    it('returns false for non-leap years', () => {
      expect(isLeapYear(2023)).toBe(false);
      expect(isLeapYear(1900)).toBe(false);
      expect(isLeapYear(2100)).toBe(false);
    });
  });

  describe('getTraditionalHalfBirthday', () => {
    it('calculates 6 months later for a standard date', () => {
      const bday = new Date(Date.UTC(2023, 0, 15)); // Jan 15
      const half = getTraditionalHalfBirthday(bday);
      expect(half).toBeInstanceOf(Date);
      if (half instanceof Date) {
        expect(half.getUTCMonth()).toBe(6); // July
        expect(half.getUTCDate()).toBe(15);
      }
    });

    it('calculates September 15, 2026 for a March 15, 2026 birthday', () => {
      const bday = new Date(Date.UTC(2026, 2, 15)); // March 15
      const half = getTraditionalHalfBirthday(bday);
      expect(half).toBeInstanceOf(Date);
      if (half instanceof Date) {
        expect(half.getUTCFullYear()).toBe(2026);
        expect(half.getUTCMonth()).toBe(8); // September
        expect(half.getUTCDate()).toBe(15);
      }
    });

    it('returns "none" for Aug 29 in a non-leap year cycle', () => {
      // Aug 29 2022 -> Feb 29 2023 (non-leap) -> none
      const bday = new Date(Date.UTC(2022, 7, 29));
      const half = getTraditionalHalfBirthday(bday);
      expect(half).toBe("none");
    });

    it('returns a Date for Aug 29 when the next Feb is a leap year', () => {
      // Aug 29 2023 -> Feb 29 2024 (leap) -> Date
      const bday = new Date(Date.UTC(2023, 7, 29));
      const half = getTraditionalHalfBirthday(bday);
      expect(half).toBeInstanceOf(Date);
    });

    it('returns "none" for Feb 29 birthday even on leap years', () => {
      const bday = new Date(Date.UTC(2024, 1, 29));
      const half = getTraditionalHalfBirthday(bday);
      expect(half).toBe("none");
    });
  });

  describe('getAccurateHalfBirthday', () => {
    it('calculates halfway point between birthdays', () => {
      const bday = new Date(Date.UTC(2023, 0, 1, 0, 0, 0));
      const half = getAccurateHalfBirthday(bday);
      // 2023 is non-leap, 365 days. 365 / 2 = 182.5 days.
      // July 2nd 12:00 UTC
      expect(half.getUTCMonth()).toBe(6); // July
      expect(half.getUTCDate()).toBe(2);
      expect(half.getUTCHours()).toBe(12);
    });

    it('handles Feb 29 4-year cycle accurately', () => {
      const bday = new Date(Date.UTC(2024, 1, 29, 0, 0, 0));
      const half = getAccurateHalfBirthday(bday);
      expect(half.getUTCFullYear()).toBe(2026);
      expect(half.getUTCMonth()).toBe(1); // Feb
      expect(half.getUTCDate()).toBe(28);
      expect(half.getUTCHours()).toBe(12);
    });
  });
});
