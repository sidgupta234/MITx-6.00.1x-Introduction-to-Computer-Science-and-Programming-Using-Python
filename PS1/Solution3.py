def item_order(order):
    order_list=order.split()
    number_of_salad=0
    number_of_hamburger=0
    number_of_water=0
    for item in order_list:
        if item=='salad':
            number_of_salad+=1
        elif item=='hamburger':
            number_of_hamburger+=1
        else:
            number_of_water+=1
            
    return "salad:"+str(number_of_salad)+" hamburger:" + str(number_of_hamburger) + " water:" +  str(number_of_water)
