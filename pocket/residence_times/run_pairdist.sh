#PA
gmx pairdist -f ../../../replica_1/production/ATPs1.0-4us.skip50.xtc -s ../../../replica_1/equilibration/minim.tpr -n ../../input_files/files_rep1/ALL_pocket_selection.ndx -xvg none -selgrouping res -cutoff 3.5 -ref 'com of group 19' -sel 16 -o 3.5_cutoff/POPA_A_1.xvg
gmx pairdist -f ../../../replica_1/production/ATPs1.0-4us.skip50.xtc -s ../../../replica_1/equilibration/minim.tpr -n ../../input_files/files_rep1/ALL_pocket_selection.ndx -xvg none -selgrouping res -cutoff 3.5 -ref 'com of group 20' -sel 16 -o 3.5_cutoff/POPA_B_1.xvg

#PC
gmx pairdist -f ../../../replica_1/production/ATPs1.0-4us.skip50.xtc -s ../../../replica_1/equilibration/minim.tpr -n ../../input_files/files_rep1/ALL_pocket_selection.ndx -xvg none -selgrouping res -cutoff 3.5 -ref 'com of group 19' -sel 13 -o 3.5_cutoff/POPC_A_1.xvg
gmx pairdist -f ../../../replica_1/production/ATPs1.0-4us.skip50.xtc -s ../../../replica_1/equilibration/minim.tpr -n ../../input_files/files_rep1/ALL_pocket_selection.ndx -xvg none -selgrouping res -cutoff 3.5 -ref 'com of group 20' -sel 13 -o 3.5_cutoff/POPC_B_1.xvg

#PE
gmx pairdist -f ../../../replica_1/production/ATPs1.0-4us.skip50.xtc -s ../../../replica_1/equilibration/minim.tpr -n ../../input_files/files_rep1/ALL_pocket_selection.ndx -xvg none -selgrouping res -cutoff 3.5 -ref 'com of group 19' -sel 14 -o 3.5_cutoff/POPE_A_1.xvg
gmx pairdist -f ../../../replica_1/production/ATPs1.0-4us.skip50.xtc -s ../../../replica_1/equilibration/minim.tpr -n ../../input_files/files_rep1/ALL_pocket_selection.ndx -xvg none -selgrouping res -cutoff 3.5 -ref 'com of group 20' -sel 14 -o 3.5_cutoff/POPE_B_1.xvg


#CDL
gmx pairdist -f ../../../replica_1/production/ATPs1.0-4us.skip50.xtc -s ../../../replica_1/equilibration/minim.tpr -n ../../input_files/files_rep1/ALL_pocket_selection.ndx -xvg none -selgrouping res -cutoff 3.5 -ref 'com of group 19' -sel 15 -o 3.5_cutoff/CDL2_A_1.xvg
gmx pairdist -f ../../../replica_1/production/ATPs1.0-4us.skip50.xtc -s ../../../replica_1/equilibration/minim.tpr -n ../../input_files/files_rep1/ALL_pocket_selection.ndx -xvg none -selgrouping res -cutoff 3.5 -ref 'com of group 20' -sel 15 -o 3.5_cutoff/CDL2_B_1.xvg







#PA
gmx pairdist -f ../../../replica_2/production/ATPs2.0-4us.skip50.xtc -s ../../../replica_2/equilibration/minim.tpr -n ../../input_files/files_rep2/ALL_pocket_selection.ndx -xvg none -selgrouping res -cutoff 3.5 -ref 'com of group 19' -sel 16 -o 3.5_cutoff/POPA_A_2.xvg
gmx pairdist -f ../../../replica_2/production/ATPs2.0-4us.skip50.xtc -s ../../../replica_2/equilibration/minim.tpr -n ../../input_files/files_rep2/ALL_pocket_selection.ndx -xvg none -selgrouping res -cutoff 3.5 -ref 'com of group 20' -sel 16 -o 3.5_cutoff/POPA_B_2.xvg

#PC
gmx pairdist -f ../../../replica_2/production/ATPs2.0-4us.skip50.xtc -s ../../../replica_2/equilibration/minim.tpr -n ../../input_files/files_rep2/ALL_pocket_selection.ndx -xvg none -selgrouping res -cutoff 3.5 -ref 'com of group 19' -sel 13 -o 3.5_cutoff/POPC_A_2.xvg
gmx pairdist -f ../../../replica_2/production/ATPs2.0-4us.skip50.xtc -s ../../../replica_2/equilibration/minim.tpr -n ../../input_files/files_rep2/ALL_pocket_selection.ndx -xvg none -selgrouping res -cutoff 3.5 -ref 'com of group 20' -sel 13 -o 3.5_cutoff/POPC_B_2.xvg

