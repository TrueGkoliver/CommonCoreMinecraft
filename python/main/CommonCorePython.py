#@author Gkoliver (original author)
#Populates loot tables based off of blockstate files.
#@param filepath The filepath of the folder with blockstates. Remember, always add an extra backslash to every backslash!
#@param modid The modid. Obviously.
#@return NONE
#@import json
#@import os
#@important THIS WILL REPLACE ALL OF THE FILES IN THE FILEPATH.
#Do NOT put this into your blockstates folder, it will replace all of it. 

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
            json.dump(ltable_file, ltable, indent=4)
            ltable_file.close()
#@author Gkoliver (original author)
#Populates a lang file based off of blockstate files.
#@param filepath The filepath of the folder with blockstates. Remember, always add an extra backslash to every backslash!
#@param modid The modid. Obviously.
#@param the file name of the lang file (keep the .json in it) relative to the lang file.
#@return NONE
#@import json
#@import os
def populateLangfile(filepath, modid, en_us):
    data = {}
    for filename in os.listdir(filepath):
        if filename.endswith(".json"):
            truename = filename.replace(".json","")
            truename = "block."+modid+"."+truename
            data[truename] = " "
    file = open(filepath+"\\"+en_us, "w")
    json.dump(data, file, indent=4)
    file.close()
