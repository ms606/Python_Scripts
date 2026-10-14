export function decodedResistorValue(colors: string[]): string {
  const resistor1 = COLORS.indexOf(colors[0]) * 10
  const resistor2 = COLORS.indexOf(colors[1])
  const resistor3 = Math.pow(10, COLORS.indexOf(colors[2]))

  let totalOhms = (resistor1+resistor2)* resistor3;
  
if (totalOhms >= 1000000000) {
    return (totalOhms / 1000000000) + ' gigaohms'
  }
  else if (totalOhms >= 1000000) {
    return (totalOhms / 1000000) + ' megaohms'
  }
  else if (totalOhms >= 1000) {
    return (totalOhms / 1000) + ' kiloohms'
  }
  else {
    return totalOhms + ' ohms'
  }
}
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