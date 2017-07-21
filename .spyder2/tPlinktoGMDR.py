# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import win32ui
import os

def findStr(string, subStr, findCnt):
    listStr = string.split(subStr,findCnt)
    if len(listStr) <= findCnt:
        return -1
    return len(string)-len(listStr[-1])-len(subStr)
        

dlg=win32ui.CreateFileDialog(1);
openflag=dlg.DoModal();
if openflag!=1:
    print "Error, Can't open the file Dialog"
    exit()
filePathname=dlg.GetPathName()
filename=os.path.basename(filePathname)[:os.path.basename(filePathname).index('.')]
filePath=os.path.dirname(filePathname)
gmdrfile=os.path.join(filePath,filename+'.gmdr')
tPEDfile=os.path.join(filePath,filename+'.tped')
tFAMfile=os.path.join(filePath,filename+'.tfam')
gmdr=open(gmdrfile,'w')
tped=open(tPEDfile,'r')
tfam=open(tFAMfile,'r')
firstline="#Mk\t"
inds=tfam.readlines()
for ind in inds:
    indinfo=ind.replace('\t',' ').split(' ')
    firstline+=indinfo[1]+'\t'
firstline=firstline[:-1]
firstline+='\n'
gmdr.write(firstline)
tfam.close()
gmdr.flush()
line=tped.readline()
indicat=0
while line:
    line=line.replace('\t',' ')
    subline=line[:findStr(line,' ',2)]
    outline=subline.split(' ')[1]
    outline+=line[findStr(line,' ',4)+1:]
    gmdr.write(outline)
    gmdr.flush()
    if indicat<10:
        for i in range(indicat):
            print '=',
    else:
        print '\r\r',
        indicat=0
    indicat+=1
    line=tped.readline()
tped.close()
gmdr.close()
print '\nAll transform are done, the file locates in :'
print gmdrfile

