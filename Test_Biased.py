import csv
from array import array
import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import transforms
import math as math
from tkinter import *
from tqdm import tqdm

#remove files from previous run
with open('Matched_Fragments.csv', 'w') as csvFile:
    csvFile.close()
os.remove('Matched_Fragments.csv')
with open('Matched_Fragments_V2.csv', 'w') as csvFile:
    csvFile.close()
os.remove('Matched_Fragments_V2.csv')

#PPM Error for fragments
file = open("PPM_Error.txt", "r")
PPM_Error_tolerance = float(file.readline())
file.close()
os.remove("PPM_Error.txt")

#Import Number Of amino acids for internal fragments
file = open("Number_of_AA.txt", "r")
entered_number = int(file.readline())
Number_of_AA_Int_frag = entered_number + 1
Int_frag_endpoint = entered_number + 1
file.close()
os.remove("Number_of_AA.txt")

#N-Terminal Modification
'''AC = 42.01056 #Acetylation
DA = -0.9846 #Deaminated
ME = 14.01565 #Methylation
DME = 28.0313 #Dimethylation
FM = 27.99491 #Formylation
NA = 0'''
file = open("N_Term_Mod.txt", "r")
N_Term_Mod = float(file.readline())
file.close()
os.remove("N_Term_Mod.txt")



#C-Terminal Mofidicaiton
'''AM = -0.9846 #Amidated
ME = 14.01565 #Methylation
DH = -18.0106 #Dehydrated
NA = 0'''
file = open("C_Term_Mod.txt", "r")
C_Term_Mod = float(file.readline())
file.close()
os.remove("C_Term_Mod.txt")

#Import Type of Fragments
file = open("A_Fragments.txt", "r")
Search_A_Fragments = int(file.readline())
file.close()
os.remove("A_Fragments.txt")

file = open("B_Fragments.txt", "r")
Search_B_Fragments = int(file.readline())
file.close()
os.remove("B_Fragments.txt")

file = open("C_Fragments.txt", "r")
Search_C_Fragments = int(file.readline())
file.close()
os.remove("C_Fragments.txt")

file = open("X_Fragments.txt", "r")
Search_X_Fragments = int(file.readline())
file.close()
os.remove("X_Fragments.txt")

file = open("Y_Fragments.txt", "r")
Search_Y_Fragments = int(file.readline())
file.close()
os.remove("Y_Fragments.txt")

file = open("Z_Fragments.txt", "r")
Search_Z_Fragments = int(file.readline())
file.close()
os.remove("Z_Fragments.txt")

file = open("AX_Fragments.txt", "r")
Search_AX_Fragments = int(file.readline())
file.close()
os.remove("AX_Fragments.txt")

file = open("AY_Fragments.txt", "r")
Search_AY_Fragments = int(file.readline())
file.close()
os.remove("AY_Fragments.txt")

file = open("AZ_Fragments.txt", "r")
Search_AZ_Fragments = int(file.readline())
file.close()
os.remove("AZ_Fragments.txt")

file = open("BX_Fragments.txt", "r")
Search_BX_Fragments = int(file.readline())
file.close()
os.remove("BX_Fragments.txt")

file = open("BY_Fragments.txt", "r")
Search_BY_Fragments = int(file.readline())
file.close()
os.remove("BY_Fragments.txt")

file = open("BZ_Fragments.txt", "r")
Search_BZ_Fragments = int(file.readline())
file.close()
os.remove("BZ_Fragments.txt")

file = open("CX_Fragments.txt", "r")
Search_CX_Fragments = int(file.readline())
file.close()
os.remove("CX_Fragments.txt")

file = open("CY_Fragments.txt", "r")
Search_CY_Fragments = int(file.readline())
file.close()
os.remove("CY_Fragments.txt")

file = open("CZ_Fragments.txt", "r")
Search_CZ_Fragments = int(file.readline())
file.close()
os.remove("CZ_Fragments.txt")

#Import whether to include proline fragments
file = open("Proline_fragments.txt", "r")
Proline_fragments = int(file.readline())
file.close()
os.remove("Proline_fragments.txt")

#Atom Masses
n = 14.003074
o = 15.994915
h = 1.007825
p = 1.007276
car = 12.000000

#Import Amino Acid Sequence
Seq = open("Sequence.txt","r")
string = Seq.read()
List = list(string)
x = len(List)
length_sequence = len(List)
Seq.close()

#Import Ammino Acid masses
open("AminoAcids.csv","r")
AAs = []
MSs = []
with open("AminoAcids.csv") as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        AAs.append(row[0])
        MSs.append(row[1])
MSs_int= list(map(float, MSs))
#print(AAs)
#print(MSs)

#print('Calculating Molecular Weight (1/7)')
#Calculating the molecular weight of the protein
Total_Mass = 0
t = 0
for i in range(0, x):
    while t != 20:
        if List[i] == AAs[t]:
            Total_Mass = Total_Mass + MSs_int[t]
            break
        else:
            t = t+1
    t = 0
Total_Mass_Two = Total_Mass + o + 2 * h
#print(Total_Mass_Two)
#print("[M+H]+ = ", round(Total_Mass_Two + p + N_Term_Mod + C_Term_Mod, 6))

#print('Generating Termainal Fragments (2/7)')
#Generate a fragments
Fragment_Mass = 0
t = 0
arra = array('d')
arra_base = array('d')
arraf = []
aflength = 1
arrlenlistaf = []
stra = ''
for i in range(0, x):
    while t != 20:
        if List[i] == AAs[t]:
            Fragment_Mass = Fragment_Mass + MSs_int[t]
            break
        else:
            t = t+1
    while i != -1:
        stra = stra + List[i]
        i = i - 1
    reversedstringa = ''.join(reversed(stra))
    arraf.append(reversedstringa)
    stra = ''
    Base_Fragment_Mass = Fragment_Mass - car - o
    Total_Fragment_Mass = Base_Fragment_Mass + h + p # Why need subtract H? Need to satisfy the carbonyl group. Maybe hooks to nitrogen?
    arra_base.append(Base_Fragment_Mass)
    arra.append(Total_Fragment_Mass)
    arrlenlistaf.append(aflength)
    aflength = aflength+1
    t = 0
#print("A_Fragments = ", arra)
#print("A_Fragments = ", arra_base)
#print("A_Numbers = ", arrlenlistaf)
#print("A_Fragments = ", arraf)
a = len(arra)

#Generate b fragments
Fragment_Mass = 0
t = 0
arrb = array('d')
arrb_base = array('d')
arrbf = []
bflength = 1
arrlenlistbf = []
strb = ''
for i in range(0, x):
    while t != 20:
        if List[i] == AAs[t]:
            Fragment_Mass = Fragment_Mass + MSs_int[t]
            break
        else:
            t = t+1
    while i != -1:
        strb = strb + List[i]
        i = i - 1
    reversedstringb = ''.join(reversed(strb))
    arrbf.append(reversedstringb)
    strb = ''
    Base_Fragment_Mass = Fragment_Mass
    Total_Fragment_Mass = Base_Fragment_Mass + p # Why need subtract H? Need to satisfy the carbonyl group. Maybe hooks to nitrogen?
    arrb_base.append(Base_Fragment_Mass)
    arrb.append(Total_Fragment_Mass)
    arrlenlistbf.append(bflength)
    bflength = bflength+1
    t = 0
#print("B_Fragments = ", arrb)
#print("B_Fragments = ", arrb_base)
#print("B_Fragments = ", arrbf)
b = len(arrb)

#Generate c fragments
Fragment_Mass = 0
t = 0
arrc = array('d')
arrc_base = array('d')
arrcf = []
cflength = 1
arrlenlistcf = []
strc = ''
for i in range(0, x-1):
    while t != 20:
        if List[i] == AAs[t]:
            Fragment_Mass = Fragment_Mass + MSs_int[t]
            break
        else:
            t = t+1
    while i != -1:
        strc = strc + List[i]
        i = i - 1
    reversedstringc = ''.join(reversed(strc))
    arrcf.append(reversedstringc)
    strc = ''
    Base_Fragment_Mass = Fragment_Mass + n + h + h + h
    Total_Fragment_Mass = Base_Fragment_Mass + p #Why add an extra H? Maybe when the bond breaks, another hydrogen is needed to satisfy the N that was separated. Same as y fragment
    arrc_base.append(Base_Fragment_Mass)
    arrc.append(Total_Fragment_Mass)
    arrlenlistcf.append(cflength)
    cflength = cflength+1
    t = 0
#print("C_Fragments = ", arrc)
#print("C_Fragments = ", arrc_base)
#print("C_Fragments = ", arrcf)
c = len(arrc)

#Generate x fragments
Fragment_Mass = 0
t = 0
arrx = array('d')
arrx_base = array('d')
arrxf = []
xflength = length_sequence
arrlenlistxf = []
strx = ''
for i in range(x-1, 0, -1):
    while t != 20:
        if List[i] == AAs[t]:
            Fragment_Mass = Fragment_Mass + MSs_int[t]
            break
        else:
            t = t+1
    while i != x:
        strx = strx + List[i]
        i = i + 1
    arrxf.append(strx)
    strx = ''
    Base_Fragment_Mass = Fragment_Mass + o + car + o
    Total_Fragment_Mass = Base_Fragment_Mass + p #Need to check this.
    arrx_base.append(Base_Fragment_Mass)
    arrx.append(Total_Fragment_Mass)
    arrlenlistxf.append(xflength)
    xflength = xflength - 1
    t = 0
#print("X_Fragments = ", arrx)
#print("X_Fragments = ", arrx_base)
#print("X_Fragments = ", arrxf)
x = len(arrx)

#Generate y fragments
Fragment_Mass = 0
t = 0
arry = array('d')
arry_base = array('d')
arryf = []
yflength = length_sequence
arrlenlistyf = []
stry = ''
for i in range(x, 0, -1):
    while t != 21:
        if List[i] == AAs[t]:
            Fragment_Mass = Fragment_Mass + MSs_int[t]
            break
        else:
            t = t+1
    while i != x+1:
        stry = stry + List[i]
        i = i + 1
    arryf.append(stry)
    stry = ''
    Base_Fragment_Mass = Fragment_Mass + o + h
    Total_Fragment_Mass = Base_Fragment_Mass + h + p #Why add an extra H? Maybe when the bond breaks, another hydrogen is needed to satisfy the N that was separated. Same as c fragment
    arry_base.append(Base_Fragment_Mass)
    arry.append(Total_Fragment_Mass)
    arrlenlistyf.append(yflength)
    yflength = yflength - 1
    t = 0
#print("Y_Fragments = ", arry)
#print("Y_Fragments = ", arry_base)
#print("Y_Fragments = ", arryf)
y = len(arry)

#Generate z fragments
Fragment_Mass = 0
t = 0
arrz = array('d')
arrz_base = array('d')
arrzf = []
zflength = length_sequence
arrlenlistzf = []
strz = ''
for i in range(x, -1, -1):
    while t != 20:
        if List[i] == AAs[t]:
            Fragment_Mass = Fragment_Mass + MSs_int[t]
            break
        else:
            t = t+1
    while i != x+1:
        strz = strz + List[i]
        i = i + 1
    arrzf.append(strz)
    strz = ''
    Base_Fragment_Mass = Fragment_Mass + o + h - n - h
    Total_Fragment_Mass = Base_Fragment_Mass + p #Correct
    arrz_base.append(Base_Fragment_Mass)
    arrz.append(Total_Fragment_Mass)
    arrlenlistzf.append(zflength)
    zflength = zflength - 1
    t = 0
#print("Z_Fragments = ", arrz)
#print("Z_Fragments = ", arrz_base)
#print("Z_Fragments = ", arrzf)
z = len(arrz)

#print('Generating Internal Fragments (3/7)')
#Make internal fragments.
List = list(string)
w = Number_of_AA_Int_frag
x = 0
v = 0
fl = 1
bh = len(List)
bl = len(List)
strintf = ''
arrintf = []
arrlenlistfl = []
arrlenlistbl = []
while v != b-1:
    fl = fl + 1
    del List[0]
    Listhold = List.copy()
    for i in range(x - b + w, x):
        bl = bl - 1
        List.reverse()
        del List[0]
        List.reverse()
        w = w + 1
        strintf = "".join(List)
        arrintf.append(strintf)
        arrlenlistfl.append(fl)
        arrlenlistbl.append(bl)
    bl = bh
    w = Number_of_AA_Int_frag
    x = x + 1
    w = w + x
    v = v + 1
    List = Listhold.copy()
b = len(arrb)
List = list(string)
#print(arrlenlistfl)
#print(arrlenlistbl)
#print("intfraglength = ", intfraglength)

#a Fragments with x Fragments
axintfrag=0
nterm = 0
cterm = 0
arrax=array('d')
for i in range(0,a-1):
    for i in range(0,x-1):
        axintfrag = Total_Mass_Two - arra_base[nterm] - arrx_base[cterm] - 2 * h
        if nterm + cterm != b-2 and b - nterm - cterm > Int_frag_endpoint:
            axintfrag = axintfrag + p
            arrax.append(float(axintfrag))
        else:
            break
        cterm = cterm + 1
    nterm = nterm + 1
    cterm = 0
intfraglength = len(arrax)
#print("AX_Fragments = ", arrax)
#print("AX_Fragments = ", arrintf)

#a Fragments with y Fragments
ayintfrag=0
nterm = 0
cterm = 0
arrays=array('d')
for i in range(0,a-1):
    for i in range(0,y-1):
        ayintfrag = Total_Mass_Two - arra_base[nterm]-arry_base[cterm] - h
        if nterm + cterm != b-2 and b - nterm - cterm > Int_frag_endpoint:
            ayintfrag = ayintfrag + p
            arrays.append(float(ayintfrag))
        else:
            break
        cterm = cterm + 1
    nterm = nterm + 1
    cterm = 0
#print("AY_Fragments = ", arrays)
#print("AY_Fragments = ", arrintf)

