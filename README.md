# INTRODUCTION
This model is used to identify ATP interacting residues in a ATP binding protiens in order to understand protien-ligands interaction.

# Input
Input is taken from a text file by using python inbuilt function open and readline. Input file name should be "train.txt" and should be in the same folder. File name for testing data should be "test1.txt".
1) train.txt - It consist of training data. First row contains headings namely Protien_ID and amino acid sequence. Subsequent rows contains the id and the sequence.
2) test1.txt - It consist of testing data. Each row consists of ID and label separated by a comma.

# Output
Output is in the form of a csv file. It includes the predictions with label along with the answer (+1 or -1). Output file name is "ans.csv". +1 is for ATP interacting residues and -1 for ATP non-interacting residues.

# How to run
First make sure imblearn module is installed in the system. If not then install it by running "pip3 install imblearn". After that run "python3 main.py".

# What was done
"xxx" was added to starting and ending of the sequence and then for each character we picked a subsequence of length 7 with that character as the mid element. A matrix was created of size 21*7 for each character and then that data was trained. Similary we created a matrix for testing data and output was predicted.