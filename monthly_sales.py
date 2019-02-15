
import os
import csv
import itertools
from operator import itemgetter

def month_lookup(month):
	year_month={'01':'January','02':'February','03':'March','04':'April',
	'05':'May','06':'June','07':'July','08':'August','09':'September','10':'October',
	'11':'November', '12':'December'}
	return year_month[month]

#Taken and adapted from https://github.com/hiepnguyen034/data_dashboard/blob/master/exec_dash.py

while True:
	CSV_FILENAME = input('Please enter the time period in the format sales-YYYYMM: ')
	CSV_NAME = CSV_FILENAME+'.csv'
	csv_filepath = os.path.join("data/", CSV_NAME)
	if not os.path.isfile(csv_filepath):
	 	print("Sorry, this file does not exist, please make sure to enter a file with correct format, e.g:'sales-201803'")
	else:
	 	break
#Taken and adapted from https://github.com/hiepnguyen034/data_dashboard/blob/master/exec_dash.py

def to_usd(my_price):
    return "${0:,.2f}".format(my_price)

transactions = []

with open(csv_filepath, "r") as csv_file:
    reader = csv.DictReader(csv_file)
    for od in reader:
        transactions.append(dict(od)) 

sales_prices = [float(transaction["sales price"]) for transaction in transactions] 
total_monthly_sales = sum(sales_prices)

product_sales = []

sorted_transactions = sorted(transactions, key=itemgetter("product"))
transactions_by_product = itertools.groupby(sorted_transactions, key=itemgetter("product"))

for product, product_transactions in transactions_by_product:
    monthly_sales = sum([float(transaction["sales price"]) for transaction in product_transactions])
    product_sales.append({"name": product, "monthly_sales": monthly_sales})

sorted_product_sales = sorted(product_sales, key=itemgetter("monthly_sales"), reverse=True)
top_sellers = sorted_product_sales[0:10] 

print("----------------------------------------")
print(f" MONTHLY SALES REPORT")
print("-----------------------")
print("TIME: "+ month_lookup(CSV_FILENAME[-2:])+' '+ str(CSV_FILENAME[6:10])) #taken from hiep 
print("-----------------------")
print("CRUNCHING THE DATA...")
print("----------------------------------------")
print(f"TOTAL SALES: {to_usd(total_monthly_sales)}")

print("-------------------------")
print("TOP SELLING PRODUCTS:")

counter = 0
for top_seller in top_sellers:
    counter = counter + 1
    product_name = top_seller["name"]
    sales_usd = to_usd(top_seller["monthly_sales"])
    print(f"  {counter}. {product_name} ({sales_usd})")

#Inspired from
#https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/master/exercises/sales-reporting/csv_solution_further.py

# breakpoint()

##Graph Output Setup (Taken from Chart Gallery exercise structure)
#import matplotlib.pyplot as plt
#
##bar_data = [top_sellers]
#
#products = []
#sales = []
#
#for d in top_sellers: 
#  products.append(d["name"])
#  sales.append(d["monthly_sales"])
#
#plt.bar(products, sales)
#plt.ylabel("Sales (Dollars) ")
#plt.xlabel("Products")
#plt.title("Top Selling Products " + month_lookup(CSV_FILENAME[-2:])+' '+ str(CSV_FILENAME[6:10]))
#plt.show()

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker

products = []
sales = []

for d in top_sellers: 
  products.append(d["name"])
  sales.append(d["monthly_sales"])

plt.rcdefaults()
fig, ax = plt.subplots()

ax.barh(products, sales, align='center',
        color='blue', ecolor='black')
ax.set_yticks(products)
ax.set_yticklabels(products)
ax.invert_yaxis() 
ax.set_ylabel('Product') 
ax.set_xlabel('Sales (Dollars)')
formatter = ticker.FormatStrFormatter('$%1.2f') #https://matplotlib.org/gallery/pyplots/dollar_ticks.html
ax.xaxis.set_major_formatter(formatter)
ax.set_title("Top Selling Products " + month_lookup(CSV_FILENAME[-2:])+' '+ str(CSV_FILENAME[6:10]))
plt.show()
#https://matplotlib.org/gallery/lines_bars_and_markers/barh.html