#a Fragments with z Fragments
azintfrag=0
nterm = 0
cterm = 0
arraz=array('d')
for i in range(0,c-1):
    for i in range(0,z-1):
        azintfrag = Total_Mass_Two - arra_base[nterm]-arrz_base[cterm] - h
        if nterm + cterm != b-2 and b - nterm - cterm > Int_frag_endpoint:
            azintfrag = azintfrag + p
            arraz.append(azintfrag)
        else:
            break
        cterm = cterm + 1
    nterm = nterm + 1
    cterm = 0
#print("AZ_Fragments = ", arraz)
#print("AZ_Fragments = ", arrintf)

#b Fragments with x Fragments
bxintfrag=0
nterm = 0
cterm = 0
arrbx=array('d')
for i in range(0,b-1):
    for i in range(0,x-1):
        bxintfrag = Total_Mass_Two - arrb_base[nterm]- arrx_base[cterm] - 2*h
        if nterm + cterm != b-2 and b - nterm - cterm > Int_frag_endpoint:
            bxintfrag = bxintfrag + p
            arrbx.append(float(bxintfrag))
        else:
            break
        cterm = cterm + 1
    nterm = nterm + 1
    cterm = 0
#print("BX_Fragments = ", arrbx)
#print("BX_Fragments = ", arrintf)

#b Fragments with y Fragments
byintfrag=0
nterm = 0
cterm = 0
arrby=array('d')
for i in range(0,b-1):
    for i in range(0,y-1):
        byintfrag = Total_Mass_Two - arrb_base[nterm] - arry_base[cterm] - h
        if nterm + cterm != b-2 and b - nterm - cterm > Int_frag_endpoint:
            byintfrag = byintfrag + p
            #print('{0:.6f}'.format(byintfrag))
            arrby.append(float(byintfrag))
        else:
            break
        cterm = cterm + 1
    nterm = nterm + 1
    cterm = 0
#print("BY_Fragments = ", arrby)
#print("BY_Fragments = ", arrintf)

#b Fragments with z Fragments
bzintfrag=0
nterm = 0
cterm = 0
arrbz=array('d')
for i in range(0,b-1):
    for i in range(0,z-1):
        bzintfrag = Total_Mass_Two - arrb_base[nterm]-arrz_base[cterm] - h
        if nterm + cterm != b-2 and b - nterm - cterm > Int_frag_endpoint:
            bzintfrag = bzintfrag + p
            arrbz.append(float(bzintfrag))
        else:
            break
        cterm = cterm + 1
    nterm = nterm + 1
    cterm = 0
#print("BZ_Fragments = ", arrbz)
#print("BZ_Fragments = ", arrintf)

#c Fragments with x Fragments
cxintfrag=0
nterm = 0
cterm = 0
arrcx=array('d')
for i in range(0,c-1):
    for i in range(0,x-1):
        cxintfrag = Total_Mass_Two - arrc_base[nterm]-arrx_base[cterm]
        if nterm + cterm != b-2 and b - nterm - cterm > Int_frag_endpoint:
            cxintfrag = cxintfrag + p
            arrcx.append(float(cxintfrag))
        else:
            break
        cterm = cterm + 1
    nterm = nterm + 1
    cterm = 0
#print("CX_Fragments = ", arrcx)
#print("CX_Fragments = ", arrintf)

#c Fragments with y Fragments
cyintfrag=0
nterm = 0
cterm = 0
arrcy=array('d')
for i in range(0,c-1):
    for i in range(0,y-1):
        cyintfrag = Total_Mass_Two - arrc_base[nterm] - arry_base[cterm] + h
        if nterm + cterm != b-2 and b - nterm - cterm > Int_frag_endpoint:
            cyintfrag = cyintfrag + p
            arrcy.append(float(cyintfrag))
        else:
            break
        cterm = cterm + 1
    nterm = nterm + 1
    cterm = 0
#print("CY_Fragments = ", arrcy)
#print("CY_Fragments = ", arrintf)

#c Fragments with z Fragments
czintfrag=0
nterm = 0
cterm = 0
arrcz=array('d')
for i in range(0,c-1):
    for i in range(0,z-1):
        czintfrag = Total_Mass_Two - arrc_base[nterm]-arrz_base[cterm] + h
        if nterm + cterm != b-2 and b - nterm - cterm > Int_frag_endpoint:
            czintfrag = czintfrag + p
            arrcz.append(float(czintfrag))
        else:
            break
        cterm = cterm + 1
    nterm = nterm + 1
    cterm = 0
#print("CZ_Fragments = ", arrcz)
#print("CZ_Fragments = ", arrintf)


# Import Instrument Measured Fragments
open("Fragments.csv","r")
instfrag = []
with open("Fragments.csv") as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        instfrag.append(row[0])
instfrags= list(map(float, instfrag))
#print("Measured Fragments =", instfrags)

# Import Instrument Measured Intensities
open("Fragments.csv","r")
intensity = []
with open("Fragments.csv") as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        intensity.append(row[1])
intensities = list(map(float, intensity))
#print("Measured Fragments =", instfrags)

# Import Known_Modificaitons
open("Known_Modifications.csv","r")
modlist = []
modnumber = []
with open("Known_Modifications.csv") as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        modlist.append(row[1])
        modnumber.append(row[2])
known_modifications = list(map(float, modlist))
modificationnumber = list(map(int, modnumber))
#print(known_modifications)
#print(modificationnumber)
k_ml = len(known_modifications)

# Import Modificaitons
open("Modifications.csv","r")
modlist = []
with open("Modifications.csv") as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        modlist.append(row[1])
modifications = list(map(float, modlist))
#print("Modificaitons = ", modifications)
ml = len(modifications)
#print(ml)

mod = 0
loop = 0

#Open a new file
with open('Output.csv', 'w') as csvFile:
    csvFile.close()

#Create a title row for matched fragemnts file
csvData = [['Frag_number', 'Frag Type', 'Fixed Mod', 'Variable Mod', 'Term Mod', 'Observed Mass', 'Theoredical Mass', 'Start AA', 'End AA', 'Error', 'Sequence', 'Intensity', 'Start AA For Fig', 'Formula']]
with open('Output.csv', 'a') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(csvData)
csvFile.close()

#Create array of terminal fragment counts
list_of_counts_arr_terminal = array('f')
for i in range(0, length_sequence):
    list_of_counts_arr_terminal.append(0)
#print(list_of_counts_arr_terminal)

#Create array of internal fragment counts
list_of_counts_arr_internal = array('f')
for i in range(0, length_sequence):
    list_of_counts_arr_internal.append(0)
#print(list_of_counts_arr_internal)

