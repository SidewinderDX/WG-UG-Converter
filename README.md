# WG-UG-Converter
Converts the regions.yml from WorldGuard to the UniverseGuard Format

During our server conversion into something with mods, we felt the need to take our WorldGuard Protections with us. But how? There was that awesome looking sponge plugin called UniverseGuard, sadly it comes without any way to easily Convert the old WorldGuard Stuff into its own Format... So here we go!

Testet on our old MC1.8 Server, works just fine.

How to:
Locate youre regions.yml file (*.\plugins\WorldGuard\worlds*) and copy it into the folder where the WG_UG_converter is located.
Now run the converter (*python WG_UG_converter.py*).
It will create one file called *index.json* and one folder called *regions*. Copy thoe two into the *./config/universeguard* folder and it should work just fine.

**As always BACKUP the server before changing anything**

Known Bugs:


Links to UniverseGuard
* https://ore.spongepowered.org/Francesco_Jimi/Universe-Guard
* https://github.com/JimiIT92/UniverseGuard2
