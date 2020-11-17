final = []
def codGen(array):
    for codon in array: #mesma funcao da roda do code crack
        if codon == "TTT" or codon == "TTC": final.append("F")
        elif codon == "TTA" or codon == "TTG" or codon == "CTT" or codon == "CTC" or codon == "CTA" or codon == "CTG": final.append("L")
        elif codon == "ATT" or codon == "ATC" or codon == "ATA": final.append("I")
        elif codon == "ATG": final.append("M")
        elif codon == "GTT" or codon == "GTC" or codon == "GTA" or codon == "GTG": final.append("V")
        elif codon == "TCT" or codon == "TCC" or codon == "TCA" or codon == "TCG" or codon == "AGT" or codon == "AGC": final.append("S")
        elif codon == "CCT" or codon == "CCC" or codon == "CCA" or codon == "CCG": final.append("P")
        elif codon == "ACT" or codon == "ACC" or codon == "ACA" or codon == "ACG": final.append("T")
        elif codon == "GCT" or codon == "GCC" or codon == "GCA" or codon == "GCG": final.append("A")
        elif codon == "TAT" or codon == "TAC": final.append("Y")
        elif codon == "TAA" or codon == "TAG" or codon == "TGA": final.append("Stop")
        elif codon == "CAT" or codon == "CAC": final.append("H")
        elif codon == "CAA" or codon == "CAG": final.append("Q")
        elif codon == "AAT" or codon == "AAC": final.append("N")
        elif codon == "AAA" or codon == "AAG": final.append("K")
        elif codon == "GAT" or codon == "GAC": final.append("D")
        elif codon == "GAA" or codon == "GAG": final.append("E")
        elif codon == "TGT" or codon == "TGC": final.append("C")
        elif codon == "TGG": final.append("W")
        elif codon == "CGT" or codon == "CGC" or codon == "CGA" or codon == "CGG" or codon == "AGA" or codon == "AGG": final.append("R")
        elif codon == "GGT" or codon == "GGC" or codon == "GGA" or codon == "GGG": final.append("G")
        else: raise ValueError("Invalid")
    if final == ["P", "G", "E", "N", "L", "C", "Y", "R", "K", "M", "W", "C"]:
        print("""
        What is it?: Snake poison protein
        What does it do?: Enables snakes to kill their food when they bite them.
        """)
    elif final == ["M", "K", "S", "A", "I", "L", "T", "G", "L", "L", "F", "V"]:
        print("""
        Antifreeze
        Stops fish from freezing.
        """)
    elif final == ["E", "N", "M", "E", "N", "D", "E", "N", "I", "V", "Y", "G"]:
      print('''
      What is it?: Light maker protein
      What does it do?: Used by fireflies to create light in their tails
      ''')
    elif final ==  ["G", "W", "A", "L", "R", "I", "M", "F", "L", "H", "L", "Y"]:
      print("""
      What is it?: Smell detector protein
      What does it do?: Helps mosquitoes smell human sweat
      """)

    print(final)
#tira o # pra testar cada um. se dois tiverem sem comentario so a primeira sequencia vai ser printada
#codGen(["ATG", "AAG", "TCA", "GCT", "ATT", "TTA", "ACC", "GGT", "TTG", "CTT", "TTC", "GTC"])
#codGen(["GAA", "AAC", "ATG", "GAG", "AAC", "GAT", "GAA", "AAT", "ATT", "GTG", "TAT", "GGT"])
#codGen(["GGT", "TGG", "GCT", "TTG", "CGG", "ATC", "ATG", "TTT", "CTA", "CAT", "CTG", "TAC"])
#codGen(["CCT", "GGG", "GAG", "AAC", "CTA", "TGC", "TAT", "AGA", "AAG", "ATG", "TGG", "TGC"])
