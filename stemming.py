import csv
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory

SWfactory = StopWordRemoverFactory()
factory = StemmerFactory()
stemmer = factory.create_stemmer()
stopword = SWfactory.create_stop_word_remover()
Sfactory = StemmerFactory()

# tentukan lokasi file, nama file, dan inisialisasi csv
f = open('datakufull.csv', 'r')
reader = csv.reader(f)
deskripsi=[]; #full deskripsi
judul=[];     #fulljudul
# membaca baris per baris

jumlah=0
for row in reader:
    jumlah+=1;
    if jumlah!=1:
        judul.append(str(row[1]))
        deskripsi.append(str(row[2]))

des_katadasar=[]

for i in deskripsi:
    hasil = ''
    kata_per_artikel={}
    for j in i.split():
        if j.isalpha():
            stop = stopword.remove(j)
            stem = stemmer.stem(stop)
            hasil += stem+ ' '
    des_katadasar.append(hasil)


import sqlite3
conn = sqlite3.connect('datakata_new.db')
c = conn.cursor()
#Create table  
c.execute('''CREATE TABLE data
             (id integer, artikel integer, kata text, jumlah integer)''')
print(len(des_katadasar))
jumlah_kata=[]
no=1
r=1
no_artikel=1
for kat in des_katadasar:
    for i in kat.split():
        print("==>>"+str(r))
        jumlah_kata.append(i)
        c.execute("INSERT INTO data VALUES ("+str(no)+","+str(no_artikel)+",'"+str(i)+"',1)")
        conn.commit()
        c.execute("SELECT count(*) FROM data WHERE kata='"+str(i)+"' and artikel="+str(no_artikel))
        #print(str(c.fetchall()))
        b=c.fetchall()[0][0]
        if(b==0):
            c.execute("INSERT INTO data VALUES ("+str(no)+",1,'"+str(i)+"',1)")
            conn.commit()
        else:
            c.execute("UPDATE data set jumlah="+str(b+1)+" WHERE kata='"+str(i)+"' and artikel="+str(no_artikel))
            conn.commit()
        r=r+1
        no=no+1
    no_artikel=no_artikel+1;


print("selesai")

    

   
