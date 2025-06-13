class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class ToDoList:
    def __init__(self):
        self.head = None

    def menambahkan_list(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def menambahkan_list_depan(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def menghapus_list_index(self, index):
        if not self.head:
            return
        if index == 0:
            self.head = self.head.next
            return
        current = self.head
        for _ in range(index - 1):
            if not current.next:
                return
            current = current.next
        if current.next:
            current.next = current.next.next

    def menghapus_list_depan(self):
        if self.head:
            self.head = self.head.next

    def menghapus_list_lokasi_index(self, index):
        if not self.head:
            return
        if index == 0:
            self.head = self.head.next
            return
        current = self.head
        for _ in range(index - 1):
            if not current.next:
                return
            current = current.next
        if current.next:
            current.next = current.next.next

    def mengecek_jumlah(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def display(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

def main():
    todo = ToDoList()
    while True:
        print("\nMenu:")
        print("1. Menambahkan List")
        print("2. Menambahkan List dari depan")
        print("3. Menampilkan List berdasarkan index")
        print("4. Menghapus List dari depan")
        print("5. Menghapus List berdasarkan lokasi index")
        print("6. Mengecek Jumlah To do List")
        print("7. Menu Exit")
        print("9. Menu jika pilihan tidak ada")
        
        choice = int(input("Masukkan pilihan: "))
        
        if choice == 1:
            data = input("Masukkan tugas: ")
            todo.menambahkan_list(data)
        elif choice == 2:
            data = input("Masukkan tugas: ")
            todo.menambahkan_list_depan(data)
        elif choice == 3:
            index = int(input("Masukkan index: "))
            current = todo.head
            for _ in range(index):
                if not current:
                    print("Index tidak ada")
                    break
                current = current.next
            if current:
                print(f"Tugas di index {index}: {current.data}")
        elif choice == 4:
            todo.menghapus_list_depan()
            print("Tugas di depan dihapus")
        elif choice == 5:
            index = int(input("Masukkan index untuk dihapus: "))
            todo.menghapus_list_lokasi_index(index)
            print(f"Tugas di index {index} dihapus")
        elif choice == 6:
            jumlah = todo.mengecek_jumlah()
            print(f"Jumlah tugas: {jumlah}")
        elif choice == 7:
            print("Keluar dari program")
            break
        else:
            print("Pilihan tidak ada")

if __name__ == "__main__":
    main()