command = "Product: ap0053dx, Specifications: Microprocessor Memory Hard Display, Maintenance: 45, Drivers: sp96858.exe sp112143.exe, Support"

individual_commands = command.split(",")

for individual_command in individual_commands:
    split_individual_command = individual_command.split(" ")
    command_number = command_type(split_individual_command[0])
    if command_number == 1:
        Main_Product_Page(split_individual_command[1])
    elif command_number == 2:
    elif command_number == 3:
    elif command_number == 4:
    elif command_number == 5:
        answer += "<p>The command '<i>%s</i>' was not recognized.</p>" % (split_individual_command[0])

def command_type(identifier):
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
        
    return switcher.get(identifier.lower(), 5)
    }