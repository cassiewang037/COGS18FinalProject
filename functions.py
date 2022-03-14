import pandas as pd
number = input("How many colors/style does this project have? ") 
count = 1

def create_catalog(): 
    """ This can create a catalog of product style or color and its price. 
    The length of the list is restricted by the number of color/style input above. 
    
    PARAMETERS
    ----------
    none
    
    RETURNS
    -------
    cat : DataFrame 
        List of color or style of the product and its price. 
    """
    product_list = []
    count = 1

    while count <= int(number): 
        color = str(input("What color/style it is? "))
        product_price = input("What is the price of product in this color/style? ")
        product_list.append({'color': color, 
                             'price': product_price}) 
        count += 1 

    global cat
    cat = pd.DataFrame(product_list)
    print("This is your catalog:")
    
    return cat

def create_order(): 
    """Create a list of order with customer ID and price of their orders. 
    The price also includes splited design and mold fee and delivery fee. 
    
    PARAMETERS
    ----------
    none
    
    RETURNS
    -------
    updated_list : DataFrame 
        DataFrame of customer ID and updated price with split. 
    """
    global customer_id 
    customer_id = []
    price_list = []
    
    while True: 
        current_id = input("What is the ID of this customer? ")
        price = 0
        count = 1
        order_list = []
        customer_list = [] 
        customer_id.append(current_id)
        

        while count <= int(number): 

            amount_purchase = input("How much " + cat['color'][count-1] + " product is this customer purchasing?")
            order_list.append({'selected color': cat['color'][count-1], 
                               'product price': cat['price'][count-1], 
                               'amount purchased': amount_purchase})
            price += float(cat['price'][count-1]) * int(amount_purchase)
            count += 1
            print(order_list)
        
        price_list.append(price)
        customer_list = pd.DataFrame({'price': price_list}, index = customer_id)
        
        answer = input("Would you like to add more order? (please eneter'yes' or 'no') ")
        if answer == 'yes':
            print(customer_list)
        if answer == 'no':
            print(customer_list)
            break 
    
    design_fee = input("What is the design fee?") 
    mold_fee = input("What is the mold fee?") 
    num = input("What is the amount of people spilting the fee?")  
    split = (float(design_fee) + float(mold_fee)) / int(num)
    delivery = input("What is the delivery fee? ")
    split_fee = split + float(delivery)
    print("The splited fee for everyone is: " + str(split_fee))
    
    global updated_list 
    updated_list = customer_list + split_fee 
    
    return updated_list 


def create_payment(): 
    """ Create list of payment with customer ID and amount they paid. 
    It does not have to be in the same order as the list of orders. 
    
    PARAMETERS
    ----------
    none
    
    RETURNS
    -------
    paid_df : DataFrame 
        List of customer ID and payment. 
    """
    count = 1
    paid_list = []
    paid_id_list = []

    while count <= len(updated_list): 
        paid_id = input("What is the ID of this customer that made payment? ")
        paid_id_list.append(paid_id)

        customer_paid = input("How much does " + paid_id + " paid? ")
        paid_list.append(float(customer_paid))
        count += 1   

    print("This is your list of payment:") 
    global paid_df 
    paid_df = pd.DataFrame({'paid': paid_list}, index = paid_id_list)
    
    return paid_df

def compare(): 
    """This matches the list of orders and payment together if the IDs are correctly inputed. 
    
    PARAMETERS
    ----------
    none
    RETURNS
    -------
    frame : DataFrame 
        List of customer ID, order price and payment.
    """
    print("This is a list of orders and payment:")
    global frame 
    frame = updated_list.join(paid_df)
    
    return frame

def reminder(): 
    """This compares how much each customer paid and how much they are supposed to pay. 
    If the customer paid more or less than the order price, it will print out a message to remind them. 
    
    PARAMETERS
    ----------
    none
    
    RETURNS
    -------
    none
    """
    for name in customer_id: 
        if frame.loc[name]['price'] == frame.loc[name]['paid']: 
            print('@' + name + ', thank you so much!')
        if frame.loc[name]['price'] > frame.loc[name]['paid']: 
            difference = float(frame.loc[name]['price']) - float(frame.loc[name]['paid'])
            print('@' + name + ', please pay ' + str(difference) + '. Thank you for your support!')
        if frame.loc[name]['price'] < frame.loc[name]['paid']: 
            extra = float(frame.loc[name]['paid']) - float(frame.loc[name]['price'])
            print('@' + name + ', you paid extra ' + str(extra) + '. I will return the amount to you.')