# Comprehensive Localization of Internal Protein Sequences (ClipsMS)
Software that can analyze terminal and internal fragments resulting from top-down mass spectrometry data.

Installation Instructions:
1. Download the zip file from github. (This can be found under "Code" on the top right)
2. Go to your downloads file and extract the files
3. Place the unzipped file where it will be easy to find.
4. Download and install Anaconda.
  4a.	Open file and begin installation. 
  4b.	We recommend installing for all users.
  4c.	Install in the "ProgramData" folder.
  4d.	If this is your first time installing python and anaconda click both boxes in the "advanced installation options" dialog box.
  4e.	Install the software. 
  4f.	Once installed click next.
  4g.	Go through all the other options, click finish. 
5. Once anaconda is downloaded and installed search for “anaconda prompt” on your computer.
6. Type “start spyder” to start Spyder software
7. Make sure that Spyder is running at least python 3.7.
8. On the top right side of the software, open the unzipped folder that contains all the .csv and .py files from the zip file.
9. On the bottom of the top right panel click "Files." (This should have all the files in the unzipped folder.)
10. Open the setup.py file and run the script. (This will download all the packages need to run the script and print each package as it is being downloaded.)
11. The program should be ready to run. Open the Test_GUI.py file and run it. (Green Arrow at the top of Spyder)


Program instructions:
1. Run the Test_GUI.py file. 
2. Insert user parameters into the GUI that appears.
a.	PPM error indicates the maximum PPM error allowed to match a fragment. (We recommended a PPM error of less than 2 to reduce false positives when searching for internal fragments)
b.	Insert the protein sequence you want to compare the fragments against in the sequence box. (Make sure there are no spaces or commas between the letters or at the ends of the sequence and that all characters are standard one letter amino acid codes.)
c.	Insert a number for the smallest internal fragment size. (We recommend 5 amino acids for most proteins.)
d.	Click "Observed Fragments" and upload a .csv file with the deconvoluted masses ([M+H]+ format) in one column and the intensities in the second column. (If the intensity is not known, insert "1" for all intensity values)
e.	To insert fixed modifications, upload a .csv file by clicking the "Fixed Modifications" tab. The .csv file should have 3 columns including name of the modification in the first column, the monoisotopic molecular weight in the second column, and the amino acid number that contains the modifications and the third column.
f.	To insert variable modifications, upload a .csv file by clicking the "Variable Modifications" tab. The .csv file should have 3 columns including the name of the modification in the first column, the monoisotopic molecular weight in the second column, and the one letter amino acid codes that the modification ascribes to in the third column, if any. If the modification does not ascribe to any specific amino acid write "None" in the third column.
g.	Choose a terminal modification if you expect one on your sequence. If a terminal modification exists on the protein but does not show up in the list treat it as a known modification and place it on the first/last amino acid. 
h.	Select the fragmentation technique used for the TD-MS experiment. This will preselect certain fragment types that are expected for that technique.
i.	If you would like to search for specific fragment types they can be checked/unchecked under "Search Fragment Type".
j.	If you are searching for fragments that contain c or z cleavages, you can exclude cleavages that occur at proline residues by checking the last box. 
3. Once all parameters have been input, click "Run Program".
4. If you are looking for both internal and terminal fragments, a dialog box will ask if you want to bias for terminal fragments. Click "Yes" if you want to bias for terminal fragments or "No" if you want to treat terminal fragments and internal fragments equally likely.
5. Depending on the sequence length, the number of observed fragments, and the types of fragments searched, the program could run from ~5s to ~1hour. A progress bar should show in the Spyder software indicating the progress of ClipsMS.
6. Once completed, a "Matched_Fragments_Final.csv" file should appear in the "ClipsMS-main" folder with all matched fragments.
7. In addition, three figures indicating the sequence coverage, the cleavage sites, and the fragment location should be output in the "ClipsMS-main" folder.
If you have any questions or concerns email: internalfragments.loolab@gmail.com
