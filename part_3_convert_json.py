import cc_dat_utils
import cc_classes
import json

#Part 3
#Load your custom JSON file
#Convert JSON data to CCLevelPack
#Save converted data to DAT file

json_file_name = "level.json"
with open(json_file_name, "r") as reader:
    data1 = json.load(reader)

def make_cc_class( json_data ):
	new_level_pack = cc_classes.CCLevelPack()
	for value in json_data:
		level = cc_classes.CCLevel()
		level.level_number = value["level_number"]
		level.time = value["time_limit"]
		level.num_chips = value["num_chips"]
		level.upper_layer = value["upper_layer"]
		#level.optional_fields = value["optional_fields"]

		for json_field in value["optional_fields"]:
			field_type = json_field["field_type"]
			if field_type == "hint":
				new_hint = cc_classes.CCMapHintField(json_field["value"])
				level.add_field(new_hint)
			elif field_type == "title":
				new_title = cc_classes.CCMapTitleField(json_field["value"])
				level.add_field(new_title)
			elif field_type == "password":
				new_password = cc_classes.CCEncodedPasswordField(json_field["value"])
				level.add_field(new_password)
			elif field_type == "monster":
				monsters = []
				for json_monster in json_field["monsters"]:
					x = json_monster["x"]
					y = json_monster["y"]
					new_monster_coord == cc_classes.CCCoordinate(x, y)
					monster.append(new_monster_coord)
				new_monster_field = cc_classes.CCMonsterMovementField(monsters)
				level.add_field(new_monster_field)
		
	new_level_pack.add_level(level)

	return new_level_pack

new_level_pack = make_cc_class(data1)
#print(levelPack)
cc_dat_utils.write_cc_level_pack_to_dat(new_level_pack, "data/bweng_cc1.dat")
#write_cc_level_pack_to_date(levelPack, "data/bweng_cc1.dat")


