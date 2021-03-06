import menu_options
import validate

def display_key_and_value(key,value,left_size=15,right_size=15):
    if value != "" and value != 0:
        if value == None:
            value = ""
        new_key = key
        if len(key) > 2:
            new_key = key[0].upper() + key[1:len(key)].lower()
        return_str = "|{:<" + str(left_size)+"}:{:<" + str(right_size) + "}|"
        return_str = return_str.format(new_key,value)
        print(return_str)
        return True
    return False

def display_pokemon(dictionary):
    first_last_str = " "
    first_last_str += "_" * 32
    print(first_last_str)
    display_key_and_value("name",dictionary.get("name"),16,15)
    display_key_and_value("type 1",dictionary.get("type1"),16,15)
    if dictionary.get("type_2") != "":
        display_key_and_value("type 2",dictionary.get("type2"),16,15)
    display_key_and_value("Health",dictionary.get("hp"),16,15)
    display_key_and_value("primary attack",dictionary.get("primary_attack"),16,15)
    display_key_and_value("secondary attack",dictionary.get("secondary_attack"),16,15)
    if dictionary.get("evolution_level") != 0:
        display_key_and_value("evolves at level",dictionary.get("evolution_level"),16,15)
    print(first_last_str)

def display_attack(dic):
    print(" " + "_" * 51)
    display_key_and_value("Attack Name",dic.get("name"),20,30)
    if dic.get("damage") != None and str(dic.get("damage")) != "" and dic.get("damage") != 0:
        display_key_and_value("Damage",str(dic.get("damage")),20,30)
    else:
        display_key_and_value("No damage","see effect",20,30)
    display_key_and_value("Targets",dic.get("targets"),20,30)
    display_key_and_value("Power points",dic.get("pp"),20,30)
    if dic.get("acc") != "0" and dic.get("acc") != None and dic.get("acc")!=0 and str(dic.get("acc"))!="":
        display_key_and_value("Accuracy",str(dic.get("acc")),20,30)
    else:
        display_key_and_value("No accuracy","See effect",20,30)
    if dic.get("location") != "" and dic.get("location") != None and dic.get("location") != 0 and dic.get("location") != "0":
        display_key_and_value("Found in",dic.get("location"),20,30)
    display_key_and_value("Effect",dic.get("effect"),20,30)
    print(" " + "_" * 51)

def display_pokemon_evolutions(list_of_dics, poke_name):
    header = poke_name[0].upper() + poke_name[1:len(poke_name)] + " Evolutions"
    print("\n\n{:^50}".format(header))
    print("_" * 52)
    for dic in list_of_dics:
        print(" " + "_" * 51)
        #print(dic)
        if dic.get("is_parent"):
            display_key_and_value("Parent Poke"," " +dic.get('poke_name'),20,30)
        if dic.get("is_child"):
            display_key_and_value("Child Poke", " " +dic.get("poke_name"),20,30)
        if dic.get("is_item_used") != None and dic.get("is_item_used") != 0:
            display_key_and_value("Item used",dic.get("item_used"),20,30)
        if dic.get("is_bred") != None and dic.get("is_bred") != 0:
            display_key_and_value("Acquired"," by breeding.",20,30)
        if dic.get("is_evolve") != None and dic.get("is_evolve") != 0:
            display_key_and_value("Acquired", " by evolution.",20,30)
        if dic.get("is_traded") != None and dic.get("is_traded") != 0:
            display_key_and_value("Acquired"," by trading.",20,30)
        if dic.get("additional_requirements") != "0" and dic.get("additional_requirements") != 0 and dic.get("additional_requirements") != None and dic.get("additional_requirements") != "":
            display_key_and_value("Additional reqs"," " +dic.get("additional_requirements"),20,30)
        print(" " + "_" * 51)
    print("No more associated evolutions")

def display_pokemon_attacks(dic,pokemon_name):
    header = pokemon_name[0].upper() + pokemon_name[1:len(pokemon_name)].lower()
    header = header + " Attacks"

    print("\n\n{:^50}".format(header))
    print(" " +"_" * 51)
    if dic.get("primary_att_name") != "":
        display_key_and_value("Primary attack",dic.get("primary_att_name"),20,30)
        if dic.get("primary_att_damage") != None and str(dic.get("primary_att_damage")) != "" and dic.get("primary_att_damage") != 0:
            display_key_and_value("Damage",str(dic.get("primary_att_damage")),20,30)
        else:
            display_key_and_value("No damage","see effect",20,30)
        display_key_and_value("Targets",dic.get("primary_att_targets"),20,30)
        display_key_and_value("Power points",dic.get("primary_att_pp"),20,30)
        if dic.get("primary_att_accuracy") != None and dic.get("primary_att_accuracy")!=0 and str(dic.get("primary_att_accuracy"))!="":
            display_key_and_value("Accuracy",dic.get("primary_att_accuracy"),20,30)
        else:
            display_key_and_value("No accuracy","See effect",20,30)
        display_key_and_value("Effect",dic.get("primary_att_effect"),20,30)
    else:
        print("No primary attack found.")
    print(" " +"_" * 51)
    if dic.get("secondary_att_name") != "":
        display_key_and_value("Secondary attack",dic.get("secondary_att_name"),20,30)
        if dic.get("secondary_att_damage") != None and str(dic.get("secondary_att_damage")) != "" and dic.get("secondary_att_damage") != 0:
            display_key_and_value("Damage",str(dic.get("secondary_att_damage")),20,30)
        else:
            display_key_and_value("No damage","See effect",20,30)
        display_key_and_value("Targets",dic.get("secondary_att_targets"),20,30)
        display_key_and_value("Power points",dic.get("secondary_att_pp"),20,30)
        if dic.get("secondary_att_accuracy") != None and dic.get("secondary_att_accuracy")!=0 and str(dic.get("secondary_att_accuracy"))!="":
            display_key_and_value("Accuracy",dic.get("secondary_att_accuracy"),20,30)
        else:
            display_key_and_value("No accuracy","See effect",20,30)
        display_key_and_value("Effect",dic.get("secondary_att_effect"),20,30)
    else:
        print("No secondary attack found.")
    print(" " + "_" * 51)
    
