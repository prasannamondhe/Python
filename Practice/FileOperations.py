import os
#Way to specify path in python
#print(os.path.join('home','prasanna','PythonRepo','Python','Game'))

#Open CSV file => remove comma => write data into another CSV file
# with open('Practice/insurance.csv') as infile, open('Practice/insuranceWithoutComma.csv','w') as outfile:
#     for line in infile:
#         outfile.write(line.replace(","," "))


# readTarget = open('Practice/insuranceWithoutComma.csv')
# print(readTarget.read())

# #Open CSV file => remove comma => write data into PDF file
# with open('Practice/insurance.csv') as infile, open('Practice/target.pdf','w') as outfile:
#     for line in infile:
#         outfile.write(line.replace(","," "))

# readTarget = open('Practice/target.pdf')
# print(readTarget.read())

#Open CSV and write details of itnto text file
with open('Practice/insurance.csv') as infile, open('Practice/hello.txt','w') as outfile:
    for line in infile:
        outfile.write(line.replace(","," "))

readTarget = open('Practice/hello.txt')
print(readTarget.read())

