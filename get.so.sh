#!/bin/bash 

rm -f foo.nc

for y in 2016;do
	for m in $(seq -f %02.0f 10 12);do
		nd=$(cal $m $y |tr ' ' '\n' | grep -v ^$ | tail -1)
		rm -f tmp/mercatorglorys12v1.so.$y$m.da.ab.nc
		for d in $(seq -f %02.0f 1 $nd);do
			o=tmp/foo.so.$y$m$d.da.ab.nc
			echo $y $m $d
			while [ ! -f foo.nc ];do 
				python -u get.so.da.py $y $m $d
			done 
			cp foo.nc $o
			rm foo.nc
			cdo -s cat $o tmp/mercatorglorys12v1.so.$y$m.da.ab.nc
		done 
		rm tmp/foo.*.nc
		f=tmp/mercatorglorys12v1.so.$y$m.da.ab.nc
		mean=mercatorglorys12v1.so.mean.mo.ab.nc
		max=mercatorglorys12v1.so.max.mo.ab.nc
		cdo -s cat -timmean $f $mean 
		cdo -s cat -timmax $f $max 
	done 
done 

for y in `seq 2017 2019`;do
    for m in $(seq -f %02.0f 01 12);do
        nd=$(cal $m $y |tr ' ' '\n' | grep -v ^$ | tail -1)
        rm -f tmp/mercatorglorys12v1.so.$y$m.da.ab.nc
        for d in $(seq -f %02.0f 1 $nd);do
            o=tmp/foo.so.$y$m$d.da.ab.nc
            echo $y $m $d
            while [ ! -f foo.nc ];do 
                python -u get.so.da.py $y $m $d
            done 
            cp foo.nc $o
            rm foo.nc
            cdo -s cat $o tmp/mercatorglorys12v1.so.$y$m.da.ab.nc
        done 
        rm tmp/foo.*.nc
        f=tmp/mercatorglorys12v1.so.$y$m.da.ab.nc
        mean=mercatorglorys12v1.so.mean.mo.ab.nc
        max=mercatorglorys12v1.so.max.mo.ab.nc
        cdo -s cat -timmean $f $mean 
        cdo -s cat -timmax $f $max 
    done 
done 

for y in 2020;do
    for m in $(seq -f %02.0f 01 05);do
        nd=$(cal $m $y |tr ' ' '\n' | grep -v ^$ | tail -1)
        rm -f tmp/mercatorglorys12v1.so.$y$m.da.ab.nc
        for d in $(seq -f %02.0f 1 $nd);do
            o=tmp/foo.so.$y$m$d.da.ab.nc
            echo $y $m $d
            while [ ! -f foo.nc ];do 
                python -u get.so.da.py $y $m $d
            done 
            cp foo.nc $o
            rm foo.nc
            cdo -s cat $o tmp/mercatorglorys12v1.so.$y$m.da.ab.nc
        done 
        rm tmp/foo.*.nc
        f=tmp/mercatorglorys12v1.so.$y$m.da.ab.nc
        mean=mercatorglorys12v1.so.mean.mo.ab.nc
        max=mercatorglorys12v1.so.max.mo.ab.nc
        cdo -s cat -timmean $f $mean 
        cdo -s cat -timmax $f $max 
    done 
done 


echo "DONE !"
