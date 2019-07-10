import pandas as pd
import time

df = pd.read_csv('sample_1Jt.csv')

'''
print ('TABEL MAHASISWA')
tabel = df.iloc[:,0:27]
print (tabel)
'''

daftar_nilai = ['nilai1','nilai2','nilai3','nilai4',
                'nilai5','nilai6','nilai7','nilai8',
                'nilai9','nilai10','nilai11','nilai12',
                'nilai13','nilai14','nilai15','nilai16',
                'nilai17','nilai18','nilai19','nilai20',
                'nilai21','nilai22','nilai23','nilai24']

start = time.time()

#Tentukan banyak mahasiswa yang dihitung
jumlah_mahasiswa = 1000

for x in range (0,jumlah_mahasiswa):
    sample = df.iloc[x,3:27].sum()
    rerata = sample / 24
    print ('Rerata MHS -',x+1 , ':',rerata)
    print ('Done in : ',time.time()-start,' Seconds')
    
for x in range (0,23):
    nilai = df.loc[0:int(jumlah_mahasiswa-1),daftar_nilai[x]].sum()
    rerata = nilai/jumlah_mahasiswa
    print ('Total Rerata Nilai -',x+1,':', int(rerata))
    print ('Done in : ',time.time()-start,' Seconds')
    
print ('Serial Done in : ',time.time()-start,' Seconds')
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
