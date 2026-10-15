export function toRna(nucleotides : string) :string {
  let RNA = "";

   const TRANSACTION_MAP: Record<string, string> = {
    G: 'C',
    C: 'G',
    T: 'A',
    A: 'U'
  }
  
  for (const nucleotide of nucleotides)  {  
    if (!TRANSACTION_MAP[nucleotide]) {
      throw new Error('Invalid input DNA.')
    }
    RNA += TRANSACTION_MAP[nucleotide]
  }
  return RNA
}