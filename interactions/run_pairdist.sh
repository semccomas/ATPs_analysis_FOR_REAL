rep=3
input_fdir=/data2/segmented_ATP_synthase/analysis/input_files/files_rep$rep

echo 'POPA'

gmx pairdist -f ../../replica_$rep/production/ATPs$rep.0-4us.skip50.xtc -s ../../replica_$rep/production/ATPs$rep.1.3us.tpr -n $input_fdir/final_sel.ndx -xvg none -selgrouping res -refgrouping res -cutoff 1.1 -o xvg_files/POPA.A.$rep.xvg -sel '21' -ref 'group 26 and name PO4 GL1 GL2'

gmx pairdist -f ../../replica_$rep/production/ATPs$rep.0-4us.skip50.xtc -s ../../replica_$rep/production/ATPs$rep.1.3us.tpr -n $input_fdir/final_sel.ndx -xvg none -selgrouping res -refgrouping res -cutoff 1.1 -o xvg_files/POPA.B.$rep.xvg -sel '22' -ref 'group 26 and name PO4 GL1 GL2'



#echo 'POPC'

#gmx pairdist -f ../../replica_$rep/production/ATPs$rep.0-4us.skip50.xtc -s ../../replica_$rep/production/ATPs.$re1.p.3us.tpr -n $input_fdir/final_sel.ndx -xvg none -selgrouping res -refgrouping res -cutoff 1.1 -o xvg_files/POPC.A.$rep.xvg -sel '21' -ref 'group 23 and name PO4 GL1 GL2 NC3'

#gmx pairdist -f ../../replica_$rep/production/ATPs$rep.0-4us.skip50.xtc -s ../../replica_$rep/production/ATPs.$re1.p.3us.tpr -n $input_fdir/final_sel.ndx -xvg none -selgrouping res -refgrouping res -cutoff 1.1 -o xvg_files/POPC.B.$rep.xvg -sel '22' -ref 'group 23 and name PO4 GL1 GL2 NC3'


echo 'POPE'

gmx pairdist -f ../../replica_$rep/production/ATPs$rep.0-4us.skip50.xtc -s ../../replica_$rep/production/ATPs$rep.1.3us.tpr -n $input_fdir/final_sel.ndx -xvg none -selgrouping res -refgrouping res -cutoff 1.1 -o xvg_files/POPE.A.$rep.xvg -sel '21' -ref 'group 24 and name PO4 GL1 GL2 NH3'

gmx pairdist -f ../../replica_$rep/production/ATPs$rep.0-4us.skip50.xtc -s ../../replica_$rep/production/ATPs$rep.1.3us.tpr -n $input_fdir/final_sel.ndx -xvg none -selgrouping res -refgrouping res -cutoff 1.1 -o xvg_files/POPE.B.$rep.xvg -sel '22' -ref 'group 24 and name PO4 GL1 GL2 NH3'


echo 'CDL2'

gmx pairdist -f ../../replica_$rep/production/ATPs$rep.0-4us.skip50.xtc -s ../../replica_$rep/production/ATPs$rep.1.3us.tpr -n $input_fdir/final_sel.ndx -xvg none -selgrouping res -refgrouping res -cutoff 1.1 -o xvg_files/CDL2.A.$rep.xvg -sel '21' -ref 'group 25 and name GL0 1PO4 1GL1 1GL2 2PO4 1GL2 2GL2'

gmx pairdist -f ../../replica_$rep/production/ATPs$rep.0-4us.skip50.xtc -s ../../replica_$rep/production/ATPs$rep.1.3us.tpr -n $input_fdir/final_sel.ndx -xvg none -selgrouping res -refgrouping res -cutoff 1.1 -o xvg_files/CDL2.B.$rep.xvg -sel '22' -ref 'group 25 and name GL0 1PO4 1GL1 1GL2 2PO4 1GL2 2GL2'





echo 'POPC'

gmx pairdist -f ../../replica_$rep/production/ATPs$rep.1.3us.skip50.xtc -s ../../replica_$rep/production/ATPs$rep.1.3us.tpr -n $input_fdir/final_sel.ndx -xvg none -selgrouping res -refgrouping res -cutoff 1.1 -o xvg_files/POPC.A.$rep.0-400.xvg -sel '21' -ref 'group 23 and name PO4 GL1 GL2 NC3'

gmx pairdist -f ../../replica_$rep/production/ATPs$rep.1.3us.skip50.xtc -s ../../replica_$rep/production/ATPs$rep.1.3us.tpr -n $input_fdir/final_sel.ndx -xvg none -selgrouping res -refgrouping res -cutoff 1.1 -o xvg_files/POPC.B.$rep.0-400.xvg -sel '22' -ref 'group 23 and name PO4 GL1 GL2 NC3'



gmx pairdist -f ../../replica_$rep/production/ATPs$rep.2.3us.skip50.xtc -s ../../replica_$rep/production/ATPs$rep.2.3us.tpr -n $input_fdir/final_sel.ndx -xvg none -selgrouping res -refgrouping res -cutoff 1.1 -o xvg_files/POPC.A.$rep.400-800.xvg -sel '21' -ref 'group 23 and name PO4 GL1 GL2 NC3'

gmx pairdist -f ../../replica_$rep/production/ATPs$rep.2.3us.skip50.xtc -s ../../replica_$rep/production/ATPs$rep.2.3us.tpr -n $input_fdir/final_sel.ndx -xvg none -selgrouping res -refgrouping res -cutoff 1.1 -o xvg_files/POPC.B.$rep.400-800.xvg -sel '22' -ref 'group 23 and name PO4 GL1 GL2 NC3'


