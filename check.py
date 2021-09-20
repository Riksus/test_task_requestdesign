
def read_checklist(checklisfile):
    with open(checklisfile, "r") as ins:
        array = []
        for line in ins:
            line=line.rstrip()
            array.append(line)
        return array

iplist=read_checklist("checklist.txt")