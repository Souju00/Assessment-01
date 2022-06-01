#import sqlite3 module
import sqlite3


#Create Table 
conn = sqlite3.connect("database.db")  #Connecting to sqlite3 creating database named database.db
cur  = conn.cursor() #creating cursor object using cursor method() 
#Create new table if it does not exist 
cur.execute("CREATE TABLE IF NOT EXISTS Movies (movie VARCHAR(40), actor VARCHAR(30), actress VARCHAR(30), year_of_release INTEGER, director VARCHAR(30))")
conn.commit() #Commiting or reverting changes made to database
conn.close() #Closing the connection
    
print("Table Created.")

#Inserting items or data to database table Movies
def insert(movie, actor,actress,year_of_release,director):
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO Movies VALUES (?,?,?,?,?)", (movie, actor,actress,year_of_release,director))
    conn.commit()
    conn.close()
  
#Inserting data values 
insert('Race Gurram', 'Allu Arjun', 'Samantha', 2014, 'Sureder Reddy')
insert('Jathi Ratnalu', 'Naveen', 'Faria', 2021, 'Anudeep K V')
insert('K G F', 'Yash', 'Srinidhi shetty', 2022, 'Prashanth Neel')
insert('Andhadhun', 'Ayushmann Khurana', 'Radhika', 2018, 'Sriram Raghavan')
insert('Ala Vaikunthapurramuloo', 'Allu Arjun', 'Pooja Hegde', 2019, 'Trivikram Srinivas')
insert('777 Charlie', 'Rakshith Shetty', 'Sangeetha', 2022, 'Kiranraj')
insert('Love Mocktail2', 'Darling Krishna', 'Milana Nagraj', 2022, 'Darling Krishna')
insert('Radhe Shyam', 'Prabhas', 'Pooja Hegde', 2022, 'Radha Krishna Kumar')
insert('Bahubali', 'Prabhas', 'Anushka Shetty', 2015, 'Rajmouli')
insert('Love Mocktail', 'Darling Krishna', 'Milana Nagraj', 2020, 'Darling Krishna')

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
    cur.execute("SELECT * FROM Movies  wHERE actor='Allu Arjun' ")  
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
