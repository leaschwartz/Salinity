import xarray as xr

# Dataset ID
DATASET_ID = "global-analysis-forecast-phy-001-024"

# Subsetting parameters
TIME = '2022-01-01'
DEPTH = 0
LATITUDE = slice(35,60)
LONGITUDE = slice(-15,5)

# Read product via OPeNDAP
DS = (
    xr.open_dataset(f"https://nrt.cmems-du.eu/thredds/dodsC/global-analysis-forecast-phy-001-024")
    .sel(time=TIME, latitude=LATITUDE, longitude=LONGITUDE)
    .isel(depth=DEPTH)
)
