#importing sqlite3
import sqlite3
print('sqlite imported')
import csv
print('csv successful')
#connect to data base
conn = sqlite3.connect('students.db')
print('database successfull')
#create cursor
c=conn.cursor()
print('cursor created successfully')
#creating table
# create_table = """
# CREATE TABLE waec_students(
#      name text,
#      maths int,
#      english int,
#      biology int,
#      CRS text int,
#      physics int,
#      chemistry int,
#      geography int, 
#      economics int,
#      literature int
# )
# """
#c.execute(create_table)

print('table created successfully')

#LOADING EXISTING CSV FILE
with open('waec_students.csv', 'r') as opened_file:
    read_file = csv.reader(opened_file)
    
    c.executemany("""
                  INSERT INTO waec_students VALUES(?,?,?,?,?,?,?,?,?,?)
                  """ , read_file)

print('students data successfully loaded into table waec students')  

 #QUERYING TABLE CREATED
query = c.execute("SELECT * FROM waec_students")
rows = c.fetchall()

print(f" WAEC STUDENTS\n{'-' * 100}")
for row in rows:
    name, maths, english,biology,crs,physics,chemistry,geography,economics,literature = row
    print(f"{name:18}{maths:8}{english:10}{biology:10}{crs:8}{physics:10}{chemistry:10}{geography:10}{economics:10}{literature:10}")

# 1 FOR HIGHEST IN MATHS

def highest_in_maths():
    query1 = """SELECT name, MAX(maths) 
    FROM waec_students;
    """ 
    print(f" HIGHEST IN MATHS \n{'-' * 100}")
    c.execute(query1)
    items = c.fetchmany()
    for items in items:
     print(items) 
highest_in_maths()

#2LOWEST IN ENGLISH
def lowest_in_english():
    query2 = """SELECT name, MIN(english) 
    FROM waec_students;"""
    print(f" LOWEST IN ENGLISH\n{'-' * 100}")
    c.execute(query2)
    items = c.fetchall()
    print(items)  
lowest_in_english()
    
#3 AVERAGE SCORE IN MATHS
def AVG_maths():
    query3 = """
    SELECT AVG(maths) 
    FROM waec_students;
    """
    print(f" AVERAGE SCORE IN MATHS\n{'-' * 100}")
    c.execute(query3)
    items = c.fetchmany(19)
    print(items)
AVG_maths()
#4 AVERAGE SCORE IN ENGLISH
def AVG_english():
    query4 = """
    SELECT AVG(english) 
    FROM waec_students;
    """
    print(f" AVERAGE SCORE IN ENGLISH\n{'-' * 100}")
    c.execute(query4)
    items = c.fetchmany(19)
    print(items)
AVG_english()
#5 BEST PERFORMING STUDENT SCROSS ALL 9 SUBJECTS
def best_performing():
    query5 = """
    SELECT name, MAX(maths+english+biology+crs+physics+chemistry+geography+economics+literature)
    AS total
    FROM waec_students
    ORDER BY total DESC
    LIMIT 1""" 
    
    print(f" BEST PERFORMING ACROSS 9 SUBJECTS\n{'-' * 100}")
    c.execute(query5)
    items = c.fetchmany(19)
    print(items)
best_performing()
#6BEST AVERAGE ACROSS ALL 9 SUBJECTS
def best_average():
    query6 = """
    SELECT AVG(maths+english+biology+crs+physics+chemistry+geography+economics+literature)
    AS total
    FROM waec_students
    """ 
    
    print(f" BEST AVERAGE ACROSS 9 SUBJECTS\n{'-' * 100}")
    c.execute(query6)
    items = c.fetchmany(19)
    print(items)
best_average()


 

  


