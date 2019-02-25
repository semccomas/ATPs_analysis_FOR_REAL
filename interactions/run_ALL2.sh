##echo 'make pairdist 1'
##
##sed -i 's/rep=./rep=1/g' run_pairdist.sh
##bash run_pairdist.sh
##
##cd xvg_files
##echo 'boolean 1'
##sed -i 's/.3.xvg/.1.xvg/g' boolean_matrix.sh
##sed -i 's/3.0-400.xvg/1.0-400.xvg/g' boolean_matrix.sh
##sed -i 's/3.400-800.xvg/1.400-800.xvg/g' boolean_matrix.sh
##bash boolean_matrix.sh
##
##echo 'pytable'
##sed -i 's/\.3/.1/g' run_parse_and_pytable.sh
##sed -i 's/rep1/rep1/g' run_parse_and_pytable.sh
##bash run_parse_and_pytable.sh
##
##cd ..
##echo 'REP 1 DONE!!'






##echo 'make pairdist 2'
##
##sed -i 's/rep=./rep=2/g' run_pairdist.sh
#bash run_pairdist.sh
##
#cd xvg_files
##echo 'boolean 2'
##sed -i 's/.3.xvg/.2.xvg/g' boolean_matrix2.sh
##sed -i 's/3.0-400.xvg/2.0-400.xvg/g' boolean_matrix2.sh
##sed -i 's/3.400-800.xvg/2.400-800.xvg/g' boolean_matrix2.sh
#bash boolean_matrix2.sh
##
##echo 'pytable'
##sed -i 's/\.3/.2/g' run_parse_and_pytable.sh
##sed -i 's/rep3/rep2/g' run_parse_and_pytable.sh
#bash run_parse_and_pytable.sh
##
##cd ..
##echo 'REP 2 DONE!!'
##
##
##
##
##
##
##echo 'make pairdist 3'
##
##sed -i 's/rep=./rep=3/g' run_pairdist.sh
bash run_pairdist.sh
##
cd xvg_files
##echo 'boolean 3'
##sed -i 's/.2.xvg/.3.xvg/g' boolean_matrix2.sh
##sed -i 's/2.0-400.xvg/3.0-400.xvg/g' boolean_matrix2.sh
##sed -i 's/2.400-800.xvg/3.400-800.xvg/g' boolean_matrix2.sh
bash boolean_matrix2.sh
##
##echo 'pytable'
##sed -i 's/\.2/.3/g' run_parse_and_pytable.sh
##sed -i 's/rep2/rep3/g' run_parse_and_pytable.sh
bash run_parse_and_pytable2.sh
##
##cd ..
##echo 'REP 3 DONE!!'




