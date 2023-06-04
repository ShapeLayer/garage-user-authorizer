from enum import IntFlag, auto

class UserAcl(IntFlag):
    REGISTRANT = auto()
    LOGINABLE  = auto()
    MANAGER    = auto()

class UserType(IntFlag):
    IS_SOLDIER   = auto() # 군인 여부
    IS_THIS_UNIT = auto() # 본 부대 소속 여부
    IS_FIXED     = auto() # 고정출입자 여부
    IS_ORG       = auto() # 사람이 아님(각 처부 또는 조직)

class User:
    def __init__(self, id: str, name: str, acl: UserAcl, user_type: UserType, image_path: str):
        self.id: str = id
        self.name: str = name
        self.acl: UserAcl = acl
        self.user_type: UserType = user_type
        self.image_path: str = image_path
