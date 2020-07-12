#@author Gkoliver (original author)
#Populates loot tables based off of blockstate files.
#@param filepath The filepath of the folder with blockstates. Remember, always add an extra backslash to every backslash!
#@param modid The modid. Obviously.
#@return NONE
#@import json
#@import os

def populateLootTables(filepath, modid):
    for filename in os.listdir(filepath):
        if filename.endswith(".json"):
            truename = filename.replace(".json","")
            ide = filename.replace(".json","")
            item = ""
            ltable = {
                      "type": "minecraft:block",
                      "pools": [
                        {
                          "rolls": 1,
                          "entries": [
                            {
                              "type": "minecraft:item",
                              "name": modid+ide
                            }
                          ],
                          "conditions": [
                            {
                              "condition": "minecraft:survives_explosion"
                            }
                          ]
                        }
                      ]
                    }
            ltable_file = open(filepath+"\\"+filename, "w")
            json.dump(ltable_file, records_json, indent=4)