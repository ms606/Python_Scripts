export const COLORS = [
  'black',
  'brown',
  'red',
  'orange',
  'yellow',
  'green',
  'blue',
  'violet',
  'grey',
  'white',
];

export function decodedResistorValue(colors: string[]): string {
  const code1 = COLORS.indexOf(colors[0]);
  const code2 = COLORS.indexOf(colors[1]);
  const code3 = COLORS.indexOf(colors[2]);

  let totalOhms = (code1 * 10 + code2) * Math.pow(10, code3);

  // Dynamic unit conversion
  const units = ['ohms', 'kiloohms', 'megaohms', 'gigaohms'];
  let unitIndex = 0;

  while (totalOhms >= 1000 && unitIndex < units.length - 1) {
    totalOhms /= 1000;
    unitIndex++;
  }

  return `${totalOhms} ${units[unitIndex]}`;
}