frag_number = 0
#print('Match Fragments (4/7)')
#Start Matching and modification matching
for i in range(0, ml):
    v_mod = modifications[loop]
    mod = v_mod
    loop = loop + 1
    #Match peaks with A fragments
    if Search_A_Fragments == 1:
        #print('A Fragemnts')
        ifl = len(instfrags)
        g = 0
        m = 0
        for i in tqdm(range(0, ifl), total=ifl, desc="A Fragments"):
            for i in range(0, a):
                for i in range(0, k_ml):
                    if arrlenlistaf[m] >= modificationnumber[i]:
                        mod = mod + known_modifications[i]
                    else:
                        mod = mod
                if abs((instfrags[g] - arra[m] - mod - N_Term_Mod)/(arra[m] + mod + N_Term_Mod)*1000000) < PPM_Error_tolerance:
                    #print("A Fragment")
                    #print(instfrags[g])
                    #print(arra[m])
                    Error = (instfrags[g] - arra[m] - mod - N_Term_Mod)/(arra[m] + mod + N_Term_Mod)*1000000
                    #print(Error)
                    #print(arraf[m])
                    frag_number = frag_number + 1
                    csvData = [[frag_number, 'A Fragment', str(mod - v_mod), str(v_mod), str(N_Term_Mod), str(round(instfrags[g],5)), str(round(arra[m],5)), str(1), str(arrlenlistaf[m]), str(round(Error,5)), str(arraf[m]), str(intensities[g]), str(0)]]
                    holdv = m
                    for i in range(holdv, -1, -1):
                        list_of_counts_arr_terminal[holdv] = list_of_counts_arr_terminal[holdv] + 1
                        holdv = holdv - 1
                    with open('Output.csv', 'a') as csvFile:
                        writer = csv.writer(csvFile)
                        writer.writerows(csvData)
                    csvFile.close()
                else:
                    v=9
                m = m + 1
                mod = v_mod
            g = g + 1
            #print(g / ifl * 100)
            m = 0

    #Match peaks with B fragments
    if Search_B_Fragments == 1:
        #print('B Fragemnts')
        ifl = len(instfrags)
        g = 0
        m = 0
        for i in tqdm(range(0, ifl), total = ifl, desc = "B Fragments"):
            for i in range(0, b):
                for i in range(0, k_ml):
                    if arrlenlistbf[m] >= modificationnumber[i]:
                        mod = mod + known_modifications[i]
                    else:
                        mod = mod
                if abs((instfrags[g] - arrb[m] - mod - N_Term_Mod)/(arrb[m] + mod + N_Term_Mod)*1000000) < PPM_Error_tolerance:
                    #print("B Fragment")
                    #print(instfrags[g])
                    #print(arrb[m])
                    Error = (instfrags[g] - arrb[m] - mod - N_Term_Mod)/(arrb[m] + mod + N_Term_Mod)*1000000
                    #print(Error)
                    #print(arrbf[m])
                    frag_number = frag_number + 1
                    csvData = [[frag_number, 'B Fragment', str(mod - v_mod), str(v_mod), str(N_Term_Mod), str(round(instfrags[g],5)), str(round(arrb[m],5)), str(1), str(arrlenlistbf[m]), str(round(Error,5)), str(arrbf[m]), str(intensities[g]), str(0)]]
                    holdv = m
                    for i in range(holdv, -1, -1):
                        list_of_counts_arr_terminal[holdv] = list_of_counts_arr_terminal[holdv] + 1
                        holdv = holdv - 1
                    with open('Output.csv', 'a') as csvFile:
                        writer = csv.writer(csvFile)
                        writer.writerows(csvData)
                    csvFile.close()
                else:
                    v=9
                m = m + 1
                mod = v_mod
            g = g + 1
            #print(g / ifl * 100)
            m = 0

    #Match peaks with C fragments
    if Search_C_Fragments == 1:
        #print('C Fragemnts')
        ifl = len(instfrags)
        g = 0
        m = 0
        for i in tqdm(range(0, ifl), total=ifl, desc="C Fragments"):
            for i in range(0, c):
                for i in range(0, k_ml):
                    if arrlenlistcf[m] >= modificationnumber[i]:
                        mod = mod + known_modifications[i]
                    else:
                        mod = mod
                if abs((instfrags[g] - arrc[m] - mod - N_Term_Mod)/(arrc[m] + mod + N_Term_Mod)*1000000) < PPM_Error_tolerance:
                    #print("C Fragment")
                    #print(instfrags[g])
                    #print(arrc[m])
                    Error = (instfrags[g] - arrc[m] - mod - N_Term_Mod)/(arrc[m] + mod + N_Term_Mod)*1000000
                    #print(Error)
                    #print(arrcf[m])
                    frag_number = frag_number + 1
                    csvData = [[frag_number, 'C Fragment', str(mod - v_mod), str(v_mod), str(N_Term_Mod), str(round(instfrags[g],5)), str(round(arrc[m],5)), str(1), str(arrlenlistcf[m]), str(round(Error,5)), str(arrcf[m]), str(intensities[g]), str(0)]]
                    holdv = m
                    for i in range(holdv, -1, -1):
                        list_of_counts_arr_terminal[holdv] = list_of_counts_arr_terminal[holdv] + 1
                        holdv = holdv - 1
                    with open('Output.csv', 'a') as csvFile:
                        writer = csv.writer(csvFile)
                        writer.writerows(csvData)
                    csvFile.close()
                else:
                    v=9
                m = m + 1
                mod = v_mod
            g = g + 1
            #print(g / ifl * 100)
            m = 0


    #Match peaks with X fragments
    if Search_X_Fragments == 1:
        #print('X Fragemnts')
        ifl = len(instfrags)
        g = 0
        m = 0
        for i in tqdm(range(0, ifl), total=ifl, desc="X Fragments"):
            for i in range(0, x):
                for i in range(0, k_ml):
                    if arrlenlistxf[m] <= modificationnumber[i]:
                        mod = mod + known_modifications[i]
                    else:
                        mod = mod
                if abs((instfrags[g] - arrx[m] - mod - C_Term_Mod)/(arrx[m] + mod + C_Term_Mod)*1000000) < PPM_Error_tolerance:
                    #print("X Fragment")
                    #print(instfrags[g])
                    #print(arrx[m])
                    Error = (instfrags[g] - arrx[m] - mod - C_Term_Mod)/(arrx[m] + mod + C_Term_Mod)*1000000
                    #print(Error)
                    #print(arrxf[m])
                    frag_number = frag_number + 1
                    csvData = [[frag_number, 'X Fragment', str(mod - v_mod), str(v_mod), str(C_Term_Mod), str(round(instfrags[g],5)), str(round(arrx[m],5)), str(arrlenlistxf[m]), str(length_sequence), str(round(Error,5)), str(arrxf[m]), str(intensities[g]), arrlenlistxf[m]-1]]
                    holdv = length_sequence - m - 1
                    for i in range(holdv, length_sequence, 1):
                        list_of_counts_arr_terminal[holdv] = list_of_counts_arr_terminal[holdv] + 1
                        holdv = holdv + 1
                    with open('Output.csv', 'a') as csvFile:
                        writer = csv.writer(csvFile)
                        writer.writerows(csvData)
                    csvFile.close()
                else:
                    v=9
                m = m + 1
                mod = v_mod
            g = g + 1
            #print(g / ifl * 100)
            m = 0

    #Match peaks with Y fragments
    if Search_Y_Fragments == 1:
        #print('Y Fragemnts')
        ifl = len(instfrags)
        g = 0
        m = 0
        for i in tqdm(range(0, ifl), total=ifl, desc="Y Fragments"):
            for i in range(0, y):
                for i in range(0, k_ml):
                    if arrlenlistyf[m] <= modificationnumber[i]:
                        mod = mod + known_modifications[i]
                    else:
                        mod = mod
                if abs((instfrags[g] - arry[m] - mod - C_Term_Mod)/(arry[m] + mod + C_Term_Mod) * 1000000) < PPM_Error_tolerance:
                    #print("Y Fragment")
                    #print(instfrags[g])
                    #print(arry[m])
                    Error = (instfrags[g] - arry[m] - mod - C_Term_Mod)/(arry[m] + mod + C_Term_Mod) * 1000000
                    #print(Error)
                    #print(arryf[m])
                    frag_number = frag_number + 1
                    csvData = [[frag_number, 'Y Fragment', str(mod - v_mod), str(v_mod), str(C_Term_Mod), str(round(instfrags[g],5)), str(round(arry[m],5)), str(arrlenlistyf[m]), str(length_sequence), str(round(Error,5)), str(arryf[m]), str(intensities[g]), arrlenlistyf[m]-1]]
                    holdv = length_sequence - m - 1
                    for i in range(holdv, length_sequence, 1):
                        list_of_counts_arr_terminal[holdv] = list_of_counts_arr_terminal[holdv] + 1
                        holdv = holdv + 1
                    with open('Output.csv', 'a') as csvFile:
                        writer = csv.writer(csvFile)
                        writer.writerows(csvData)
                    csvFile.close()
                else:
                    v=9
                m = m + 1
                mod = v_mod
            g = g + 1
            #print(g / ifl * 100)
            m = 0

    #Match peaks with Z fragments
    if Search_Z_Fragments == 1:
        #print('Z Fragemnts')
        ifl = len(instfrags)
        g = 0
        m = 0
        for i in tqdm(range(0, ifl), total=ifl, desc="Z Fragments"):
            for i in range(0, z):
                for i in range(0, k_ml):
                    if arrlenlistzf[m] <= modificationnumber[i]:
                        mod = mod + known_modifications[i]
                    else:
                        mod = mod
                if abs((instfrags[g] - arrz[m] - mod - C_Term_Mod)/(arrz[m] + mod + C_Term_Mod) * 1000000) < PPM_Error_tolerance:
                    #print("Z Fragment")
                    #print(instfrags[g])
                    #print(arrz[m])
                    Error = (instfrags[g] - arrz[m] - mod - C_Term_Mod)/(arrz[m] + mod + C_Term_Mod) * 1000000
                    #print(Error)
                    #print(arrzf[m])
                    frag_number = frag_number + 1
                    csvData = [[frag_number, 'Z Fragment', str(mod - v_mod), str(v_mod), str(C_Term_Mod), str(round(instfrags[g],5)), str(round(arrz[m],5)), str(arrlenlistzf[m]), str(length_sequence), str(round(Error,5)), str(arrzf[m]), str(intensities[g]), arrlenlistzf[m]-1]]
                    holdv = length_sequence - m - 1
                    for i in range(holdv, length_sequence, 1):
                        list_of_counts_arr_terminal[holdv] = list_of_counts_arr_terminal[holdv] + 1
                        holdv = holdv + 1
                    with open('Output.csv', 'a') as csvFile:
                        writer = csv.writer(csvFile)
                        writer.writerows(csvData)
                    csvFile.close()
                else:
                    v=9
                m = m + 1
                mod = v_mod
            g = g + 1
            #print(g / ifl * 100)
            m = 0

    #Match peaks with AX fragments
    if Search_AX_Fragments == 1:
        #print('AX Fragemnts')
        ifl = len(instfrags)
        g = 0
        m = 0
        for i in tqdm(range(0, ifl), total=ifl, desc="AX Fragments"):
            for i in range(0, intfraglength):
                for i in range(0, k_ml):
                    if arrlenlistfl[m] <= modificationnumber[i] and arrlenlistbl[m] >= modificationnumber[i]:
                        mod = mod + known_modifications[i]
                    else:
                        mod = mod
                if abs((instfrags[g] - arrax[m] - mod)/(arrax[m] + mod)*1000000) < PPM_Error_tolerance:
                    #print("AX Fragment")
                    #print(instfrags[g])
                    #print(arrax[m])
                    Error = (instfrags[g] - arrax[m] - mod)/(arrax[m] + mod)*1000000
                    #print(Error)
                    #print(arrintf[m])
                    frag_number = frag_number + 1
                    csvData = [[frag_number, 'AX Int Fragment', str(mod - v_mod), str(v_mod), str(0), str(round(instfrags[g],5)), str(round(arrax[m],5)), str(arrlenlistfl[m]), str(arrlenlistbl[m]), str(round(Error,5)), str(arrintf[m]), str(intensities[g]), arrlenlistfl[m]-1]]
                    holdv = arrlenlistfl[m] - 1
                    holdvn = arrlenlistbl[m]
                    for i in range(holdv, holdvn):
                        list_of_counts_arr_internal[holdv] = list_of_counts_arr_internal[holdv] + 1
                        holdv = holdv + 1
                    with open('Output.csv', 'a') as csvFile:
                        writer = csv.writer(csvFile)
                        writer.writerows(csvData)
                    csvFile.close()
                else:
                    v=9
                m = m + 1
                mod = v_mod
            g = g + 1
            #print(g / ifl * 100)
            m = 0

    #Match peaks with AY fragments
    if Search_AY_Fragments == 1:
        #print('AY Fragemnts')
        ifl = len(instfrags)
        g = 0
        m = 0
        for i in tqdm(range(0, ifl), total=ifl, desc="AY Fragments"):
            for i in range(0, intfraglength):
                for i in range(0, k_ml):
                    if arrlenlistfl[m] <= modificationnumber[i] and arrlenlistbl[m] >= modificationnumber[i]:
                        mod = mod + known_modifications[i]
                    else:
                        mod = mod
                if abs((instfrags[g] - arrays[m] - mod)/(arrays[m] + mod)*1000000) < PPM_Error_tolerance:
                    #print("AY Fragment")
                    #print(instfrags[g])
                    #print(arrays[m])
                    Error = (instfrags[g] - arrays[m] - mod)/(arrays[m] + mod)*1000000
                    #print(Error)
                    #print(arrintf[m])
                    frag_number = frag_number + 1
                    csvData = [[frag_number, 'AY Int Fragment', str(mod - v_mod), str(v_mod), str(0), str(round(instfrags[g],5)), str(round(arrays[m],5)), str(arrlenlistfl[m]), str(arrlenlistbl[m]), str(round(Error,5)), str(arrintf[m]), str(intensities[g]), arrlenlistfl[m]-1]]
                    holdv = arrlenlistfl[m] - 1
                    holdvn = arrlenlistbl[m]
                    for i in range(holdv, holdvn):
                        list_of_counts_arr_internal[holdv] = list_of_counts_arr_internal[holdv] + 1
                        holdv = holdv + 1
                    with open('Output.csv', 'a') as csvFile:
                        writer = csv.writer(csvFile)
                        writer.writerows(csvData)
                    csvFile.close()
                else:
                    v=9
                m = m + 1
                mod = v_mod
            g = g + 1
            #print(g / ifl * 100)
            m = 0

    #Match peaks with AZ fragments
    if Search_AZ_Fragments == 1:
        #print('AZ Fragemnts')
        ifl = len(instfrags)
        g = 0
        m = 0
        for i in tqdm(range(0, ifl), total=ifl, desc="AZ Fragments"):
            for i in range(0, intfraglength):
                for i in range(0, k_ml):
                    if arrlenlistfl[m] <= modificationnumber[i] and arrlenlistbl[m] >= modificationnumber[i]:
                        mod = mod + known_modifications[i]
                    else:
                        mod = mod
                if abs((instfrags[g] - arraz[m] - mod)/(arraz[m] + mod)*1000000) < PPM_Error_tolerance:
                    #print("AZ Fragment")
                    #print(instfrags[g])
                    #print(arraz[m])
                    Error = (instfrags[g] - arraz[m] - mod)/(arraz[m] + mod)*1000000
                    #print(Error)
                    #print(arrintf[m])
                    frag_number = frag_number + 1
                    csvData = [[frag_number, 'AZ Int Fragment', str(mod - v_mod), str(v_mod), str(0), str(round(instfrags[g],5)), str(round(arraz[m],5)), str(arrlenlistfl[m]), str(arrlenlistbl[m]), str(round(Error,5)), str(arrintf[m]), str(intensities[g]), arrlenlistfl[m]-1]]
                    holdv = arrlenlistfl[m] - 1
                    holdvn = arrlenlistbl[m]
                    for i in range(holdv, holdvn):
                        list_of_counts_arr_internal[holdv] = list_of_counts_arr_internal[holdv] + 1
                        holdv = holdv + 1
                    with open('Output.csv', 'a') as csvFile:
                        writer = csv.writer(csvFile)
                        writer.writerows(csvData)
                    csvFile.close()
                else:
                    v=9
                m = m + 1
                mod = v_mod
            g = g + 1
            #print(g / ifl * 100)
            m = 0

    # Match peaks with BX fragments
    if Search_BX_Fragments == 1:
        #print('BX Fragemnts')
        ifl = len(instfrags)
        g = 0
        m = 0
        for i in tqdm(range(0, ifl), total=ifl, desc="BX Fragments"):
            for i in range(0, intfraglength):
                for i in range(0, k_ml):
                    if arrlenlistfl[m] <= modificationnumber[i] and arrlenlistbl[m] >= modificationnumber[i]:
                        mod = mod + known_modifications[i]
                    else:
                        mod = mod
                if abs((instfrags[g] - arrbx[m] - mod) / (arrbx[m] + mod) * 1000000) < PPM_Error_tolerance:
                    #print("BX Fragment")
                    #print(instfrags[g])
                    #print(arrbx[m])
                    Error = (instfrags[g] - arrbx[m] - mod) / (arrbx[m] + mod) * 1000000
                    #print(Error)
                    #print(arrintf[m])
                    frag_number = frag_number + 1
                    csvData = [[frag_number, 'BX Int Fragment', str(mod - v_mod), str(v_mod), str(0), str(round(instfrags[g],5)), str(round(arrbx[m],5)), str(arrlenlistfl[m]), str(arrlenlistbl[m]), str(round(Error,5)), str(arrintf[m]), str(intensities[g]), arrlenlistfl[m]-1]]
                    holdv = arrlenlistfl[m] - 1
                    holdvn = arrlenlistbl[m]
                    for i in range(holdv, holdvn):
                        list_of_counts_arr_internal[holdv] = list_of_counts_arr_internal[holdv] + 1
                        holdv = holdv + 1
                    with open('Output.csv', 'a') as csvFile:
                        writer = csv.writer(csvFile)
                        writer.writerows(csvData)
                    csvFile.close()
                else:
                    v = 9
                m = m + 1
                mod = v_mod
            g = g + 1
            #print(g / ifl * 100)
            m = 0

    # Match peaks with BY fragments
    if Search_BY_Fragments == 1:
        #print('BY Fragemnts')
        ifl = len(instfrags)
        g = 0
        m = 0
        for i in tqdm(range(0, ifl), total=ifl, desc="BY Fragments"):
            for i in range(0, intfraglength):
                for i in range(0, k_ml):
                    if arrlenlistfl[m] <= modificationnumber[i] and arrlenlistbl[m] >= modificationnumber[i]:
                        mod = mod + known_modifications[i]
                    else:
                        mod = mod
                if abs((instfrags[g] - arrby[m] - mod) / (arrby[m] + mod) * 1000000) < PPM_Error_tolerance:
                    #print("BY Fragment")
                    #print(instfrags[g])
                    #print(arrby[m])
                    Error = (instfrags[g] - arrby[m] - mod) / (arrby[m] + mod) * 1000000
                    #print(Error)
                    #print(arrintf[m])
                    frag_number = frag_number + 1
                    csvData = [[frag_number, 'BY Int Fragment', str(mod - v_mod), str(v_mod), str(0), str(round(instfrags[g],5)), str(round(arrby[m],5)), str(arrlenlistfl[m]), str(arrlenlistbl[m]), str(round(Error,5)), str(arrintf[m]), str(intensities[g]), arrlenlistfl[m]-1]]
                    holdv = arrlenlistfl[m] - 1
                    holdvn = arrlenlistbl[m]
                    for i in range(holdv, holdvn):
                        list_of_counts_arr_internal[holdv] = list_of_counts_arr_internal[holdv] + 1
                        holdv = holdv + 1
                    with open('Output.csv', 'a') as csvFile:
                        writer = csv.writer(csvFile)
                        writer.writerows(csvData)
                    csvFile.close()
                else:
                    v = 9
                m = m + 1
                mod = v_mod
            g = g + 1
            #print(g / ifl * 100)
            m = 0

    # Match peaks with BZ fragments
    if Search_BZ_Fragments == 1:
        #print('BZ Fragemnts')
        ifl = len(instfrags)
        g = 0
        m = 0
        for i in tqdm(range(0, ifl), total=ifl, desc="BZ Fragments"):
            for i in range(0, intfraglength):
                for i in range(0, k_ml):
                    if arrlenlistfl[m] <= modificationnumber[i] and arrlenlistbl[m] >= modificationnumber[i]:
                        mod = mod + known_modifications[i]
                    else:
                        mod = mod
                if abs((instfrags[g] - arrbz[m] - mod) / (arrbz[m] + mod) * 1000000) < PPM_Error_tolerance:
                    #print("BZ Fragment")
                    #print(instfrags[g])
                    #print(arrbz[m])
                    Error = (instfrags[g] - arrbz[m] - mod) / (arrbz[m] + mod) * 1000000
                    #print(Error)
                    #print(arrintf[m])
                    frag_number = frag_number + 1
                    csvData = [[frag_number, 'BZ Int Fragment', str(mod - v_mod), str(v_mod), str(0), str(round(instfrags[g],5)), str(round(arrbz[m],5)), str(arrlenlistfl[m]), str(arrlenlistbl[m]), str(round(Error,5)), str(arrintf[m]), str(intensities[g]), arrlenlistfl[m]-1]]
                    holdv = arrlenlistfl[m] - 1
                    holdvn = arrlenlistbl[m]
                    for i in range(holdv, holdvn):
                        list_of_counts_arr_internal[holdv] = list_of_counts_arr_internal[holdv] + 1
                        holdv = holdv + 1
                    with open('Output.csv', 'a') as csvFile:
                        writer = csv.writer(csvFile)
                        writer.writerows(csvData)
                    csvFile.close()
                else:
                    v = 9
                m = m + 1
                mod = v_mod
            g = g + 1
            #print(g / ifl * 100)
            m = 0

    # Match peaks with CX fragments
    if Search_CX_Fragments == 1:
        #print('CX Fragemnts')
        ifl = len(instfrags)
        g = 0
        m = 0
        for i in tqdm(range(0, ifl), total=ifl, desc="CX Fragments"):
            for i in range(0, intfraglength):
                for i in range(0, k_ml):
                    if arrlenlistfl[m] <= modificationnumber[i] and arrlenlistbl[m] >= modificationnumber[i]:
                        mod = mod + known_modifications[i]
                    else:
                        mod = mod
                if abs((instfrags[g] - arrcx[m] - mod) / (arrcx[m] + mod) * 1000000) < PPM_Error_tolerance:
                    #print("CX Fragment")
                    #print(instfrags[g])
                    #print(arrcx[m])
                    Error = (instfrags[g] - arrcx[m] - mod) / (arrcx[m] + mod) * 1000000
                    #print(Error)
                    #print(arrintf[m])
                    frag_number = frag_number + 1
                    csvData = [[frag_number, 'CX Int Fragment', str(mod - v_mod), str(v_mod), str(0), str(round(instfrags[g],5)), str(round(arrcx[m],5)), str(arrlenlistfl[m]), str(arrlenlistbl[m]), str(round(Error,5)), str(arrintf[m]), str(intensities[g]), arrlenlistfl[m]-1]]
                    holdv = arrlenlistfl[m] - 1
                    holdvn = arrlenlistbl[m]
                    for i in range(holdv, holdvn):
                        list_of_counts_arr_internal[holdv] = list_of_counts_arr_internal[holdv] + 1
                        holdv = holdv + 1
                    with open('Output.csv', 'a') as csvFile:
                        writer = csv.writer(csvFile)
                        writer.writerows(csvData)
                    csvFile.close()
                else:
                    v = 9
                m = m + 1
                mod = v_mod
            g = g + 1
            #print(g / ifl * 100)
            m = 0
    
    # Match peaks with CY fragments
    if Search_CY_Fragments == 1:
        #print('CY Fragemnts')
        ifl = len(instfrags)
        g = 0
        m = 0
        for i in tqdm(range(0, ifl), total=ifl, desc="CY Fragments"):
            for i in range(0, intfraglength):
                for i in range(0, k_ml):
                    if arrlenlistfl[m] <= modificationnumber[i] and arrlenlistbl[m] >= modificationnumber[i]:
                        mod = mod + known_modifications[i]
                    else:
                        mod = mod
                if abs((instfrags[g] - arrcy[m] - mod) / (arrcy[m] + mod) * 1000000) < PPM_Error_tolerance:
                    #print("CY Fragment")
                    #print(instfrags[g])
                    #print(arrcy[m])
                    Error = (instfrags[g] - arrcy[m] - mod) / (arrcy[m] + mod) * 1000000
                    #print(Error)
                    #print(arrintf[m])
                    frag_number = frag_number + 1
                    csvData = [[frag_number, 'CY Int Fragment', str(mod - v_mod), str(v_mod), str(0), str(round(instfrags[g],5)), str(round(arrcy[m],5)), str(arrlenlistfl[m]), str(arrlenlistbl[m]), str(round(Error,5)), str(arrintf[m]), str(intensities[g]), arrlenlistfl[m]-1]]
                    holdv = arrlenlistfl[m] - 1
                    holdvn = arrlenlistbl[m]
                    for i in range(holdv, holdvn):
                        list_of_counts_arr_internal[holdv] = list_of_counts_arr_internal[holdv] + 1
                        holdv = holdv + 1
                    with open('Output.csv', 'a') as csvFile:
                        writer = csv.writer(csvFile)
                        writer.writerows(csvData)
                    csvFile.close()
                else:
                    v = 9
                m = m + 1
                mod = v_mod
            g = g + 1
            #print(g / ifl * 100)
            m = 0

    # Match peaks with CZ fragments
    if Search_CZ_Fragments == 1:
        #print('CZ Fragemnts')
        ifl = len(instfrags)
        g = 0
        m = 0
        for i in tqdm(range(0, ifl), total=ifl, desc="CZ Fragments"):
            for i in range(0, intfraglength):
                for i in range(0, k_ml):
                    if arrlenlistfl[m] <= modificationnumber[i] and arrlenlistbl[m] >= modificationnumber[i]:
                        mod = mod + known_modifications[i]
                    else:
                        mod = mod
                if abs((instfrags[g] - arrcz[m] - mod) / (arrcz[m] + mod) * 1000000) < PPM_Error_tolerance:
                    #print("CZ Fragment")
                    #print(instfrags[g])
                    #print(arrcz[m])
                    Error = (instfrags[g] - arrcz[m] - mod) / (arrcz[m] + mod) * 1000000
                    #print(Error)
                    #print(arrintf[m])
                    frag_number = frag_number + 1
                    csvData = [[frag_number, 'CZ Int Fragment', str(mod - v_mod), str(v_mod), str(0), str(round(instfrags[g],5)), str(round(arrcz[m],5)), str(arrlenlistfl[m]), str(arrlenlistbl[m]), str(round(Error,5)), str(arrintf[m]), str(intensities[g]), arrlenlistfl[m]-1]]
                    holdv = arrlenlistfl[m] - 1
                    holdvn = arrlenlistbl[m]
                    for i in range(holdv, holdvn):
                        list_of_counts_arr_internal[holdv] = list_of_counts_arr_internal[holdv] + 1
                        holdv = holdv + 1
                    with open('Output.csv', 'a') as csvFile:
                        writer = csv.writer(csvFile)
                        writer.writerows(csvData)
                    csvFile.close()
                else:
                    v = 9
                m = m + 1
                mod = v_mod
            g = g + 1
            #print(g / ifl * 100)
            m = 0
