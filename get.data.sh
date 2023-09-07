#!/bin/bash

for y in 1999;do 

echo "downloading ..." $y

#python -m motuclient --motu http://my.cmems-du.eu/motu-web/Motu --service-id MULTIOBS_GLO_PHY_REP_015_004-DGF --product-id global-reanalysis-phy-001-030-daily --longitude-min -100 --longitude-max -55 --latitude-min 6 --latitude-max 30 --date-min "$y-01-01 12:00:00" --date-max "$y-12-25 12:00:00" --depth-min 0.493 --depth-max 0.4942 --variable so --out-dir "./" --out-name "so.$y.nc" --user "lschwartz" --pwd "9ribouillE*"

python -m motuclient -u lschwartz -p  "9ribouillE*" --motu https://my.cmems-du.eu/motu-web/Motu -s  -d dataset-uv-rep-monthly -t "2000-01-01 null" -T "2000-12-31 null" -o "./" -f "so.$y.nc" 
done
