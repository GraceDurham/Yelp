# user_state="CA"#raw_input("Please enter a state")
# user_city="San_Francisco"#raw_input("Please enter a city")

# use weather api to return current conditions for city, state 
# here are current weather conditions 
# Based on todays weather 
# use yelp api for resteraunts with out door seating 
# use conditional if 60-80 suggest resteraunts with out door seating 
# else less than 60 suggest resetaunts with indoor seating 
# here are the results with out door seating for restaurants in sf or city, and state they choose

# # idea maybe create class contact with self, first_name, last_name, email="", mobile_phone="", text_message, 
# send text message to friends to hang out at resteraunt 






from urllib2 import urlopen 
from json import load 
from config_secret import*

# use two apis one from weather underground and one from yelp 

# def get_temperature_from_weather_underground(user_state,user_city):

# 	url_base = 'http://api.wunderground.com/api/' + weather_underground_key
# 	apiUrl = url_base+"/conditions/q/"+user_state+"/"+user_city+".json"

# 	response=urlopen(apiUrl)

# 	json_obj=load(response)

# 	temperature=json_obj["current_observation"]["feelslike_f"]
# 	return float(temperature)
# pip install yelp 

from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator

auth = Oauth1Authenticator(
    consumer_key=YOUR_CONSUMER_KEY,
    consumer_secret=YOUR_CONSUMER_SECRET,
    token=YOUR_TOKEN,
    token_secret=YOUR_TOKEN_SECRET
)

client = Client(auth)


params = {
    'term': 'outdoor seating',
    'lang': 'en'
}


#search for and print businesses
def fetch_and_print_resturants(place):
    #go to yelp api and fetch business
    response= client.search(place, **params)
    busisness_objs_list = response.businesses

    #print the name of all the businesses that came back from yelp
    for place in busisness_objs_list:
	   print place.name

# location=json_obj["location"]["city"]
# print location 
# apiUrl= yelp api use key in my gmail 

# response=urlopen 

# json_obj=load(response)
# print json_obj 
 



def main():
    

    while True:
    #ask the user to enter in the city and state or quit and save it to place
        place = raw_input("Please enter city and state abbreviation (e.g. San Francisco CA) or Q to quit:\n");
        if place=="q":
            break 
        else:    
            fetch_and_print_resturants(place)
            

    # fetch_and_print_resturants()


if __name__ == '__main__':
 	main()
