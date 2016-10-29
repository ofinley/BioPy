# 
# github.com/ofinley
# BioPy v1.0
# Python 2.7.6
#
#
#   Data Entry/Handling: 1-3
#   Functions          : 4-12
#   Shell Program Menu : 13
#
#
#       TABLE OF CONTENTS
#   ___________________________________
#
#   1. FASTA format handling            
#                                           
#   2. FASTA Object                         
#
#   3. File Reading/Handling
#
#   4. Counting of Nucleotides
#
#   5. Transcription (DNA to RNA)
#
#   6. Reverse Complement of DNA
#
#   7. Compute GC Content
#
#   8. Count Point Mutations
#
#   9. Amino Acid Table
#
#   10. Translation (RNA to Protein)
#
#   11. Length of Sequence
#
#   12. Find a Motif in DNA
#
#   13. Shell Program Menu
#   ____________________________________
#
#
#   FASTA format handling not implemented yet.
#   This program only accepts raw sequences.
#   
#   Current Objectives/Ideas:
#   
#   1.) Complete FASTA format handling - Completed 
#
#   2.) Add more analytical functions / Expand Table of Contents
#
#   3.) Add file reading - Completed
#   
#   4.) Create GUI through Visual Basic/Other
#
#   





###############################################################################

#   DATA ENTRY

###############################################################################



# Detecting FASTA sequence
def detect_FASTA(string):
    if '>' in string:
        return True
    else:
        return False

# Enter Sequence
def enter_Seq():
    print 'Enter Sequence:'
    sequence = raw_input()

    # Detect for FASTA sequence
    if detect_FASTA(sequence) == True:
        new_seq = parse_Fasta(sequence)
        return new_seq.sequence
    else:
        return sequence


# FASTA files begin a '>' followed by a title identifying the sequence
# The line directly under the title is all of the sequence information
# of that identified in the title.

# Entering Fasta sequences
def parse_f():
    print 'Enter Fasta Sequence: '
    sequence = raw_input()
    result = parse_Fasta(sequence)

    return result
    

# Parsing Fasta formats
def parse_Fasta(d):

    # Get Title of FASTA
    d.find('>')
    entry = d.splitlines(0)
    title = entry[0]

    # Rebuild Sequence into String from List
    sequence = entry[0:]
    rebuilt_seq = ''

    for i in range(1,len(sequence)):
        rebuilt_seq = rebuilt_seq + sequence[i]
        
    fasta = fastaObject(title,rebuilt_seq)

    return fasta

def enter_File():
    print 'Enter File Path: '
    file_path = raw_input()

    return file_path

def read_File(f):

    i = open(f)
    j = i.read()

    if detect_FASTA(j)== True:
        print 'true'
        fasta = parse_Fasta(j)
        print fasta.title
        print 'sequence found'
        print fasta.sequence
    else:
        print j

    i.close() 
    
    
    



################################################################################

#   END OF DATA ENTRY                                                          #

################################################################################






###############################################################################

#   OBJECTS                                                                   #

###############################################################################



class fastaObject(object):
    def __init__(self,title,sequence):
        self.title = title
        self.sequence = sequence
        

        
###############################################################################

#   END OF OBJECTS

###############################################################################






###############################################################################

#   FUNCTIONS                                                                 #

###############################################################################



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


# Amino Acid Table
def aa_table(rna):
    
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

    protein = amino_acids[rna]

    return protein


# Translates RNA into Protein
def translation(rna):

    protein_seq = ''
    start = rna.find('AUG')
    sequence = rna[start:]

    for i in range(0, len(sequence), 3):
        tablet = sequence[i] + sequence[i+1] + sequence[i+2]
        protein_seq = protein_seq + aa_table(tablet)


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

###############################################################################

#   END OF FUNCTIONS                                                          #    

###############################################################################






 
# Program Menu | Display Menu for Shell
def menu():
    while True:
        print ''
        print '    BioPy v1.0'
        print '**************************\n'
        print '1) Count Nucleotides'
        print '2) Transcribe DNA to RNA'
        print '3) Reverse Complement of DNA'
        print '4) Compute GC Content'
        print '5) Count Point Mutations in two sequences'
        print '6) Translate RNA to Protein'
        print '7) Length of Sequence'
        print '8) Find Motif in DNA'
        print '9) File Read Test'
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

        # Translate RNA to Protein | Sequence must contain AUG at the moment!
        elif selection =='6':
            seq = enter_Seq()
            print '\nProtein Sequence: '+ str(translation(seq))

        # Length of Sequence 
        elif selection =='7':
            seq = enter_Seq()
            length = seq.strip('\n')
            print '\nLength of Sequence: ' + str(len(length)) + ' bases long.'

        # Find Motif in DNA
        elif selection =='8':
            seq1 = enter_Seq()
            print 'Enter Motif to find.'
            seq2 = enter_Seq()
            print '\nMotif Locations: ' + str(find_Motif(seq1,seq2))

        # Read File Test
        elif selection =='9':
            file_entry = enter_File()
            read_File(file_entry)


        # Quits Program
        elif selection =='0':
            break

        # Invalid user input
        else:
            print '\nNot a valid selection!'

            

menu()