#PE
gmx pairdist -f ../../../replica_2/production/ATPs2.0-4us.skip50.xtc -s ../../../replica_2/equilibration/minim.tpr -n ../../input_files/files_rep2/ALL_pocket_selection.ndx -xvg none -selgrouping res -cutoff 3.5 -ref 'com of group 19' -sel 14 -o 3.5_cutoff/POPE_A_2.xvg
gmx pairdist -f ../../../replica_2/production/ATPs2.0-4us.skip50.xtc -s ../../../replica_2/equilibration/minim.tpr -n ../../input_files/files_rep2/ALL_pocket_selection.ndx -xvg none -selgrouping res -cutoff 3.5 -ref 'com of group 20' -sel 14 -o 3.5_cutoff/POPE_B_2.xvg


#CDL
gmx pairdist -f ../../../replica_2/production/ATPs2.0-4us.skip50.xtc -s ../../../replica_2/equilibration/minim.tpr -n ../../input_files/files_rep2/ALL_pocket_selection.ndx -xvg none -selgrouping res -cutoff 3.5 -ref 'com of group 19' -sel 15 -o 3.5_cutoff/CDL2_A_2.xvg
gmx pairdist -f ../../../replica_2/production/ATPs2.0-4us.skip50.xtc -s ../../../replica_2/equilibration/minim.tpr -n ../../input_files/files_rep2/ALL_pocket_selection.ndx -xvg none -selgrouping res -cutoff 3.5 -ref 'com of group 20' -sel 15 -o 3.5_cutoff/CDL2_B_2.xvg









#PA
gmx pairdist -f ../../../replica_3/production/ATPs3.0-4us.skip50.xtc -s ../../../replica_3/equilibration/minim.tpr -n ../../input_files/files_rep3/ALL_pocket_selection.ndx -xvg none -selgrouping res -cutoff 3.5 -ref 'com of group 19' -sel 16 -o 3.5_cutoff/POPA_A_3.xvg
gmx pairdist -f ../../../replica_3/production/ATPs3.0-4us.skip50.xtc -s ../../../replica_3/equilibration/minim.tpr -n ../../input_files/files_rep3/ALL_pocket_selection.ndx -xvg none -selgrouping res -cutoff 3.5 -ref 'com of group 20' -sel 16 -o 3.5_cutoff/POPA_B_3.xvg

#PC
gmx pairdist -f ../../../replica_3/production/ATPs3.0-4us.skip50.xtc -s ../../../replica_3/equilibration/minim.tpr -n ../../input_files/files_rep3/ALL_pocket_selection.ndx -xvg none -selgrouping res -cutoff 3.5 -ref 'com of group 19' -sel 13 -o 3.5_cutoff/POPC_A_3.xvg
gmx pairdist -f ../../../replica_3/production/ATPs3.0-4us.skip50.xtc -s ../../../replica_3/equilibration/minim.tpr -n ../../input_files/files_rep3/ALL_pocket_selection.ndx -xvg none -selgrouping res -cutoff 3.5 -ref 'com of group 20' -sel 13 -o 3.5_cutoff/POPC_B_3.xvg

#PE
gmx pairdist -f ../../../replica_3/production/ATPs3.0-4us.skip50.xtc -s ../../../replica_3/equilibration/minim.tpr -n ../../input_files/files_rep3/ALL_pocket_selection.ndx -xvg none -selgrouping res -cutoff 3.5 -ref 'com of group 19' -sel 14 -o 3.5_cutoff/POPE_A_3.xvg
gmx pairdist -f ../../../replica_3/production/ATPs3.0-4us.skip50.xtc -s ../../../replica_3/equilibration/minim.tpr -n ../../input_files/files_rep3/ALL_pocket_selection.ndx -xvg none -selgrouping res -cutoff 3.5 -ref 'com of group 20' -sel 14 -o 3.5_cutoff/POPE_B_3.xvg


#CDL
gmx pairdist -f ../../../replica_3/production/ATPs3.0-4us.skip50.xtc -s ../../../replica_3/equilibration/minim.tpr -n ../../input_files/files_rep3/ALL_pocket_selection.ndx -xvg none -selgrouping res -cutoff 3.5 -ref 'com of group 19' -sel 15 -o 3.5_cutoff/CDL2_A_3.xvg
gmx pairdist -f ../../../replica_3/production/ATPs3.0-4us.skip50.xtc -s ../../../replica_3/equilibration/minim.tpr -n ../../input_files/files_rep3/ALL_pocket_selection.ndx -xvg none -selgrouping res -cutoff 3.5 -ref 'com of group 20' -sel 15 -o 3.5_cutoff/CDL2_B_3.xvg

