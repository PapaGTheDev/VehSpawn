# VehSpawn
Grab Vehicle Spawn Codes from Handling.meta and create lua table for QBCore vehicles.

Tested on
Ubuntu 22
Python 3.10.12

*At this point the script does not remove duplicates, I'll update this later*

Install:
Install Requirements
Clone Repo
Replace: 
    folder_path = "Vehicles Folder"
    
With your actual vehicle's folder name, in our case its [Vehicles] (you need to supply full path!)
Usage: 
python3 vehicles.py

Vehicle Spawn in Lua table will be created in console, just copy and paste


Updated - 5/3/24

Added createshop.py 
This will create a shop table with all of your vehicles from handling.meta search. 
Script will output a config.lua with the shop template. 

Just remove what you dont need, dont forget to update the XYZ coords for each car you add. 

https://i.imgur.com/NOyR5k2.png

