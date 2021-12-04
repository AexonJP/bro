import pickle
import os
from datetime import date, datetime
from time import sleep

def load():
    return pickle.load(open("schedule.save", "rb") )

def save(data):
    return pickle.dump(data, open("schedule.save", "wb") )

def bulan(angka_bulan):
    bulan = int(angka_bulan)
    if bulan == 1:
        bulan = "Januari"
    elif bulan == 2:
        bulan = "Februari"
    elif bulan == 3:
        bulan = "Maret"
    elif bulan == 4:
        bulan = "April"
    elif bulan == 5:
        bulan = "Mei"
    elif bulan == 6:
        bulan = "Juni"
    elif bulan == 7:
        bulan = "Juli"
    elif bulan == 8:
        bulan = "Agustus"
    elif bulan == 9:
        bulan = "September"
    elif bulan == 10:
        bulan = "Oktober"
    elif bulan == 11:
        bulan = "November"
    elif bulan == 12:
        bulan = "Desember"
    return bulan
     
def tanggal_today():
    waktu = date.today()
    hari = waktu.strftime("%A")    
    tanggal = waktu.strftime(f"%d {bulan(waktu.strftime('%m'))} %Y")
    if hari == "Monday":
        hari = "Senin"
    elif hari == "Tuesday" :
        hari = "Selasa"
    elif hari == "Wednesday":
        hari = "Rabu"
    elif hari == "Thursday":
        hari = "kamis"
    elif hari == "Friday":
        hari = "Jum'at"
    elif hari == "Saturday":
        hari = "Sabtu"
    elif hari == "Sunday":
        hari = "Minggu"
    print (f"Tanggal {tanggal}\nHari {hari}")

def tahun():
    waktu = date.today()
    tahun = waktu.strftime("%Y")
    return tahun

def check(masukan):
    try:
        masukan = int(masukan)
        if masukan > 0 :
            return masukan
        else:
            raise ValueError
    except ValueError:
        return 0

def data_jadwal():
    data = {
    "jadwal":[],
    "kode":[],
    "tanggal":[]}
    return data

def daftar_menu(jadwal, kode):
    for i in range(len(jadwal)):
        sleep(0.3)
        print (f"{i+1}. {jadwal[i]} ({kode[i]})\n")
    

