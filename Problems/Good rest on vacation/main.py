# put your python code here
days = int(input())
daily_food_cost = int(input())
flight_cost = int(input())
night_hotel_cost = int(input())

print(days
      * (daily_food_cost + night_hotel_cost)
      - night_hotel_cost
      + 2 * flight_cost
      )
