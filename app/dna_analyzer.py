def analyze_dna_sequence(dna_sequence):
    # Simple analysis example: Counting nucleotides
    analysis = {
        'length': len(dna_sequence),
        'A': dna_sequence.count('A'),
        'T': dna_sequence.count('T'),
        'C': dna_sequence.count('C'),
        'G': dna_sequence.count('G'),
    }
    return analysis
