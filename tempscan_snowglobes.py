#     ssh_password="KjUlp4599",

import os
import shutil
from os import listdir, system
from pathlib import Path

path = '/home/dnewmark/supernova_sims/sources/snowglobes/fluxes/temp_test'
os.chdir(path)
list = os.listdir(path)
number_files = len(list)


path = '/home/dnewmark/supernova_sims/sources/snowglobes'
os.chdir(path)

## for loop to calculate event numbers for each temp
for i in range(number_files):
    path = '/home/dnewmark/supernova_sims/sources/snowglobes'
    os.chdir(path)
    flux = list[i].strip(".dat")
    os.system('./supernova.pl temp_test/%s' % flux + ' argon_dn ar40kt')

    ## now let's get organized
    path_out = '/home/dnewmark/supernova_sims/sources/snowglobes/out/temp_test'
    os.chdir(path_out)
    # temp_intermediate = list[i].split('_')
    # temp_name = temp_intermediate[1].split('.dat')
    temp_flavor = list[i].split('.dat') ## new list name w flavor and temp info, temp_flavor[0]

    p = Path('/home/dnewmark/supernova_sims/sources/snowglobes/out/temp_test/%s' % temp_flavor[0])

    if p.is_dir() == True:
        print('directory exists')

    if p.is_dir() == False:
        os.mkdir('%s' % temp_flavor[0])

    os.chdir(path_out)
    result_list = os.listdir(path_out)
    for j in range(len(result_list)):
        print(result_list[j])
        if result_list[j].find('_nc_') != -1:
            ## these are the nc files
            if result_list[j].endswith('_smeared.dat'):
                ## these are the smeared files
                shutil.move('/home/dnewmark/supernova_sims/sources/snowglobes/out/temp_test/%s' % result_list[j] , '/home/dnewmark/supernova_sims/sources/snowglobes/out/temp_test/%s' % temp_flavor[0])
