import pandas as pd
import csv
#from pandas import read_csv
#print(contact)
# rows=[['Name', 'Surname', 'contact'], ['Jay', 'Shah', '1234'], ['Amit', 'hhjb', '2341'], ['Maitri', 'Varia', '4567'], ['Devesh', 'patel', '61926']]
# file = open('Condetail.csv','a+')
# csvwriter = csv.writer(file)
# csvwriter.writerows(rows)
# file.close()
#contact = pd.read('D:\Internship\Contacts\Condetail.csv') 
def contdata():
    a=input("Select what to do 1)Show all contacts  2)Edit Contact 3)Search contact: ")
    if a=='1':
        file = open('Condetail.csv','r')
        reader_obj = list(csv.reader(file))
        for row in reader_obj:
            print(f'{row[0]} \t\t {row[1]} \t\t {row[2]}')
        file.close()
    elif a=='2':
        b=input("1)Insert 2)Edit")
        if b=='1': 
            file = open('Condetail.csv','a+')
            csvwriter = csv.writer(file)
            print("Entering data for contacts: ")
            fname=input("Enter First name: ")
            lname=input("Enter last name: ")
            no=input("Enter Phone number: ")
            rows=[fname,lname,no]
            csvwriter.writerow(rows)
            print("Contat addedd successfully")
            file.close()
        elif b=='2':
            print("Editing contact..")
            file = open('Condetail.csv','r')
            reader_obj = list(csv.reader(file))
            edit=input("Enter name of contact to edit: ")
            file.close()
            flag=0
            for row in reader_obj:
                # print(row)
                if row is None:
                    pass
                else:
                    if row[0]==edit:
                        flag=1
                        e=input("What to edit a)fname b)lname )contactno: ")
                        if e=='a':
                            n1=input("Enter new fname: ")
                            row[0]=n1
                        elif e=='b':
                            n2=input("Enter new lname: ")
                            row[1]=n2
                        elif e=='c':
                            n3=input("Enter new contactno: ")
                            row[2]=n3
                        else:
                            print("option not availaible!!")
            if flag==0:
                print("Contact not found!")
            else:
                # print(reader_obj)
                file = open('Condetail.csv','w',newline='')
                csvwriter = csv.writer(file)
                csvwriter.writerows(reader_obj)
                # file.close()
                file.close()
                
        else:
            print("invalid input!!") 
    elif a=='3':
        c=input("Enter fname/Contact no to serach: ")
        file = open('Condetail.csv','r')
        reader_obj = list(csv.reader(file))
        for row in reader_obj:
            if row[0]==c or row[2]==c:        
                print(f"The details of {c} are \n fname: {row[0]} \n lname: {row[1]} \n contactno: {row[2]} ")
    else:
        print("invalid input!!") 
contdata()