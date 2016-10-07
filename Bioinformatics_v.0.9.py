# Ofinley
# 
# Bioinformatics v0.9
#
#
#
#       TABLE OF CONTENTS
#   ___________________________________
#
#   1. Count of nucleotides in sequence
#
#   2. Transcription DNA to RNA
#
#   3. Reverse Complement of DNA
#
#   4. Fasta format handling
#
#   5. Compute GC Content
#
#   6. Count Point Mutations
#
#   7. Translation RNA to Protein
#
#   8. Length of Sequence
#
#   9. Find a Motif in DNA
#
#   10. Program Menu
#   ____________________________________
#
#
#   FASTA format handling not implemented yet.
#   This program only accepts raw sequences.
#   
#   Current Objectives/Ideas:
#   
#   1.) Complete FASTA format handling
#
#   2.) Add more analytical functions / Expand Table of Contents
#
#   3.) Add file reading
#   
#   4.) Create GUI through Visual Basic
#
#   

# Counts how many of each nucleotide in sample
def count_nuc(nu):
    count = {}
    count['A'] = 0
    count['C'] = 0
    count['T'] = 0
    count['G'] = 0

    for nucs in nu:
        count[nucs] += 1
    return count


# Transcribes DNA into RNA
def transcribe_DNA(dna):
    rna = ''
    for nu in dna:
        if nu == 'T':
            rna+= 'U'
        else:
            rna += nu
    return  rna

# Reverse Complement of a DNA strand
def reverse_Complement(dna):
    rc_dna = ''
    com =  {'G' : 'C', 'C' : 'G', 'A' : 'T', 'T' : 'A'}
    for nu in dna:
        rc_dna = com[nu] + rc_dna
    return rc_dna

# Enter Sequence
def enter_Seq():
    print 'Enter Sequence:'
    sequence = raw_input()

    return sequence

##############################
#       UNDER CONSTRUCTION   #

# Entering Fasta sequences
def parse_f():
    print 'Enter Fasta Sequence: '
    sequence = raw_input()
    result = parse_Fasta(sequence)

    return result
    

# Parsing Fasta formats
def parse_Fasta(d):
    results = {}
    strings = d.strip().split('>')

    for d in strings:
        if len(d) == 0:
            continue

        parts = d.split()
        label = parts[0]
        bases = ''.join(parts[1:])

        results[label] = bases

    return results

#      UNDER CONSTRUCTION    #
##############################

# Compute GC Content
def get_GC_Content(dna):
    size = len(dna)
    i = 0

    for j in dna:
        if j == 'G' or j == 'C':
            i+= 1
            
    return str(100 * (float(i) / size))


# Count Point Mutations between two strands
def count_Point_Mutations(s,t):
    result = abs(len(s) - len(t))
    
    for i in range(0,len(s)):
        if s[i] <> t[i]:
            result += 1
    return result


# Translates RNA into Protein
# Sequence must have AUG ** current error: String index out of range
# Currently runs only if sequence starts with AUG
# Errors occur when AUG is not at the front
# Purpose of this function is to find AUG and begin translation there
# until comes across a STOP or string ends.
def translation(rna):
    amino_acids = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
        "UCU":"S", "UCC":"s", "UCA":"S", "UCG":"S",
        "UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"STOP",
        "UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
        "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
        "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
        "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
        "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
        "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
        "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
        "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
        "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
        "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
        "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
        "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
        "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G",}

    
    protein_seq = ''
    start = rna.find('AUG')
    sequence = rna[start:]

    for i in range(0, len(sequence), 3):
        tablet = sequence[i] + sequence[i+1] + sequence[i+2]
        protein_seq = protein_seq + amino_acids[tablet]


    return protein_seq


# Find Motif in DNA
def find_Motif(s,t):
    locations = []
    slen = len(s)
    tlen = len(t)

    for i in range(0, slen, 1):
        if s[i:i+tlen] == t:
            locations.append(i)

    return locations
    
 
# Program Menu | Display Menu for Shell
def menu():
    while True:
        print ''
        print '    Bioinformatics v1.0'
        print '**************************\n'
        print '1) Count Nucleotides'
        print '2) Transcribe DNA to RNA'
        print '3) Reverse Complement of DNA'
        print '4) Compute GC Content'
        print '5) Count Point Mutations in two sequences'
        print '6) Translate RNA to Protein'
        print '7) Length of Sequence'
        print '8) Find Motif in DNA'
        print '9) FASTA TEST'
        print '\nPress 0 to quit'

        # Retrieve User input to determine what function to run
        selection = raw_input('Enter Selection: ')
        
        # Count Nucleotides
        if selection == '1':
            seq = enter_Seq()
            print '\nNucleotide count' + str(count_nuc(seq))
            
        # Transcribe DNA
        elif selection == '2':
            seq = enter_Seq()
            print '\nRNA: ' + str(transcribe_DNA(seq))
            
        # Reverse Complement of DNA
        elif selection == '3':
            seq = enter_Seq()
            print '\nReverse Complement: ' + str(reverse_Complement(seq))

        # Compute GC Content
        elif selection =='4':
            seq = enter_Seq()
            print '\nGC Content: ' + str(get_GC_Content(seq))

        # Count Point Mutations
        elif selection =='5':
            seq1 = enter_Seq()
            seq2 = enter_Seq()
            print '\nNumber of Point Mutations: ' + str(count_Point_Mutations(seq1,seq2))

        # Translate RNA to Protein | Sequence entered must start with AUG!
        elif selection =='6':
            seq = enter_Seq()
            print '\nProtein Sequence: '+ str(translation(seq))

        # Length of Sequence 
        elif selection =='7':
            seq = enter_Seq()
            print '\nLength of Sequence: ' + str(len(seq)) + ' bases long.'

        # Find Motif in DNA
        elif selection =='8':
            seq1 = enter_Seq()
            print 'Enter Motif to find.'
            seq2 = enter_Seq()
            print '\nMotif Locations: ' + str(find_Motif(seq1,seq2))

        # FASTA TEST **UNDER CONSTRUCTION**
        elif selection =='9':
            seq = enter_Seq()
            print str(parse_Fasta(seq))

        # Quits Program
        elif selection =='0':
            break

        # Invalid user input
        else:
            print '\nNot a valid selection!'

            

menu()