#print(list_of_counts_arr_terminal)
#print(list_of_counts_arr_internal)

#Delete Blank rows from Output.csv file and transfer to Matched_Fragments.csv or Matched_Fragments_V2.csv file
df = pd.read_csv('Output.csv')
with open('Output.csv',"r") as f:
    reader = csv.reader(f)
    data = list(reader)
    row_count_frags = len(data)
os.remove('Output.csv')
if row_count_frags == 2:
    messagebox.showinfo("CALIF Error", "No Fragment Were Found")
elif row_count_frags == 4:
    df.to_csv('Matched_Fragments_V2.csv', index = False)
else:
    df.to_csv('Matched_Fragments.csv', index=False)

#Molecular formulas for all fragments
open("AminoAcids.csv","r")
Carbons = []
Hydrogens = []
Nitrogens = []
Oxygens = []
Sulfurs = []

with open("AminoAcids.csv") as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        Carbons.append(row[2])
        Hydrogens.append(row[3])
        Nitrogens.append(row[4])
        Oxygens.append(row[5])
        Sulfurs.append(row[6])
Carbons_int= list(map(int, Carbons))
Hydrogens_int= list(map(int, Hydrogens))
Nitrogens_int= list(map(int, Nitrogens))
Oxygens_int= list(map(int, Oxygens))
Sulfurs_int= list(map(int, Sulfurs))
#print(Carbons)
#print(Hydrogens)
#print(Nitrogens)
#print(Oxygens)
#print(Sulfurs)
if row_count_frags == 4:
    with open('Matched_Fragments_V2.csv') as csvDataFile:
        fragment_Sequence = [row for row in csv.reader(csvDataFile)]
        row_count = sum(1 for row in fragment_Sequence)
        #print(row_count)
        x = 1
        for i in tqdm(range(1,row_count), total = row_count, desc = 'Generate Molecular Formualas'):
            Seq_Frag = fragment_Sequence[x][10]
            List_Frag = list(Seq_Frag)
            #print(List_Frag)
            length_fragment = len(List_Frag)
            #print(length_fragment)
            Carbon_Atoms = 0
            Hydrogen_Atoms = 0
            Nitrogen_Atoms = 0
            Oxygen_Atoms = 0
            Sulfur_Atoms = 0
            t = 0
            for i in range(0, length_fragment):
                while t != 20:
                    if List_Frag[i] == AAs[t]:
                        Carbon_Atoms = Carbon_Atoms + Carbons_int[t]
                        Hydrogen_Atoms = Hydrogen_Atoms + Hydrogens_int[t]
                        Nitrogen_Atoms = Nitrogen_Atoms + Nitrogens_int[t]
                        Oxygen_Atoms = Oxygen_Atoms + Oxygens_int[t]
                        Sulfur_Atoms = Sulfur_Atoms + Sulfurs_int[t]
                        break
                    else:
                        t = t + 1
                t = 0
            if fragment_Sequence[x][1] == "A Fragment":
                Carbon_Atoms = Carbon_Atoms - 1
                Oxygen_Atoms = Oxygen_Atoms - 1
                Hydrogen_Atoms = Hydrogen_Atoms + 1
                if N_Term_Mod == 42.01056:
                    Carbon_Atoms = Carbon_Atoms + 2
                    Hydrogen_Atoms = Hydrogen_Atoms + 2
                    Oxygen_Atoms = Oxygen_Atoms + 1
                if N_Term_Mod == 0.98401:
                    Hydrogen_Atoms = Hydrogen_Atoms + 1
                    Nitrogen_Atoms = Nitrogen_Atoms + 1
                    Oxygen_Atoms = Oxygen_Atoms - 1
                if N_Term_Mod == 14.01565:
                    Carbon_Atoms = Carbon_Atoms + 1
                    Hydrogen_Atoms = Hydrogen_Atoms + 2
                if N_Term_Mod == 28.0313:
                    Carbon_Atoms = Carbon_Atoms + 2
                    Hydrogen_Atoms = Hydrogen_Atoms + 4
                if N_Term_Mod == 27.99491:
                    Carbon_Atoms = Carbon_Atoms + 1
                    Oxygen_Atoms = Oxygen_Atoms + 1
            if fragment_Sequence[x][1] == "B Fragment":
                Hydrogen_Atoms = Hydrogen_Atoms + 1
                if N_Term_Mod == 42.01056:
                    Carbon_Atoms = Carbon_Atoms + 2
                    Hydrogen_Atoms = Hydrogen_Atoms + 2
                    Oxygen_Atoms = Oxygen_Atoms + 1
                if N_Term_Mod == 0.98401:
                    Hydrogen_Atoms = Hydrogen_Atoms + 1
                    Nitrogen_Atoms = Nitrogen_Atoms + 1
                    Oxygen_Atoms = Oxygen_Atoms - 1
                if N_Term_Mod == 14.01565:
                    Carbon_Atoms = Carbon_Atoms + 1
                    Hydrogen_Atoms = Hydrogen_Atoms + 2
                if N_Term_Mod == 28.0313:
                    Carbon_Atoms = Carbon_Atoms + 2
                    Hydrogen_Atoms = Hydrogen_Atoms + 4
                if N_Term_Mod == 27.99491:
                    Carbon_Atoms = Carbon_Atoms + 1
                    Oxygen_Atoms = Oxygen_Atoms + 1
            if fragment_Sequence[x][1] == "C Fragment":
                Hydrogen_Atoms = Hydrogen_Atoms + 4
                Nitrogen_Atoms = Nitrogen_Atoms + 1
                if N_Term_Mod == 42.01056:
                    Carbon_Atoms = Carbon_Atoms + 2
                    Hydrogen_Atoms = Hydrogen_Atoms + 2
                    Oxygen_Atoms = Oxygen_Atoms + 1
                if N_Term_Mod == 0.98401:
                    Hydrogen_Atoms = Hydrogen_Atoms + 1
                    Nitrogen_Atoms = Nitrogen_Atoms + 1
                    Oxygen_Atoms = Oxygen_Atoms - 1
                if N_Term_Mod == 14.01565:
                    Carbon_Atoms = Carbon_Atoms + 1
                    Hydrogen_Atoms = Hydrogen_Atoms + 2
                if N_Term_Mod == 28.0313:
                    Carbon_Atoms = Carbon_Atoms + 2
                    Hydrogen_Atoms = Hydrogen_Atoms + 4
                if N_Term_Mod == 27.99491:
                    Carbon_Atoms = Carbon_Atoms + 1
                    Oxygen_Atoms = Oxygen_Atoms + 1
            if fragment_Sequence[x][1] == "X Fragment":
                Carbon_Atoms = Carbon_Atoms + 1
                Oxygen_Atoms = Oxygen_Atoms + 2
                Hydrogen_Atoms = Hydrogen_Atoms + 1
                if C_Term_Mod == -0.98401:
                    Hydrogen_Atoms = Hydrogen_Atoms + 1
                    Nitrogen_Atoms = Nitrogen_Atoms + 1
                    Oxygen_Atoms = Oxygen_Atoms - 1
                if C_Term_Mod == 14.01565:
                    Carbon_Atoms = Carbon_Atoms + 1
                    Hydrogen_Atoms = Hydrogen_Atoms + 2
                    Oxygen_Atoms = Oxygen_Atoms - 1
                if C_Term_Mod == -18.0106:
                    Hydrogen_Atoms = Hydrogen_Atoms - 1
                    Oxygen_Atoms = Oxygen_Atoms - 1
            if fragment_Sequence[x][1] == "Y Fragment":
                Oxygen_Atoms = Oxygen_Atoms + 1
                Hydrogen_Atoms = Hydrogen_Atoms + 3
                if C_Term_Mod == -0.98401:
                    Hydrogen_Atoms = Hydrogen_Atoms + 1
                    Nitrogen_Atoms = Nitrogen_Atoms + 1
                    Oxygen_Atoms = Oxygen_Atoms - 1
                if C_Term_Mod == 14.01565:
                    Carbon_Atoms = Carbon_Atoms + 1
                    Hydrogen_Atoms = Hydrogen_Atoms + 2
                    Oxygen_Atoms = Oxygen_Atoms - 1
                if C_Term_Mod == -18.0106:
                    Hydrogen_Atoms = Hydrogen_Atoms - 1
                    Oxygen_Atoms = Oxygen_Atoms - 1
            if fragment_Sequence[x][1] == "Z Fragment":
                Oxygen_Atoms = Oxygen_Atoms + 1
                Nitrogen_Atoms = Nitrogen_Atoms - 1
                Hydrogen_Atoms = Hydrogen_Atoms + 1
                if C_Term_Mod == -0.98401:
                    Hydrogen_Atoms = Hydrogen_Atoms + 1
                    Nitrogen_Atoms = Nitrogen_Atoms + 1
                    Oxygen_Atoms = Oxygen_Atoms - 1
                if C_Term_Mod == 14.01565:
                    Carbon_Atoms = Carbon_Atoms + 1
                    Hydrogen_Atoms = Hydrogen_Atoms + 2
                    Oxygen_Atoms = Oxygen_Atoms - 1
                if C_Term_Mod == -18.0106:
                    Hydrogen_Atoms = Hydrogen_Atoms - 1
                    Oxygen_Atoms = Oxygen_Atoms - 1
            if fragment_Sequence[x][1] == "AX Int Fragment":
                Hydrogen_Atoms = Hydrogen_Atoms + 1
            if fragment_Sequence[x][1] == "BY Int Fragment":
                Hydrogen_Atoms = Hydrogen_Atoms + 1
            if fragment_Sequence[x][1] == "CZ Int Fragment":
                Hydrogen_Atoms = Hydrogen_Atoms + 1
            if fragment_Sequence[x][1] == "AY Int Fragment":
                Carbon_Atoms = Carbon_Atoms + 1
                Oxygen_Atoms = Oxygen_Atoms + 1
                Hydrogen_Atoms = Hydrogen_Atoms + 1
            if fragment_Sequence[x][1] == "AZ Int Fragment":
                Carbon_Atoms = Carbon_Atoms + 1
                Oxygen_Atoms = Oxygen_Atoms + 1
                Hydrogen_Atoms = Hydrogen_Atoms + 2
                Nitrogen_Atoms = Nitrogen_Atoms + 1
            if fragment_Sequence[x][1] == "BX Int Fragment":
                Carbon_Atoms = Carbon_Atoms - 1
                Oxygen_Atoms = Oxygen_Atoms - 1
                Hydrogen_Atoms = Hydrogen_Atoms + 1
            if fragment_Sequence[x][1] == "BZ Int Fragment":
                Hydrogen_Atoms = Hydrogen_Atoms + 2
                Nitrogen_Atoms = Nitrogen_Atoms + 1
            if fragment_Sequence[x][1] == "CX Int Fragment":
                Carbon_Atoms = Carbon_Atoms - 1
                Oxygen_Atoms = Oxygen_Atoms - 1
                Hydrogen_Atoms = Hydrogen_Atoms - 1
                Nitrogen_Atoms = Nitrogen_Atoms - 1
                Hydrogen_Atoms = Hydrogen_Atoms + 1
            if fragment_Sequence[x][1] == "CY Int Fragment":
                Hydrogen_Atoms = Hydrogen_Atoms - 1
                Hydrogen_Atoms = Hydrogen_Atoms + 1
                Nitrogen_Atoms = Nitrogen_Atoms - 1
            frag_formula = 'C' + str(Carbon_Atoms) + ' ' + 'H' + str(Hydrogen_Atoms) + ' ' + 'N' + str(Nitrogen_Atoms) + ' ' + 'O' + str(Oxygen_Atoms) + ' ' + 'S' + str(Sulfur_Atoms)
            #print(frag_formula)
            fragment_Sequence[x][13] = str(frag_formula)
            writer = csv.writer(open('Matched_Fragments_V2.csv', 'w', newline=''))
            writer.writerows(fragment_Sequence)
            x = x + 1