def display_pokemon_locations(location_array,pokemon_name):
    
    if location_array:
        to_display = pokemon_name[0].upper() + pokemon_name[1:len(pokemon_name)] + " can be found in:"
        print("\n{:<25}".format(to_display))
        print(" " + "_" * 40)
        for location in location_array:
            display_key_and_value("",location[0],7,33)
            
    else:
        to_display = "No locations found for that pokemon."
    print(" " + "_" * 40)

def display_pokemon_in_location(pokemon_array,location_name):

    if pokemon_array:
        to_display = "\n" + location_name[0].upper() + location_name[1:len(location_name)] + " contains the following pokemon:"
        print(to_display)
        print(" " + "_" * 40)
        for pokemon in pokemon_array:
            poke_name = pokemon[0][0].upper()
            poke_name += pokemon[0][1:len(pokemon[0])]
            display_key_and_value("",poke_name,5,35)
        print(" " + "_"*40)
    else:
        print("No pokemon found for that location.")

def list_table(table_name):
    table_name = table_name.lower()
    to_return = {}
    if table_name == "attacks":
        sql = 'select name, damage, effect, targets, power_points, accuracy, location_name from attacks;'
        results = menu_options.execute(sql)
        if results:
            print("{:^51}" . format("ATTACKS TABLE"))

            for attack in results:
                print(" " + "_" * 51)
                pokename = attack[0][0].upper()
                pokename += attack[0][1:len(attack[0])]
                display_key_and_value("Name",pokename,10,40)
                if attack[1] != None and attack[1] != 0 and attack[1] != "":
                    display_key_and_value("Damage",str(attack[1]),10,40)
                else:
                    display_key_and_value("No damage","See effect",10,40)
                display_key_and_value("Targets", attack[3],10,40)
                display_key_and_value("PP",str(attack[4]),10,40)
                if attack[5] != 0 and attack[5] != "":
                    display_key_and_value("Accuracy", str(attack[5]),10,40)
                if attack[6] != None and attack[6] != 0 and attack[6] != "" and attack[6] != "none":
                    display_key_and_value("Found in",attack[6],10,40)
                if attack[2] != None and attack[2] !=0 and attack[2] != "":
                    display_key_and_value("Effect",attack[2],10,40)
                print(" " + "_" * 51)
        else:
            raise validate.Input_Error("No attacks. Perhaps the db has not been set up yet.")
    elif table_name == "locations":
        sql = "select name, description from locations;"
        results = menu_options.execute(sql)
        if results:
            print("{:^55}" . format("LOCATIONS"))
            print(" " + "_"*55)
            header_str = "\n|{:^25}:".format("Name")
            header_str += "{:^30}|".format("Description")
            print(header_str)
            print("|{:^56}|".format(""))
            for location in results:
                if location[1] != "" and location[1] != "0" and location[1] != None and location[1] != 0:
                    display_key_and_value(location[0],location[1],25,30)
                else:
                    display_key_and_value(location[0],"No description",25,30)
            print(" " + "_"*55)

        else:
            raise validate.Input_error("No locations. Perhaps the db has not been set up yet.")

    elif table_name == "pokemon":
        results = menu_options.select_all_pokemon()
        print("{:^34}" . format("POKEMON"))
       # print(results)
        for pokemon in results:
            display_pokemon(pokemon)

    elif table_name == "evolutions":
        sql = 'select parent_poke,child_poke,evolved,item_used,item,traded,bred,notes from evolutions;'
        results = menu_options.execute(sql)
        if results:
            print("\n{:^46}" . format("EVOLUTIONS TABLE"))
            for evolution in results:
                print(" " + "_"*45)
                parent_poke = evolution[0][0].upper() + evolution[0][1:len(evolution[0])]
                child_poke = evolution[1][0].upper() + evolution[1][1:len(evolution[1])]
                display_key_and_value("Parent Poke",parent_poke,15,30)
                display_key_and_value("Child Poke", child_poke,15,30)
                if evolution[2] == 1:
                    display_key_and_value("Acquired", "through level up",15,30)
                if evolution[3] == 1 and evolution[4] != None:
                    display_key_and_value("Acquired","by using " + evolution[4],15,30)
                if evolution[5] == 1:
                    display_key_and_value("Acquired","through trading", 15, 30)
                if evolution[6] == 1:
                    display_key_and_value("Acquired","through breeding",15,30)
                if evolution[7] != None and evolution[7] != 0 and evolution[7] != "" and evolution[7] != "0":
                    display_key_and_value("Additional reqs",evolution[7],15,30)
                print(" " +"_"*45)
        else:
                raise validate.Input_Error("No evolutions. Perhaps the db has not been set up yet.")

def display_all_tables():
    print("\nLISTING ALL TABLES:")
    list_table("evolutions")
    list_table("pokemon")
    list_table("locations")
    list_table("attacks")
