import pandas as pd

#Load Data
customers = pd.read_csv('../data/raw/olist_customers_dataset.csv')
orders = pd.read_csv('/../data/raw/olist_orders_dataset.csv')
order_items = pd.read_csv('../data/raw/olist_order_items_dataset.csv')

#Below lines are used to check the information about the datasets
# customers.info()
# orders.info()
# order_items.info()

#Convert date columns to datetime
date_columns = [
    'order_purchase_timestamp',
    'order_approved_at',
    'order_delivered_carrier_date',
    'order_delivered_customer_date',
    'order_estimated_delivery_date'
]

for col in date_columns:
    orders[col] = pd.to_datetime(orders[col], errors='coerce')

order_items['shipping_limit_date'] = pd.to_datetime(order_items['shipping_limit_date'], errors='coerce')

#verifying the above conversion
# orders.info()
# order_items.info()

#check if you have nulls in the important columns
print(customers.isnull().sum())#columns
print(orders.isnull().sum())
print(order_items.isnull().sum())
#Here order_approved_at, order_Delivered_carrier_date and order_delivery_ustomer_date can be null in real
#scenariors as well. So leaving them as is.

# Merge datasets
df = orders.merge(customers, on='customer_id')
df = df.merge(order_items, on='order_id')

# Save processed data
df.to_csv("../data/processed/cleaned_sales_data.csv", index=False)

print("Data cleaned and saved!")