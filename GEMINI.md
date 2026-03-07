# Half Birthday Calculator Mandates (TypeScript)

This document outlines the core logic and development standards for the `half-birthday-calc` library.

## Project Goal
Create a robust, well-tested TypeScript library for calculating half birthdays with two primary calculation methods.

## Core Logic Requirements

### 1. Traditional Half Birthday (`getTraditionalHalfBirthday`)
*   **Standard Rule**: Add exactly six months to the birthday.
*   **Aug 29th Special Case**: In non-leap years, if the half-birthday would fall on February 29th, the function returns `"none"`.
*   **Feb 29th Birthday Special Case**: Always returns `"none"`.
*   **Input**: A `Date` object representing the birthday.
*   **Output**: The next occurring half birthday (as a `Date`) or `"none"`.

### 2. Accurate Half Birthday (`getAccurateHalfBirthday`)
*   **Rule**: Calculate the halfway point in time (total milliseconds divided by two) between two consecutive birthdays.
*   **Time Support**: Supports time of birth for higher precision.
*   **Feb 29th Birthday Special Case**: Calculate the halfway point of the full 4-year cycle.
*   **Aug 29th Handling**: No special handling (standard day-count logic applies).
*   **Input**: A `Date` object representing the birthday.
*   **Output**: The next occurring half birthday (as a `Date`).

## Engineering Standards
*   **Environment**: Node.js/Browser compatible (compile to ESM/CJS).
*   **Testing**: Use **Vitest** for comprehensive unit testing.
*   **Documentation**: Maintain a `README.md` with clear instructions on library inclusion and API usage.
*   **Surgical Edits**: Follow the codebase conventions and maintain high type safety/documentation standards.
*   **Build Tooling**: Use `tsc` for compilation.
