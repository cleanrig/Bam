choice = input("Do you want to print as an index?")
userin = input("What text do you want to print?")
CP850list = []
for letter in userin:
    if letter == "a":
        CP850list.append('97')
    if letter == "b":
        CP850list.append('98')
    if letter == "c":
        CP850list.append('99')
    if letter == "d":
        CP850list.append('100')
    if letter == "e":
        CP850list.append('101')
    if letter == "f":
        CP850list.append('102')
    if letter == "g":
        CP850list.append('103')
    if letter == "h":
        CP850list.append('104')
    if letter == "i":
        CP850list.append('105')
    if letter == "j":
        CP850list.append('106')
    if letter == "k":
        CP850list.append('107')
    if letter == "l":
        CP850list.append('108')
    if letter == "m":
        CP850list.append('109')
    if letter == "n":
        CP850list.append('110')
    if letter == "o":
        CP850list.append('111')
    if letter == "p":
        CP850list.append('112')
    if letter == "q":
        CP850list.append('113')
    if letter == "r":
        CP850list.append('114')
    if letter == "s":
        CP850list.append('115')
    if letter == "t":
        CP850list.append('116')
    if letter == "u":
        CP850list.append('117')
    if letter == "v":
        CP850list.append('118')
    if letter == "w":
        CP850list.append('119')
    if letter == "x":
        CP850list.append('120')
    if letter == "y":
        CP850list.append('121')
    if letter == "z":
        CP850list.append('122')
if choice.lower == "yes":
    print(CP850list)
else:
    for integer in CP850list:
        print(integer, end=' ')