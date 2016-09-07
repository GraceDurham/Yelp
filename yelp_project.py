Choice=raw_input("Please enter a state")
Choice1=raw_input("Please enter a city")

# use weather api to return current conditions for city, state 
# here are current weather conditions 
# Based on todays weather 
# use yelp api for resteraunts with out door seating 
# use conditional if 60-80 suggest resteraunts with out door seating 
# else less than 60 suggest resetaunts with indoor seating 
# here are the results with out door seating for restaurants in sf or city, and state they choose

# idea maybe create class contact with self, first_name, last_name, email="", mobile_phone="", text_message, 
send text message to friends to hang out at resteraunt 






from urllib2 import urlopen 
from json import load 

# use two apis one from weather underground and one from yelp 

apiUrl = "http://api.wunderground.com/api/d16efc3860428b14/conditions/q/CA/San_Francisco.json"

response=urlopen

json_obj=load(response)

print json_obj 


# apiUrl= yelp api use key in my gmail 

# response=urlopen 

# json_obj=load(response)
# print json_obj 

# 3 classes 1 yelp, 1 weather, and 1 class to tie everything together 


# def main():



# if __name__ == '__main__':
# 	main()
