import os
import subprocess
import tkinter as tk
from tkinter import *
import tkinter.font as font
import tkinter.messagebox
from tkinter.filedialog import askopenfile

root = tk.Tk()
root.title("Comprehensive Localization of Internal Protein Sequences (ClipsMS)")
topframe = Frame(root)
topframe.pack(side = TOP)
bottomframe = Frame(root)
bottomframe.pack(side = BOTTOM)
leftframe = Frame(root)
leftframe.pack(side = LEFT)
rightframe = Frame(root)
rightframe.pack(side = RIGHT)

Title_Font = font.Font(family='Helvetica', size=15, weight='bold')
Name_of_Program = Label(topframe, text = 'Comprehensive Localization of Internal Protein Sequences (ClipsMS)')
Name_of_Program['font']=Title_Font

Name_of_Institution = Label(topframe, text = 'UCLA Department of Chemistry and Biochemistry')
Disclaimer = Label(bottomframe, text = 'If data is analyzed with this program, please cite ClipsMS: An Algorithm for Analyzing Internal Fragments Resulting from Top-Down Mass Spectrometry')

Font = font.Font(family='Helvetica', size=10, weight='bold')
Space_Font = font.Font(family='Helvetica', size=2, weight='bold')

photo = PhotoImage(file = 'Logo.png')
label_photo = Label(root, image = photo)

canvas1 = tk.Canvas(leftframe, width = 350, height = 20)
canvas2 = tk.Canvas(leftframe, width = 350, height = 20)
canvas3 = tk.Canvas(leftframe, width = 350, height = 20)
canvas4 = tk.Canvas(leftframe, width = 350, height = 20)
canvas5 = tk.Canvas(leftframe, width = 350, height = 20)
canvas6 = tk.Canvas(leftframe, width = 350, height = 20)

entry1 = tk.Entry(root)
canvas1.create_window(175,10, window = entry1)
Label1 = Label(leftframe, text = 'Error (PPM)')
Label1['font']=Font

entry2 = tk.Entry(root)
canvas2.create_window(175,10, window = entry2)
Label2 = Label(leftframe, text = 'Sequence')
Label2['font']=Font

entry3 = tk.Entry(root)
canvas5.create_window(175,10, window = entry3)
Label11 = Label(leftframe, text = 'Smallest Int Frag Size (#AA)')
Label11['font']=Font

Label_Space_1 = Label(leftframe, text = ' ')
Label_Space_1['font']=Space_Font
Label_Space_2 = Label(leftframe, text = ' ')
Label_Space_2['font']=Space_Font
Label_Space_3 = Label(leftframe, text = ' ')
Label_Space_3['font']=Space_Font
Label_Space_4 = Label(rightframe, text = ' ')
Label_Space_4['font']=Space_Font
Label_Space_5 = Label(leftframe, text = ' ')
Label_Space_5['font']=Space_Font

Label3 = Label(leftframe, text = 'N-Terminal Modification')
Label3['font']=Font
Label4 = Label(leftframe, text = 'C-Terminal Modification')
Label4['font']=Font
Label10 = Label(leftframe, text = ' ')
Label7 = Label(rightframe, text = 'Search Fragment Type')
Label7['font']=Font
Label9 = Label(rightframe, text = 'Fragmentation Method Used')
Label9['font']=Font

