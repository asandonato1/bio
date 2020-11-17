wiki = {1:''}
pegasId = False
minotId = False
def pegasCheck(pegasId):
    if pegasId == True:
        wiki[1] = "Pegasus = P, G, E, W, H, T"
        #print(wiki)
    else:
        pass
def minotCheck(minotId):
    if minotId == True:
        wiki[2] = "Minotaur"
        print(wiki)
    else:
        pass

f = open("text.txt", 'a')
f.write("stop appending me")
f.close()
