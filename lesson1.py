#importing sqlite3
import sqlite3
print('sqlite imported')
#connect to data base
conn = sqlite3.connect('students.db')
print('database successfull')
#create cursor
c = conn.cursor()
print('cursor successfull')
#1a CREATING INVENTORY TABLE
# c.execute("""
#           CREATE TABLE inventory(
#               id int,
#               items text,
#               prices int,
#               quantity text
#             )
#         """)
print('inventory table successfull')
#1b ADDING VALUES TO INVENTORY TABLE
inventory_list = [('01', 'Note_book', '#500', '2Cartons'),
                 ('02', 'Textbook', '#300', '1Carton'),
                 ('03', 'Dictionary', '#150', '3Cartons'),
                 ('04', 'Pencil', '#100', '8Cartons'),
                 ('05', 'Novel', '#450', '5Cartons'),
                 ('06', 'Diary', '#600', '1Carton'),
                 ('07', 'Journal', '#550', '8Cartons'),
                 ('08', 'Register', '#300', '4Cartons'),
                 ('09', 'Plain_sheet', '#110', '8Cartons'),
                 ('10', 'Jotter', '#250', '8Cartons')
                 ]
#insert multiple rows into table
c.executemany('INSERT INTO inventory VALUES( ?,?,?,? )', inventory_list)
print('have inserted', c.rowcount, 'records to table inventory.')

#c.execute("SELECT * FROM inventory")

# item = c.fetchall()
# print('id' + '\titems' + '\t\tprices'  + '\t\tquantity')
# print('..' + '\t....' + '\t\t.....'  + '\t\t........')

# #formatting through

# for item in item:
#     print(item)
# id, items, prices, quantity = item
# print(f"{id:6}{items:18}{prices:16}{quantity:16}")

#2a QUERYING TO FIND ITEMS TO RESTOCK
c.execute("""
          SELECT * FROM inventory WHERE quantity = '1Carton'
        """)
item = c.fetchall()
print(f" ITEMS TO RESTOCK\n{'-' * 100}")


for item in item:
    print(item)
 

#2b QUERYING SUFFICIENT ITEMS FROM HIGHEST TO LOWEST COST PRICE
c.execute("""
          SELECT * FROM inventory 
          WHERE QUANTITY > '1Carton'
         ORDER BY quantity DESC;
         """)

item = c.fetchall()
print(f" SUFFICIENT ITEMS IN DESCENDING ORDER\n{'-' * 100}")

for item in item:
    print(item)
  
  
