import yaml
import uuid
import requests
import UG
import json
import os

def getUsername(uuid):
    # Just for testing
    # uuid = "f6322e93-4c9b-4a9f-bc3c-7ea6b8600d6f"
    try:
        response = requests.get(f"https://playerdb.co/api/player/minecraft/{uuid}")
        jsonDecode = response.json()
        return(jsonDecode["data"]["player"]["username"])
    except:
        print("Something went wrong, can't fetch the username!")
        return -1


if __name__== "__main__":
    regions = None
    regionIndex = {}

    os.mkdir("regions")

    with open("regions.yml", 'r') as stream:
        try:
            regions = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)

    for region in regions["regions"]:
        # print(regions["regions"][region])
        if region == "__global__":
            continue
        newRegion = UG.UG()

        # Region name
        newRegion.data["NAME"] = region
        # First anker point of the region
        newRegion.data["FIRST_POINT"]["x"] = regions["regions"][region]["min"]["x"]
        newRegion.data["FIRST_POINT"]["y"] = regions["regions"][region]["min"]["y"]
        newRegion.data["FIRST_POINT"]["z"] = regions["regions"][region]["min"]["z"]
        # Second anker point of the region
        newRegion.data["SECOND_POINT"]["x"] = regions["regions"][region]["max"]["x"]
        newRegion.data["SECOND_POINT"]["y"] = regions["regions"][region]["max"]["y"]
        newRegion.data["SECOND_POINT"]["z"] = regions["regions"][region]["max"]["z"]
        # UUID for the region
        newRegion.data["ID"] = str(uuid.uuid1())
        # Greeting/farewell message
        try:
            newRegion.data["GREETING_MESSAGE"] = regions["regions"][region]["flags"]["greeting"]
        except:
            newRegion.data["GREETING_MESSAGE"] = ""
        try:
            newRegion.data["FAREWELL_MESSAGE"] = regions["regions"][region]["flags"]["farewell"]
        except:
            newRegion.data["FAREWELL_MESSAGE"] = ""

        # Adding the region owners and members, if there is a parent region in WorldGuard, the "superowners" are also added
        try:
            parent = regions["regions"][region]["parent"]
            try:
                while True:
                    newRegion.data["PRIORITY"] = newRegion.data["PRIORITY"] + 1
                    parent = regions["regions"][parent]["parent"]
            except:
                print("No more parents!")
            for superowner in regions["regions"][parent]["owners"]["unique-ids"]:
                newOner = {  
                "UUID" : "",
                "USERNAME" : "",
                "ROLE" : "OWNER"
                }
                newOner["UUID"] = superowner
                newOner["USERNAME"] = getUsername(superowner)

                newRegion.data["MEMBERS"].append(newOner)
        except:
            print("No parent region found!")
        
        try:
            for owner in regions["regions"][region]["owners"]["unique-ids"]:
                newOner = {  
                    "UUID" : "",
                    "USERNAME" : "",
                    "ROLE" : "OWNER"
                }
                newOner["UUID"] = owner
                newOner["USERNAME"] = getUsername(owner)

                
                newRegion.data["MEMBERS"].append(newOner)
        except:
            print("Region has no Owner or just a Superowner")
        try:
            for member in regions["regions"][region]["members"]["unique-ids"]:
                newMember = {  
                    "UUID" : "",
                    "USERNAME" : "",
                    "ROLE" : "MEMBER"
                }
                newOner["UUID"] = member
                newOner["USERNAME"] = getUsername(member)

                
                newRegion.data["MEMBERS"].append(newMember)
        except:
            print("Region has no Member")
            
        # Set all the flags if a flag is not set it gets the default defined in UG.py
        for flag in newRegion.data["FLAGS"]:
            try:
                if regions["regions"][region]["flags"][UG.flagDict[flag["name"]]] == "deny":
                    flag["value"] = False
                elif regions["regions"][region]["flags"][UG.flagDict[flag["name"]]] == "allow":
                    flag["value"] = True
            except:
                pass

        # Set all the INTERACT flags
        for interact in newRegion.data["INTERACTS"]:
            try: 
                if regions["regions"][region]["flags"][UG.flagDict[interact["BLOCK"]]] == "deny":
                    interact["USE"] = False
                elif regions["regions"][region]["flags"][UG.flagDict[interact["BLOCK"]]] == "allow":
                    interact["USE"] = True    
            except:
                pass

        # Set all the VEHICLES flags
        for vehicle in newRegion.data["VEHICLES"]:
            try:
                if regions["regions"][region]["flags"][UG.vehicleDict[vehicle["VEHICLE"]["place"]]] == "deny":
                    vehicle["PLACE"] = False
                elif regions["regions"][region]["flags"][UG.vehicleDict[vehicle["VEHICLE"]["place"]]] == "allow":
                    vehicle["PLACE"] = True
                if regions["regions"][region]["flags"][UG.vehicleDict[vehicle["VEHICLE"]["destroy"]]] == "deny":
                    vehicle["DESTROY"] = False    
                elif regions["regions"][region]["flags"][UG.vehicleDict[vehicle["VEHICLE"]["destroy"]]] == "allow":
                    vehicle["DESTROY"] = True
            except:
                pass

        # Set all the EXPLOSIONS flags
        for explosion in newRegion.data["EXPLOSIONS"]:
            try:
                if regions["regions"][region]["flags"][UG.explosionDict[explosion["EXPLOSION"]["DAMAGE"]]] == "deny":
                    vehicle["DAMAGE"] = False
                elif regions["regions"][region]["flags"][UG.explosionDict[explosion["EXPLOSION"]["DAMAGE"]]] == "allow":
                    vehicle["DAMAGE"] = True
                if regions["regions"][region]["flags"][UG.explosionDict[explosion["EXPLOSION"]["DESTROY"]]] == "deny":
                    vehicle["DAMAGE"] = False
                elif regions["regions"][region]["flags"][UG.explosionDict[explosion["EXPLOSION"]["DESTROY"]]] == "allow":
                    vehicle["DESTROY"] = True
            except:
                pass


        jsonDump = json.dumps(newRegion.data, indent=4)
        fname = newRegion.data["ID"]
        f = open(f"regions/{fname}.json", "w")
        f.write(jsonDump)
        f.close()
        
        regionIndex[newRegion.data["NAME"]] = newRegion.data["ID"]

    jsonDump = json.dumps(regionIndex, indent=4)
    f = open("index.json", "w")
    f.write(jsonDump)
    f.close()
