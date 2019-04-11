import sqlite3
import math

conn = sqlite3.connect('datakata_new.db')
c = conn.cursor()
b = conn.cursor()
b.execute("SELECT DISTINCT artikel FROM data")

data=[]
for a in b.fetchall():
    print(a[0])
    c.execute("SELECT DISTINCT kata,jumlah FROM data WHERE artikel="+str(a[0]))
    
    data_artikel=[]
    for i in c.fetchall():
        b.execute("SELECT DISTINCT artikel FROM data WHERE kata='"+i[0]+"'")
        dt=len(b.fetchall());
        d=[i[0],i[1],dt,int(i[1])*dt,math.log(int(i[1])*dt)]
        data_artikel.append(d)
    data.append(data_artikel)
print(data)

