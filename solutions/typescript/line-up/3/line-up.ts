export function format(name: string, number: number): string {
  const specialTeens = number % 100;
  let suffix = 'th';
  
  
  if (specialTeens !== 11 && specialTeens !== 12 && specialTeens !== 13 ) {
    switch(number % 10){
      case 1: suffix = 'st'; break;
      case 2: suffix = 'nd'; break;
      case 3: suffix = 'rd'; break;
        
    }
  }

  return `${name}, you are the ${number}${suffix} customer we serve today. Thank you!`
}
