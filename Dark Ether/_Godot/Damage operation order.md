1. Calculate unmitigated damage
	- Flat damage:
		1. Get the skills min and max damage for Spells and Get the weapon's min and max base damages for Attacks.
		2. Add all "added damage".
		3. Apply damage conversion.
		4. Calculate a random damage in the min/max range for each damage type.
		   
	* Damage Multipliers
		1. Apply the skill's damage multiplier on each results.
		2. Apply all increased damage.
		3. Apply all more damage.
		
			Damage formula at this point is:
			Damage = ((Base_Damage + Added_Damage) x Increased_Damage) x More_Damage)
		   
1. Calculate mitigate damage
	1. Convert the "Damage taken as"
	2. Apply corresponding resistance on each damage type
	3. 
2. 
3. Applying Status Effect
4. Take the final damage