# Some configurations for plotting 

# only want to use these columns below
cols_to_use = ['dllwave_flux', 'dwpt2m', 'fric_vel', 'gflux', 'high_cloud',
            'lat_hf', 'low_cloud', 'mid_cloud', 'sat_irbt', 'sens_hf',
            'sfcT_hrs_ab_frez', 'sfcT_hrs_bl_frez', 'sfc_rough', 'sfc_temp',
            'swave_flux','temp2m', 'tmp2m_hrs_ab_frez', 'tmp2m_hrs_bl_frez',
            'tot_cloud', 'uplwav_flux','vbd_flux', 'vdd_flux','wind10m',
            'date_marker', 'urban','rural','d_ground','d_rad_d','d_rad_u',
            'hrrr_dT']

units = ['W m$^{-2}$', '$^{\circ}$C', 'm s$^{-1}$', 'W m$^{-2}$', '%', 'W m$^{-2}$', '%', '%', 
         '$^{\circ}$C', 'W m$^{-2}$', 'hrs', 'hrs', 'unitless','$^{\circ}$C', 'W m$^{-2}$', '$^{\circ}$C', 
         'hrs', 'hrs', '%', 'W m$^{-2}$', 'W m$^{-2}$', 'W m$^{-2}$', 'm s$^{-1}$', 'days', 'unitless', 
         'unitless', 'W m$^{-2}$', 'W m$^{-2}$', 'W m$^{-2}$', '$^{\circ}$C']


#units = ['W \ m^{-2}', '^{\circ}C', 'm \ s^{-1}', 'W \ m^{-2}', '%', 'W \ m^{-2}', '%', '%', 
#         '^{\circ}C', 'W \ m^{-2}', 'hrs', 'hrs', 'unitless','^{\circ}C', 'W \ m^{-2}', '^{\circ}C', 
#         'hrs', 'hrs', '%', 'W \ m^{-2}', 'W \ m^{-2}', 'W \ m^{-2}', 'm \ s^{-1}', 'days', 'unitless', 
#         'unitless', 'W \ m^{-2}', 'W \ m^{-2}', 'W \ m^{-2}', '^{\circ}C']

pretty_names = [ '$\lambda_{\downarrow}$', '$T_{d}$', '$V_{fric}$', 'Gflux', '$Cloud_{high}$',
 '$Lat_{F}$', '$Cloud_{low}$', '$Cloud_{mid}$', 'IRBT', '$Sens_{F}$',
 'Hours $T_{sfc}$ $>$ 0', 'Hours $T_{sfc} \leq 0$', 'SfcRough', '$T_{sfc}$',
 '$I_{S}$', '$T_{2m}$', 'Hours $T_{2m}$ $>$ 0', 'Hours $T_{2m}$ $\leq $ 0',
 '$Cloud_{Tot}$', r'$\lambda_{\uparrow}$', 'VBD', 'VDD', '10m wind',
 'Date marker', 'Urban', 'Rural', 'Diff1', 'Diff2', 'Diff3',
 '$T_{sfc}$ - $T_{2m}$']


#pretty_names = [ '\lambda_{\downarrow}', 'T_{d}', 'V_{fric}', 'Gflux', 'Cloud_{high}',
# 'Lat_{F}', 'Cloud_{low}', 'Cloud_{mid}', 'IRBT', 'Sens_{F}',
# 'Hours \ T_{sfc} \ > \0', 'Hours  \ T_{sfc} \ <= \ 0', 'SfcRough', 'T_{sfc}',
# 'I_{S}', 'T_{2m}', 'Hours  \ T_{2m} \ > \ 0', 'Hours \ T_{2m} \ <= \ 0',
# 'Cloud_{Tot}', 
#  '\\lambda_{\\uparrow}', 'VBD', 'VDD', '10m \ wind',
# 'Date \ marker', 'Urban', 'Rural', 'Diff1', 'Diff2', 'Diff3',
# 'T_{sfc} - T_{2m}']

color_dict = { 'dllwave_flux':'xkcd:light light green',
              'dwpt2m': 'xkcd:powder blue',
              'gflux':'xkcd:light light green',
              'high_cloud':'xkcd:light periwinkle',
              'lat_hf':'xkcd:light light green',
              'low_cloud':'xkcd:light periwinkle',
              'mid_cloud':'xkcd:light periwinkle',
              'sat_irbt':'xkcd:light periwinkle',
              'sens_hf':'xkcd:light light green',
            'sfcT_hrs_ab_frez':'xkcd:powder blue',
            'sfcT_hrs_bl_frez':'xkcd:powder blue',
            'sfc_rough':'xkcd:orangish',
            'sfc_temp':'xkcd:powder blue',
            'swave_flux':'xkcd:light light green',
            'temp2m':'xkcd:powder blue',
            'tmp2m_hrs_ab_frez':'xkcd:powder blue',
            'tmp2m_hrs_bl_frez':'xkcd:powder blue',
            'tot_cloud':'xkcd:light periwinkle',
            'uplwav_flux':'xkcd:light light green',
            'vbd_flux':'xkcd:light light green',
            'vdd_flux':'xkcd:light light green',
            'wind10m':'xkcd:orangish',
            'date_marker':'xkcd:orangish',
            'urban':'xkcd:orangish',
            'rural':'xkcd:orangish',
            'd_ground':'xkcd:light light green',
            'd_rad_d':'xkcd:light light green',
            'd_rad_u':'xkcd:light light green',
            'hrrr_dT':'xkcd:powder blue', 
             'fric_vel' : 'xkcd:orangish'}

display_units = {c : u for c,u in zip(cols_to_use, units)}
display_feature_names = {c : u for c,u in zip(cols_to_use, pretty_names)}