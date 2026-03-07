# half-birthday-calc

A TypeScript library for calculating somebody's half birthday.

## Features
- **Traditional Half Birthday**: Calculated by adding exactly six months to the birthday.
- **Accurate Half Birthday**: Calculated by finding the halfway point in time between consecutive birthdays.

## Installation

### From GitHub Packages
To install this library from the GitHub Package Registry, you first need to configure npm to use the GitHub Packages registry for the `@seancrosby` scope. Create or update your `.npmrc` file:

```text
@seancrosby:registry=https://npm.pkg.github.com
```

Then install the package:
```bash
npm install @seancrosby/half-birthday-calc
```

## Usage

### In an HTML Page (using a CDN like unpkg)
> Note: For GitHub Packages, CDN access might differ. If published to npm, use:
```html
<script type="module">
  import { getTraditionalHalfBirthday, getAccurateHalfBirthday } from 'https://unpkg.com/@seancrosby/half-birthday-calc/dist/index.js';

  const myBirthday = new Date('1990-06-15');
  console.log('Traditional:', getTraditionalHalfBirthday(myBirthday));
  console.log('Accurate:', getAccurateHalfBirthday(myBirthday));
</script>
```

### In a TypeScript/JavaScript project
```typescript
import { getTraditionalHalfBirthday, getAccurateHalfBirthday } from '@seancrosby/half-birthday-calc';

const birthday = new Date('1992-02-29');
// Traditional returns "none" for Feb 29
console.log(getTraditionalHalfBirthday(birthday)); 
// Accurate returns the halfway point of the 4-year cycle
console.log(getAccurateHalfBirthday(birthday));
```

## API Documentation

### `isLeapYear(year: number): boolean`
Returns `true` if the year is a leap year, `false` otherwise.

### `getTraditionalHalfBirthday(birthday: Date): Date | "none"`
Calculates the traditional half birthday by adding six months. 
- **Special Case**: For February 29th birthdays, always returns `"none"`.
- **Special Case**: For August 29th birthdays, returns `"none"` in non-leap years if the corresponding half-birthday would fall on Feb 29th.

### `getAccurateHalfBirthday(birthday: Date): Date`
Calculates the accurate half birthday by finding the halfway point in time between birthdays.
- **Feb 29th Birthday**: Considers the full 4-year leap cycle and returns the halfway point (approximately 2 years later).
- **Precision**: If the `Date` object includes hours/minutes/seconds, the calculation will account for them.
