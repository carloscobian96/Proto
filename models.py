class Type:
    def __init__(self, idtype):
        self.idtype:int = int.from_bytes(   idtype, 
                                            byteorder='big', 
                                            signed=False)
        self.name:str = Type.getTypeName(idtype)

    def getTypeName(idType):
        type = {
            b'\x00': "Debit",
            b'\x01': "Credit",
            b'\x02': "StartAutopay",
            b'\x03': "EndAutopay"
        }
        return type.get(idType, "Invalid State")

    def hasField(idType):
        type = {
            b'\x00': True,
            b'\x01': True,
            b'\x02': False,
            b'\x03': False
        }
        return type.get(idType, "Invalid State")

class User:
    def __init__(self, iduser):
        self.iduser = int.from_bytes(   iduser, 
                                        byteorder='big', 
                                        signed=False)

class Record: 
    def __init__(self, idrecord:int, type_idtype, timestamp, user_iduser, ammount:float):
        self.idrecord:int = idrecord
        self.type_idtype:Type = Type(type_idtype)
        self.timestamp:int = int.from_bytes(timestamp, 
                                            byteorder='big', 
                                            signed=False)
        self.user_iduser:User = User(user_iduser)
        self.ammount:float = ammount

