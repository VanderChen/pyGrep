import re
import os
import os.path


def printdir(str):
    print(str)
    return

def chcontent(rootfloder,str):
    file_name = rootfloder+"/"+str

    fp = open(file_name, 'r')
    alllines = fp.readlines()
    fp.close()
    fp = open(file_name, 'w')
    for eachline in alllines:
        a = re.sub('hyenae-', 'GJ288-', eachline)
        fp.writelines(a)
    fp.close()

    fp = open(file_name, 'r')
    alllines = fp.readlines()
    fp.close()
    fp = open(file_name, 'w')
    for eachline in alllines:
        a = re.sub('HYENAE_', 'GJ288_', eachline)
        fp.writelines(a)
    fp.close()

    fp = open(file_name, 'r')
    alllines = fp.readlines()
    fp.close()
    fp = open(file_name, 'w')
    for eachline in alllines:
        a = re.sub('hy_', 'gj_', eachline)
        fp.writelines(a)
    fp.close()

    fp = open(file_name, 'r')
    alllines = fp.readlines()
    fp.close()
    fp = open(file_name, 'w')
    for eachline in alllines:
        a = re.sub('HY_', 'GJ_', eachline)
        fp.writelines(a)
    fp.close()

    fp = open(file_name, 'r')
    alllines = fp.readlines()
    fp.close()
    fp = open(file_name, 'w')
    for eachline in alllines:
        a = re.sub('Hyenae', 'GJ288', eachline)
        fp.writelines(a)
    fp.close()
    return


print("Please input the floder name")
rootfloder = input()
for root, dirs, files in os.walk(rootfloder):
    for name in files:
        chcontent(rootfloder,name)
