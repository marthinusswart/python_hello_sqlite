import sqlite3
from person import Person

def init_table(cur):
    cur.execute("""CREATE TABLE person (
            first text,
            last text         
            )""")

    per1 = Person("John", "Doe")
    print (per1.fullname)

    insert_person(per1)
    return 0


def insert_person(per):
    with conn:
        try:
            c.execute("INSERT INTO person VALUES (:first, :last)", {'first': per.first, 'last': per.last})
        except ValueError:
            print ("Error")


def get_person_by_name(lastname):
    try:
        c.execute("SELECT * FROM person WHERE last=:last", {'last': lastname})
        return c.fetchall()
    except sqlite3.OperationalError as err:
        print ("error {0}".format(err))
        return []

def remove_person(per):
    with conn:
        c.execute("DELETE from person WHERE first = :first AND last = :last",
                  {'first': per.first, 'last': per.last})

conn = sqlite3.connect('person.db')
c = conn.cursor()

#Check if the table exists with the default person or not
plist =  get_person_by_name("Doe")

if len (plist) == 0:    
    print ("count is 0, going to init the table")
    init_table(c)
else:
    print ("count {0}".format(str(len(plist))))
    for p in plist:
        person = Person(p[0], p[1])
        print (person.fullname)    
        print (person.email)   
#All good moving on

conn.close()
