print("Hi, I'll tell you here what is the porcentage of taxes you must pay in Spain.")
anualearnings = float(input("Introduce your annual income: "))
if  anualearnings > 60000:
    print("Your porcentage of taxes is about 45.")
elif  anualearnings >= 35000 and anualearnings <= 60000:
    print("Your porcentage of taxes is about 30.")
elif  anualearnings >= 20000 and anualearnings < 35000:
    print("Your porcentage of taxes is about 20.")
elif  anualearnings >= 10000 and anualearnings < 20000:
    print("Your porcentage of taxes is about 15.")
elif  anualearnings < 10000:
    print("Your porcentage of taxes is about 5.")
