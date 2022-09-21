# fungsi garisnya 
def garis():
    print ("==================================")

def garis2():
    print ("----------------------------------")

# Perpus kosong untuk meyimpan buku
buku = []

# fungsi show buku ( perlihatkan buku )
def show_buku():
    if len(buku) <= 0:
        garis()
        print("Buku kosong mas!")   
        garis()  
    else:
        for indeks in range(len(buku)):
            garis()
            print ("[{}] {}".format (indeks,buku [indeks]))
            garis()

# fungsi untuk edit buku
def edit_buku():
    show_buku()
    indeks = int(input("Inputkan ID Buku : "))
    if indeks > len(buku):
        print("ID SALAH")
        garis2()
    else:
        judul_baru = input("Judul Baru : ")
        buku[indeks] = judul_baru 
        garis2()
        print("Buku berhasil dirubah!")
        show_buku()
        garis()   

# funsi insert buku
def insert_buku():
    garis()
    buku_baru = input("Judul Buku : ")
    buku.append(buku_baru)
    garis2()
    print("Buku Berhasil ditambah!")
    garis()

# fungsi delete buku 
def delete_buku():
    show_buku()
    indeks = int(input("Inputkan ID Buku : "))
    if indeks > len(buku):
        print ("ID SALAH")
    else:
        buku.remove(buku[indeks])
        garis()
        print ("Buku berhasil dihapus!")    
        garis2()
#Menu untuk tampilan perpus
def show_menu():
    print("\n")
    print("-Selamat datang di perpus-")
    print("1. Show buku")
    print("2. Insert buku")
    print("3. Edit buku")
    print("4. Delete buku")
    print("5. Keluar")

    menu = int(input("Pilih Menu : > "))


    if menu == 1:
        show_buku()
    elif menu == 2:
        insert_buku()
    elif menu == 3:
        edit_buku()
    elif menu == 4:
        delete_buku()
    elif menu == 5:
        exit()
    else:
        print ("Upss Salaahh")        

#tampilkan Menu
if __name__ == "__main__":
    while True:
        show_menu()