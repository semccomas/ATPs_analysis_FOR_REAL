END=438
rep=1 #oBS remember to change tpr in rep2
for i in $(seq 1 $END)
do
echo $i
gmx rdf -f ../../replica_1/production/ATPs1.0-4us.skip50.xtc -s ../../replica_1/production/ATPs.1.3us.tpr -n ../input_files/files_rep1/RDF_and_nobadlip_rep1.ndx -xvg none -o new_xvg/RDF.1.$i.xvg -ref $i -sel -sf lipid_selection.dat
done



rep=2 #oBS remember to change tpr in rep2
for i in $(seq 1 $END)
do
echo $i
gmx rdf -f ../../replica_2/production/ATPs2.0-4us.skip50.xtc -s ../../replica_2/production/ATPs2.1.3us.tpr -n ../input_files/files_rep2/RDF_and_nobadlip_rep2.ndx -xvg none -o new_xvg/RDF.2.$i.xvg -ref $i -sel -sf lipid_selection.dat
done




rep=3 #oBS remember to change tpr in rep2
for i in $(seq 1 $END)
do
echo $i
gmx rdf -f ../../replica_3/production/ATPs3.0-4us.skip50.xtc -s ../../replica_3/production/ATPs3.1.3us.tpr -n ../input_files/files_rep3/RDF_and_nobadlip_rep3.ndx -xvg none -o new_xvg/RDF.3.$i.xvg -ref $i -sel -sf lipid_selection.dat
done

