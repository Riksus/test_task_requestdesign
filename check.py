import urllib.request
import requests
def read_checklist(checklisfile):
    with open(checklisfile, "r") as ins:
        array = []
        for line in ins:
            line=line.rstrip()
            array.append(line)
        return array

def status_check(adress):
    adress = "http://" + adress
    status = urllib.request.urlopen(adress).getcode()
    if status == "200":
        return adress
    else:
        return 0

def sendfail(adress,sendlist):
    failmess = {"failed" : adress}
    for ip in sendlist:
        requests.post(ip, data=failmess)
    return

ipchecklist=read_checklist("checklist.txt")
ipsendlist=read_checklist("sendlist.txt")