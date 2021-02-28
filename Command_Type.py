def Command_Type(identifier):
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
            
    return switcher.get(identifier.lower(), 5)

command = "Product: ap0053dx, Specifications: Microprocessor Memory Hard Display, Maintenance: 45, Drivers: sp96858.exe sp112143.exe, Support"

individual_commands = command.split(",")

for individual_command in individual_commands:
    split_individual_command = individual_command.split(" ")
    command_number = Command_Type(split_individual_command[0])
    if command_number == 1:
        pass
    elif command_number == 2:
        final_answer += Product_Specifications(individual_command[1:])
    elif command_number == 3:
        if len(individual_command) == 1:
            final_answer += Maintenance_and_Service_Guide(none)
        else:
            final_answer += Maintenance_and_Service_Guide(split_individual_command[1])
    elif command_number == 4:
        Drivers(individual_command[1:])
    elif command_number == 5:
        #SQL stuff
        pass
    else:
        final_answer += "<p>The function '<i>%s</i>' was not recognized.</p>" % (split_individual_command[0])