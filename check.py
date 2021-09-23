import requests
import time
from datetime import datetime
#функции

def read_checklist(checklisfile):
    with open(checklisfile, "r") as ins:
        array = []
        for line in ins:
            line=line.rstrip()
            array.append(line)
        return array

def status_check(adress):
    adress = "http://" + adress
    status = 0
    try: 
        status = requests.get(adress).status_code
    except requests.exceptions.HTTPError as errh:
        print("Http Error:",adress,errh,now, file=log)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:",adress,errc,now, file=log,)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:",adress,errt,now, file=log)
    except requests.exceptions.RequestException as err:
        print("OOps: Something Else",adress,err,now, file=log)
    if status == 200:
        return 1
    else:
        return 0

def sendfail(adress,sendlist):
    failmess = {"failed" : adress}
    for ip in sendlist:
        try: 
            requests.post(ip, data=failmess)
        except requests.exceptions.HTTPError as errh:
            print("Http Error:",adress,errh,now, file=log)
        except requests.exceptions.ConnectionError as errc:
            print("Error Connecting:",adress,errc,now, file=log,)
        except requests.exceptions.Timeout as errt:
            print("Timeout Error:",adress,errt,now, file=log)
        except requests.exceptions.RequestException as err:
            print("OOps: Something Else",adress,err,now, file=log)
    return print (requests.post(ip, data=failmess), ip)

#функции

#логика
ipchecklist=read_checklist("checklist.txt")
ipsendlist=read_checklist("sendlist.txt")
log=open('log.txt','a')
now = datetime.now()
while True:
    for ip in ipchecklist:
        print(ip) 
        if status_check(ip) == 0:
            print("недоступен",ip)
            sendfail(ip,ipsendlist)
    print("сделал")
    time.sleep(60)
    print("минута")