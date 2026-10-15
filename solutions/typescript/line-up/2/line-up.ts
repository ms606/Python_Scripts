export function format(name: string, number: number): string {
  const numStr = number.toString();
  let suffix = 'th'
  
  if (numStr.endsWith('1') && !numStr.endsWith('11')){
    suffix = 'st'
  }
  if (numStr.endsWith('2') && !numStr.endsWith('12') ){
    suffix = 'nd'
  }
  if (numStr.endsWith('3') && !numStr.endsWith('13')){
    suffix = 'rd'
  }
  
  return `${name}, you are the ${number}${suffix} customer we serve today. Thank you!`
}
