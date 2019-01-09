#PA
gmx pairdist -f ../../replica_3/production/ATPs3.0-4us.skip50.xtc -s ../../replica_3/equilibration/minim.tpr -n ../input_files/files_rep3/ALL_pocket_selection.ndx -xvg none -selgrouping res -cutoff 2.3 -ref 'com of group 19' -sel 16 -o POPA_A_3.xvg
gmx pairdist -f ../../replica_3/production/ATPs3.0-4us.skip50.xtc -s ../../replica_3/equilibration/minim.tpr -n ../input_files/files_rep3/ALL_pocket_selection.ndx -xvg none -selgrouping res -cutoff 2.3 -ref 'com of group 20' -sel 16 -o POPA_B_3.xvg

#PC
gmx pairdist -f ../../replica_3/production/ATPs3.0-4us.skip50.xtc -s ../../replica_3/equilibration/minim.tpr -n ../input_files/files_rep3/ALL_pocket_selection.ndx -xvg none -selgrouping res -cutoff 2.3 -ref 'com of group 19' -sel 13 -o POPC_A_3.xvg
gmx pairdist -f ../../replica_3/production/ATPs3.0-4us.skip50.xtc -s ../../replica_3/equilibration/minim.tpr -n ../input_files/files_rep3/ALL_pocket_selection.ndx -xvg none -selgrouping res -cutoff 2.3 -ref 'com of group 20' -sel 13 -o POPC_B_3.xvg

#PE
gmx pairdist -f ../../replica_3/production/ATPs3.0-4us.skip50.xtc -s ../../replica_3/equilibration/minim.tpr -n ../input_files/files_rep3/ALL_pocket_selection.ndx -xvg none -selgrouping res -cutoff 2.3 -ref 'com of group 19' -sel 14 -o POPE_A_3.xvg
gmx pairdist -f ../../replica_3/production/ATPs3.0-4us.skip50.xtc -s ../../replica_3/equilibration/minim.tpr -n ../input_files/files_rep3/ALL_pocket_selection.ndx -xvg none -selgrouping res -cutoff 2.3 -ref 'com of group 20' -sel 14 -o POPE_B_3.xvg


#CDL
gmx pairdist -f ../../replica_3/production/ATPs3.0-4us.skip50.xtc -s ../../replica_3/equilibration/minim.tpr -n ../input_files/files_rep3/ALL_pocket_selection.ndx -xvg none -selgrouping res -cutoff 2.3 -ref 'com of group 19' -sel 15 -o CDL2_A_3.xvg
gmx pairdist -f ../../replica_3/production/ATPs3.0-4us.skip50.xtc -s ../../replica_3/equilibration/minim.tpr -n ../input_files/files_rep3/ALL_pocket_selection.ndx -xvg none -selgrouping res -cutoff 2.3 -ref 'com of group 20' -sel 15 -o CDL2_B_3.xvg

