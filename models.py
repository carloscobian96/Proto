class Type():
    idtype:int 
    name:str
    def __init__(self, idtype, name):
        self.idtype = idtype
        self.name = name

class User():
    iduser:int
    def __init__(self, iduser):
        self.iduser = iduser

class Record():
    idrecord:int
    type_idtype:Type 
    timestamp:int
    user_iduser:User
    ammount:float
    def __init__(self, idrecord:int, type_idtype:Type, timestamp:int, user_iduser:User, ammount:float):
        self.idrecord = idrecord
        self.type_idtype = type_idtype
        self.timestamp = timestamp
        self.user_iduser = user_iduser
        self.ammount = ammount


