Software that can analyze terminal and internal fragments in top-down mass spectrometry data.
Installation Instructions:
1.	Make sure that your device is running at least python 3.7.
2.	Click on “Releases” on GitHub on the right side of your window.
3.	Go to your downloads folder and extract the files.
4.	Place the unzipped file where it will be easy to find.
5.	Double click the ClipsMS_2.0.1.exe file in the unzipped folder to run the program.
Program instructions:
1.	Run the ClipsMS_2.0.1.exe file.
2.	Insert user parameters into the GUI that appears. 
A. Insert a PPM error tolerance value for terminal and internal fragments. (We recommended a PPM error of less than 2 to reduce false positives when searching for internal fragments)
B. Insert the protein sequence you want to compare the fragments against in the sequence box.
C. Insert a number for the smallest internal fragment size. (We recommend 5 amino acids for most proteins.) 
D. Click "Observed Fragments" and upload a .csv file with the deconvoluted masses ([M+H]+ format) in column 1 and the intensities in column 2. (If the intensity is not known, insert "1" for all intensity values) 
E. Choose a terminal modification if you expect one on your protein. If a terminal modification exists on the protein but does not show up in the list, treat it as a localized modification and place it on the first/last amino acid. 
F. To insert localized modifications, upload a .csv file by clicking the "Localized Modifications" tab. The .csv file should have 4 columns including name of the modification in column 1, the monoisotopic molecular weight in column 2, the amino acid number that contains the modifications in column 3, and a color in the column 4 (all lower case and no spaces). For an example of the format, open the No_Localized_Modificaitons.csv file.
G. To insert unlocalized modifications, upload a .csv file by clicking the "Unlocalized Modifications" tab. The .csv file should have 12 columns. For an example of the format, open the No_Unlocalized_Modificaitons.csv file.
i. Column 1 should contain the name of the modification and column 2 should contain the monoisotopic molecular weight of the modification. 
ii. To limit modification assignment to fragments containing specific amino acid(s), insert the one letter amino acid code(s) the modification ascribes to column 3 and the number of amino acids the fragment must contain to column 4. If not applicable, write “None” in column 3 and “0” in column 4.
iii. To limit the modification to contain part of a region of the protein, insert the number of the amino acid that is closest to the N-terminus in column 5 and the number of the amino acid closest to the C-terminus in column 6. If not applicable, write “0” in column 5 and “0” in column 6. 
iv. To limit the modification to contain an entire region, insert the number of the amino acid that is closest to the N-terminus in column 7 and the number of the amino acid closest to the C-terminus in column 8. If not applicable, write “0” in column 7 and “0” in column 8. 
v. To apply a link to two amino acids in the same protein chain, insert a name for the link in column 9, the number of the amino acid that is closest to the N-terminus in column 10, and the number of the amino acid closest to the C-terminus in column 11. If not applicable, write “None” in column 9, “0” in column 10, and “0” in column 11.
vi. Lastly, write a color that represents the modification in column 12 (all lower case and no spaces).
H. Select the fragmentation technique used for the TD-MS experiment. This will preselect certain fragment types that are expected for that technique. 
I. If you would like to include/exclude certain fragment types they can be checked/unchecked under "Search Fragment Type". 
J. If you are searching for fragments that contain c or z cleavages, you can exclude cleavages that occur at proline residues by checking the last box.
3.	Once all parameters have been input, click "Run Program".
4.	If you are looking for both internal and terminal fragments, a dialog box will ask if you want to bias for terminal fragments. Click "Yes" if you want to bias for terminal fragments or "No" if you want to treat terminal fragments and internal fragments equally likely.
5.	Depending on the sequence length, the number of observed fragments, and the types of fragments searched, the program could run from ~5s to ~1hour. A progress bar should appear in the dialog box indicating the progress of ClipsMS.
6.	Once completed, a "Matched_Fragments_Final.csv" file should appear in the "ClipsMS_2.0.0" folder with all matched fragments.
7.	In addition, three figures should automatically pop up indicating the sequence coverage, the cleavage sites, and the fragment location. 
8.	If you have any questions email: internalfragments.loolab@gmail.com
