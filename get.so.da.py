#####script to download with OPenDAP from https://resources.marine.copernicus.eu/products in netcdf files 

import matplotlib.pyplot as plt
import xarray as xr
import getpass
import sys 

USERNAME = 'lschwartz'
PASSWORD = '9ribouillE*'
DATASET_ID = 'cmems_mod_glo_phy_my_0.083_P1D-m' ### the dataset_id is found when opening a dataset from https://resources.marine.copernicus.eu/products in the data access tab (OPENDAP). ex:it is the last part of https://my.cmems-du.eu/thredds/dodsC/cmems_mod_glo_phy_my_0.083_P1D-m of the data url when opening the opendap link 

yyyy=str(sys.argv[1]).zfill(4)
mm=str(sys.argv[2]).zfill(2)
dd=str(sys.argv[3]).zfill(2)

date='{}-{}-{}'.format(yyyy,mm,dd)

#! /usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "Copernicus Marine User Support Team"
__copyright__ = "(C) 2022 E.U. Copernicus Marine Service Information"
__credits__ = ["E.U. Copernicus Marine Service Information"]
__license__ = "MIT License - You must cite this source"
__version__ = "202104"
__maintainer__ = "D. Bazin, E. DiMedio, C. Giordan"
__email__ = "servicedesk dot cmems at mercator hyphen ocean dot eu"

def copernicusmarine_datastore(dataset, username, password):
    from pydap.client import open_url
    from pydap.cas.get_cookies import setup_session
    cas_url = 'https://cmems-cas.cls.fr/cas/login'
    session = setup_session(cas_url, username, password)
    session.cookies.set("CASTGC", session.cookies.get_dict()['CASTGC'])
    database = ['my', 'nrt']
    url = f'https://{database[0]}.cmems-du.eu/thredds/dodsC/{dataset}'
    try:
        data_store = xr.backends.PydapDataStore(open_url(url, session=session, user_charset='utf-8')) # needs PyDAP >= v3.3.0 see https://github.com/pydap/pydap/pull/223/commits 
    except:
        url = f'https://{database[1]}.cmems-du.eu/thredds/dodsC/{dataset}'
        data_store = xr.backends.PydapDataStore(open_url(url, session=session, user_charset='utf-8')) # needs PyDAP >= v3.3.0 see https://github.com/pydap/pydap/pull/223/commits
    return data_store


data_store = copernicusmarine_datastore(DATASET_ID, USERNAME, PASSWORD)

ds=xr.open_dataset(data_store)

ds=ds['so'] #### selecting salinity variable 

ds=ds.sel(depth=0.494025)

ds=ds.sel(time=date) ##selecting the depth and the date (surface salinity )  

ds.to_netcdf('foo.nc',format="NETCDF3_64BIT")


