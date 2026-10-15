export function format(name: string, number: number): string {
  const numStr = number.toString();
  
  if (numStr.endsWith('1') && !numStr.endsWith('11')){
    return  `${name}, you are the ${numStr}st customer we serve today. Thank you!`
  }
  if (numStr.endsWith('2') && !numStr.endsWith('12') ){
    return  `${name}, you are the ${numStr}nd customer we serve today. Thank you!`
  }
  if (numStr.endsWith('3') && !numStr.endsWith('13')){
    return  `${name}, you are the ${numStr}rd customer we serve today. Thank you!`
  }
  
  return `${name}, you are the ${numStr}th customer we serve today. Thank you!`
}
