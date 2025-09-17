weather = input("Whats the weather condition today: \n"
                "1.Sunny\n"
                "2.Rainy\n"
                "3.Cold\n").lower()
if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")