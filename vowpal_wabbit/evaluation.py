import csv
import sklearn
from sklearn.metrics import classification_report

actualFile = open('cleaned-Validation-2.csv', 'r')
csvreader = csv.reader(actualFile)

header = []
header = next(csvreader)

rows = []
y_true = []

for row in csvreader:
    label = int(row[1])
    y_true.append(label)
    rows.append(row)

predictionFile = open('prediction2.txt','r')

y_pred = predictionFile.readlines()
for i in range(len(y_pred)):
    y_pred[i] = int(y_pred[i])
print(type(y_pred[0]))

report = classification_report(y_true, y_pred)
print(report)