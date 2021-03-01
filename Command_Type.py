def Command_Type(command):
    switcher = {
        "product:": 1,
        "product": 1,
        "name:": 1,
        "name": 1,
        "p:": 1,
        "p": 1,

        "specifications:": 2,
        "specifications": 2,
        "specification:": 2,
        "specification": 2,
        "specs:": 2,
        "specs": 2,
        "spec:": 2,
        "spec": 2,
        "s:": 2,
        "s": 2,

        "maintenance:": 3,
        "maintenance": 3,
        "main:": 3,
        "main": 3,
        "m:": 3,
        "m": 3,
        "guide:": 3,
        "guide": 3,
        "g:": 3,
        "g": 3,
        "service:": 3,
        "service": 3,
        "msg:": 3,
        "msg": 3,

        "drivers:": 4,
        "drivers": 4,
        "driver:": 4,
        "driver": 4,
        "software:": 4,
        "software": 4,
        "soft:": 4,
        "soft": 4,
        "d:": 4,
        "d": 4,
        
        "support": 5
    }
            
    return switcher.get(command.lower(), 5)