def runProgram():
    Error = entry1.get()
    #print(int(Error))
    file = open("PPM_Error.txt", "w")
    file.write(Error)
    file.close()
    Sequence = entry2.get()
    file = open("Sequence.txt", "w")
    file.write(Sequence)
    file.close()
    Num_AA_Int_Frag = entry3.get()
    file = open("Number_of_AA.txt", "w")
    file.write(Num_AA_Int_Frag)
    file.close()
    if var1.get() == 1:
        value = 42.01056
        file = open("N_Term_Mod.txt", "w")
        file.write(str(value))
        file.close()
    if var2.get() == 1:
        value = 0.98401
        file = open("N_Term_Mod.txt", "w")
        file.write(str(value))
        file.close()
    if var3.get() == 1:
        value = 14.01565
        file = open("N_Term_Mod.txt", "w")
        file.write(str(value))
        file.close()
    if var4.get() == 1:
        value = 28.0313
        file = open("N_Term_Mod.txt", "w")
        file.write(str(value))
        file.close()
    if var5.get() == 1:
        value = 27.99491
        file = open("N_Term_Mod.txt", "w")
        file.write(str(value))
        file.close()
    if var1.get() == 0 and var2.get() == 0 and var3.get() == 0 and var4.get() == 0 and var5.get() == 0:
        value = 0
        file = open("N_Term_Mod.txt", "w")
        file.write(str(value))
        file.close()
    if var6.get() == 1:
        value = -0.98401
        file = open("C_Term_Mod.txt", "w")
        file.write(str(value))
        file.close()
    if var7.get() == 1:
        value = 14.01565
        file = open("C_Term_Mod.txt", "w")
        file.write(str(value))
        file.close()
    if var8.get() == 1:
        value = -18.0106
        file = open("C_Term_Mod.txt", "w")
        file.write(str(value))
        file.close()
    if var6.get() == 0 and var7.get() == 0 and var8.get() == 0:
        value = 0
        file = open("C_Term_Mod.txt", "w")
        file.write(str(value))
        file.close()
    if var9.get() == 1:
        valueA = 1
        file = open("A_Fragments.txt", "w")
        file.write(str(valueA))
        file.close()
    else:
        valueA = 0
        file = open("A_Fragments.txt", "w")
        file.write(str(valueA))
        file.close()
    if var10.get() == 1:
        valueB = 1
        file = open("B_Fragments.txt", "w")
        file.write(str(valueB))
        file.close()
    else:
        valueB = 0
        file = open("B_Fragments.txt", "w")
        file.write(str(valueB))
        file.close()
    if var11.get() == 1:
        valueC = 1
        file = open("C_Fragments.txt", "w")
        file.write(str(valueC))
        file.close()
    else:
        valueC = 0
        file = open("C_Fragments.txt", "w")
        file.write(str(valueC))
        file.close()
    if var12.get() == 1:
        valueX = 1
        file = open("X_Fragments.txt", "w")
        file.write(str(valueX))
        file.close()
    else:
        valueX = 0
        file = open("X_Fragments.txt", "w")
        file.write(str(valueX))
        file.close()
    if var13.get() == 1:
        valueY = 1
        file = open("Y_Fragments.txt", "w")
        file.write(str(valueY))
        file.close()
    else:
        valueY = 0
        file = open("Y_Fragments.txt", "w")
        file.write(str(valueY))
        file.close()
    if var14.get() == 1:
        valueZ = 1
        file = open("Z_Fragments.txt", "w")
        file.write(str(valueZ))
        file.close()
    else:
        valueZ = 0
        file = open("Z_Fragments.txt", "w")
        file.write(str(valueZ))
        file.close()
    if var15.get() == 1:
        valueAX = 1
        file = open("AX_Fragments.txt", "w")
        file.write(str(valueAX))
        file.close()
    else:
        valueAX = 0
        file = open("AX_Fragments.txt", "w")
        file.write(str(valueAX))
        file.close()
    if var16.get() == 1:
        valueAY = 1
        file = open("AY_Fragments.txt", "w")
        file.write(str(valueAY))
        file.close()
    else:
        valueAY = 0
        file = open("AY_Fragments.txt", "w")
        file.write(str(valueAY))
        file.close()
    if var17.get() == 1:
        valueAZ = 1
        file = open("AZ_Fragments.txt", "w")
        file.write(str(valueAZ))
        file.close()
    else:
        valueAZ = 0
        file = open("AZ_Fragments.txt", "w")
        file.write(str(valueAZ))
        file.close()
    if var18.get() == 1:
        valueBX = 1
        file = open("BX_Fragments.txt", "w")
        file.write(str(valueBX))
        file.close()
    else:
        valueBX = 0
        file = open("BX_Fragments.txt", "w")
        file.write(str(valueBX))
        file.close()
    if var19.get() == 1:
        valueBY = 1
        file = open("BY_Fragments.txt", "w")
        file.write(str(valueBY))
        file.close()
    else:
        valueBY = 0
        file = open("BY_Fragments.txt", "w")
        file.write(str(valueBY))
        file.close()
    if var20.get() == 1:
        valueBZ = 1
        file = open("BZ_Fragments.txt", "w")
        file.write(str(valueBZ))
        file.close()
    else:
        valueBZ = 0
        file = open("BZ_Fragments.txt", "w")
        file.write(str(valueBZ))
        file.close()
    if var21.get() == 1:
        valueCX = 1
        file = open("CX_Fragments.txt", "w")
        file.write(str(valueCX))
        file.close()
    else:
        valueCX = 0
        file = open("CX_Fragments.txt", "w")
        file.write(str(valueCX))
        file.close()
    if var22.get() == 1:
        valueCY = 1
        file = open("CY_Fragments.txt", "w")
        file.write(str(valueCY))
        file.close()
    else:
        valueCY = 0
        file = open("CY_Fragments.txt", "w")
        file.write(str(valueCY))
        file.close()
    if var23.get() == 1:
        valueCZ = 1
        file = open("CZ_Fragments.txt", "w")
        file.write(str(valueCZ))
        file.close()
    else:
        valueCZ = 0
        file = open("CZ_Fragments.txt", "w")
        file.write(str(valueCZ))
        file.close()
    if var29.get() == 1:
        value = 1
        file = open("Proline_fragments.txt", "w")
        file.write(str(value))
        file.close()
    else:
        value = 0
        file = open("Proline_fragments.txt", "w")
        file.write(str(value))
        file.close()
    if valueA == 1 \
            or valueB == 1 \
            or valueC == 1 \
            or valueX == 1 \
            or valueY == 1 \
            or valueZ == 1:
        if valueAX == 1 \
            or valueAY == 1 \
            or valueAZ == 1 \
            or valueBX == 1 \
            or valueBY == 1 \
            or valueBZ == 1 \
            or valueCX == 1 \
            or valueCY == 1 \
            or valueCZ == 1:
            answer = tkinter.messagebox.askquestion('Assign Fragments', 'Do you want to assign terminal fragments first?')
            if answer == 'yes':
                #os.system(['Test_Biased.py')
                process = subprocess.Popen(['python', 'Test_Biased.py'], shell=True, stdout=subprocess.PIPE)
                print(process.communicate()[0])
            else:
                #os.system('Test_Unbiased.py')
                process = subprocess.Popen(['python', 'Test_Unbiased.py'], shell=True, stdout=subprocess.PIPE)
                print(process.communicate()[0])
        else:
            #os.system('Test_Unbiased.py')
            process = subprocess.Popen(['python', 'Test_Unbiased.py'], shell=True, stdout=subprocess.PIPE)
            print(process.communicate()[0])
    else:
        #os.system('Test_Unbiased.py')
        process = subprocess.Popen(['python', 'Test_Unbiased.py'], shell=True, stdout=subprocess.PIPE)
        print(process.communicate()[0])

