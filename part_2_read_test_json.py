import test_data
import json

json_file_name = "test_data.json"
with open(json_file_name, "r") as reader:
    data1 = json.load(reader)

#Creates and returns a GameLibrary object(defined in test_data) from loaded json_data
def make_game_library_from_json( json_data ):
    #Initialize a new GameLibrary
    game_library = test_data.GameLibrary()


    ### Begin Add Code Here ###
    #Loop through the json_data
        #Create a new Game object from the json_data by reading
        #  title
        #  year
        #  platform (which requires reading name and launch_year)
        #Add that Game object to the game_library
    ### End Add Code Here ###

    for game in data1:
        title = game["name"]
        year = game["Years"]
        platform_launchyear = game["platform"]["launch_year"]
        platform_name = game["platform"]["name"]

        new_platform = test_data.Platform(platform_name, platform_launchyear)
        
        new_game = test_data.Game(title, new_platform, year)
        game_library.add_game(new_game)


    return game_library


print(make_game_library_from_json(data1))



#Part 2
input_json_file = "data/test_data.json"

### Begin Add Code Here ###
#Open the file specified by input_json_file
#Use the json module to load the data from the file
#Use make_game_library_from_json(json_data) to convert the data to GameLibrary data
#Print out the resulting GameLibrary data using print()
### End Add Code Here ###
