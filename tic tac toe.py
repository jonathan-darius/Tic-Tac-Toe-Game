"""
Projek Game Tic Tac Toe
By B.JD
"""
##################################### Variabel Global ######################################
papan = [
        "-","-","-",
        "-","-","-",
        "-","-","-",
        ]
game_berjalan = True

pemenang = None

giliran = "x"

########################################## FUNGSI ###########################################

#Menampilkan Papan
def tampilkan_papan():
    print(" | " + papan[0] + " | " + papan[1] + " | " + papan[2] + " | " + "     | 1 | 2 | 3 |")
    print(" | " + papan[3] + " | " + papan[4] + " | " + papan[5] + " | " + "     | 4 | 5 | 6 |")
    print(" | " + papan[6] + " | " + papan[7] + " | " + papan[8] + " | " + "     | 7 | 8 | 9 |")

#Mengatur Giliran Pemain
def pengatur_giliran (giliran):
    pilihan = int(input("Masukkan Pilihan 1-9 = "))
    while pilihan > 9 or pilihan <0 or papan[pilihan-1] !="-":
        print(pilihan)
        print("Pilihan Tidak Valid")
        pilihan = int(input("Masukkan Pilihan 1-9 = "))

    papan[pilihan-1] = giliran
    tampilkan_papan()

def gantian():
    global giliran
    if giliran == "x":
        giliran = "o"
    elif giliran == "o":
        giliran = "x"

#Periksa Kemenangan Atau Seri
def periksa_pemanang():
    periksa_kemenangan()
    periksa_seri()

def periksa_kemenangan():
    global pemenang
    baris = cek_baris()
    kolom = cek_kolom()
    diagonal = cek_diagonal()

    if baris:
        pemenang = baris
    elif kolom:
        pemenang = kolom
    elif diagonal:
        pemenang = diagonal
    else:
        pemenang = None

def cek_baris():
    global game_berjalan
    baris1 = papan[0] == papan[1] == papan[2] != "-"
    baris2 = papan[3] == papan[4] == papan[5] != "-"
    baris3 = papan[6] == papan[7] == papan[8] != "-"

    if baris1 or baris2 or baris3:
        game_berjalan = False
    if baris1:
        return papan[0]
    elif baris2:
        return papan[3]
    elif baris3:
        return papan[6]

def cek_kolom():
    global game_berjalan
    kolom1 = papan[0] == papan[3] == papan[6] != "-"
    kolom2 = papan[1] == papan[4] == papan[7] != "-"
    kolom3 = papan[2] == papan[5] == papan[8] != "-"

    if kolom1 or kolom2 or kolom3:
        game_berjalan = False
    if kolom1:
        return papan[0]
    elif kolom2:
        return papan[1]
    elif kolom3:
        return papan[2]

def cek_diagonal():
    global game_berjalan
    diagonal1 = papan[0] == papan[4] == papan[8] != "-"
    diagonal2 = papan[2] == papan[4] == papan[6] != "-"

    if diagonal1 or diagonal2:
        game_berjalan = False
    if diagonal1:
        return papan[0]
    elif diagonal2:
        return papan[2]
def periksa_seri():
    global game_berjalan
    if "-" not in papan:
        game_berjalan = False

#Mengatur Alur Permainan
def permainan():
    tampilkan_papan()
    while game_berjalan:
        pengatur_giliran(giliran)

        periksa_pemanang()

        gantian()
    if pemenang == "x" or pemenang =="o":
        print(f"Permainan Dimenangkan oleh {pemenang.upper()}")
    elif pemenang == None:
        print('Permainan Seri')

#################################### Jalankan Permainan #####################################
permainan()