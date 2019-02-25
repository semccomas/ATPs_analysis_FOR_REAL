###commands used

cd files_rep3

rm plain_index.ndx
gmx make_ndx -f ATPs3.system.pre_eq.pdb -o plain_index.ndx << EOF
q
EOF

#make protein pocket
gmx select -f ATPs3.system.pre_eq.pdb -n plain_index.ndx -on protein_pocket.ndx -ofpdb protein_pocket.pdb -select -sf ../selection_proteins.dat -s ../../../replica_3/equilibration/minim.tpr

rm ALL_pocket_selection.ndx
cat plain_index.ndx >> ALL_pocket_selection.ndx
cat protein_pocket.ndx >> ALL_pocket_selection.ndx



