
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
print("MONTH: March 2018") # TODO: get month and year
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

import matplotlib.pyplot as plt

bar_data = [sorted_product_sales]

products = []
sales = []

for d in bar_data:
  products.append(d["name"])
  sales.append(d["monthly_sales"])

plt.bar(products, sales)
plt.ylabel("Sales")
plt.xlabel("Products")
plt.show()
