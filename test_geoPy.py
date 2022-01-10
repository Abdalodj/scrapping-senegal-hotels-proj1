#Importing the Nominatim geocoder class 
from geopy.geocoders import Nominatim
import traceback
 
try:
  #address we need to geocode
  loc = "Africa Fried Chicken, Dakar"
  
  #making an instance of Nominatim class
  geolocator = Nominatim(user_agent="my_request")
  
  #applying geocode method to get the location
  location = geolocator.geocode(loc)
  
  #printing address and coordinates
  print(location.address)
  print((location.latitude, location.longitude))

except Exception:
  print(traceback.format_exc())