def Fragments():
    Label3 = Label(leftframe, text='                             ')
    canvas3.create_window(175, 10, window=Label3)
    file = askopenfile(mode = 'r', filetypes = [('csv files', '*.csv')])
    content = file.read()
    print('Data Read')
    with open('Fragments.csv', 'w') as csvFile:
        data = content
        csvFile.write(data)
    csvFile.close()
    Label3 = Label(leftframe, text='Data Received')
    canvas3.create_window(175, 10, window=Label3)

def Modifications():
    Label4 = Label(leftframe, text='                            ')
    canvas4.create_window(175, 10, window=Label4)
    file = askopenfile(mode = 'r', filetypes = [('csv files', '*.csv')])
    content = file.read()
    print('Modifications Read')
    with open('Modifications.csv', 'w') as csvFile:
        data = content
        csvFile.write(data)
    csvFile.close()
    var28.set(0)
    Label4 = Label(leftframe, text='Data Received')
    canvas4.create_window(175, 10, window=Label4)

def Known_Modifications():
    Label12 = Label(leftframe, text='                            ')
    canvas6.create_window(175, 10, window=Label12)
    file = askopenfile(mode = 'r', filetypes = [('csv files', '*.csv')])
    content = file.read()
    print('Localized Modifications Read')
    with open('Known_Modifications.csv', 'w') as csvFile:
        data = content
        csvFile.write(data)
    csvFile.close()
    var30.set(0)
    Label12 = Label(leftframe, text='Data Received')
    canvas6.create_window(175, 10, window=Label12)

def No_Variable_Modifications():
    file = open('No_Modifications_2.csv', 'r')
    content = file.read()
    with open('Modifications.csv', 'w') as csvFile:
        data = content
        csvFile.write(data)
    csvFile.close()
    Label4 = Label(leftframe, text = '                                ')
    canvas4.create_window(175, 10, window= Label4)

def No_Known_Modifications():
    file = open('No_Modifications.csv', 'r')
    content = file.read()
    with open('Known_Modifications.csv', 'w') as csvFile:
        data = content
        csvFile.write(data)
    csvFile.close()
    Label12 = Label(leftframe, text = '                                ')
    canvas6.create_window(175, 10, window= Label12)

def Uncheck_boxes_1():
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
def Uncheck_boxes_2():
    var1.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
def Uncheck_boxes_3():
    var1.set(0)
    var2.set(0)
    var4.set(0)
    var5.set(0)
