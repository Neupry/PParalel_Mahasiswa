import pandas as pd
from multiprocessing import Process
import time

'''
print ('TABEL MAHASISWA')
tabel = df.iloc[:,0:27]
print (tabel)
'''

start = time.time()

df = pd.read_csv('sample_1Jt.csv')

#Tentukan banyak mahasiswa yang dihitung
jumlah_mahasiswa = 100000

def calc_MHS_25(number):
    for x in range (0,number):
        #time.sleep(1)
        sample = df.iloc[x,3:27].sum()
        rerata = sample / 24
        print ('Rerata MHS -',x+1 , ':',rerata)
        print ('Done in : ',time.time()-start,'Seconds')

def calc_MHS_50(number):
    for x in range (25000,number):
        #time.sleep(1)
        sample = df.iloc[x,3:27].sum()
        rerata = sample / 24
        print ('Rerata MHS -',x+1 , ':',rerata)
        print ('Done in : ',time.time()-start,'Seconds')

def calc_MHS_75(number):
    for x in range (50000,number):
        #time.sleep(1)
        sample = df.iloc[x,3:27].sum()
        rerata = sample / 24
        print ('Rerata MHS -',x+1 , ':',rerata)
        print ('Done in : ',time.time()-start,'Seconds')

def calc_MHS_100(number):
    for x in range (75000,number):
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
        nilai = df[daftar_nilai[x]].sum()
        rerata = nilai/number
        print ('Total Rerata Nilai -',x+1,':', int(rerata))
        print ('Done in : ',time.time()-start,'Seconds')

if __name__ == '__main__':
    
    num1 = 25000
    num2 = 50000
    num3 = 75000
    num4 = 100000
    ttl = jumlah_mahasiswa
    
    t1 = Process(target=calc_MHS_25, args=(num1,))
    #t1.start()
    #t1.join()
    t2 = Process(target=calc_MHS_50, args=(num2,))
    #t2.start()
    #t2.join()
    t3 = Process(target=calc_MHS_75, args=(num3,))
    #t3.start()
    #t3.join()
    t4 = Process(target=calc_MHS_100, args=(num4,))
    #t4.start()
    #t4.join()
    t5 = Process(target=calc_rerata, args=(ttl,))
    #t5.start()
    #t5.join()

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
    
    print ('MultiProcessing Done in :', time.time()-start, ' Seconds')
    
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
