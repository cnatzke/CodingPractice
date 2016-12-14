#!/usr/bin/env python

#Query user for beam radius
beamRad=str(input('What is the beam radius?(mm) '))
rtpath='\t\trtpath+='+beamRad+';\n'

#Query used for filtered indices
yes = set(['yes','y', 'ye'])
skipBool=raw_input('Do you need to remove extra indices (y/n)? ').lower()
if skipBool in yes:
    a=raw_input('What indices should be filtered out? ').split(',')
    moda='\t\tif(i!=0'
    for j in range(0,len(a)):
        moda=moda+'&&i!='+a[j]
    moda=moda+'){\n'
else:
    moda='\t\tif(i!=0){\n'


#Open ggac analysis macro and create list by line number
with open('angCorr.C','r') as file:
    data=file.readlines()

#Query for fitting or no fitting
fitBool=raw_input('Do you want to fit the ggac? (y/n)')
if fitBool in yes:
    data[266]='\t\tg->Fit("efit");\n'
else:
    data[266]='// \t\tg->Fit("efit");\n'

#Change desired lines (linenumber-1)
data[67]=data[134]=moda
data[308]=rtpath

#Write file
with open('angCorr.C','w') as output_file:
    output_file.writelines(data)
   