def mulai():
    data = data_jadwal()
    try :
        data =load()
        for i in range(len(data['tanggal'])):
            if datetime.strptime(data["tanggal"][i], "%d/%m/%Y") < datetime.strptime((datetime.today()).strftime("%d/%m/%Y"), "%d/%m/%Y"):
                del data['jadwal'][i]
                del data['kode'][i]
                del data['tanggal'][i]
    except :
        pass
    
    while(True): 
        tanggal_today()
        print(  "======================================\n"
                "1. Melihat jadwal ke depannya.\n"
                "2. Menambahkan jadwal baru.\n"
                "3. Menghapus Jadwal yang sudah ada.\n"
                "4. Daftar tanggal merah (Tetap).\n"
                "5. Mengubah jadwal yang sudah ada\n"
                "=======================================")
        kode = input ("Ingin membuka nomor : ")
        kode = check(kode)
        
        # Mensortir jadwal
        sorted_lists = sorted(zip(data['tanggal'], data["jadwal"], data['kode']), key=lambda x: datetime.strptime(x[0], "%d/%m/%Y"))
        data['tanggal'], data["jadwal"], data['kode'] = [[x[i] for x in sorted_lists] for i in range(3)]
        
        if kode == 1:
            os.system("cls")
            print ("=======================================")
            print ("Berikut adalah jadwal yang ada :\n")
            if len(data["jadwal"]) > 0:
                daftar_menu(data['jadwal'], data['kode'])
                sleep(0.5)
                input("\nPress Enter to continue...")
                os.system("cls")
            else :
                print ("Masih belum ada jadwal terbaru\n\n")
            
        elif kode == 2:
            os.system("cls")
            print ("=======================================")
            print ("Berikut adalah jadwal yang ada :\n")
            if len(data["jadwal"]) > 0:
                daftar_menu(data['jadwal'], data['kode'])
            else :
                print ("Masih belum ada jadwal terbaru\n\n")
            judul_tambah = input ("Judul dari jadwal yang akan di tambah : ")
            tanggal_tambah = input ("Masukkan tanggal (day/month/year or 00/00/0000) : ")
            try:
                format_data = datetime.strptime(tanggal_tambah, "%d/%m/%Y")
                format_tanggal = format_data.strftime(f"%d {bulan(format_data.strftime('%m'))} %Y")
                if format_data >= datetime.today():
                    data['jadwal'].append (judul_tambah)
                    data['kode'].append (format_tanggal)
                    data["tanggal"].append (format_data.strftime(f"%d/%m/%Y"))
                    sleep(0.3)
                    print("\nJadwal berhasil di tambahkan")
                else:
                    raise ValueError
            except ValueError:
                sleep(0.3)
                print("\nJadwal gagal di tambahkan")
            input("\nPress Enter to continue...")
            os.system("cls")

            
        elif kode == 3:
            os.system("cls")
            print ("=======================================")
            print ("Berikut adalah jadwal yang ada :\n")
            if len(data["jadwal"]) > 0:
                daftar_menu(data['jadwal'], data['kode'])
            else :
                print ("Masih belum ada jadwal terbaru\n\n")
            hapus = input ("Nomor dari jadwal yang ingin di hapus : ")
            hapus = check(hapus)
            if len (data["jadwal"])+1 > hapus > 0 :
                try:
                    del data['jadwal'][hapus-1]
                    del data['kode'][hapus-1]
                    del data['tanggal'][hapus-1]
                    sleep(0.3)
                    print ("\nJadwal berhasil di hapus")
                except:
                    sleep(0.3)
                    print("\nPenghapusan jadwal gagal")
            else:
                sleep(0.3)
                print("\nPenghapusan jadwal gagal")
            sleep(0.3)
            input("\nPress Enter to continue...")
            os.system("cls")
        elif kode == 4:
            tanggal_merah = {
                    f'Tahun Baru {tahun()} Masehi':'01 Januari',
                    'Tahun Buruh Internasional':'01 Mei',
                    'Tahun Lahir Pancasila':'01 Juni',
                    'Tahun Kemerdekaan Republik Indonesia':'17 Agustus',
                    'Tahun Raya Natal':'25 Desember'}
            os.system("cls")
            print ("=======================================")
            print ("Berikut adalah tanggal merah (tetap) :\n")
            directory_sementara = []
            for i in tanggal_merah:
                directory_sementara.append (f"{i} ({tanggal_merah[i]} {tahun()})")
            for i in range(len(directory_sementara)):
                sleep(0.3)
                print (f"{i+1}. {directory_sementara[i]}")
            print ()
            input("\nPress Enter to continue...")
            os.system("cls")
        elif kode == 5 :
            os.system("cls")
            print ("=======================================")
            print ("Berikut adalah jadwal yang ada :\n")
            if len(data["jadwal"]) > 0:
              daftar_menu(data['jadwal'], data['kode'])
            else :
                print ("Masih belum ada jadwal terbaru\n\n")
            ubah_jadwal = input("Masukkan nomor jadwal yang ingin di ubah : ")
            ubah_jadwal = check(ubah_jadwal)
            if len(data["jadwal"])+1 > ubah_jadwal > 0:
                try:
                    ubah_judul= input("Masukkan judul baru jadwal : ")
                    ubah_tanggal= input("Masukkan tanggal (day/month/year or 00/00/0000) : ")
                    format_data = datetime.strptime(ubah_tanggal, "%d/%m/%Y")
                    format_tanggal = format_data.strftime(f"%d {bulan(format_data.strftime('%m'))} %Y")
                    if format_data >= datetime.today():
                        data['jadwal'][ubah_jadwal-1] = ubah_judul
                        data['kode'][ubah_jadwal-1] = format_tanggal
                        data['tanggal'][ubah_jadwal-1] = format_data.strftime(f"%d/%m/%Y")
                        sleep(0.5)
                        print ("\nJadwal berhasil di ubah") 
                    else :
                        raise ValueError   
                except ValueError:
                    sleep(0.5)
                    print("\nPengubahan jadwal gagal")
            else:
                sleep(0.5)
                print("\nPengubahan jadwal gagal")
            input("\nPress Enter to continue...")
            os.system("cls")   
        else:
            sleep(0.3)
            print()
            print("Format yang anda masukkan salah\n")
            sleep(0.3)
            input("\nPress Enter to continue...")
            os.system("cls")
        save(data)

mulai()