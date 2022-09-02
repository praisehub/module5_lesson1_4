#importing sqlite3
import sqlite3
print('sqlite imported')
#connect to data base
conn = sqlite3.connect('students.db')
print('database successfull')
#create cursor
c = conn.cursor()
print('cursor successfull')
#CREATING INVENTORY TABLE
# c.execute("""
#           CREATE TABLE inventory(
#               id int,
#               items text,
#               prices int,
#               quantity text
#             )
#         """)
# print('inventory table successfull')
#ADDING VALUES TO INVENTORY TABLE
inventory_list = [('01', 'Note_book', '500', '20'),
                 ('02', 'Textbook', '900', '70'),
                 ('03', 'Dictionary', '150', '30'),
                 ('04', 'Pencil', '100', '80'),
                 ('05', 'Novel', '450', '55'),
                 ('06', 'Diary', '600', '43'),
                 ('07', 'Journal', '550', '89'),
                 ('08', 'Register', '300', '48'),
                 ('09', 'Plain_sheet', '110', '88'),
                 ('10', 'Jotter', '250', '90')
                 ]
#insert multiple rows into table
c.executemany('INSERT INTO inventory VALUES( ?,?,?,? )', inventory_list)
print('have inserted', c.rowcount, 'records to table inventory.')

#c.execute = ("SELECT * FROM inventory")
#1 AMOUNT INVESTED IN PROCUMENT OF ITEMS
def procurement_amount():
    query = """
    SELECT SUM(prices)
    FROM inventory;
    """
    print(f" AMOUNT INVESTED IN PROCUMENT OF ITEMS\n{'-' * 100}")
    c.execute(query)
    rows = c.fetchall()
    print(rows)
procurement_amount()
#2 AVERAGE QUANTITY OF ITEMS IN STOCK
def AVG_quantity():
    query2 = """
    SELECT AVG(quantity) 
    FROM inventory;
    """
    print(f" AVERAGE QUANTITY OF ITEMS IN STOCK\n{'-' * 100}")
    c.execute(query2)
    items = c.fetchmany(10)
    print(items)
AVG_quantity()
     
#3 ITEM WITH THE LEAST QUANTITY IN STOCK
def least_quantity():
    query3 = """
    SELECT MIN(quantity)
    FROM inventory
    """
    print(f" LEAST QUANTITY IN STOCK\n{'-' * 100}")
    c.execute(query3)
    items = c.fetchall()
    print(items)
least_quantity()
    
#4 ITEM WITH THE MOST QUANTITY IN STOCK
def most_quantity():
    query4 = """
    SELECT MAX(quantity)
    FROM inventory
    """
    print(f" MOST QUANTITY IN STOCK\n{'-' * 100}")
    c.execute(query4)
    items = c.fetchall()
    print(items)
most_quantity()
    