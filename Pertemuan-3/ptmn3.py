# Membuat List 
myList = ["Mahardika", 1, True, 4.6]
# List Besifat mutable / indexing
# untuk menampilkan isi list index ke 0
print(myList[0])
print(myList[-4])

# 3.Sifat Slicing
# Menampilkan index ke 1 sampai 3
print(f"menampilkan index ke 0-2 {myList[0:3]}")
print(f"dari index awa sampai ke index 2 {myList[:3]}")
dataMhs =[{"nama":"Budi", "NIM":12345, "Prodi":"Informatika"},
          {"nama":"Andi","NIM":12346, "Prodi":"Informatika"}]
# menampilkan list berdasar index

# menambahkan nomor urut pada list
no=0
for i in dataMhs:
    no+=1
    print(f"{no}.Nama = {i['nama']} NIM = {i['NIM']} Prodi = {i['Prodi']}")
# Sifat merubah isi List
myList[0] = "Informatika"
# print(type(dataMhs))
# Menghitung jumlah data dalam list
# print(f"Jumlah elemen dalam data List dataMhs = {len(dataMhs)}")
# print(f"Jumlah elemen dalam data List myList = {len(myList)}")
# Menambahkan Elemen dalam list 
print(myList)
myList.insert(0,"Mahardika")
print(f"List setelah ditambah didepan{myList}") 
# Menambahkan elemen di belakang list
myList.append("ITEKES")
print(myList)
# Menghapus list dengan remove
myList.remove(4.6)
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
