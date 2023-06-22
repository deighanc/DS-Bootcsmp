
# Define a list of available cities
cities = ['New York', 'Paris', 'Tokyo', 'Sydney']

# Prompt the user to select a city
city_flight = input(f"Which city would you like to fly to? Choose from {cities}: ").lower() #added the lower method so that any version of the correct string canbe inputted e.g uppercase

# Check if the selected city is in the list of available cities
if city_flight in [city.lower() for city in cities]: # convert each element to lowercase and iterate though the cities list then check if city_flight is 'in' the cties list  // https://www.w3schools.com/python/ref_keyword_in.asp
    print(f"You have selected {city_flight.title()}.") # title method is used to print out the capitalised the correctly selected city. 
else:
    print(f"Sorry, {city_flight} is not a valid choice. Please choose from {cities}.")
    exit() # this will exit the programme if the incorrect city is entered // https://stackoverflow.com/questions/6190776/what-is-the-best-way-to-exit-a-function-which-has-no-return-value-in-python-be 

num_nights = int(input("How many nights will you be staying for? "))
rental_days = int(input("How many days your will be renting the car for? "))


# create four functions
def hotel_cost(num_nights): 
#calculation for total cost of the stay.     
     total_cost_stay = 75 * num_nights
#return total cost of stay. 
     return total_cost_stay 

def plane_cost(city_flight):  
# create an elif statement to determine the different flight prices  https://www.w3schools.com/python/python_conditions.asp 
    if city_flight  == 'new york':  # city names are in lowercase so that they can meet the conditions - the input was converted to lowercase previously T
        flight_price = 400
    elif city_flight  ==  'paris': 
        flight_price = 180
    elif city_flight  ==  'tokyo': 
        flight_price = 900
    elif city_flight  ==  'sydney': 
        flight_price = 1200
    else: 
        print(f"Sorry,{city_flight} is not a valid choice. Please choose from {cities}.")
        exit()  # this will exit the program if the incorrect city is entered 

    return flight_price
    


def car_rental(rental_days):  
    #Calculate the total car rental cost and assign it to a variable
    total_rental_cost = rental_days * 35
    #Return the total cost
    return total_rental_cost


def holiday_cost(num_nights, city_flight, rental_days):
# Assign the results of each function to a variable as per the example code
    hotel_total = hotel_cost(num_nights)
    plane_total = plane_cost(city_flight)
    car_total = car_rental(rental_days)

# Print the total cost of each item
    print("The total hotel cost will be £" + str(hotel_total))
    print("The total flight cost will be £" + str(plane_total))
    print("The total car rental cost will be £" + str(car_total))

 # Calculate the total holiday cost
    total_cost = hotel_total + plane_total + car_total

# Print the total holiday cost
    print("The total cost of your holiday will be £" + str(total_cost))



# Call the holiday_cost function with the required arguments created earlier // https://www.freecodecamp.org/news/how-to-call-a-function-in-python-def-syntax-example/ 
holiday_cost(num_nights, city_flight, rental_days)