import sqlite3

#Process Queries And Display the output
#Query 1:
def view():
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM Movies") #Select all item from Movies table
    rows = cur.fetchall() #Fetches all rows from Movie table and store it in rows object
    conn.commit()
    conn.close()
    return rows
    
#Query 2:
def view1():
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    #Select movie name, actor and actress from Movie table Order it by actor name
    cur.execute("SELECT movie,actor,actress FROM Movies  ORDER BY actor")  
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def view2():
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    #Select movie name, actor and actress from Movie table Order it by actor name
    cur.execute("SELECT * FROM Movies  WHERE actor= 'Allu Arjun' ")  
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

#Display the output for Quries
print()
print("Query 1: Query to display all rows from Movie table: \n")
print(view())
print("\n Query 2: Query to display movie, actor & actress based on actor from Movie table\n ")
print(view1())
print()
print(view2())