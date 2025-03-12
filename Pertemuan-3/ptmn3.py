# membuat List 
myList = ["Mahardika", 1, True, 4.6]
#List Bersifat mutable / indexing
#untuk menampilkan isi list index ke 0
print(myList[0])
print(myList[-4])

# 3.sifat Slicing 
# Manampilkan index ke 1 sampai 3
print(f"menampilakan index ke 0-2 {myList[0:3]}")
print(f"dari index awal samapi ke 2 {myList[ :3]}")
dataMhs =[{"nama":"Budi", "NIM":"12345", "Prodi":"Informatika",},
          {"nama":"Andi","NIM":"123456", "Prodi":"Informatika"}]

# menampilkan list berdasarkan index
no=0
for i in dataMhs:
    no=no+1
    print(f"{no}. Nama = {i['nama']} NIM = {i['NIM']} Prodi = {i['Prodi']}")
# sifat merubah isi List
myList[0] = "Informatika"
print(type(dataMhs))
# menghitung jumlah data dalam list
print(f"Jumlah elemen dalam data List dataMhs = {len(dataMhs)}")
print(f"Jumlah elemen dalam data List myList = {len(myList)}")
# Menambahkan Elemen dalam list
print(myList)
myList.insert(0,"Mahardika")
print(f"List setelah ditambah didepan{myList}")
# Menambahkan elemen di belakang list
myList.append("ITEKES")
print(myList)
# Menghapus list dengan remove 
myList.remove("ITEKES")
print(myList)
myList.pop(4)
print(myList)
# Mengurutkan List
listWarna = ["Merah", "Kuning", "Hijau", "Biru"]
listWarna.sort()
print(listWarna)
# Membalik List
listWarna.reverse()
print(listWarna)
# Menjumlahkan isi List
listAngka = [1,2,3,4,5]
print(sum(listAngka))
# Membuat salinan dengan copy
b = listWarna.copy()
print(b)
