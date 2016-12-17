#!/usr/bin/python

import fileinput 
import sys

#Query user for beam radius
beamRad=input('What is the beam radius?(mm) ')
rtpath='\t\trtpath+='+beamRad+';\n'

#Query used for filtered indices
yes = set(['yes','y', 'ye'])
skipBool=input('Do you need to remove extra indices (y/N)? ').lower()
if skipBool in yes:
    a=input('What indices should be filtered out? ').split(',')
    moda='\t\tif(i!=0'
    for j in range(0,len(a)):
        moda=moda+'&&i!='+a[j]
    moda=moda+'){\n'
else:
    moda='\t\tif(i!=0){\n'

#Query for fitting
yesFit = set(['yes','y', 'ye',''])
fitBool=input('Do you want to fit the histogram (Y/n)? ').lower()
if fitBool in yesFit:
    fitMod='\t\tg->Fit("efit");\n'
else:
    fitMod='//\t\tg->Fit("efit");\n'


#Reads input file line by line
changeBool=False
for line in fileinput.input(['angCorr.C'], inplace=True, backup='.bk'):

#Changes beam radius for output .root file
    if line.strip().startswith('rtpath+=') and changeBool==False:
        line = rtpath
        changeBool=True
#Changes filtered indices
    if line.strip().startswith('if(i!=0'):
        line = moda
#Toggles Fitting
    if 'g->Fit(' in line:
        line = fitMod
    sys.stdout.write(line)
