import re

def reader():
    with open("test.conf",'r') as f:
        txt = f.read()

    return txt

def swapper_to_kn(txt,kn):
    return txt.replace(kn, '?kn')

def swapper(txt,kn):
    return txt.replace('?kn',str(kn))

def evller(txt, kn):
    findings = re.finditer(r'\?kn(\+|\-)[0-9]{1,3}', txt)
    for found in findings:
        txt = txt.replace(found.group(0), str(eval(f"{kn}{found.group(0)[3:]}")))
    return txt

def writer(txt, kn):
    with open(f"conf{kn}.txt", 'w') as f:
        f.write(txt)

if __name__ == '__main__':
    
    kn = [7,15,16,29]
    for i in kn:
        writer(swapper(evller(reader(),i),i),i)