def Uncheck_boxes_4():
    var1.set(0)
    var2.set(0)
    var3.set(0)
    var5.set(0)
def Uncheck_boxes_5():
    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
def Uncheck_boxes_6():
    var7.set(0)
    var8.set(0)
def Uncheck_boxes_7():
    var6.set(0)
    var8.set(0)
def Uncheck_boxes_8():
    var6.set(0)
    var7.set(0)
def Uncheck_boxes_9():
    var9.set(0)
    var10.set(1)
    var11.set(0)
    var12.set(0)
    var13.set(1)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    var17.set(0)
    var18.set(0)
    var19.set(1)
    var20.set(0)
    var21.set(0)
    var22.set(0)
    var23.set(0)
    var25.set(0)
    var26.set(0)
    var27.set(0)
    var29.set(0)
def Uncheck_boxes_10():
    var9.set(0)
    var10.set(0)
    var11.set(1)
    var12.set(0)
    var13.set(0)
    var14.set(1)
    var15.set(0)
    var16.set(0)
    var17.set(0)
    var18.set(0)
    var19.set(0)
    var20.set(0)
    var21.set(0)
    var22.set(0)
    var23.set(1)
    var24.set(0)
    var26.set(0)
    var27.set(0)
    var29.set(1)
def Uncheck_boxes_11():
    var9.set(1)
    var10.set(1)
    var11.set(1)
    var12.set(1)
    var13.set(1)
    var14.set(1)
    var15.set(1)
    var16.set(1)
    var17.set(1)
    var18.set(1)
    var19.set(1)
    var20.set(1)
    var21.set(1)
    var22.set(1)
    var23.set(1)
    var24.set(0)
    var25.set(0)
    var27.set(0)
    var29.set(0)
def Uncheck_boxes_12():
    var9.set(1)
    var10.set(0)
    var11.set(1)
    var12.set(1)
    var13.set(0)
    var14.set(1)
    var15.set(1)
    var16.set(0)
    var17.set(1)
    var18.set(0)
    var19.set(0)
    var20.set(0)
    var21.set(1)
    var22.set(0)
    var23.set(1)
    var24.set(0)
    var25.set(0)
    var26.set(0)
    var29.set(0)

var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()
var4 = tk.IntVar()
var5 = tk.IntVar()
var6 = tk.IntVar()
var7 = tk.IntVar()
var8 = tk.IntVar()
var9 = tk.IntVar()
var10 = tk.IntVar()
var11 = tk.IntVar()
var12 = tk.IntVar()
var13 = tk.IntVar()
var14 = tk.IntVar()
var15 = tk.IntVar()
var16 = tk.IntVar()
var17 = tk.IntVar()
var18 = tk.IntVar()
var19 = tk.IntVar()
var20 = tk.IntVar()
var21 = tk.IntVar()
var22 = tk.IntVar()
var23 = tk.IntVar()
var24 = tk.IntVar()
var25 = tk.IntVar()
var26 = tk.IntVar()
var27 = tk.IntVar()
var28 = tk.IntVar()
var29 = tk.IntVar()
var30 = tk.IntVar()

Button_Font = font.Font(family='Helvetica', size=12, weight='bold')
button_1 = Button(bottomframe, text = "Run Program", command = runProgram)
button_1['font']= Button_Font

button_2 = Button(leftframe, text = "Observed Fragments", command = Fragments)
button_3 = Button(leftframe, text = "Unlocalized Modifications", command = Modifications)
button_4 = Button(leftframe, text = "Localized Modifications", command = Known_Modifications)
check_box_28 = tk.Checkbutton(leftframe,text = 'No Unlocalized Modifications', variable = var28, onvalue = 1, command = No_Variable_Modifications)
check_box_30 = tk.Checkbutton(leftframe,text = 'No Localized Modifications', variable = var30, onvalue = 1, command = No_Known_Modifications)
check_box_1= tk.Checkbutton(leftframe, text = 'Acetylation', variable = var1, onvalue = 1, command = Uncheck_boxes_1)
check_box_2= tk.Checkbutton(leftframe, text = 'Deamination', variable = var2, onvalue = 1, command = Uncheck_boxes_2)
check_box_3= tk.Checkbutton(leftframe, text = 'Methylation', variable = var3, onvalue = 1, command = Uncheck_boxes_3)
check_box_4= tk.Checkbutton(leftframe, text = 'Dimethylation', variable = var4, onvalue = 1, command = Uncheck_boxes_4)
check_box_5= tk.Checkbutton(leftframe, text = 'Formylation', variable = var5, onvalue = 1, command = Uncheck_boxes_5)
check_box_6= tk.Checkbutton(leftframe, text = 'Amidation', variable = var6, onvalue = 1, command = Uncheck_boxes_6)
check_box_7= tk.Checkbutton(leftframe, text = 'Methylation', variable = var7, onvalue = 1, command = Uncheck_boxes_7)
check_box_8= tk.Checkbutton(leftframe, text = 'Dehydration', variable = var8, onvalue = 1, command = Uncheck_boxes_8)

