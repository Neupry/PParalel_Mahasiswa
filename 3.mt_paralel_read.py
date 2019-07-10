import pandas as pd
from threading import Thread
import time

'''
print ('TABEL MAHASISWA')
tabel = df.iloc[:,0:27]
print (tabel)
'''

start = time.time()

df = pd.read_csv('sample_1Jt.csv')

jumlah_mahasiswa = 1000

def calc_MHS_25(number):
    for x in range (0,number):
        #time.sleep(1)
        sample = df.iloc[x,3:27].sum()
        rerata = sample / 24
        print ('Rerata MHS -',x+1 , ':',rerata)
        print ('Done in : ',time.time()-start,'Seconds')

def calc_MHS_50(number):
    for x in range (250,number):
        #time.sleep(1)
        sample = df.iloc[x,3:27].sum()
        rerata = sample / 24
        print ('Rerata MHS -',x+1 , ':',rerata)
        print ('Done in : ',time.time()-start,'Seconds')

def calc_MHS_75(number):
    for x in range (500,number):
        #time.sleep(1)
        sample = df.iloc[x,3:27].sum()
        rerata = sample / 24
        print ('Rerata MHS -',x+1 , ':',rerata)
        print ('Done in : ',time.time()-start,'Seconds')

def calc_MHS_100(number):
    for x in range (1000,number):
        #time.sleep(1)
        sample = df.iloc[x,3:27].sum()
        rerata = sample / 24
        print ('Rerata MHS -',x+1 , ':',rerata)
        print ('Done in : ',time.time()-start,'Seconds')

def calc_rerata(number):
    daftar_nilai = ['nilai1','nilai2','nilai3','nilai4',
                    'nilai5','nilai6','nilai7','nilai8',
                    'nilai9','nilai10','nilai11','nilai12',
                    'nilai13','nilai14','nilai15','nilai16',
                    'nilai17','nilai18','nilai19','nilai20',
                    'nilai21','nilai22','nilai23','nilai24']
    for x in range (0,23):
        #time.sleep(1)
        nilai = df.loc[0:int(number-1),daftar_nilai[x]].sum()
        rerata = nilai/number
        print ('Total Rerata Nilai -',x+1,':', int(rerata))
        print ('Done in : ',time.time()-start,' Seconds')

if __name__ == '__main__':

    #Banyaknya data yang diolah oleh tiap fungsi
    num1 = 250
    num2 = 500
    num3 = 750
    num4 = 1000
    
    t1 = Thread(target=calc_MHS_25, args=(num1,))
    t2 = Thread(target=calc_MHS_50, args=(num2,))
    t3 = Thread(target=calc_MHS_75, args=(num3,))
    t4 = Thread(target=calc_MHS_100, args=(num4,))
    t5 = Thread(target=calc_rerata, args=(num4,))
    
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    
    print ('MultiThread Done in :', time.time()-start, ' Seconds')
    
end = time.time()
dur = end-start
if dur<60:
    print("Execution Time:",dur,"seconds")
elif dur>60 and dur<3600:
    dur=dur/60
    print("Execution Time:",dur,"minutes")
else:
    dur=dur/(60*60)
    print("Execution Time:",dur,"hours")
'''
for x in range (0,10):
    nilai = df[daftar_nilai[x]].sum()
    rerata = nilai/jumlah_mahasiswa
    print ('Total Rerata Nilai -',x+1,':', int(rerata))
'''
