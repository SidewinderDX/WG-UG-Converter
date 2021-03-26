class UG:
    def __init__(self):
        self.data = {
            "FIRST_POINT" : {
                "x" : 0,
                "y" : 0,
                "z" : 0,
                "dimension" : "minecraft:overworld",
                "world" : "world"
            },
            "SECOND_POINT" : {
                "x" : 0,
                "y" : 0,
                "z" : 0,
                "dimension" : "minecraft:overworld",
                "world" : "world"
            },
            "PRIORITY" : 0,
            "TELEPORT_LOCATION" : {
                "x" : 0,
                "y" : 0,
                "z" : 0,
                "dimension" : "minecraft:overworld",
                "world" : "world"
            },
            "SPAWN_LOCATION" : {
                "x" : 0,
                "y" : 0,
                "z" : 0,
                "dimension" : "minecraft:overworld",
                "world" : "world"
            },
            "MEMBERS" : [],
            "FAREWELL_MESSAGE": "",
            "GREETING_MESSAGE": "",
            "EFFECTS": [],
            "SOLD": False,
            "VALUE": None,
            "VERSION": 2.34,
            "ID": "",
            "TYPE": "LOCAL",
            "NAME": "",
            "GAMEMODE": "minecraft:not_set",
            "FLAGS": [
                {
                "name": "place",
                "value": False
                },
                {
                "name": "destroy",
                "value": False
                },
                {
                "name": "pvp",
                "value": True
                },
                {
                "name": "expdrop",
                "value": True
                },
                {
                "name": "itemdrop",
                "value": True
                },
                {
                "name": "itempickup",
                "value": True
                },
                {
                "name": "enderpearl",
                "value": True
                },
                {
                "name": "sleep",
                "value": True
                },
                {
                "name": "lighter",
                "value": False
                },
                {
                "name": "chests",
                "value": False
                },
                {
                "name": "trappedchests",
                "value": False
                },
                {
                "name": "waterflow",
                "value": True
                },
                {
                "name": "lavaflow",
                "value": True
                },
                {
                "name": "otherliquidsflow",
                "value": True
                },
                {
                "name": "leafdecay",
                "value": True
                },
                {
                "name": "firespread",
                "value": True
                },
                {
                "name": "potionsplash",
                "value": True
                },
                {
                "name": "falldamage",
                "value": True
                },
                {
                "name": "cantp",
                "value": False
                },
                {
                "name": "canspawn",
                "value": False
                },
                {
                "name": "hunger",
                "value": True
                },
                {
                "name": "enderchests",
                "value": False
                },
                {
                "name": "walldamage",
                "value": True
                },
                {
                "name": "drown",
                "value": True
                },
                {
                "name": "invincible",
                "value": False
                },
                {
                "name": "cactusdamage",
                "value": True
                },
                {
                "name": "firedamage",
                "value": True
                },
                {
                "name": "endermangrief",
                "value": False
                },
                {
                "name": "enderdragonblockdamage",
                "value": True
                },
                {
                "name": "hidelocation",
                "value": False
                },
                {
                "name": "hideflags",
                "value": False
                },
                {
                "name": "hidemembers",
                "value": False
                },
                {
                "name": "hideregion",
                "value": False
                },
                {
                "name": "icemelt",
                "value": True
                },
                {
                "name": "exit",
                "value": True
                },
                {
                "name": "enter",
                "value": True
                },
                {
                "name": "vinesgrowth",
                "value": True
                },
                {
                "name": "sendchat",
                "value": True
                },
                {
                "name": "trample",
                "value": True
                },
                {
                "name": "shulkerboxes",
                "value": True
                },
                {
                "name": "pistons",
                "value": True
                },
                {
                "name": "frostwalker",
                "value": False
                },
                {
                "name": "fishingpole",
                "value": True
                }
            ],
            "INTERACTS": [
                {
                "BLOCK": "craftingtable",
                "USE": True
                },
                {
                "BLOCK": "enchantingtable",
                "USE": False
                },
                {
                "BLOCK": "itemframe",
                "USE": False
                },
                {
                "BLOCK": "armorstand",
                "USE": False
                },
                {
                "BLOCK": "anvil",
                "USE": False
                },
                {
                "BLOCK": "hopper",
                "USE": True
                },
                {
                "BLOCK": "lever",
                "USE": False
                },
                {
                "BLOCK": "button",
                "USE": False
                },
                {
                "BLOCK": "furnace",
                "USE": False
                },
                {
                "BLOCK": "door",
                "USE": False
                },
                {
                "BLOCK": "fencegate",
                "USE": False
                },
                {
                "BLOCK": "trapdoor",
                "USE": False
                },
                {
                "BLOCK": "pressureplate",
                "USE": False
                },
                {
                "BLOCK": "sign",
                "USE": True
                }
            ],
            "VEHICLES": [
                {
                "VEHICLE": "minecart",
                "PLACE": False,
                "DESTROY": False
                },
                {
                "VEHICLE": "boat",
                "PLACE": False,
                "DESTROY": False
                }
            ],
            "EXPLOSIONS": [
                {
                "EXPLOSION": "tnt",
                "DAMAGE": True,
                "DESTROY": False
                },
                {
                "EXPLOSION": "creeper",
                "DAMAGE": True,
                "DESTROY": False
                },
                {
                "EXPLOSION": "endercrystal",
                "DAMAGE": True,
                "DESTROY": False
                },
                {
                "EXPLOSION": "fireball",
                "DAMAGE": True,
                "DESTROY": False
                },
                {
                "EXPLOSION": "enderdragon",
                "DAMAGE": True,
                "DESTROY": False
                },
                {
                "EXPLOSION": "otherexplosions",
                "DAMAGE": True,
                "DESTROY": False
                }
            ],
            "MOBS": [],
            "COMMANDS": [],
            "EXCLUDED_BLOCKS": {
                "PLACE": [],
                "DESTROY": []
            },
            "DISALLOWED_ITEMS": [],
            "DISALLOWED_BLOCKS": [],
            "TEMPLATE": False
        }

