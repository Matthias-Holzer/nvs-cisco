import re


def reader(path):
    with open(f"lab14/{path}",'r') as f:
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
    with open(f"./personalised/{kn}{path}", 'w') as f:
        f.write(txt)

if __name__ == '__main__':
    files = [
        'lab14_B1-S1.conf',
        'lab14_B1-S2.conf',
        'lab14_B1-S3.conf',
        'lab14_B1.conf',
        'lab14_HQ.conf',
    ]
    kn_numbers = [9]

    #lab14
    things = {
        '?1kn' : [147],    #hat sich bis jetzt nur einmal geändert
        '?vlan' : [57],   #Katalog nummer
    }
    lab15="""
    things = {
    '?1kn': [76,120,206],
    '?2kn': [32,191,55],
    '?3kn': [2,27,123],
    '?area': [5,15,20],
    '?ospf-id': [10,7,15],
    }
    """

    for i in range(len(kn_numbers)):
        for f in files:
            txt = reader(f)
            for k, v in things.items():
                txt = swapper(txt,k,v[i])
            writer(txt,f,kn_numbers[i])



