#  prompt the user to input the current weather.
weather = input("What's the weather like today? (sunny/rainy/cold): ")

# --- Provide clothing recommendations based on conditions ---

# Check if the weather is "sunny".
if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
# Check if the weather is "rainy".
elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
# Check if the weather is "cold".
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
# If none of the above conditions are met, provide a default response.
else:
    print("Sorry, I don't have recommendations for this weather.")

