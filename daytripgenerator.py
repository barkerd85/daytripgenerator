

import random 


cities = ['Cincinnati', 'Chicago', 'Dallas']



restaraunts_in_Cincinnati = ('Skyline Chili', 'Frishces', 'Larosas')

restaraunts_in_Dallas = ('Zalats', 'Halal Guys', 'Gen Korean')

restaraunts_in_Chicago = ('Portillos', 'Lou Malnatis', 'Hot Dog Station')


transportation_in_Cincinnati = ('Cincy Metro Bus', 'Uber', 'Zipcars')

transportation_in_Dallas = ('DART', 'M-Line Trolley', 'Bird electric scooters')

transportation_in_Chicago = ('Water Taxis', 'CTA', 'Divvy Bikes')



activities_in_Cincinnati = ('Kings Island theme park', 'Ohio Renaissance Festival', 'Cincinnati History Musuem')

activities_in_Dallas = ('Dallas Art Musuem', 'Cowgirls game', 'JFK tour')

activities_in_Chicago = ('Chicago Bulls game', 'Chicago Crime and Mob tour', 'Downtown boat tour')

def set_city(): 
    return random.choice(cities)

def set_transportation_cincy():
    return random.choice (transportation_in_Cincinnati)

def set_activity_cincy():
    return random.choice (activities_in_Cincinnati)

def set_food_cincy():
    return random.choice (restaraunts_in_Cincinnati)



def set_transportation_dallas():
    return random.choice (transportation_in_Dallas)

def set_activity_dallas():
    return random.choice (activities_in_Dallas)

def set_food_dallas():
    return random.choice (restaraunts_in_Dallas)


def set_transportation_chicago():
    return random.choice (transportation_in_Chicago)

def set_activity_chicago():
    return random.choice (activities_in_Chicago)

def set_food_chicago():
    return random.choice (restaraunts_in_Chicago)

def random_city():
    randcity = set_city()

    if randcity == 'Cincinnati': 
        transportation = set_transportation_cincy()
        activity = set_activity_cincy()
        food = set_food_cincy()
    
    if randcity == 'Dallas': 
        transportation = set_transportation_dallas()
        activity = set_activity_dallas()
        food = set_food_dallas()


    if randcity == 'Chicago': 
        transportation = set_transportation_chicago()
        activity = set_activity_chicago()
        food = set_food_chicago()

    return [randcity, transportation, activity, food]

activities_list = random_city()
print(f'Your day trip is planned to {activities_list[0]} where you will be riding in style with {activities_list[1] }, and having dinner at {activities_list[3]}. Then you will be enjoying the {activities_list[2]}. ')
question = input ('Are you happy with your day trip selections?')

while question != 'yes' and question != 'no':
    question = input('Please answer yes or no.')

while question != ('yes'):
    if question != ('no'):
        question = input('Please answer yes or no.')
    else:    
        
        question2 = input('What would you like to change?')
        if question2 == 'city':
            activities_list2 = random_city()
            while activities_list[0] == activities_list2 [0]:
                activities_list2 = random_city()
            activities_list = activities_list2
            print(f'Your day trip is planned to {activities_list[0]} where you will be riding in style with {activities_list[1] }, and having dinner at {activities_list[3]}. Then you will be enjoying the {activities_list[2]}. ')
            
            question = input ('Are you happy with your day trip selections?')       
        elif question2 == 'transportation':
            if activities_list[0] == 'Chicago':
                activities_list[1] = set_transportation_chicago()
            if activities_list[0] == 'Dallas':
                activities_list[1] = set_transportation_dallas()
            if activities_list[0] == 'Cincinnati':
                activities_list[1] = set_transportation_cincy()
            print(f'Your day trip is planned to {activities_list[0]} where you will be riding in style with {activities_list[1] }, and having dinner at {activities_list[3]}. Then you will be enjoying the {activities_list[2]}. ')
            question = input ('Are you happy with your day trip selections?')


        elif question2 == 'food':
            if activities_list[0] == 'Chicago':
                activities_list[3] = set_food_chicago()
            if activities_list[0] == 'Dallas':
                activities_list[3] = set_food_dallas()
            if activities_list[0] == 'Cincinnati':
                activities_list[3] = set_food_cincy()
            print(f'Your day trip is planned to {activities_list[0]} where you will be riding in style with {activities_list[1] }, and having dinner at {activities_list[3]}. Then you will be enjoying the {activities_list[2]}. ')
            question = input ('Are you happy with your day trip selections?')


        elif question2 == 'activity':
            if activities_list[0] == 'Chicago':
                activities_list[2] = set_activity_chicago()
            if activities_list[0] == 'Dallas':
                activities_list[2] = set_activity_dallas()
            if activities_list[0] == 'Cincinnati':
                activities_list[2] = set_activity_cincy()
            print(f'Your day trip is planned to {activities_list[0]} where you will be riding in style with {activities_list[1] }, and having dinner at {activities_list[3]}. Then you will be enjoying the {activities_list[2]}. ')
            question = input ('Are you happy with your day trip selections?')
        else:
            print('Please pick city, transportation, food, or activity.')

print(f'Your day trip is planned to {activities_list[0]} where you will be riding in style with {activities_list[1] }, and having dinner at {activities_list[3]}. Then you will be enjoying the {activities_list[2]}. ')
print('enjoy yourself')








