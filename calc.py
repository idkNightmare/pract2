list_pok=[]
def add_item(name,price,quantity):
    list_pok.append({"name":name,"price":price,"quantity":quantity})
def show_item():
    if not list_pok:
        print("список пустий")
        return
    
    for item in list_pok:
        subtotal=item['quantity']*item['price']
        print(f"{item['name']}: {item['quantity']}*{item['price']:.2f} = {subtotal:.2f} грн")
def total_price():
    total=sum(item['quantity']*item['price'] for item in list_pok)
    return total
while True:
    item_name=input("введіть назву предмету(або stop щоб закінчити): ").strip()
    if not item_name:
        print("ви не ввели предмет")
        continue
    elif item_name=="stop".lower():
        break
    
    try:
        item_price=float(input("введіть ціну предмета: "))
        item_quantity=float(input("введіть кількість предметів: "))
        if item_price<0 or item_quantity<0:
            print("Ціна або кількість не може бути відємною")
            continue
        add_item(item_name,item_price,item_quantity)
    except ValueError:
        print("Помилка!! ви ввели не той тип данних")
        continue   
print("-" * 30)
show_item()
print("=" * 30)
print(f"загальна сума: {total_price():.2f} грн")
print("=" * 30)