else:
    with open('Matched_Fragments.csv') as csvDataFile:
        fragment_Sequence = [row for row in csv.reader(csvDataFile)]
        row_count = sum(1 for row in fragment_Sequence)
        #print(row_count)
        x = 1
        for i in tqdm(range(1,row_count), total = row_count - 1, desc = 'Generate Molecular Formulas'):
            Seq_Frag = fragment_Sequence[x][10]
            List_Frag = list(Seq_Frag)
            #print(List_Frag)
            length_fragment = len(List_Frag)
            #print(length_fragment)
            Carbon_Atoms = 0
            Hydrogen_Atoms = 0
            Nitrogen_Atoms = 0
            Oxygen_Atoms = 0
            Sulfur_Atoms = 0
            t = 0
            for i in range(0, length_fragment):
                while t != 20:
                    if List_Frag[i] == AAs[t]:
                        Carbon_Atoms = Carbon_Atoms + Carbons_int[t]
                        Hydrogen_Atoms = Hydrogen_Atoms + Hydrogens_int[t]
                        Nitrogen_Atoms = Nitrogen_Atoms + Nitrogens_int[t]
                        Oxygen_Atoms = Oxygen_Atoms + Oxygens_int[t]
                        Sulfur_Atoms = Sulfur_Atoms + Sulfurs_int[t]
                        break
                    else:
                        t = t + 1
                t = 0
            if fragment_Sequence[x][1] == "A Fragment":
                Carbon_Atoms = Carbon_Atoms - 1
                Oxygen_Atoms = Oxygen_Atoms - 1
                Hydrogen_Atoms = Hydrogen_Atoms + 1
                if N_Term_Mod == 42.01056:
                    Carbon_Atoms = Carbon_Atoms + 2
                    Hydrogen_Atoms = Hydrogen_Atoms + 2
                    Oxygen_Atoms = Oxygen_Atoms + 1
                if N_Term_Mod == 0.98401:
                    Hydrogen_Atoms = Hydrogen_Atoms + 1
                    Nitrogen_Atoms = Nitrogen_Atoms + 1
                    Oxygen_Atoms = Oxygen_Atoms - 1
                if N_Term_Mod == 14.01565:
                    Carbon_Atoms = Carbon_Atoms + 1
                    Hydrogen_Atoms = Hydrogen_Atoms + 2
                if N_Term_Mod == 28.0313:
                    Carbon_Atoms = Carbon_Atoms + 2
                    Hydrogen_Atoms = Hydrogen_Atoms + 4
                if N_Term_Mod == 27.99491:
                    Carbon_Atoms = Carbon_Atoms + 1
                    Oxygen_Atoms = Oxygen_Atoms + 1
            if fragment_Sequence[x][1] == "B Fragment":
                Hydrogen_Atoms = Hydrogen_Atoms + 1
                if N_Term_Mod == 42.01056:
                    Carbon_Atoms = Carbon_Atoms + 2
                    Hydrogen_Atoms = Hydrogen_Atoms + 2
                    Oxygen_Atoms = Oxygen_Atoms + 1
                if N_Term_Mod == 0.98401:
                    Hydrogen_Atoms = Hydrogen_Atoms + 1
                    Nitrogen_Atoms = Nitrogen_Atoms + 1
                    Oxygen_Atoms = Oxygen_Atoms - 1
                if N_Term_Mod == 14.01565:
                    Carbon_Atoms = Carbon_Atoms + 1
                    Hydrogen_Atoms = Hydrogen_Atoms + 2
                if N_Term_Mod == 28.0313:
                    Carbon_Atoms = Carbon_Atoms + 2
                    Hydrogen_Atoms = Hydrogen_Atoms + 4
                if N_Term_Mod == 27.99491:
                    Carbon_Atoms = Carbon_Atoms + 1
                    Oxygen_Atoms = Oxygen_Atoms + 1
            if fragment_Sequence[x][1] == "C Fragment":
                Hydrogen_Atoms = Hydrogen_Atoms + 4
                Nitrogen_Atoms = Nitrogen_Atoms + 1
                if N_Term_Mod == 42.01056:
                    Carbon_Atoms = Carbon_Atoms + 2
                    Hydrogen_Atoms = Hydrogen_Atoms + 2
                    Oxygen_Atoms = Oxygen_Atoms + 1
                if N_Term_Mod == 0.98401:
                    Hydrogen_Atoms = Hydrogen_Atoms + 1
                    Nitrogen_Atoms = Nitrogen_Atoms + 1
                    Oxygen_Atoms = Oxygen_Atoms - 1
                if N_Term_Mod == 14.01565:
                    Carbon_Atoms = Carbon_Atoms + 1
                    Hydrogen_Atoms = Hydrogen_Atoms + 2
                if N_Term_Mod == 28.0313:
                    Carbon_Atoms = Carbon_Atoms + 2
                    Hydrogen_Atoms = Hydrogen_Atoms + 4
                if N_Term_Mod == 27.99491:
                    Carbon_Atoms = Carbon_Atoms + 1
                    Oxygen_Atoms = Oxygen_Atoms + 1
            if fragment_Sequence[x][1] == "X Fragment":
                Carbon_Atoms = Carbon_Atoms + 1
                Oxygen_Atoms = Oxygen_Atoms + 2
                Hydrogen_Atoms = Hydrogen_Atoms + 1
                if C_Term_Mod == -0.98401:
                    Hydrogen_Atoms = Hydrogen_Atoms + 1
                    Nitrogen_Atoms = Nitrogen_Atoms + 1
                    Oxygen_Atoms = Oxygen_Atoms - 1
                if C_Term_Mod == 14.01565:
                    Carbon_Atoms = Carbon_Atoms + 1
                    Hydrogen_Atoms = Hydrogen_Atoms + 2
                    Oxygen_Atoms = Oxygen_Atoms - 1
                if C_Term_Mod == -18.0106:
                    Hydrogen_Atoms = Hydrogen_Atoms - 1
                    Oxygen_Atoms = Oxygen_Atoms - 1
            if fragment_Sequence[x][1] == "Y Fragment":
                Oxygen_Atoms = Oxygen_Atoms + 1
                Hydrogen_Atoms = Hydrogen_Atoms + 3
                if C_Term_Mod == -0.98401:
                    Hydrogen_Atoms = Hydrogen_Atoms + 1
                    Nitrogen_Atoms = Nitrogen_Atoms + 1
                    Oxygen_Atoms = Oxygen_Atoms - 1
                if C_Term_Mod == 14.01565:
                    Carbon_Atoms = Carbon_Atoms + 1
                    Hydrogen_Atoms = Hydrogen_Atoms + 2
                    Oxygen_Atoms = Oxygen_Atoms - 1
                if C_Term_Mod == -18.0106:
                    Hydrogen_Atoms = Hydrogen_Atoms - 1
                    Oxygen_Atoms = Oxygen_Atoms - 1
            if fragment_Sequence[x][1] == "Z Fragment":
                Oxygen_Atoms = Oxygen_Atoms + 1
                Nitrogen_Atoms = Nitrogen_Atoms - 1
                Hydrogen_Atoms = Hydrogen_Atoms + 1
                if C_Term_Mod == -0.98401:
                    Hydrogen_Atoms = Hydrogen_Atoms + 1
                    Nitrogen_Atoms = Nitrogen_Atoms + 1
                    Oxygen_Atoms = Oxygen_Atoms - 1
                if C_Term_Mod == 14.01565:
                    Carbon_Atoms = Carbon_Atoms + 1
                    Hydrogen_Atoms = Hydrogen_Atoms + 2
                    Oxygen_Atoms = Oxygen_Atoms - 1
                if C_Term_Mod == -18.0106:
                    Hydrogen_Atoms = Hydrogen_Atoms - 1
                    Oxygen_Atoms = Oxygen_Atoms - 1
            if fragment_Sequence[x][1] == "AX Int Fragment":
                Hydrogen_Atoms = Hydrogen_Atoms + 1
            if fragment_Sequence[x][1] == "BY Int Fragment":
                Hydrogen_Atoms = Hydrogen_Atoms + 1
            if fragment_Sequence[x][1] == "CZ Int Fragment":
                Hydrogen_Atoms = Hydrogen_Atoms + 1
            if fragment_Sequence[x][1] == "AY Int Fragment":
                Carbon_Atoms = Carbon_Atoms + 1
                Oxygen_Atoms = Oxygen_Atoms + 1
                Hydrogen_Atoms = Hydrogen_Atoms + 1
            if fragment_Sequence[x][1] == "AZ Int Fragment":
                Carbon_Atoms = Carbon_Atoms + 1
                Oxygen_Atoms = Oxygen_Atoms + 1
                Hydrogen_Atoms = Hydrogen_Atoms + 2
                Nitrogen_Atoms = Nitrogen_Atoms + 1
            if fragment_Sequence[x][1] == "BX Int Fragment":
                Carbon_Atoms = Carbon_Atoms - 1
                Oxygen_Atoms = Oxygen_Atoms - 1
                Hydrogen_Atoms = Hydrogen_Atoms + 1
            if fragment_Sequence[x][1] == "BZ Int Fragment":
                Hydrogen_Atoms = Hydrogen_Atoms + 2
                Nitrogen_Atoms = Nitrogen_Atoms + 1
            if fragment_Sequence[x][1] == "CX Int Fragment":
                Carbon_Atoms = Carbon_Atoms - 1
                Oxygen_Atoms = Oxygen_Atoms - 1
                Hydrogen_Atoms = Hydrogen_Atoms - 1
                Nitrogen_Atoms = Nitrogen_Atoms - 1
                Hydrogen_Atoms = Hydrogen_Atoms + 1
            if fragment_Sequence[x][1] == "CY Int Fragment":
                Hydrogen_Atoms = Hydrogen_Atoms - 1
                Hydrogen_Atoms = Hydrogen_Atoms + 1
                Nitrogen_Atoms = Nitrogen_Atoms - 1
            frag_formula = 'C' + str(Carbon_Atoms) + ' ' + 'H' + str(Hydrogen_Atoms) + ' ' + 'N' + str(Nitrogen_Atoms) + ' ' + 'O' + str(Oxygen_Atoms) + ' ' + 'S' + str(Sulfur_Atoms)
            #print(frag_formula)
            fragment_Sequence[x][13] = str(frag_formula)
            writer = csv.writer(open('Matched_Fragments.csv', 'w', newline=''))
            writer.writerows(fragment_Sequence)
            x = x + 1

    #Create DataFrame from Matched_Fragments.csv
    my_dataframe = pd.read_csv('Matched_Fragments.csv')

    #print(my_dataframe)
    #print(frag_formula)
    #print(row_count)
    my_dataframe.at[row_count - 2, 'Formula'] = frag_formula
    #print(my_dataframe)

    #Count the number of fragments
    count = len(my_dataframe)

    # Delete Proline residue fragments for C, Z, and CZ fragments
    if Proline_fragments == 1:
        #print('it ran')
        if Search_C_Fragments == 1 or Search_Z_Fragments == 1 or Search_CZ_Fragments == 1 or Search_CY_Fragments == 1 or Search_CX_Fragments == 1 or Search_AZ_Fragments == 1 or Search_BZ_Fragments == 1:
            row = 0
            for i in tqdm(range(0, count),total = count, desc='Delete C/Z Fragments on Proline Residues'):
                mychar = 'H'
                mychar_last = 'H'
                mychar_first = 'H'
                mystring = my_dataframe['Sequence'][row]
                if my_dataframe['Frag Type'][row] == 'Z Fragment' \
                        or my_dataframe['Frag Type'][row] == 'CX Int Fragment' \
                        or my_dataframe['Frag Type'][row] == 'CY Int Fragment':
                    mychar = mystring[0]
                if my_dataframe['Frag Type'][row] == 'C Fragment' \
                        or my_dataframe['Frag Type'][row] == 'AZ Int Fragment' \
                        or my_dataframe['Frag Type'][row] == 'BZ Int Fragment':
                    the_last_amino_acid = int(my_dataframe['End AA'][row])
                    mychar = List[the_last_amino_acid]
                if my_dataframe['Frag Type'][row] == 'CZ Int Fragment':
                    length = len(mystring)
                    mychar_first = mystring[0]
                    the_last_amino_acid = int(my_dataframe['End AA'][row])
                    mychar_last = List[the_last_amino_acid]
                else:
                    nothing = 0
                if my_dataframe['Frag Type'][row] != 'CZ Int Fragment':
                    if mychar == 'P':
                        if my_dataframe['Start AA'][row] == 1 or my_dataframe['End AA'][row] == length_sequence:
                            holdv = int(my_dataframe['Start AA'][row]) - 1
                            holdvn = int(my_dataframe['End AA'][row])
                            for i in range(holdv, holdvn):
                                list_of_counts_arr_terminal[holdv] = list_of_counts_arr_terminal[holdv] - 1
                                holdv = holdv + 1
                        else:
                            holdv = int(my_dataframe['Start AA'][row]) - 1
                            holdvn = int(my_dataframe['End AA'][row])
                            for i in range(holdv, holdvn):
                                list_of_counts_arr_internal[holdv] = list_of_counts_arr_internal[holdv] - 1
                                holdv = holdv + 1
                        my_dataframe.iloc[my_dataframe.index[row]] = np.nan
                elif my_dataframe['Frag Type'][row] == 'CZ Int Fragment':
                    if mychar_first == 'P' or mychar_last == 'P':
                        if my_dataframe['Start AA'][row] == 1 or my_dataframe['End AA'][row] == length_sequence:
                            holdv = int(my_dataframe['Start AA'][row]) - 1
                            holdvn = int(my_dataframe['End AA'][row])
                            for i in range(holdv, holdvn):
                                list_of_counts_arr_terminal[holdv] = list_of_counts_arr_terminal[holdv] - 1
                                holdv = holdv + 1
                        else:
                            holdv = int(my_dataframe['Start AA'][row]) - 1
                            holdvn = int(my_dataframe['End AA'][row])
                            for i in range(holdv, holdvn):
                                list_of_counts_arr_internal[holdv] = list_of_counts_arr_internal[holdv] - 1
                                holdv = holdv + 1
                        my_dataframe.iloc[my_dataframe.index[row]] = np.nan
                else:
                    nothing = 0
                row = row + 1
        else:
            nothing = 0
    else:
        Nothing = 0

    #Count the number of fragments
    count = len(my_dataframe)
    #print(length_sequence)

    # Import Modificaitons Amino Acids
    open("Modifications.csv", "r")
    Mod_AA = []
    with open("Modifications.csv") as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            Mod_AA.append(row[2])

    #Delete Fragments that contain modificaitons on the wrong amino acids
    row = 0
    rowd = 0
    for i in tqdm(range(0, ml), total = ml, desc= 'Processing Other Fragments'):
        if Mod_AA[rowd] == 'None':
            row = 0
            rowd = rowd + 1
        else:
            for i in range(0, count):
                if my_dataframe['Variable Mod'][row] == modifications[rowd]:
                    List_seq_mods = list(Mod_AA[rowd])
                    length_List_seq_mods = len(List_seq_mods)
                    List_seq_seq = list(my_dataframe['Sequence'][row])
                    length_List_seq_seq = len(List_seq_seq)
                    for i in range (0, length_List_seq_mods):
                        for k in range(0, length_List_seq_seq):
                            char_mods = List_seq_mods[i]
                            char_seq = List_seq_seq [k]
                            if char_mods == char_seq:
                                Answer = 1
                                break
                            else:
                                Answer = 2
                            k = k + 1
                        if Answer == 1:
                            break
                        else:
                            i = i + 1
                    if Answer == 1:
                        nothing = 0
                    else:
                        if my_dataframe['Start AA'][row] == 1 or my_dataframe['End AA'][row] == length_sequence:
                            holdv = int(my_dataframe['Start AA'][row]) - 1
                            holdvn = int(my_dataframe['End AA'][row])
                            for i in range(holdv, holdvn):
                                list_of_counts_arr_terminal[holdv] = list_of_counts_arr_terminal[holdv] - 1
                                holdv = holdv + 1
                        else:
                            holdv = int(my_dataframe['Start AA'][row]) - 1
                            holdvn = int(my_dataframe['End AA'][row])
                            for i in range(holdv, holdvn):
                                list_of_counts_arr_internal[holdv] = list_of_counts_arr_internal[holdv] - 1
                                holdv = holdv + 1
                        my_dataframe.iloc[my_dataframe.index[row]] = np.nan
                else:
                    nothing = 0
                row = row + 1
            row = 0
            rowd = rowd + 1
    
    count = len(my_dataframe)
    #Delete Duplicate Rows and past duplicates in duplicates.csv
    #print('Deleting Duplicates (7/9)')
    row = 0
    rowd = 0
    for i in tqdm(range(0, count), total = count, desc = 'Deleting Duplicates'): #'Deleting Duplicates (5/7)'
        for i in range(0, count):
            if my_dataframe['Frag_number'][row] != my_dataframe['Frag_number'][rowd] \
                    and my_dataframe['Observed Mass'][row] == my_dataframe['Observed Mass'][rowd] \
                    and abs(my_dataframe['Error'][row]) < abs(my_dataframe['Error'][rowd]):
                if my_dataframe['Frag Type'][row] == 'A Fragment' \
                        or my_dataframe['Frag Type'][row] == 'B Fragment' \
                        or my_dataframe['Frag Type'][row] == 'C Fragment' \
                        or my_dataframe['Frag Type'][row] == 'X Fragment' \
                        or my_dataframe['Frag Type'][row] == 'Y Fragment' \
                        or my_dataframe['Frag Type'][row] == 'Z Fragment':
                    if my_dataframe['Frag Type'][rowd] == 'AX Int Fragment' \
                            or my_dataframe['Frag Type'][rowd] == 'AY Int Fragment' \
                            or my_dataframe['Frag Type'][rowd] == 'AZ Int Fragment' \
                            or my_dataframe['Frag Type'][rowd] == 'BX Int Fragment' \
                            or my_dataframe['Frag Type'][rowd] == 'BY Int Fragment' \
                            or my_dataframe['Frag Type'][rowd] == 'BZ Int Fragment' \
                            or my_dataframe['Frag Type'][rowd] == 'CX Int Fragment' \
                            or my_dataframe['Frag Type'][rowd] == 'CY Int Fragment' \
                            or my_dataframe['Frag Type'][rowd] == 'CZ Int Fragment':
                        holdv = int(my_dataframe['Start AA'][rowd]) - 1
                        holdvn = int(my_dataframe['End AA'][rowd])
                        for i in range(holdv, holdvn):
                            list_of_counts_arr_internal[holdv] = list_of_counts_arr_internal[holdv] - 1
                            holdv = holdv + 1
                        my_dataframe.iloc[my_dataframe.index[rowd]] = np.nan
                    elif my_dataframe['Frag Type'][rowd] == 'A Fragment' \
                            or my_dataframe['Frag Type'][rowd] == 'B Fragment' \
                            or my_dataframe['Frag Type'][rowd] == 'C Fragment' \
                            or my_dataframe['Frag Type'][rowd] == 'X Fragment' \
                            or my_dataframe['Frag Type'][rowd] == 'Y Fragment' \
                            or my_dataframe['Frag Type'][rowd] == 'Z Fragment':
                        holdv = int(my_dataframe['Start AA'][rowd]) - 1
                        holdvn = int(my_dataframe['End AA'][rowd])
                        for i in range(holdv, holdvn):
                            list_of_counts_arr_internal[holdv] = list_of_counts_arr_internal[holdv] - 1
                            holdv = holdv + 1
                        my_dataframe.iloc[my_dataframe.index[rowd]] = np.nan
                    else:
                        print('Check Fragments File')
                elif my_dataframe['Frag Type'][row] == 'AX Int Fragment' \
                        or my_dataframe['Frag Type'][row] == 'AY Int Fragment' \
                        or my_dataframe['Frag Type'][row] == 'AZ Int Fragment' \
                        or my_dataframe['Frag Type'][row] == 'BX Int Fragment' \
                        or my_dataframe['Frag Type'][row] == 'BY Int Fragment' \
                        or my_dataframe['Frag Type'][row] == 'BZ Int Fragment' \
                        or my_dataframe['Frag Type'][row] == 'CX Int Fragment' \
                        or my_dataframe['Frag Type'][row] == 'CY Int Fragment' \
                        or my_dataframe['Frag Type'][row] == 'CZ Int Fragment':
                    if my_dataframe['Frag Type'][rowd] == 'AX Int Fragment' \
                            or my_dataframe['Frag Type'][rowd] == 'AY Int Fragment' \
                            or my_dataframe['Frag Type'][rowd] == 'AZ Int Fragment' \
                            or my_dataframe['Frag Type'][rowd] == 'BX Int Fragment' \
                            or my_dataframe['Frag Type'][rowd] == 'BY Int Fragment' \
                            or my_dataframe['Frag Type'][rowd] == 'BZ Int Fragment' \
                            or my_dataframe['Frag Type'][rowd] == 'CX Int Fragment' \
                            or my_dataframe['Frag Type'][rowd] == 'CY Int Fragment' \
                            or my_dataframe['Frag Type'][rowd] == 'CZ Int Fragment':
                        holdv = int(my_dataframe['Start AA'][rowd]) - 1
                        holdvn = int(my_dataframe['End AA'][rowd])
                        for i in range(holdv, holdvn):
                            list_of_counts_arr_internal[holdv] = list_of_counts_arr_internal[holdv] - 1
                            holdv = holdv + 1
                        my_dataframe.iloc[my_dataframe.index[rowd]] = np.nan
                    elif my_dataframe['Frag Type'][rowd] == 'A Fragment' \
                            or my_dataframe['Frag Type'][rowd] == 'B Fragment' \
                            or my_dataframe['Frag Type'][rowd] == 'C Fragment' \
                            or my_dataframe['Frag Type'][rowd] == 'X Fragment' \
                            or my_dataframe['Frag Type'][rowd] == 'Y Fragment' \
                            or my_dataframe['Frag Type'][rowd] == 'Z Fragment':
                        holdv = int(my_dataframe['Start AA'][row]) - 1
                        holdvn = int(my_dataframe['End AA'][row])
                        for i in range(holdv, holdvn):
                            list_of_counts_arr_internal[holdv] = list_of_counts_arr_internal[holdv] - 1
                            holdv = holdv + 1
                        my_dataframe.iloc[my_dataframe.index[row]] = np.nan
                    else:
                        print('Check Fragments File')
            elif my_dataframe['Frag_number'][row] != my_dataframe['Frag_number'][rowd] \
                    and my_dataframe['Observed Mass'][row] == my_dataframe['Observed Mass'][rowd] \
                    and abs(my_dataframe['Error'][row]) > abs(my_dataframe['Error'][rowd]):
                if my_dataframe['Frag Type'][row] == 'A Fragment' \
                        or my_dataframe['Frag Type'][row] == 'B Fragment' \
                        or my_dataframe['Frag Type'][row] == 'C Fragment' \
                        or my_dataframe['Frag Type'][row] == 'X Fragment' \
                        or my_dataframe['Frag Type'][row] == 'Y Fragment' \
                        or my_dataframe['Frag Type'][row] == 'Z Fragment':
                    if my_dataframe['Frag Type'][rowd] == 'AX Int Fragment' \
                            or my_dataframe['Frag Type'][rowd] == 'AY Int Fragment' \
                            or my_dataframe['Frag Type'][rowd] == 'AZ Int Fragment' \
                            or my_dataframe['Frag Type'][rowd] == 'BX Int Fragment' \
                            or my_dataframe['Frag Type'][rowd] == 'BY Int Fragment' \
                            or my_dataframe['Frag Type'][rowd] == 'BZ Int Fragment' \
                            or my_dataframe['Frag Type'][rowd] == 'CX Int Fragment' \
                            or my_dataframe['Frag Type'][rowd] == 'CY Int Fragment' \
                            or my_dataframe['Frag Type'][rowd] == 'CZ Int Fragment':
                        holdv = int(my_dataframe['Start AA'][rowd]) - 1
                        holdvn = int(my_dataframe['End AA'][rowd])
                        for i in range(holdv, holdvn):
                            list_of_counts_arr_internal[holdv] = list_of_counts_arr_internal[holdv] - 1
                            holdv = holdv + 1
                        my_dataframe.iloc[my_dataframe.index[rowd]] = np.nan
                    elif my_dataframe['Frag Type'][rowd] == 'A Fragment' \
                            or my_dataframe['Frag Type'][rowd] == 'B Fragment' \
                            or my_dataframe['Frag Type'][rowd] == 'C Fragment' \
                            or my_dataframe['Frag Type'][rowd] == 'X Fragment' \
                            or my_dataframe['Frag Type'][rowd] == 'Y Fragment' \
                            or my_dataframe['Frag Type'][rowd] == 'Z Fragment':
                        holdv = int(my_dataframe['Start AA'][row]) - 1
                        holdvn = int(my_dataframe['End AA'][row])
                        for i in range(holdv, holdvn):
                            list_of_counts_arr_internal[holdv] = list_of_counts_arr_internal[holdv] - 1
                            holdv = holdv + 1
                        my_dataframe.iloc[my_dataframe.index[row]] = np.nan
                    else:
                        print('Check Fragments Files')
                elif my_dataframe['Frag Type'][row] == 'AX Int Fragment' \
                        or my_dataframe['Frag Type'][row] == 'AY Int Fragment' \
                        or my_dataframe['Frag Type'][row] == 'AZ Int Fragment' \
                        or my_dataframe['Frag Type'][row] == 'BX Int Fragment' \
                        or my_dataframe['Frag Type'][row] == 'BY Int Fragment' \
                        or my_dataframe['Frag Type'][row] == 'BZ Int Fragment' \
                        or my_dataframe['Frag Type'][row] == 'CX Int Fragment' \
                        or my_dataframe['Frag Type'][row] == 'CY Int Fragment' \
                        or my_dataframe['Frag Type'][row] == 'CZ Int Fragment':
                    if my_dataframe['Frag Type'][rowd] == 'AX Int Fragment' \
                            or my_dataframe['Frag Type'][rowd] == 'AY Int Fragment' \
                            or my_dataframe['Frag Type'][rowd] == 'AZ Int Fragment' \
                            or my_dataframe['Frag Type'][rowd] == 'BX Int Fragment' \
                            or my_dataframe['Frag Type'][rowd] == 'BY Int Fragment' \
                            or my_dataframe['Frag Type'][rowd] == 'BZ Int Fragment' \
                            or my_dataframe['Frag Type'][rowd] == 'CX Int Fragment' \
                            or my_dataframe['Frag Type'][rowd] == 'CY Int Fragment' \
                            or my_dataframe['Frag Type'][rowd] == 'CZ Int Fragment':
                        holdv = int(my_dataframe['Start AA'][row]) - 1
                        holdvn = int(my_dataframe['End AA'][row])
                        for i in range(holdv, holdvn):
                            list_of_counts_arr_internal[holdv] = list_of_counts_arr_internal[holdv] - 1
                            holdv = holdv + 1
                        my_dataframe.iloc[my_dataframe.index[row]] = np.nan
                    elif my_dataframe['Frag Type'][rowd] == 'A Fragment' \
                            or my_dataframe['Frag Type'][rowd] == 'B Fragment' \
                            or my_dataframe['Frag Type'][rowd] == 'C Fragment' \
                            or my_dataframe['Frag Type'][rowd] == 'X Fragment' \
                            or my_dataframe['Frag Type'][rowd] == 'Y Fragment' \
                            or my_dataframe['Frag Type'][rowd] == 'Z Fragment':
                        holdv = int(my_dataframe['Start AA'][row]) - 1
                        holdvn = int(my_dataframe['End AA'][row])
                        for i in range(holdv, holdvn):
                            list_of_counts_arr_internal[holdv] = list_of_counts_arr_internal[holdv] - 1
                            holdv = holdv + 1
                        my_dataframe.iloc[my_dataframe.index[row]] = np.nan
                    else:
                        print('Check Fragments Files')
            elif my_dataframe['Frag_number'][row] != my_dataframe['Frag_number'][rowd] \
                    and my_dataframe['Observed Mass'][row] == my_dataframe['Observed Mass'][rowd] \
                    and abs(my_dataframe['Error'][row]) == abs(my_dataframe['Error'][rowd]):
                if my_dataframe['Frag Type'][row] == 'A Fragment' \
                        or my_dataframe['Frag Type'][row] == 'B Fragment' \
                        or my_dataframe['Frag Type'][row] == 'C Fragment' \
                        or my_dataframe['Frag Type'][row] == 'X Fragment' \
                        or my_dataframe['Frag Type'][row] == 'Y Fragment' \
                        or my_dataframe['Frag Type'][row] == 'Z Fragment':
                    if my_dataframe['Frag Type'][rowd] == 'AX Int Fragment' \
                            or my_dataframe['Frag Type'][rowd] == 'AY Int Fragment' \
                            or my_dataframe['Frag Type'][rowd] == 'AZ Int Fragment' \
                            or my_dataframe['Frag Type'][rowd] == 'BX Int Fragment' \
                            or my_dataframe['Frag Type'][rowd] == 'BY Int Fragment' \
                            or my_dataframe['Frag Type'][rowd] == 'BZ Int Fragment' \
                            or my_dataframe['Frag Type'][rowd] == 'CX Int Fragment' \
                            or my_dataframe['Frag Type'][rowd] == 'CY Int Fragment' \
                            or my_dataframe['Frag Type'][rowd] == 'CZ Int Fragment':
                        holdv = int(my_dataframe['Start AA'][rowd]) - 1
                        holdvn = int(my_dataframe['End AA'][rowd])
                        for i in range(holdv, holdvn):
                            list_of_counts_arr_internal[holdv] = list_of_counts_arr_internal[holdv] - 1
                            holdv = holdv + 1
                        my_dataframe.iloc[my_dataframe.index[rowd]] = np.nan
                    elif my_dataframe['Frag Type'][rowd] == 'A Fragment' \
                            or my_dataframe['Frag Type'][rowd] == 'B Fragment' \
                            or my_dataframe['Frag Type'][rowd] == 'C Fragment' \
                            or my_dataframe['Frag Type'][rowd] == 'X Fragment' \
                            or my_dataframe['Frag Type'][rowd] == 'Y Fragment' \
                            or my_dataframe['Frag Type'][rowd] == 'Z Fragment':
                        nothing = 0
                    else:
                        print('Check Fragments File')
                elif my_dataframe['Frag Type'][row] == 'AX Int Fragment' \
                        or my_dataframe['Frag Type'][row] == 'AY Int Fragment' \
                        or my_dataframe['Frag Type'][row] == 'AZ Int Fragment' \
                        or my_dataframe['Frag Type'][row] == 'BX Int Fragment' \
                        or my_dataframe['Frag Type'][row] == 'BY Int Fragment' \
                        or my_dataframe['Frag Type'][row] == 'BZ Int Fragment' \
                        or my_dataframe['Frag Type'][row] == 'CX Int Fragment' \
                        or my_dataframe['Frag Type'][row] == 'CY Int Fragment' \
                        or my_dataframe['Frag Type'][row] == 'CZ Int Fragment':
                    if my_dataframe['Frag Type'][rowd] == 'AX Int Fragment' \
                            or my_dataframe['Frag Type'][rowd] == 'AY Int Fragment' \
                            or my_dataframe['Frag Type'][rowd] == 'AZ Int Fragment' \
                            or my_dataframe['Frag Type'][rowd] == 'BX Int Fragment' \
                            or my_dataframe['Frag Type'][rowd] == 'BY Int Fragment' \
                            or my_dataframe['Frag Type'][rowd] == 'BZ Int Fragment' \
                            or my_dataframe['Frag Type'][rowd] == 'CX Int Fragment' \
                            or my_dataframe['Frag Type'][rowd] == 'CY Int Fragment' \
                            or my_dataframe['Frag Type'][rowd] == 'CZ Int Fragment':
                        nothing = 0
                    elif my_dataframe['Frag Type'][rowd] == 'A Fragment' \
                            or my_dataframe['Frag Type'][rowd] == 'B Fragment' \
                            or my_dataframe['Frag Type'][rowd] == 'C Fragment' \
                            or my_dataframe['Frag Type'][rowd] == 'X Fragment' \
                            or my_dataframe['Frag Type'][rowd] == 'Y Fragment' \
                            or my_dataframe['Frag Type'][rowd] == 'Z Fragment':
                        holdv = int(my_dataframe['Start AA'][row]) - 1
                        holdvn = int(my_dataframe['End AA'][row])
                        for i in range(holdv, holdvn):
                            list_of_counts_arr_internal[holdv] = list_of_counts_arr_internal[holdv] - 1
                            holdv = holdv + 1
                        my_dataframe.iloc[my_dataframe.index[row]] = np.nan
                    else:
                        print('Check Fragments File')
            else:
                nothing = 0
            rowd = rowd + 1
        rowd = 0
        row = row + 1
    #print(my_dataframe)
    my_dataframe = my_dataframe[pd.notnull(my_dataframe['Start AA'])]
    my_dataframe.to_csv('Matched_Fragments_V2.csv')

