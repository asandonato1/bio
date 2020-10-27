final = []
def codGen(codon):  # tyr = y, ser = s , trp = w. thr = t, asn = n
  if codon == "TTT" or codon == "TTC":
    final.append("F")
    return "F"
  elif codon == "TTA" or codon == "TTG" or codon == "CTT" or codon == "CTC" or codon == "CTA" or codon == "CTG":
    final.append("L")
    return "L"
  elif codon == "ATT" or codon == "ATC" or codon == "ATA":
    final.append("I")
    return "I"
  elif codon == "ATG":
    final.append("M")
    return "M"
  elif codon == "GTT" or codon == "GTC" or codon == "GTA" or codon == "GTG":
    final.append("V")
    return "V"
  elif codon == "TCT" or codon == "TCC" or codon == "TCA" or codon == "TCG" or codon == "AGT" or codon == "AGC":
    final.append("S")
    return "S"
  elif codon == "CCT" or codon == "CCC" or codon == "CCA" or codon == "CCG":
    final.append("P")
    return "P"
  elif codon == "ACT" or codon == "ACC" or codon == "ACA" or codon == "ACG":
    final.append("T")
    return "T"
  elif codon == "GCT" or codon == "GCC" or codon == "GCA" or codon == "GCG":
    final.append("A")
    return "A"
  elif codon == "TAT" or codon == "TAC":
    final.append("Y")
    return "Y"
  elif codon == "TAA" or codon == "TAG" or codon == "TGA":
    final.append("Stop")
    return "Stop"
  elif codon == "CAT" or codon == "CAC":
    final.append("H")
    return "H"
  elif codon == "CAA" or codon == "CAG":
    final.append("Q")
    return "Q"
  elif codon == "AAT" or codon == "AAC":
    final.append("N")
    return "N"
  elif codon == "AAA" or codon == "AAG":
    final.append("K")
    return "K"
  elif codon == "GAT" or codon == "GAC":
    final.append("D")
    return "D"
  elif codon == "GAA" or codon == "GAG":
    final.append("E")
    return "E"
  elif codon == "TGT" or codon == "TGC":
    final.append("C")
    return "C"
  elif codon == "TGG":
    final.append("W")
    return "W"
  elif codon == "CGT" or codon == "CGC" or codon == "CGA" or codon == "CGG" or codon == "AGA" or codon == "AGG":
    final.append("R")
    return "R"
  elif codon == "GGT" or codon == "GGC" or codon == "GGA" or codon == "GGG":
    final.append("G")
    return "G"
#codon = input("Enter a codon: ")
codGen("CCT")
codGen("GGG")
codGen("GAG")
codGen("AAC")
codGen("CTA")
codGen("TGC")
codGen("TAT")
codGen("AGA")
codGen("AAG")
codGen("ATG")
codGen("TGG")
codGen("TGC")
final_format = final.split("'")
print(final)
