import os
import numpy as np
import pandas as pd
from mpl_toolkits import mplot3d
# %matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
import glob

pdg_codes = {
                'nue' : 12,
                'nuebar' : -12,
                'numu' : 14,
                'numubar' : -14,
                'nutau' : 16,
                'nutaubar' : -16,
}

base_path = '/home/dnewmark/supernova_sims/sources/snowglobes/out/temp_test/'

files = []

for dir_flavor in ['nue', 'nuebar', 'nux']:
    if dir_flavor == 'nux':
        for flavor in ['numu', 'numubar', 'nutau', 'nutaubar']:
            file_names = glob.glob(base_path+dir_flavor+'_temp=*/'+flavor+'_temp=*_nc_dn_'+flavor+'_Ar40_ar40kt_events_smeared.dat')
            files.extend([(flavor, float(s.split('temp=')[1].split('/')[0]), s) for s in file_names]) ## tupeles w flavor, temp, file name

    else:
        file_names = glob.glob(base_path+dir_flavor+'_temp=*/'+dir_flavor+'_temp=*_nc_dn_'+dir_flavor+'_Ar40_ar40kt_events_smeared.dat')
        files.extend([(dir_flavor, float(s.split('temp=')[1].split('/')[0]), s) for s in file_names]) ## tupeles w flavor, temp, file name



def filereader(file):
    data = pd.read_csv('%s' % file, sep = " ", header = None)
    df = pd.DataFrame(data)
    df = df.iloc[:-2]
    df.columns = ['energy','event']
    df_x = np.array(df['event'])
    df_e = np.array(df['energy'])

    return df_x, df_e

nue = np.linspace(0.5, 100, 200) ## energy array snowglobes uses

events = np.array([])
temps = np.array([])
flavors = np.array([])
energy = np.array([])


for flavor, temp, file_name in files:
    file_events, energy_test = filereader(file_name)
    print(nue)
    print(energy_test)
    file_temps = np.full_like(file_events, temp)
    file_flavor = np.full_like(file_events, pdg_codes[flavor])
    file_energy = nue

    events = np.concatenate((events, file_events))
    temps = np.concatenate((temps, file_temps))
    flavors = np.concatenate((flavors, file_flavor))
    energy = np.concatenate((energy, file_energy))

data = np.array([flavors, temps, energy, events]).T
np.savetxt('/home/dnewmark/total_data.txt', data, header = 'flavor temperature energy events')