#print('Making Figures (6/7)')
#Add two count arrays
list_of_counts_arr_total = array('f')
for i in range(0, length_sequence):
    list_of_counts_arr_total.append(0)



#print(list_of_counts_arr_total)
for i in range (0, length_sequence):
    list_of_counts_arr_total[m] = list_of_counts_arr_terminal[m] + list_of_counts_arr_internal[m]
    m = m +1
#print(list_of_counts_arr_total)

#Open a new file to put counts in.
with open('Counts.csv', 'w') as csvFile:
    csvFile.close()
m = 0
counts = [['AA','Terminal', 'Internal','Total']]
with open('Counts.csv', 'a') as writeFile:
    writer = csv.writer(writeFile)
    writer.writerows(counts)

for i in range(1, length_sequence+1):
    counts = [[List[m],str(list_of_counts_arr_terminal[m]),str(list_of_counts_arr_internal[m]),list_of_counts_arr_total[m]]]
    with open('Counts.csv', 'a') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(counts)
    m = m + 1

#Open a new file to put counts in.
with open('Counts.csv', 'w') as csvFile:
    csvFile.close()
m = 0
counts = [['AA','Terminal', 'Internal','Total']]
with open('Counts.csv', 'a') as writeFile:
    writer = csv.writer(writeFile)
    writer.writerows(counts)

