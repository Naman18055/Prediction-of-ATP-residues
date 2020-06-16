import csv
import numpy as np
from pyteomics import mass
from sklearn import svm
from imblearn.ensemble import BalancedBaggingClassifier
import sys

rows=[]
file = open("train.txt","r")
reader = file.readline()
reader = file.readline()
while reader:
	rows.append(reader)
	reader = file.readline()

sequences=[]
for i in rows:
	sequences.append("xxx"+i[i.index(",")+1:-1]+"xxx")

X=[]
Y=[]
amino = {"A":0,"R":1,"N":2,"D":3,"C":4,"Q":5,"E":6,"G":7,"H":8,"I":9,"L":10,"K":11,"M":12,"F":13,"P":14,"S":15,"T":16,"W":17,"Y":18,"V":19,"X":20}
for i in sequences:
	for j in range(3,len(i)-3):
		matrix = [[0 for k in range(7)] for l in range(21)]
		seq = i[j-3:j+4]
		for k in range(21):
			for char in range(7):
				if k==amino[seq[char].upper()]:
					matrix[k][char]=1
		x=[]
		for k in matrix:
			x.extend(k)
		X.append(x)
		if ord(i[j])>=97:
			Y.append(1)
		else:
			Y.append(-1)

print ("Arrays Created")
X=np.array(X)
Y=np.array(Y)

print ("Training Data ...")

bbc = BalancedBaggingClassifier(random_state=42)
bbc.fit(X,Y)

print ("Data Trained")
print ("Creating Testing Arrays ...")

rows=[]
file = open("test1.txt","r")
reader = file.readline()
reader = file.readline()
while reader:
	rows.append(reader)
	reader = file.readline()

sequence="xxx"
labels=[]
for i in rows:
	sequence+=i[-2]
	labels.append(i[0:-2])
sequence+="xxx"

ans=[]
count=0
for i in range(3,len(sequence)-3):
	matrix = [[0 for j in range(7)] for k in range(21)]
	seq = sequence[i-3:i+4]
	for k in range(21):
		for char in range(7):
			if k==amino[seq[char].upper()]:
				matrix[k][char]=1
	y=[]
	for k in matrix:
		y.extend(k)
	pred = bbc.predict([y])
	if pred==1:
		ans.append("+1")
	else:
		ans.append("-1")
	if ans[-1]=="+1":
		count+=1

with open('ans.csv', 'w', newline='') as file:
	writer = csv.writer(file)
	writer.writerow(["ID","Lable"])
	for i in range(len(ans)):
		w = [labels[i][0:-1],ans[i]]
		writer.writerow(w)

print ("Answer Predicted")
print ("Number of Ones - ")
print (count)

