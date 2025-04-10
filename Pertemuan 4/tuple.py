# Membuat Struktur Data Tuple
# Contoh 1
data = ("Budi", 19, "Informatika")
print(data)
data = ("Andi",20,"Informatika")
print(data)
# Mengakses Tuple
print(f"Ini adalah index ke 0 {data[0]}")
print(f"ini adalah index ke -1 {data[-1]}")
# Tuple tidak bisa menerima tambahan elemen
# data.append("Mahardika")

# Tuple bisa copy dan duplicate 
dataWarna =("Merah", "Kuning", "Hijau", "Hitam")
dataWarna1 = dataWarna[0:2]
print(f"Data warna {dataWarna}")
print(f"Data warna 1 {dataWarna1}")
dataWarna3 = dataWarna[:]
print(f"Data warna 3 {dataWarna3}")

# Tuple bisa inisiasi ke variabel
kotakMerah, kotakKuning, kotakHijau, kotakHitam = dataWarna
print(f"isi kotak merah adalah {kotakKuning}")

# apa benar strukdat List dan Tuple menerima data 
# sama sedangkan set tidak menerima 
List = ["Andi", "Dika"]
Tuple = ("Andi", "Andi")
Set = {"Andi", "Andi"}
print(List, Tuple, Set)
ubahSet = set(List)
set2 = set()
print(type(set2))
print(type(ubahSet))
print(ubahSet)
# Set tidak bisa diakses dengan index
# print(ubahSet[0])
# menghapus data di set
ubahSet.discard("Andi")
print(ubahSet)
ubahSet.remove("Dika")
print(ubahSet)
# Iplementasi add dan Update Set
ubahSet.add(24)
print(ubahSet)
ubahSet.update([25,26,27])
print(ubahSet)

# Teknik rubah set
mySet = {1,2,3,4,5,6,7,8}
print(mySet)
mySet.remove(4)
print(mySet)
mySet.add(10)
print(mySet)

# Operasi pada Set
# Union
setA = {1,2,3,4}
setB = {3,4,7,8}
setUnion = setA | setB
print(setUnion)
setIntersection = setA & setB
print(setIntersection)
setDifference = setB - setA
print(setDifference)
setsymmetric = setA ^ setB
print(setsymmetric)

# Struktur Data Dictionary
dataMhs = [{
    "nim": 123456,
    "nama": "Budi",
    "prodi": "Informatika",   
},
  {"nim": 123457,
    "nama": "Andi",
    "prodi": "Informatika"}]
# print(dataMhs)
# print(dataMhs[1]["nim"])
# print(dataMhs["prodi"])
# print(dataMhs["nama"])
no = 0
for c in dataMhs:
    no += 1
    print(no, c["nim"], c["nama"], c["prodi"])

# Merubah elemen Dictionary
dataMhs[0]["nim"] = "Teknik Informatika"
print(dataMhs)
