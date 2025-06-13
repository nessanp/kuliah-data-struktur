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

# Node Level 0
root = Mytree("Menu Utama")  # 1

# Level 1
account = Mytree("Account")        # 2
setting = Mytree("Setting")        # 3
dashboard = Mytree("Dashboard")    # 4

# Level 2 - Account
profile = Mytree("Profile")        # 5
security = Mytree("Security")      # 6
logout = Mytree("Logout")          # 7
login = Mytree("Login")            # 8
register = Mytree("Register")      # 9
email = Mytree("Email")            #10
password = Mytree("Password")      #11
recovery = Mytree("Recovery")      #12

# Level 2 - Setting
notif = Mytree("Notification")     #13
display = Mytree("Display")        #14
theme = Mytree("Theme")            #15
language = Mytree("Language")      #16
privacy = Mytree("Privacy")        #17
shortcut = Mytree("Shortcut")      #18
security_setting = Mytree("2FA")   #19
darkmode = Mytree("Dark Mode")     #20

# Level 2 - Dashboard
tambah = Mytree("Tambah data")     #21
edit = Mytree("Edit data")         #22
hapus = Mytree("Hapus data")       #23
export = Mytree("Export data")     #24
import_data = Mytree("Import data")#25
analytics = Mytree("Analytics")    #26
report = Mytree("Report")          #27
usergrowth = Mytree("User Growth") #28

# Level 3 - Notification
reminder = Mytree("Reminder")      #29
sound = Mytree("Sound")            #30
sms_alert = Mytree("SMS Alert")    #31
push_alert = Mytree("Push Alert")  #32
email_alert = Mytree("Email Alert")#33

# Level 3 - Display
font = Mytree("Font")              #34
contrast = Mytree("Contrast")      #35
zoom = Mytree("Zoom")              #36

# Level 3 - Profile
address = Mytree("Address")        #37
phone = Mytree("Phone")            #38
dob = Mytree("Date of Birth")      #39

# Level 3 - Security
security_q = Mytree("Security Question") #40
activity_log = Mytree("Activity Log")    #41

# Level 3 - Tambah Data
input_data = Mytree("Input Manual")      #42
scan_data = Mytree("Scan Document")      #43
upload_file = Mytree("Upload File")      #44

# Level 3 - Analytics
charts = Mytree("Charts")                #45
tables = Mytree("Tables")                #46
summary = Mytree("Summary")              #47

# Extra nodes to complete 50
backup = Mytree("Backup")                #48
restore = Mytree("Restore")              #49
logs = Mytree("Logs")                    #50

# Build tree
root.addChild(account)
root.addChild(setting)
root.addChild(dashboard)

account.addChild(profile)
account.addChild(security)
account.addChild(logout)
account.addChild(login)
account.addChild(register)

profile.addChild(email)
profile.addChild(password)
profile.addChild(address)
profile.addChild(phone)
profile.addChild(dob)

security.addChild(recovery)
security.addChild(security_q)
security.addChild(activity_log)

setting.addChild(notif)
setting.addChild(display)
setting.addChild(theme)
setting.addChild(language)
setting.addChild(privacy)
setting.addChild(shortcut)
setting.addChild(security_setting)
setting.addChild(darkmode)

notif.addChild(reminder)
notif.addChild(sound)
notif.addChild(sms_alert)
notif.addChild(push_alert)
notif.addChild(email_alert)

display.addChild(font)
display.addChild(contrast)
display.addChild(zoom)

dashboard.addChild(tambah)
dashboard.addChild(edit)
dashboard.addChild(hapus)
dashboard.addChild(export)
dashboard.addChild(import_data)
dashboard.addChild(analytics)
dashboard.addChild(report)
dashboard.addChild(usergrowth)
dashboard.addChild(backup)
dashboard.addChild(restore)
dashboard.addChild(logs)

tambah.addChild(input_data)
tambah.addChild(scan_data)
tambah.addChild(upload_file)

analytics.addChild(charts)
analytics.addChild(tables)
analytics.addChild(summary)

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