flagDict = {
    "place" : "block-place",
    "destroy" : "block-break",
    "pvp" : "pvp",
    "expdrop" : "exp-drops",
    "itemdrop" : "item-drop",
    "itempickup" : "item-pickup",
    "enderpearl" : "enderpearl",
    "sleep" : "sleep",
    "lighter" : "lighter",
    "chests" : "chest-access",
    "trappedchests" : None,
    "waterflow" : "water-flow",
    "lavaflow" : "lava-flow",
    "otherliquidsflow" : None,
    "leafdecay" : "leaf-decay",
    "firespread" : "fire-spread",
    "potionsplash" : "potion-splash",
    "falldamage" : "fall-damage",
    "cantp" : None,
    "canspawn" : None,
    "hunger" : "natural-hunger-drain",
    "enderchests" : "chest-access",
    "walldamage" : None,
    "drown" : None,
    "invincible" : "invincible",
    "cactusdamage" : None,
    "firedamage" : None,
    "endermangrief" : "enderman-grief",
    "enderdragonblockdamage" : "enderdragon-block-damage",
    "hidelocation" : None,
    "hideflags" : None,
    "hidemembers" : None,
    "hideregion" : None,
    "icemelt" : "ice-melt",
    "exit" : "exit",
    "enter" : "entry",
    "vinesgrowth" : "vine-growth",
    "sendchat" : "send-chat",
    "trample" : "block-trampling",
    "shulkerboxes" : "chest-access",
    "pistons" : "pistons",
    "frostwalker" : "frosted-ice-form",
    "fishingpole" : None,
    "craftingtable" : "use",
    "enchantingtable" : "use",
    "itemframe" : "use",
    "armorstand" : "use",
    "anvil" : "use",
    "hopper" : "use",
    "lever" : "use",
    "button" : "use",
    "furnace" : "use",
    "door" : "use",
    "fencegate" : "use",
    "trapdoor" : "use",
    "pressurplate" : "use",
    "sign" : "use"
}

vehicleDict = {
    "minecart" : {
        "place" : "vehicle-place",
        "destroy" : "vehicle-destroy"
    },
    "boat" : {
        "place" : "vehicle-place",
        "destroy" : "vehicle-destroy"
    }
}

explosionDict = {
    "tnt" : {
        "DAMAGE" : "tnt",
        "DESTROY" : "tnt"
    },
    "creeper" : {
        "DAMAGE" : "creeper-explosion",
        "DESTROY" : "creeper-explosion" 
    },
    "fireball" : {
        "DAMAGE" : "ghast-fireball",
        "DESTROY" : "ghast-fireball" 
    },
    "enderdragon" : {
        "DAMAGE" : "enderdragon-block-damage",
        "DESTROY" : "enderdragon-block-damage" 
    },
    "otherexplosions" : {
        "DAMAGE" : "other-explosion",
        "DESTROY" : "other-explosion" 
    },
}