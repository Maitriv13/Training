import mysql.connector
from mysqlx import Column
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='db1',
                                         user='root',
                                         password='')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
        
    val=()
    while True:
        print("Login")
        print("Signup")
        n=input("Choose[login/signup]: ")
        if (n.lower()=='signup'):
            user=input("Enter Firstname: ")
            user1=input("Enter Lastname: ")
            user2=input("Enter Email: ")
            user3=input("Enter Contactno: ")
            user4=input("Enter Username: ")
            user5=input("Enter Password: ")
            sql = "INSERT INTO userdata (fname, lname, email, contactno, username, password) VALUES (%s, %s, %s, %s, %s, %s)"
            val=(user,user1,user2,user3,user4,user5)
            cursor.execute(sql, val)
            connection.commit()
            print(cursor.rowcount, "details inserted")
            print("Account created successfully!!")
        elif n=='q':
            break
        elif n.lower()=='login' :
            user6=input("Enter Username/Email/Contactno: ")
            user7=input("Enter Password: ")
            if (user6=="Admin" and user7=="2341"):
                n1=input("choose to edit/delete: ")
                if n1=='edit':
                    n2=input("enter username to edit user details: ")
                    query1= f"select * from userdata where username='{n2}'"
                    sql_select_query = (query1)
                    cursor.execute(sql_select_query)
                    row = cursor.fetchone()   
                    if row:
                        edit=input("enter which field to edit: ").lower()
                        new=input(f"enter new {edit}: ")
                        query2=f"update userdata set {edit}='{new}' where username='{n2}'"
                        sql_update_query = (query2)
                        cursor.execute(sql_update_query)
                        connection.commit()
                        
                    else:
                        print("username does not exist!!")
                        continue

                else :
                    n3=input("Enter username to delete record: ")
                    query3=f"DELETE FROM userdata WHERE username='{n3}'"
                    sql_delete_query = (query3)
                    cursor.execute(sql_delete_query)
                    connection.commit()

            else:
                query= f"select * from userdata where email='{user6}' or contactno='{user6}' or username='{user6}' and password='{user7}'"
                sql_select_Query = (query)
                cursor.execute(sql_select_Query)
                mrow = cursor.fetchone()
                if mrow :
                    print("logged in successfully")
                else:
                    print("invalid")

        else :
            print("Invalid input")
except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

