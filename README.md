Readme made 2 Oct 2018- Sarah Mc

This contains 3 replicas of 4 MICROSECONDS each simulation time
All .trr files removed
the 0-4us.skip50.xtc files were used for analysis in ./analysis
	These are 1 frame per 5ns => 800 frames in each replica

if you're wondering why this is called segmented_ATP_synthase it's because each dimer has ~60 chains, didn't separate them at first into separate topologies, so this was initially just a trial to see if my separation techinque worked. It did so the directory is named as such :)

Despite the simulation name, each .xtc contains 2 microseconds, not 3 (I thought I could reach 30fs timestep when I started production but it was not stable and I don't know why I didn't ever change the name beyond that - other replicas kept the same title for consistency sake...)


Some good info to know:
- each equilib is in 8 steps, same conditions for all
- this was run on TCB cluster using 2GPU's - I'd say I would get an average of 150ns a day, so 4us took about a month to complete
- Same dimer in all 3 replicates, the only thing that is different is lipid placement, concentration is the same in all 3 
- some readme info in replica_2/system_setup on how I made the system




