import classes
import dicts
player = classes.Player("me", 15)
final = []
skills = []
def codGen(array):
    for codon in array:
        codon = codon.upper()
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
        else: raise ValueError("Input invalido")
    if "P" in final and "G" in final and "E" in final or "W" in final and "H" in final and "T" in final or final == ["P", "G", "E", "W", "H", "T"]:
        skills.append("Flight") #?
        skills.append("Horse")
    elif "Stop" in final:
        pass
    elif "V" in final and "N" in final and "K" in final and "P" in final and "G" in final and "E" in final or final == ["V", "N", "K", "P", "G", "E"]:
        skills.append("Human torso")
        skills.append("Horse")
    print(final)
    print(skills)
    if "Flight" in skills and "Horse" in skills:
        print('''
                Sequence identified!
                ["P", "G", "E", "W", "H", "T"] identified 
                You have developed a pegasus!
                ''')
        dicts.pegasId = True
        dicts.pegasCheck(dicts.pegasId)
    elif "Human torso" in skills and "Horse" in skills:
        print('''
        You have developed a centaur!
        ''')
        dicts.minotId = True
        dicts.minotCheck(dicts)

choice = input("Choose an option: ")
print('''
1: Append to species     
2: Calculate survival 
''')
if int(choice) == 1:
    print("1 working")

elif int(choice) == 2:
    print("2 working")
else:
    print("invalid ")


codGen(["TGG", "CAC", "ACG", "CCG", "GGA", "GAG", "CCA", "AAT", "TTA", "AAA", "TTT", "GGC"])
test = classes.Creature(name="Pegasus", skills=["Horse", "Flight"])
test.successRate = 11
print(test.successRate)
print(test.failRate(test.successRate))

