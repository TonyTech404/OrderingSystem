data_gulay=[]
total=[]
while True:
    print("Teket's Gulay Store")
    def gulay(uri):
        return uri
    print("Kangkong $50")
    print("Alogbate $40")
    print("Talbos ng Kamote $40")
    print("Upo $20")
    print("Sitaw $50")
    uri = input("What you want to buy? ").upper()
    data_gulay.append(uri)

    def quantity():
        return ilan
    ilan = float(input("How many did you want to purchase? "))

    def calculation():
        if uri == "KANGKONG":
            a = ilan * 50
            print("Your order is Kangkong ", "with a quantity of : ", ilan)
            print("The total amount of your purchased is: ",a)
        elif uri == "ALOGBATE":
            b = ilan * 40
            print("Your order is Alogbate ", "with a quantity of : ", ilan)
            print("The total amount of your purchased is: ",b)
        elif uri == "TALBOS NG KAMOTE":
            c = ilan * 40
            print("Your order is Talbos ng Kamote ", "with a quantity of : ", ilan)
            print("The total amount of your purchased is: ",c)
        elif uri == "UPO":
            d = ilan * 20
            print("Your order is Upo ", "with a quantity of : ", ilan)
            print("The total amount of your purchased is: ",d)
        elif uri == "SITAW":
            e = ilan * 50
            print("Your order is Sitaw ", "with a quantity of : ", ilan)
            print("The total amount of your purchased is: ",e)
        else:
            exit()
    total.append(calculation())

    print("")
    aalis = input("Do you still want to order: Yes/No?").upper()
    if aalis == "YES":
        continue
    elif aalis == "NO":
        break
    else:
        exit()

data = data_gulay
print(data)
katapusan = sum(total)
print(katapusan)