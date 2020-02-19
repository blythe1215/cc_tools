import json
import family_class

json_file_name = "data/family_data.json"

with open(json_file_name, "r") as reader:
    family_json_data = json.load(reader)

parents = family_json_data["parents"]
new_family = family_class.Family(parents);

kids = family_json_data["kids"]

for kid in kids:
	new_kid = family_class.kid(kid["name"], kid["age"])
	new_family.add_kid(new_kid)
	print(kid)

kid1 = kids[0]
new_kid1 = family_class.kid(kid1["name"], kid1["age"])
kid2 = kids[1]
print(new_family)


#print(family_json_data)
#print("----------------------------------------")
#print("Just the parents:")
#print(family_json_data["parents"])
#print("----------------------------------------")
#print("Just the first parent:")
#print(family_json_data["parents"][0])