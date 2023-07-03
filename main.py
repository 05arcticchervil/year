function isLeapYear(year) {
  if (year % 4 === 0) {
    if (year % 100 === 0) {
      if (year % 400 === 0) {
        return true;
      } else {
        return false;
      }
    } else {
      return true;
    }
  } else {
    return false;
  }
}

// Prompt the user to enter a year
const year = parseInt(prompt("Enter a year:"));

// Check if the year is a leap year
const leapYear = isLeapYear(year);

// Display the result
if (leapYear) {
  console.log(`${year} is a leap year.`);
} else {
  console.log(`${year} is not a leap year.`);
}
