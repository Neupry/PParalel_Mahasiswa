import pandas as pd
from concurrent.futures import ProcessPoolExecutor
import time

start = time.time()

df = pd.read_csv('sample_1Jt.csv')

jumlah_mahasiswa = 1000

def calc_MHS_25(number):
    for x in range (0,number):
        #time.sleep(1)
        sample = df.iloc[x,3:27].sum()
        rerata = sample / 24
        print ('Rerata MHS -',x+1 , ':',rerata)
        print ('Done in : ',time.time()-start,' Seconds')

def calc_MHS_50(number):
    for x in range (250,number):
        #time.sleep(1)
        sample = df.iloc[x,3:27].sum()
        rerata = sample / 24
        print ('Rerata MHS -',x+1 , ':',rerata)
        print ('Done in : ',time.time()-start,' Seconds')

def calc_MHS_75(number):
    for x in range (500,number):
        #time.sleep(1)
        sample = df.iloc[x,3:27].sum()
        rerata = sample / 24
        print ('Rerata MHS -',x+1 , ':',rerata)
        print ('Done in : ',time.time()-start,' Seconds')

def calc_MHS_100(number):
    for x in range (750,number):
        #time.sleep(1)
        sample = df.iloc[x,3:27].sum()
        rerata = sample / 24
        print ('Rerata MHS -',x+1 , ':',rerata)
        print ('Done in : ',time.time()-start,' Seconds')

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
    num1 = 250
    num2 = 500
    num3 = 750
    num4 = jumlah_mahasiswa
    with ProcessPoolExecutor(max_workers=5) as exc:
        task1 = exc.submit(calc_MHS_25, num1)
        task2 = exc.submit(calc_MHS_50, num2)
        task3 = exc.submit(calc_MHS_75, num3)
        task4 = exc.submit(calc_MHS_100, num4)
        task5 = exc.submit(calc_rerata, num4)
    print ('Concurrent Done in : ',time.time()-start,' Seconds')

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
