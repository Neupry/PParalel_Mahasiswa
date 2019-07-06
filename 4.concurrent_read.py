import pandas as pd
from concurrent.futures import ThreadPoolExecutor
import time

start = time.time()

df = pd.read_csv('sample_1Jt.csv')

#Tentukan banyak mahasiswa yang dihitung
jumlah_mahasiswa = 100000

def calc_MHS_25():
    for x in range (0,25000):
        #time.sleep(1)
        sample = df.iloc[x,3:27].sum()
        rerata = sample / 24
        print ('Rerata MHS -',x+1 , ':',rerata)
        print ('Done in : ',time.time()-start,' Seconds')

def calc_MHS_50():
    for x in range (25000,50000):
        #time.sleep(1)
        sample = df.iloc[x,3:27].sum()
        rerata = sample / 24
        print ('Rerata MHS -',x+1 , ':',rerata)
        print ('Done in : ',time.time()-start,' Seconds')

def calc_MHS_75():
    for x in range (50000,75000):
        #time.sleep(1)
        sample = df.iloc[x,3:27].sum()
        rerata = sample / 24
        print ('Rerata MHS -',x+1 , ':',rerata)
        print ('Done in : ',time.time()-start,' Seconds')

def calc_MHS_100():
    for x in range (75000,100000):
        #time.sleep(1)
        sample = df.iloc[x,3:27].sum()
        rerata = sample / 24
        print ('Rerata MHS -',x+1 , ':',rerata)
        print ('Done in : ',time.time()-start,' Seconds')

def calc_rerata():
    daftar_nilai = ['nilai1','nilai2','nilai3','nilai4',
                    'nilai5','nilai6','nilai7','nilai8',
                    'nilai9','nilai10','nilai11','nilai12',
                    'nilai13','nilai14','nilai15','nilai16',
                    'nilai17','nilai18','nilai19','nilai20',
                    'nilai21','nilai22','nilai23','nilai24']
    for x in range (0,100000):
        #time.sleep(1)
        nilai = df[daftar_nilai[x]].sum()
        rerata = nilai/jumlah_mahasiswa
        print ('Total Rerata Nilai -',x+1,':', int(rerata))
        print ('Done in : ',time.time()-start,' Seconds')

def run():
    with ThreadPoolExecutor(max_workers=5) as executor:
        task1 = executor.submit(calc_MHS_25)
        #time.sleep(0.002)
        task2 = executor.submit(calc_MHS_50)
        #time.sleep(0.002)
        task2 = executor.submit(calc_MHS_75)
        #time.sleep(0.002)
        task2 = executor.submit(calc_MHS_100)
        #time.sleep(0.001)
        task3 = executor.submit(calc_rerata)
    print ('Concurrent Done in : ',time.time()-start,' Seconds')

if __name__ == '__main__':
    run()

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
