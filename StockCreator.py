# Written by Aaron Barge

import pandas as pd

df = pd.read_csv('companylist.csv', usecols=[0,1,2], header=0)
with open('create_stocks.txt', "w") as output:
    for index,row in df.iterrows():
        price = 0.0 if row['LastSale'] == 'nan' else row['LastSale']
        output.write("Stock.objects.create_stock(symbol=\"" + row['Symbol'] + "\", name=\"" + row['Name'] + "\", current_price=" + str(price) + ")\n")
