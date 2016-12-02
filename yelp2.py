# user_state="CA"#raw_input("Please enter a state")
# user_city="San_Francisco"#raw_input("Please enter a city")

# use weather api to return current conditions for city, state 
# here are current weather conditions 
# Based on todays weather 
# use yelp api for resteraunts with out door seating 
# use conditional if 60-80 suggest resteraunts with out door seating 
# else less than 60 suggest resetaunts with indoor seating 
# here are the results with out door seating for restaurants in sf or city, and state they choose 

from urllib2 import urlopen 
from json import load 
from config_secret import*
from urllib import pathname2url 
from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
# use two apis one from weather underground and one from yelp 

def get_temperature_from_weather_underground(user_state, user_city):
    url_base = 'http://api.wunderground.com/api/' + weather_underground_key
    apiUrl = url_base+"/conditions/q/"+pathname2url(user_state)+"/"+pathname2url(user_city)+".json"

    response=urlopen(apiUrl)

    json_obj=load(response)
    
    if json_obj.get("current_observation"):
        return json_obj["current_observation"]["feelslike_f"]
     
    return 0   

auth = Oauth1Authenticator(
    consumer_key=YOUR_CONSUMER_KEY,
    consumer_secret=YOUR_CONSUMER_SECRET,
    token=YOUR_TOKEN,
    token_secret=YOUR_TOKEN_SECRET
)

client = Client(auth)


params = {
    'lang': 'en'
}


#search for and print businesses
def fetch_and_print_resturants(state, city, search_term):
    #go to yelp api and fetch business

    params['term'] = search_term;
    response= client.search(state + " " + city, **params)
    busisness_objs_list = response.businesses

    #print the name of all the businesses that came back from yelp
    for place in busisness_objs_list:
	   print place.name

def main():
    while True:
    #ask the user to enter in the city and state or quit and save it to place
        state = raw_input("Please enter state abbreviation (e.g.CA) or Q to quit:\n")
        if state=="q":
            break 
        else:
            city = raw_input("Please enter city (e.g.San Francisco)\n")
            temp = get_temperature_from_weather_underground(state, city)
            float_temp = float(temp)

            if(float_temp > 65):
                print "It feels like" + temp + " outside. What a great day to go to an outdoor resturant. Pick one below."
                search_term = 'outdoor seating'
            elif(float_temp < 40):
                print "It feels like" + temp + " outside. Better grub somewhere warm with soup. Pick one below."
                search_term = 'soup'
            else:
                print "It feels like" + temp + " outside. How about eating somewhere inside. Pick one below."
                search_term = 'indoor seating'    

            
            fetch_and_print_resturants(state, city, search_term)

if __name__ == '__main__':
 	main()
