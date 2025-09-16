# prompt the user for weather conditions

weather = input("What's the weather like today?(sunny/rainy/cold): ").lower()

# Give clothing recomendations

if weather == "sunny": 
   print("wear a t-shirt and sunglasses." )
elif weather == "rainy":
  print("Dont forget your umbrella and rain coat.")
elif weather == "cold":
  print("Make sure to wear a warm coat and a scarf.")
else:
  print("Sorry, I don't have a recommendation for this weather.")

