#exersice 4.13
buffet_style=("biryani","pulao","kheer","malai","karai")
print("before menu")
for a in buffet_style:
    print(a.title())
buffet_styles=["biryani","pulao","kheer","malai","karai"]
buffet_styles[2]="pizza"
buffet_styles[3]="tikka"
buffet_style=(buffet_styles)
print("renew menu")
for a in buffet_style:
    print(a.title())