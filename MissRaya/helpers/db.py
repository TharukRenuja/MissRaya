import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from MissRaya.vars import FDBURL


cred = credentials.Certificate(
    'Database.json')

firebase_admin.initialize_app(cred, {
    'databaseURL': f'{FDBURL}'
})

# Main Ref
ref = db.reference('MissRaya/')

# Users and Groups
Grps = ref.child('Groups/')
Users = ref.child('Users/')

# All Users And Admins
All = Users.child('All/')
Admins = Users.child('Admins/')

# Data Ref
Data = ref.child('Data/')

# Funcs
def AddGroup(Title: str, ID: int):
    data = {ID: Title}
    Grps.update(data)
    print(f'Added {Title} to Database')


def AddUser(Username: str, ID: int):
    data = {ID: Username}
    All.update(data)
    print(f'Added User @{Username} to Database')


def AddAdmin(Username: str, ID: int):
    data = {ID: Username}
    Admins.update(data)
    print(f'Promoted User @{Username} As Admin')


def GetGrps():
    data = Grps.get()
    return data


def GetUsers():
    data = All.get()
    return data


def GetAdmins():
    data = Admins.get()
    return data


def RemUser(Id):
    data = All.get()
    data.pop(Id, None)
    All.set(data)
