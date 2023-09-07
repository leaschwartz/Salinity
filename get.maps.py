import xarray as xr
from matplotlib import cm
from matplotlib.backends.backend_pdf import PdfPages
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import cartopy.io.img_tiles as cimgt
import cmocean
import cartopy.mpl.geoaxes
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
import pandas as pd
import matplotlib.pylab as mpl
import seaborn as sb 
def plot(ax,ds,levs=20,label="",cmap=None,title=""):
	"""
		plot world maps """
	ds.plot(ax=ax,cmap=cmap,levels=levs,cbar_kwargs={'label': label})
	ax.set_title(title)
	ax.add_feature(cfeature.BORDERS)
	ax.coastlines(resolution='10m',color='black',linewidth=1)


def plot_box(ax,ds,lo1,lo2,la1,la2,levs=20,label="",cmap=None,title=""):
	"""
		plot world maps """
	ds.plot(ax=ax,cmap=cmap,levels=levs,cbar_kwargs={'label': label})
	ax.set_title(title)
	ax.add_feature(cfeature.BORDERS)
	ax.coastlines(resolution='10m',color='black',linewidth=1)
	ax.set_extent([lo1,lo2,la1,la2])
	ax.add_feature(cfeature.BORDERS)

def colorbar(cmap,levs1,levs2):
	lower_bias=cmap(np.linspace(0,0.5,int(len(levs1)))) #np.ones((1,4)) #[[1,1,1,1]] 
	upper_bias =cmap(np.linspace(1-0.5, 1,int(len(levs2)))) #cmap(np.linspace(0, 1,20))
	colors_bias = np.vstack((lower_bias,upper_bias))
	cmap_new = mcolors.LinearSegmentedColormap.from_list('map_white', colors_bias)
	return cmap_new

#pdfname="salinity.pdf"
#pdf=PdfPages(pdfname)

lo1=104.5
lo2=110
la1=8.5
la2=23.5

#vietnam location 
lon=105.8537
lat=9.2003
cmap=cm.YlGnBu_r#cmocean.cm.haline

#levs=np.arange(32,38,0.1)
#ds=xr.open_dataset('mercatorglorys12v1.so.mean.mo.ab.nc')
#ds2=xr.open_dataset('mercatorglorys12v1.so.max.mo.ab.nc')

#ts=ds['so'].interp({"longitude":lon,"latitude":lat},method='nearest').resample({'time':'AS'}).mean()
#ts2=ds['so'].interp({"longitude":lon,"latitude":lat},method='nearest').groupby('time.month').mean()
#tsmax=ds2['so'].interp({"longitude":lon,"latitude":lat},method='nearest').resample({'time':'AS'}).mean()
#ts2max=ds2['so'].interp({"longitude":lon,"latitude":lat},method='nearest').groupby('time.month').mean()
#
#fig,ax=plt.subplots(2,1,figsize=(15,7))
#axesf=ax.flat
#ts.plot(ax=axesf[0])
#tsmax.plot(ax=axesf[1])	
#axesf[0].set_title('Observed sea surface salinity mean annual 1993/2020-05')
#axesf[1].set_title('Observed sea surface salinity max annual 1993/2020-05')
#fig.tight_layout()
#plt.show()
#
#fig,ax=plt.subplots(2,1,figsize=(15,7))
#axesf=ax.flat
#ts2.plot(ax=axesf[0])
#ts2max.plot(ax=axesf[1])
#axesf[0].set_title('Observed sea surface salinity mean seasonal cycle 1993/2020-05')
#axesf[1].set_title('Observed sea surface salinity max seasonal cycle 1993/2020-05')
#fig.tight_layout()
#plt.show()

#fig,ax=plt.subplots(2,1,figsize=(15,7),subplot_kw={"projection":ccrs.PlateCarree()})
#axesf=ax.flat
#plot(axesf[1],ds2['so'].mean('time'),levs=levs, cmap=cmap,title='Observed mean sea surface salinity max 1993/2020-05')
#plot(axesf[0],ds['so'].mean('time'),cmap=cmap,levs=levs,title='Observed mean sea surface salinity mean 1993/2020-05')
##pdf.savefig(fig)
##plt.close()
#plt.show()

#fig,ax=plt.subplots(1,2,figsize=(15,7),subplot_kw={"projection":ccrs.PlateCarree()})
#axesf=ax.flat
#levs=np.arange(32,36,0.1)
#
#plot_box(axesf[0],ds['so'].mean('time'),lo1,lo2,la1,la2,cmap=cmap,levs=levs,title='Observed mean sea surface salinity mean 1993/2020-05')
#plot_box(axesf[1],ds2['so'].mean('time'),lo1,lo2,la1,la2,levs=levs, cmap=cmap,title='Observed mean sea surface salinity max 1993/2020-05')
##pdf.savefig(fig2)
##plt.close()
#plt.show()

levs=np.arange(-0.05,0.055,0.005)
ds=xr.open_dataset('trend.b.so.mean.nc')
ds2=xr.open_dataset('trend.b.so.max.nc')
cmap=cm.bwr
cmap_new=colorbar(cmap,np.arange(-0.05,0,0.005),np.arange(0,0.055,0.005))
fig,ax=plt.subplots(2,1,figsize=(15,7),subplot_kw={"projection":ccrs.PlateCarree()})
axesf=ax.flat
plot(axesf[1],ds2['so']*10,levs=levs, cmap=cmap_new,title='Observed trend sea surface salinity max 1993/2019')
plot(axesf[0],ds['so']*10,cmap=cmap_new,levs=levs,title='Observed trend sea surface salinity mean 1993/2019')
#pdf.savefig(fig)
#plt.close()
plt.show()

fig,ax=plt.subplots(1,2,figsize=(15,7),subplot_kw={"projection":ccrs.PlateCarree()})
axesf=ax.flat

plot_box(axesf[0],ds['so']*10,lo1,lo2,la1,la2,cmap=cmap_new,levs=levs,title='Observed trend sea surface salinity mean 1993/2019')
plot_box(axesf[1],ds2['so']*10,lo1,lo2,la1,la2,levs=levs, cmap=cmap_new,title='Observed trend sea surface salinity max 1993/2019')
#pdf.savefig(fig2)
#plt.close()
plt.show()