check_box_24=tk.Checkbutton(rightframe,text = 'CAD/SID/HCD/IRMPD', variable = var24, onvalue = 1, command = Uncheck_boxes_9)
check_box_25=tk.Checkbutton(rightframe,text = 'ECD/ETD', variable = var25, onvalue = 1, command = Uncheck_boxes_10)
check_box_27=tk.Checkbutton(rightframe,text = 'EID', variable = var27, onvalue = 1, command = Uncheck_boxes_12)
check_box_26=tk.Checkbutton(rightframe,text = 'UVPD', variable = var26, onvalue = 1, command = Uncheck_boxes_11)

check_box_9= tk.Checkbutton(rightframe,text = 'A Fragments', variable = var9, onvalue = 1)
check_box_10= tk.Checkbutton(rightframe,text = 'B Fragments', variable = var10, onvalue = 1)
check_box_11= tk.Checkbutton(rightframe,text = 'C Fragments', variable = var11, onvalue = 1)
check_box_12= tk.Checkbutton(rightframe,text = 'X Fragments', variable = var12, onvalue = 1)
check_box_13= tk.Checkbutton(rightframe,text = 'Y Fragments', variable = var13, onvalue = 1)
check_box_14= tk.Checkbutton(rightframe,text = 'Z Fragments', variable = var14, onvalue = 1)
check_box_15= tk.Checkbutton(rightframe,text = 'AX fragments', variable = var15, onvalue = 1)
check_box_16= tk.Checkbutton(rightframe,text = 'AY Fragments', variable = var16, onvalue = 1)
check_box_17= tk.Checkbutton(rightframe,text = 'AZ Fragments', variable = var17, onvalue = 1)
check_box_18= tk.Checkbutton(rightframe,text = 'BX Fragments', variable = var18, onvalue = 1)
check_box_19= tk.Checkbutton(rightframe,text = 'BY Fragments', variable = var19, onvalue = 1)
check_box_20= tk.Checkbutton(rightframe,text = 'BZ Fragments', variable = var20, onvalue = 1)
check_box_21= tk.Checkbutton(rightframe,text = 'CX Fragments', variable = var21, onvalue = 1)
check_box_22= tk.Checkbutton(rightframe,text = 'CY Fragments', variable = var22, onvalue = 1)
check_box_23= tk.Checkbutton(rightframe,text = 'CZ Fragments', variable = var23, onvalue = 1)

check_box_29 = tk.Checkbutton(rightframe, text = 'Do not include C, Z, and CZ fragments that cut at proline', variable = var29, onvalue = 1)

Name_of_Program.pack()
Name_of_Institution.pack()
label_photo.pack()
button_1.pack()
Label1.pack()
canvas1.pack()
Label_Space_1.pack()
Label2.pack()
canvas2.pack()
Label_Space_2.pack()
Label11.pack()
canvas5.pack()
Label_Space_3.pack()
button_2.pack()
canvas3.pack()
check_box_30.pack()
button_4.pack()
canvas6.pack()
check_box_28.pack()
button_3.pack()
canvas4.pack()
Label3.pack()
check_box_1.pack()
check_box_2.pack()
check_box_3.pack()
check_box_4.pack()
check_box_5.pack()
Label_Space_5.pack()
Label4.pack()
check_box_6.pack()
check_box_7.pack()
check_box_8.pack()
Label9.pack()
check_box_24.pack()
check_box_25.pack()
check_box_27.pack()
check_box_26.pack()
Label_Space_4.pack()
Label7.pack()
check_box_9.pack()
check_box_10.pack()
check_box_11.pack()
check_box_12.pack()
check_box_13.pack()
check_box_14.pack()
check_box_15.pack()
check_box_16.pack()
check_box_17.pack()
check_box_18.pack()
check_box_19.pack()
check_box_20.pack()
check_box_21.pack()
check_box_22.pack()
check_box_23.pack()
check_box_29.pack()
Disclaimer.pack()
root.mainloop()