for i in range(1, length_sequence+1):
    counts = [[List[m],str(list_of_counts_arr_terminal[m]),str(list_of_counts_arr_internal[m]),list_of_counts_arr_total[m]]]
    with open('Counts.csv', 'a') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(counts)
    m = m + 1

df = pd.read_csv('Counts.csv')
df.to_csv('Count.csv', index = False)
os.remove('Counts.csv')

# Open data file
data = pd.read_csv('count.csv')

# Find max value
Total = data["Total"].tolist()

max = max(Total)

# Extract Amino Acid Sequence
AA_list = data["AA"].tolist()

i = len(AA_list)
while i % 25 != 0:
    if i % 25 == 0:
        break
    else:
        i = i +1
        AA_list.append(" ")

AA_table = pd.DataFrame(np.array(AA_list).reshape(-1,25),index=None,columns=None)

AA_table_np = AA_table.to_numpy()

# Extract Terminal Fragments
Term_Frag = data["Terminal"].tolist()

i = len(Term_Frag)
while i % 25 != 0:
    if i % 25 == 0:
        break
    else:
        i = i + 1
        Term_Frag.append("0")

Term_FM = pd.to_numeric(Term_Frag)
Term_TM = pd.DataFrame(np.array(Term_FM).reshape(-1,25),index=None,columns=None)

Term_TM.to_csv('Term_TM.csv',index=None)

Term_corr = pd.read_csv('Term_TM.csv')

# Extract Internal Fragments
Int_Frag = data["Internal"].tolist()

i = len(Int_Frag)
while i % 25 != 0:
    if i % 25 == 0:
        break
    else:
        i = i +1
        Int_Frag.append("0")

Int_FM = pd.to_numeric(Int_Frag)
Int_TM = pd.DataFrame(np.array(Int_FM).reshape(-1,25),index=None,columns=None)

Int_TM.to_csv('Int_TM.csv',index=None)

Int_corr = pd.read_csv('Int_TM.csv')

# Plot heatmaps as figure
fig1, (ax1,ax2) = plt.subplots(nrows=2)
fig1.subplots_adjust(hspace=0.2,)

sns.heatmap(Term_corr,
            cmap="Reds",
            ax=ax1,
            vmin=0,
            vmax=None,
            square=True,
            linewidths=0.5,
            linecolor='white',
            cbar=False,
            xticklabels=False,
            yticklabels=False,
            annot=AA_table_np,
            fmt=''
            )

fig1.colorbar(ax1.collections[0],
             ax=ax1,
             location="right",
             use_gridspec=False,
             pad=0.05,
             shrink=0.75,
             )

ax1.set_title('Terminal Fragments',
             fontsize=10,
             loc='left'
             )

sns.heatmap(Int_corr,
            cmap="Blues",
            ax=ax2,
            vmin=0,
            vmax=None,
            square=True,
            linewidths=0.5,
            linecolor='white',
            cbar=False,
            xticklabels=False,
            yticklabels=False,
            annot=AA_table_np,
            fmt='')

fig1.colorbar(ax2.collections[0],
             ax=ax2,
             location="right",
             use_gridspec=False,
             pad=0.05,
             shrink=0.75
             )

ax2.set_title('Internal Fragments',
              fontsize=10,
              loc='left'
              )

plt.savefig('Fig1.svg' )

#Fragment sites
fig2, (ax3,ax4) = plt.subplots(nrows=2)
ax3.set_axis_off()
ax4.set_axis_off()
ax3.set_title('Terminal Fragments', fontsize=14, loc='left')
ax4.set_title('Internal Fragments', fontsize=14, loc='left')
fig2.suptitle('Fragment cleavage sites', fontsize=16)


frag = pd.read_csv(('Matched_Fragments_V2.csv'), index_col=0)
with open('Sequence.txt', 'r') as file:
    seq = file.read()

