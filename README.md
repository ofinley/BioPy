# BioPy
Python bioinformatics script that is able to count nucleotides, find length of sequence, transcription DNA to RNA, reverse complement of DNA, compute GC content, count point mutations, translate RNA to protein, and find a motif in DNA. More analytical functions to be added as well as implementing FASTA format handling, and file reading. Currently runs in Python 2.7.12.

Currently the BioPy GUI does not work correctly. Playing around with the Tkinter package in Python to learn how to utilize it properly to give BioPy a well organized and easy to use GUI.

You can download Python 2.7.12 at https://www.python.org/downloads/. GUI used for BioPy development is IDLE.

With the latest update, file reading has been implemented and being tested.






Current BioPy Functions 
-----------------------------------------
Note: FASTA is now accepted with the latest update. Enter a FASTA sequence into any function and works as if only a sequence was entered.

1.) Count Nucleotides in a sequence

    Enter a DNA sequence and returns the number of 'A','T','C', and 'G' present. Only works for DNA currently.
    
    Ex.) Input Sequence: ATTATTAGGGCC
         Result: Nucleotide count{'A': 3, 'C': 2, 'T': 4, 'G': 3}
         

2.) Transcription (DNA to RNA)
  
    Enter a DNA sequence and converts it to RNA.
    
    Ex.) Input Sequence: GATTCATTGGACCT
         Result: RNA: GAUUCAUUGGACCU
         
         
3.) Reverse Complement of DNA

    Enter a DNA sequence and returns the reverse complement of the input.
    
    Ex.) Input Sequence: ATTACTAGGCA
         Result: Reverse Complement: TGCCTAGTAAT
         
         
4.) FASTA Object/Handling
    
    Enter a sequence with a FASTA format and converts the input into a FASTA object that contains
    the title of the sequence, and the sequence itself. Useful for parsing data.

    Ex.)
    
    >gi|256355061:5001-2225382 Homo sapiens dystrophin (DMD), RefSeqGene (LRG_199) on chromosome X
    CGTTAAATGCAAACGCTGCTCTGGCTCATGTGTTTGCTCCGAGGTATAGGTTTTGTTCGACTGACGTATC
    AGATAGTCAGAGTGGTTACCACACCGACGTTGTAGCAGCTGCATAATAAATGACTGAAAGAATCATGTTA
    GGCATGCCCACCTAACCTAACTTGAATCATGCGAAAGGGGAGCTGTTGGAATTCAAATAGACTTTCTGGT
    TCCCAGCAGTCGGCAGTAATAGAATGCTTTCAGGAAGATGACAGAATCAGGAGAAAGATGCTGTTTTGCA
    CTATCTTGATTTGTTACAGCAGCCAACTTATTGGCATGATGGAGTGACAGGAAAAACAGCTGGCATGGAA
    GGTAGGATTATTAAAGCTATTACATCATTACAAATACAATTAGAAGCTGGCCATGACAAAGCATATGTTT
    GAACAAGCAGCTGTTGGTAGCTGGGGTTTGTTGCCGAGCTCTTCAAACTCTGCAAACAGTGTTGCTTTTA
    CAGAATGGATTTTAAAATTGCCTTGTGCTGCGTTAGATTTTGGGGAGGGGGTGTGCTTGCCTCCAACCTC
          

5.) Compute GC Content

    Enter DNA or RNA sequence and computes how many 'G' and 'C' occur within the sequence and returns a percentage.
    
    Ex.) Input Sequence: ATTAGCGGGGACCTGCCC
         Result: GC Content: 66.6666666667
         
         
6.) Translation (RNA to Protein)

    Enter RNA sequence and the sequence is translated to protein using an amino acid table. Note that the sequence 
    must contain the start codon 'AUG' somewhere in the sequence to start translation and the length from 'AUG' to
    the end of the string must be divisible by three. Stopping at the stop codons or checking the reading frames has
    not been implemented yet.
    
    Ex.) Input Sequence: AAAAAUUCCGAUGGGUGAUGUUAGU
         Result: MGDVS
         
         
7.) Sequence Length
 
     Enter DNA, RNA, or protein sequence and returns the length of the sequence/string.
     
     Ex.) Input Sequence: ATTAGGGATGTAAAAAAAAAAA
          Result: Length of Sequence: 22 bases long.
          
          
          
8.) Find Motif in DNA

    Enter a DNA sequence, and then enter a motif to find within that sequence. Returns locations in the sequence to 
    where the motif is found.
    
    
    Ex.) Input Sequence: ATTTACGACAGTTTAAAAACATCATCCCGG
         Input Motif   : CAT
         Result:       : Motif Locations: [19, 22]


9.) File Read Test

    Enter a path to a text file containing a FASTA sequence or raw text sequence and BioPy will read it.
    
    Ex.) Enter File Path: C:\Documents\Test_Files\test_sequence.txt
         Result: 
    >gi|1049006351:38940602-38958746 Xenopus tropicalis strain Nigerian chromosome 9, Xenopus_tropicalis_v9.1
    GCTTGTGTTTCAAATGATAAGTTCCTGGATGGCAATTAATTGCCTGTCTTGCACGACTGAGAGTCTGCAT
    TTTGCCAGCTGGATGCATTGTCTGTGTGACAGCCAATCGCTGGCTCTGATGACACAAGAGAAACTCAAGT
    TGGACTATAAAAGTTCACTTGGAAATAGCATGATTTATCATGGAGAGGTATTTTCTTCTTCACTTTTTAT
    TTCTGTAACTGTTGGCATTACCAGAAATAGAAAATTGAATTATATGACTATATAAGAACATGAATAGGTT
    ACGTGCATGGTGCTGCTGTTATCTGTGTTTGCTGGTAGCATTTAGTCCAGTGGATCTGACCAACAGCAAT
    AAAGCAACAGACAAAGATACATTGTGCAGTGCCTGTACCTGGAGACAGAACAGCAAATCTTCAAGGCTTG
    AAGCTATCAAACTGCAGATCCTTAGCAAACTTCGACTGGAGCAGGCACCTAATATTAGTAAGGATGCTAT
    AAAATATCTTTTACCTAAAGCACCACCATTAGAAGAATTAATCGACCAGTATGACCTCCAAAGTGATGAC
    AGCAGTGAGGGATCTTTGGAAGAAGATGATTACCATGCCACCACTGAAACAATCATTACAATGCCTACAG
    AATGTAAGTAAAATGTTACTGTATCAAGCAGACATCTAGTTCTCATTTGGGGCACAAGTATAAATGTATT
    TTTTTTTCTTTTTTCTACTGGCAAGCAGTTCGCTACTAAGCAGAAGGGTGGGGAATACAGTGACTTTTTC
