##fatslim apl --apl-by-type -c 4YB9.6.us.gro -t 4YB9.6.us.20frames.xtc -n bilayer_all.ndx --export-apl-raw test2.csv --plot-apl dppc_vesicle_apl.xvg



##fatslim apl --apl-by-type -c ../../../replica_3/equilibration/ATPs3.7.eq.gro -t replica_3/ATPs3.0-4us.40frames.xtc -n ../../input_files/files_rep3/APL_phos_head.ndx --export-apl-raw replica_3/rep3.csv --apl-cutoff 5.0 --apl-limit 20 

fatslim thickness -c ../../../replica_3/equilibration/ATPs3.7.eq.gro -t replica_3/ATPs3.0-4us.40frames.xtc -n ../../input_files/files_rep3/APL_phos_head.ndx --export-thickness-raw replica_3/thickness_rep3.csv 


#for i in replica_3/*.csv; do 
#sed -i 's/^87//g' $i
#sed -i 's/^0//g' $i
#done
