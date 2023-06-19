# Create dictionaries to contain prices for flights, hotels and rental cars.
# Prices obtained from britishairways.com and booking.com. and are in Sterling.
cities = {"Berlin": 262.48,
          "Budapest": 243.18,
          "Paris": 247.68,
          "Rome": 297.88
        }

hotels = {"Berlin": 109.0,
          "Budapest": 75.0,
          "Paris": 89.0,
          "Rome": 111.0
        }

cars = {"Berlin": 82.33,
          "Budapest": 14.0,
          "Paris": 100.54,
          "Rome": 29.98
        }

# Print statement to limit available holiday destinations.
print("\nWhere do you want to go for your holiday? We have flights to Berlin, Budapest, Paris and Rome plus a hotel and car \nof our choice.\t")

# Variables for destination and lengths of hotel stay and car rental.
while True:
    try:
        city_flight = input("\nWhere do you want to fly?\t")
        city_flight = city_flight.title()
        if city_flight in cities:
            break
    except NameError:
        print("Please enter a city from the list or spell the name correctly.")
        continue

while True:
    try:
        num_nights = int(input("\nHow many nights do you want to stay at your hotel?\t"))
        break
    except ValueError:
        print("Please enter the number as a number, not a word.")
        continue

while True:
    try:
        rental_days = int(input("\nHow many days do you want to hire a car?\t "))
        break
    except ValueError:
        print("Please enter the number as a number, not a word.")
        continue


# Function to retrieve flight cost from dictionary.
def plane_cost(x):
    y = cities.get(x)
    return y

# Function to get hotel cost for selected city and multiply by number of nights.
def hotel_cost(x, y):
    hotel = hotels.get(x)
    z = hotel * y
    return z

# Function to calculate car rental cost for selected city.
def car_rental(x, y):
    car = cars.get(x)
    z = car * y
    return z

# Function to calculate total cost of holiday.
def holiday_cost(w, x, y):
    z = w + x + y
    return z

# Call functions to perform calculations.
ticket = plane_cost(city_flight)

stay = hotel_cost(city_flight, num_nights)

transport = car_rental(city_flight, rental_days )
# Round method used to prevent long strings of decimal places.
transport = round(transport, 2)

total = holiday_cost(ticket, stay, transport)
total = round(total, 2)

# Several print statements used to enhance readability of code for collaborators.
print(f"\n\nThe costs for your holiday are as follows.")
print(f"\nReturn flight to {city_flight}:\t£{ticket}")
print(f"\n{num_nights} nights at hotel:\t£{stay}")
print(f"\n{rental_days} days car rental:\t£{transport}")
print(f"\nYour holiday will cost:\t£{total} in total.")