export function decodedValue(names: string[]) : number  {
  return (COLORS.indexOf(names[0])*10)+COLORS.indexOf(names[1])
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
  'white'
];