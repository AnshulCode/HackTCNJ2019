from yelpapi import YelpAPI
from pprint import pprint
# 
yelp_api = YelpAPI("6q6QMI-ZflM7L-bSlsAkJAdoGzJXuNPncSebdTFv6-2WF8BCTe-gsvCxmjqSFZuglpwP_5JL93-Nn0WlNUBf1skpedEWtFNAGudgQKcLDwUdgA9ESgvkDZ4NvXxxXHYx")
def getRestaurants(typeOfRestaurant, longi, lat, amount):
    print('***** ' + str(amount) + ' best rated ' + typeOfRestaurant + ' places near latitude:' + str(lat) + ' longitude:' + str(longi) + ' *****')
    response = yelp_api.search_query(categories=typeOfRestaurant, longitude=longi, latitude=lat, limit=amount)
    
    print('\n-------------------------------------------------------------------------\n')
    return response
