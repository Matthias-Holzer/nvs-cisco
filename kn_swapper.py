import re


def reader(path):
    with open(path,'r') as f:
        txt = f.read()

    return txt

def swapper(txt,kn_ser,kn_rep):
    return txt.replace(kn_ser,str(kn_rep))

def evller(txt, kn):
    findings = re.finditer(r'\?kn(\+|\-)[0-9]{1,3}', txt)
    for found in findings:
        txt = txt.replace(found.group(0), str(eval(f"{kn}{found.group(0)[3:]}")))
    return txt

def writer(txt, path, kn):
    with open(f"{kn}{path}", 'w') as f:
        f.write(txt)

if __name__ == '__main__':
    files = [
        'lab15_r1.conf',
        'lab15_r2.conf',
        'lab15_r3.conf',
    ]
    kn_numbers = [9,29]
    things = {
    '?1kn': [74,9],
    '?2kn': [180,119],
    '?3kn': [115,223],
    '?area': [10,15],
    '?ospf-id': [14,4],
    }
    
    for i in range(len(kn_numbers)):
        for f in files:
            txt = reader(f)
            for k, v in things.items():
                txt = swapper(txt,k,v[i])
            writer(txt,f,kn_numbers[i])



