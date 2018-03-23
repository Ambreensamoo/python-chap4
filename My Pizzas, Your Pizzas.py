#exersice 4.11
my_favorite_pizza=["chiken","vegitable","beeaf"]
my_friend_pizza=my_favorite_pizza
my_friend_pizza.append("fagita")
my_favorite_pizza.append("chinees")
print("My favriote pizza list:")
for mypizza in my_favorite_pizza:
    print(mypizza.title())
print("My friend pizza:")
for myfrend in my_friend_pizza:
    print(myfrend.title())
