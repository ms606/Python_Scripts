export function isLeap(year: number): boolean {
  const isDivisibleBy4 = year % 4 === 0;
  const isDivisibleBy100 = year % 100 === 0;
  const isDivisibleBy400 = year % 400 === 0;

  return isDivisibleBy4 && (!isDivisibleBy100 || isDivisibleBy400);
}
