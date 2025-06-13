from collections import deque
import time
class Mytree:
    def __init__(self, name):
        self.name = name
        self.children = []

    def addChild(self, node):
        self.children.append(node)

    def showTree(self, level=0):
        print("  "*level + f"->{self.name}")
        for child in self.children:
            child.showTree(level+1)

    def Dfs_search(self, target):
        if self.name == target:
            return self
        for child in self.children:
            result = child.Dfs_search(target)
            if result:
                return result
        return None
    
    def Bfs_search(self, target):
        queue = deque([self])
        while queue:
            current = queue.popleft()
            if current.name == target:
                return current
            queue.extend(current.children)
        return None

# Membuat node
root = Mytree("Menu Utama")  # 1

# Level 1
account = Mytree("Account")          # 2
setting = Mytree("Setting")          # 3
dashboard = Mytree("Dashboard")      # 4

# Level 2
profile = Mytree("Profile")          # 5
security = Mytree("Security")        # 6
notif = Mytree("Notification")       # 7
display = Mytree("Display")          # 8
tambah = Mytree("Tambah data")       # 9
edit = Mytree("Edit data")           #10
hapus = Mytree("Hapus data")         #11

# Level 3 (anak dari masing-masing)
email = Mytree("Email")              #12
password = Mytree("Password")        #13
privacy = Mytree("Privacy")          #14
theme = Mytree("Theme")              #15
analytics = Mytree("Analytics")      #16
report = Mytree("Report")            #17

# Tambahan untuk jadi 25
logout = Mytree("Logout")            #18
login = Mytree("Login")              #19
reminder = Mytree("Reminder")        #20
shortcut = Mytree("Shortcut")        #21
sound = Mytree("Sound")              #22
sms_alert = Mytree("SMS Alert")      #23
growth = Mytree("User Growth")       #24
export = Mytree("Export Data")       #25

# Membangun struktur
root.addChild(account)
root.addChild(setting)
root.addChild(dashboard)

account.addChild(profile)
account.addChild(security)
account.addChild(logout)
account.addChild(login)

profile.addChild(email)
profile.addChild(password)

security.addChild(privacy)

setting.addChild(notif)
setting.addChild(display)
setting.addChild(theme)

notif.addChild(reminder)
notif.addChild(sound)
notif.addChild(sms_alert)

display.addChild(shortcut)

dashboard.addChild(tambah)
dashboard.addChild(edit)
dashboard.addChild(hapus)

tambah.addChild(analytics)
tambah.addChild(report)
tambah.addChild(growth)
tambah.addChild(export)

print(root.showTree())

mulaicari_dfs = time.time()
pencarianDfs = root.Dfs_search("Tambah data")
selesaicari_dfs = time.time()
waktucari_dfs = selesaicari_dfs - mulaicari_dfs
print(f"data ditemukan via DFS: {pencarianDfs.name if pencarianDfs else 'Tidak Ditemukan'}")
print(f"waktu yang dibutuhkan untuk DFS search adalah: {waktucari_dfs * 1000:.3f}")


mulaicari_bfs = time.time()
pencarianBfs = root.Bfs_search("Tambah data")
selesaicari_bfs = time.time()
waktucari_bfs = selesaicari_bfs - mulaicari_bfs
print(f"data ditemukan via BFS: {pencarianBfs.name if pencarianBfs else 'Tidak Ditemukan'}")
print(f"waktu yang dibutuhkan untuk BFS search adalah: {waktucari_bfs * 1000:.3f}")