frag_loc = list(np.unique(frag['Start AA']))
frag_loc.extend(list(np.unique(frag['End AA'])))
frag_loc = np.unique(frag_loc)

Terminal_frag_loc = list(np.unique(frag['End AA'][frag['Start AA']==1]))
Terminal_frag_loc.extend(list(np.unique(frag['Start AA'][frag['End AA']==len(seq)])))
Terminal_frag_loc.append(0)
Terminal_frag_loc.append(len(seq))
Terminal_frag_loc = np.unique(Terminal_frag_loc)
Terminal_frag_loc

Internal_frag_loc = list(np.unique(frag['End AA'][frag['Start AA']!=1]))
Internal_frag_loc.extend(list(np.unique(frag['Start AA'][frag['End AA']!=len(seq)])))
Internal_frag_loc = np.unique(Internal_frag_loc)
Internal_frag_loc

Shared_frag_loc = [i for i in Internal_frag_loc if i in Terminal_frag_loc]
Shared_frag_loc = np.unique(Shared_frag_loc)
Shared_frag_loc

start_aa = np.unique(frag['Start AA'])
end_aa = np.unique(frag['End AA'])
master_string = []
colors = []
for i, aa in enumerate(seq):
    master_string.append(aa)
    colors.append('black')
    if i in start_aa:
        master_string.append('|')
        colors.append('red')
    elif i in end_aa:
        master_string.append('|')
        colors.append('red')
annotated = ''.join(i for i in master_string)
annotated

def rainbow_text(x, y, strings, colors, orientation='horizontal', ax=ax3, **kwargs):


    """
    Take a list of *strings* and *colors* and place them next to each
    other, with text strings[i] being shown in colors[i].

    Parameters
    ----------
    x, y : float
        Text position in data coordinates.
    strings : list of str
        The strings to draw.
    colors : list of color
        The colors to use.
    orientation : {'horizontal', 'vertical'}
    ax : Axes, optional
        The Axes to draw into. If None, the current axes will be used.
    **kwargs
        All other keyword arguments are passed to plt.text(), so you can
        set the font size, family, etc.
    """

    if ax is None:
        ax = plt.gca()
    t = ax.transData
    canvas = ax.figure.canvas

    assert orientation in ['horizontal', 'vertical']
    if orientation == 'vertical':
        kwargs.update(rotation=90, verticalalignment='bottom')

    for s, c in zip(strings, colors):
        text = ax.text(x, y, s + " ", color=c, transform=t, **kwargs)

        # Need to draw to update the text position.
        text.draw(canvas.get_renderer())
        ex = text.get_window_extent()
        if orientation == 'horizontal':
            t = transforms.offset_copy(
                text.get_transform(), x=ex.width, units='dots')
        else:
            t = transforms.offset_copy(
                text.get_transform(), y=ex.height, units='dots')


words = master_string
temp_words = []
temp_colors = []

Total_frag_loc = list(np.unique(frag['Start AA For Fig']))
Total_frag_loc.extend(list(np.unique(frag['End AA'])))
Total_frag_loc = np.unique(Total_frag_loc)

Terminal_frag_loc = list(np.unique(frag['End AA'][frag['Start AA For Fig']==0]))
Terminal_frag_loc.extend(list(np.unique(frag['Start AA For Fig'][frag['End AA']==len(seq)])))
Terminal_frag_loc.append(0)
Terminal_frag_loc.append(len(seq))
Terminal_frag_loc = np.unique(Terminal_frag_loc)

Internal_frag_loc = list(np.unique(frag['End AA'][frag['Start AA For Fig']!=0]))
Internal_frag_loc.extend(list(np.unique(frag['Start AA For Fig'][frag['End AA']!=len(seq)])))
Internal_frag_loc = np.unique(Internal_frag_loc)

Shared_frag_loc = [i for i in Internal_frag_loc if i in Terminal_frag_loc]
Shared_frag_loc = np.unique(Shared_frag_loc)

Colors = ['white','red','blue']

length = len(seq)+len(frag_loc)
step = 25
lines = math.ceil(len(seq)/step)
temp_words = []
temp_colors = []
shift = 1
line = 0.75
size = 14
family = 'monospace'

for i,aa in enumerate(seq):
    temp_words.append(aa)
    q = 0
    while q != k_ml:
        if modificationnumber[q] == i + 1:
            hold = 1
            break
        else:
            hold = 2
        q = q + 1
    if hold == 1:
        temp_colors.append('red')
    else:
        temp_colors.append('black')
    if i==len(seq)-shift:
        continue
    if len(Colors)==1:
        if i+shift in frag_loc:
            temp_words.append('|')
            temp_colors.append(str(Colors[1]))
        else:
            temp_words.append('|')
            temp_colors.append('white')
    elif len(Colors)==2:
        if i+shift in Shared_frag_loc:
            temp_words.append('|')
            temp_colors.append(str(Colors[1]))
        elif i+shift in Terminal_frag_loc:
            temp_words.append('|')
            temp_colors.append(str(Colors[1]))
        elif i+shift in Internal_frag_loc:
            temp_words.append('|')
            temp_colors.append(str(Colors[0]))
        else:
            temp_words.append('|')
            temp_colors.append('white')
    elif len(Colors)==3:
        if i+shift in Shared_frag_loc:
            temp_words.append('|')
            temp_colors.append(str(Colors[1]))
        elif i+shift in Terminal_frag_loc:
            temp_words.append('|')
            temp_colors.append(str(Colors[1]))
        elif i+shift in Internal_frag_loc:
            temp_words.append('|')
            temp_colors.append(str(Colors[0]))
        else:
            temp_words.append('|')
            temp_colors.append('white')
    if (i+1)%step==0:
        rainbow_text(0, ((lines-line)/lines), temp_words, temp_colors, family=family, size=size, weight = 'extra bold')
        temp_words = []
        temp_colors = []
        line+=1
rainbow_text(0, ((lines-line)/lines), temp_words, temp_colors, family=family, size=size, weight = 'extra bold')

def rainbow_text(x, y, strings, colors, orientation='horizontal',
                 ax=ax4, **kwargs):


    """
    Take a list of *strings* and *colors* and place them next to each
    other, with text strings[i] being shown in colors[i].

    Parameters
    ----------
    x, y : float
        Text position in data coordinates.
    strings : list of str
        The strings to draw.
    colors : list of color
        The colors to use.
    orientation : {'horizontal', 'vertical'}
    ax : Axes, optional
        The Axes to draw into. If None, the current axes will be used.
    **kwargs
        All other keyword arguments are passed to plt.text(), so you can
        set the font size, family, etc.
    """
    if ax is None:
        ax = plt.gca()
    t = ax.transData
    canvas = ax.figure.canvas

    assert orientation in ['horizontal', 'vertical']
    if orientation == 'vertical':
        kwargs.update(rotation=90, verticalalignment='bottom')

    for s, c in zip(strings, colors):
        text = ax.text(x, y, s + " ", color=c, transform=t, **kwargs)

        # Need to draw to update the text position.
        text.draw(canvas.get_renderer())
        ex = text.get_window_extent()
        if orientation == 'horizontal':
            t = transforms.offset_copy(
                text.get_transform(), x=ex.width, units='dots')
        else:
            t = transforms.offset_copy(
                text.get_transform(), y=ex.height, units='dots')



words = master_string
temp_words = []
temp_colors = []

Total_frag_loc = list(np.unique(frag['Start AA For Fig']))
Total_frag_loc.extend(list(np.unique(frag['End AA'])))
Total_frag_loc = np.unique(Total_frag_loc)

Terminal_frag_loc = list(np.unique(frag['End AA'][frag['Start AA For Fig']==0]))
Terminal_frag_loc.extend(list(np.unique(frag['Start AA For Fig'][frag['End AA']==len(seq)])))
Terminal_frag_loc.append(0)
Terminal_frag_loc.append(len(seq))
Terminal_frag_loc = np.unique(Terminal_frag_loc)

Internal_frag_loc = list(np.unique(frag['End AA'][frag['Start AA For Fig']!=0]))
Internal_frag_loc.extend(list(np.unique(frag['Start AA For Fig'][frag['End AA']!=len(seq)])))
Internal_frag_loc = np.unique(Internal_frag_loc)

Shared_frag_loc = [i for i in Internal_frag_loc if i in Terminal_frag_loc]
Shared_frag_loc = np.unique(Shared_frag_loc)

Colors = ['white','red','blue']

length = len(seq)+len(frag_loc)
step = 25
lines = math.ceil(len(seq)/step)
temp_words = []
temp_colors = []
shift = 1
line = 0.75
size = 14
family = 'monospace'

for i,aa in enumerate(seq):
    temp_words.append(aa)
    q = 0
    while q != k_ml:
        if modificationnumber[q] == i + 1:
            hold = 1
            break
        else:
            hold = 2
        q = q + 1
    if hold == 1:
        temp_colors.append('red')
    else:
        temp_colors.append('black')
    if i==len(seq)-shift:
        continue
    if len(Colors)==1:
        if i+shift in frag_loc:
            temp_words.append('|')
            temp_colors.append(str(Colors[2]))
        else:
            temp_words.append('|')
            temp_colors.append('white')
    elif len(Colors)==2:
        if i+shift in Shared_frag_loc:
            temp_words.append('|')
            temp_colors.append(str(Colors[2]))
        elif i+shift in Terminal_frag_loc:
            temp_words.append('|')
            temp_colors.append(str(Colors[0]))
        elif i+shift in Internal_frag_loc:
            temp_words.append('|')
            temp_colors.append(str(Colors[2]))
        else:
            temp_words.append('|')
            temp_colors.append('white')
    elif len(Colors)==3:
        if i+shift in Shared_frag_loc:
            temp_words.append('|')
            temp_colors.append(str(Colors[2]))
        elif i+shift in Terminal_frag_loc:
            temp_words.append('|')
            temp_colors.append(str(Colors[0]))
        elif i+shift in Internal_frag_loc:
            temp_words.append('|')
            temp_colors.append(str(Colors[2]))
        else:
            temp_words.append('|')
            temp_colors.append('white')
    if (i+1)%step==0:
        rainbow_text(0, ((lines-line)/lines), temp_words, temp_colors, size=size, family=family, weight = 'extra bold')
        temp_words = []
        temp_colors = []
        line+=1
rainbow_text(0, ((lines-line)/lines), temp_words, temp_colors, size=size, family=family, weight = 'extra bold')

plt.savefig('Fig2.png' , bbox_inches = 'tight')

# Open data file and convert to pandas frame
data = pd.read_csv('Matched_Fragments_V2.csv')

data_A_B_C = pd.DataFrame(columns = data.columns)
data_X_Y_Z = pd.DataFrame(columns = data.columns)
data_Int_Frag = pd.DataFrame(columns = data.columns)

cond = data['Frag Type'] == 'A Fragment'
rows = data.loc[cond, :]
data_A_B_C = data_A_B_C.append(rows, ignore_index=True)
data.drop(rows.index, inplace=True)
cond = data['Frag Type'] == 'B Fragment'
rows = data.loc[cond, :]
data_A_B_C = data_A_B_C.append(rows, ignore_index=True)
data.drop(rows.index, inplace=True)
cond = data['Frag Type'] == 'C Fragment'
rows = data.loc[cond, :]
data_A_B_C = data_A_B_C.append(rows, ignore_index=True)
data.drop(rows.index, inplace=True)

cond = data['Frag Type'] == 'X Fragment'
rows = data.loc[cond, :]
data_X_Y_Z = data_X_Y_Z.append(rows, ignore_index=True)
data.drop(rows.index, inplace=True)
cond = data['Frag Type'] == 'Y Fragment'
rows = data.loc[cond, :]
data_X_Y_Z = data_X_Y_Z.append(rows, ignore_index=True)
data.drop(rows.index, inplace=True)
cond = data['Frag Type'] == 'Z Fragment'
rows = data.loc[cond, :]
data_X_Y_Z = data_X_Y_Z.append(rows, ignore_index=True)
data.drop(rows.index, inplace=True)

data_A_B_C_two = data_A_B_C.sort_values(by=['End AA'])
data_X_Y_Z_two = data_X_Y_Z.sort_values(by=['Start AA'])
df = pd.concat([data_A_B_C_two,data,data_X_Y_Z_two])

ordered_df = df
my_range = range(1, len(df.index) + 1)

#Fragment sites
fig3 = plt.figure()
fig3.suptitle('Fragment Location', fontsize=14)

# The vertical plot is made using the hline function
plt.hlines(y=my_range, xmin=ordered_df['Start AA For Fig'], xmax=ordered_df['End AA'], color='grey', alpha=0.2)
plt.scatter(ordered_df['Start AA For Fig'], my_range, color='blue', label='Start AA For Fig', s=ordered_df['Intensity']/ordered_df['Intensity'].max()*8)
plt.scatter(ordered_df['End AA'], my_range, color='blue', label='End AA', s=ordered_df['Intensity']/ordered_df['Intensity'].max()*8)
for i in range(0,k_ml):
    if modificationnumber[i] != 0:
        plt.axvline(x=modificationnumber[i], color='k', linestyle='--')
    else:
        nothing = 0
#plt.legend()

# Add title and axis names
plt.title('Fragment location', loc='left')
plt.yticks([])
if length_sequence < 10:
    plt.xticks(np.arange(0, length_sequence + 1, step=1))
else:
    plt.xticks(np.arange(0, length_sequence + 1, step=round(length_sequence/10)))
plt.xlabel('Amino acid number')
f=pd.read_csv("Matched_Fragments_V2.csv")
keep_col = ['Frag_number', 'Frag Type', 'Fixed Mod', 'Variable Mod', 'Term Mod', 'Observed Mass', 'Theoredical Mass', 'Start AA', 'End AA', 'Error', 'Sequence', 'Intensity', 'Formula']
new_f = f[keep_col]
new_f.to_csv("Matched_Fragments_Final.csv", index=False)
os.remove("Matched_Fragments_V2.csv")
os.remove("Count.csv")
os.remove("Term_TM.csv")
os.remove("Int_TM.csv")
os.remove("Matched_Fragments.csv")
plt.savefig('Fig3.svg' )
#print('Done (7/7)')
plt.show()