import sqlite3
connection = sqlite3.connect("students_db.db")
cursor = connection.cursor()


def create_table():

    query = """ 
            create table IF NOT EXISTS students(
                id integer primary key,
                name text,
                department text ,
                total_marks integer check(total_marks between 0 and 100)
            )
            """

    cursor.execute(query)
    print("Table is created !!! ")



def add_students(id,name,department,total_marks):
    query = """ 
            insert into students(id,name,department,total_marks)
            values(?,?,?,?)
            """
    cursor.execute(query,(id,name,department,total_marks))
    connection.commit()
    print("Data has been added !!!")

def display_data():
    query = """
            select * from students
            """
    datas = cursor.execute(query)
    for data in datas:
        print(data)

def delete_data(student_id):
    q = """delete from students where id = ?"""
    cursor.execute(q,(student_id,))
    connection.commit()
    print("Data has been deleted")

def delete_data(student_name,student_id):
    q = """update students set name = ? where id = ?"""
    cursor.execute(q,(student_name,student_id))
    print("Updated")
    connection.commit()

create_table()
# add_students('13','WANDEL SHOW','CSE',90)
display_data()
delete_data("ISHIKA YADAV",12)
