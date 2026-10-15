export function toRna(nucleotides : string) :string {
  let RNA = "";

  if (nucleotides === null) throw new Error('Invalid input DNA.');
  
  for( const nucleotide of nucleotides ){
    
    if (nucleotide === 'G') {
      RNA += 'C'
    }
    else if (nucleotide === 'C') {
      RNA += 'G'
    }
    else if (nucleotide === 'T') {
      RNA += 'A'
    }
    else if (nucleotide === 'A') {
      RNA += 'U'
    }
    else {
      throw new Error('Invalid input DNA.');  
    }
  }
  return RNA;
}