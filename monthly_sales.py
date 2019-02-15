
import os
import csv
import itertools
from operator import itemgetter

def to_usd(my_price):
    return "${0:,.2f}".format(my_price)

#
# INPUTS
#

csv_filename = "sales-201803.csv" # TODO: allow user to specify

csv_filepath = os.path.join(csv_filename)

transactions = []

with open(csv_filepath, "r") as csv_file:
    reader = csv.DictReader(csv_file)
    for od in reader:
        transactions.append(dict(od)) 

sales_prices = [float(transaction["sales price"]) for transaction in transactions] 
total_monthly_sales = sum(sales_prices)

print(total_monthly_sales)

# breakpoint()

#
# OUTPUTS
#
#
#print("-----------------------")
#print("MONTH: March 2018") # TODO: get month and year
#
#print("-----------------------")
#print("CRUNCHING THE DATA...")
#
#print("-----------------------")
#print(f"TOTAL MONTHLY SALES: {to_usd(monthly_total)}")
#
#print("-----------------------")
#print("TOP SELLING PRODUCTS:")
#
#rank = 1
#for d in top_sellers:
#    print("  " + str(rank) + ") " + d["name"] + ": " + to_usd(d["monthly_sales"]))
#    rank = rank + 1
#
#print("-----------------------")
#print("VISUALIZING THE DATA...")
#
#
##Graph Output Setup (Taken from Chart Gallery exercise structure)
#
#import matplotlib.pyplot as plt
#
#bar_data = [
#]
#
#products = []
#sales = []
#
#for s in bar_data:
#  products.append(s["products"])
#  sales.append(s["sales"])
#plt.bar(products, sales)
#plt.ylabel("Products")
#plt.xlabel("Sales")
#plt.show()
