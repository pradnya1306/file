banks_list = ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]
myfile=open("file_question3.txt","w")
for i in banks_list:
    myfile.write(i+"\n")


myfile.close()