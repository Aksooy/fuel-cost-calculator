import sys

def main():
    welcome_user()
    distance, fuel_consumption, fuel_price = get_informations()
    fuel_needed, total_cost = calculate_fuel_cost(distance, fuel_consumption, fuel_price)
    round_trip = input("Do you want to calculate the round trip cost? (yes/no): ").strip().lower()
    if round_trip == "yes":
        round_trip_cost(fuel_needed, total_cost)
    elif round_trip == "no":
        print("Thank you for your interest!")
    else:
        print("Geçersiz değer girdiniz")
        sys.exit(1)
         



def welcome_user():
    print("-----------------------------------------------Welcome to the Fuel Cost Calculator!-----------------------------------------------")

def get_informations():
    distance = float(input("Enter the distance: "))
    if distance < 0:
        print("Geçersiz Değer girdiniz.")
        sys.exit(1)
    fuel_consumption = float(input("Enter the fuel consumption (Liters per 100 km): "))
    if fuel_consumption < 0:
        print('Geçersiz değer girdiniz.')
        sys.exit(1)
    fuel_price = float(input("Enter the fuel price (Per Liter):"))
    if fuel_price < 0:
        print('Geçersiz değer girdiniz.')
        sys.exit(1)
    
    return distance, fuel_consumption, fuel_price
    

def calculate_fuel_cost(distance, fuel_consumption, fuel_price):
    fuel_needed = (distance / 100) * fuel_consumption
    total_cost = fuel_needed * fuel_price
    print(f"The total fuel needed for the trip is: {fuel_needed:.2f} Liters.")
    print(f"The total fuel cost for the trip is: {total_cost:.2f} TL.")
    return fuel_needed, total_cost

def round_trip_cost(fuel_needed, total_cost):
    round_trip_needed_fuel = fuel_needed * 2
    round_trip_total_cost = total_cost * 2
    print(f"Total fuel needed for the round trip is: {round_trip_needed_fuel:.2f} Liters.")
    print(f"Total fuel cost for the round trip is: {round_trip_total_cost:.2f} TL.")

main()