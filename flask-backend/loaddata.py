def executeQuery(Query):
    import collections
    import mysql.connector
    import json
    conn = mysql.connector.connect(user='root', password='hacker', database='chatbot')
    cursor = conn.cursor()
    cursor.execute(Query)
    data = cursor.fetchall()
    
    print (data)
    #render_template('template.html', data=data)
    
    return data;

def loadData(): 
    return executeQuery("""SELECT * FROM members""")

def retriveDistinctNames():
    return executeQuery("""SELECT DISTINCT name from members""")

def filter(name):
    return executeQuery("""SELECT * from members where name='"""+name+"""'""");

if __name__ == "__main__":
    loadData()

