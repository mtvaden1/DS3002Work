# Vaden, Michael (mtv2eva)
# 1. Write a query to get Product name and quantity/unit.  
Select northwind.products.product_name, northwind.products.quantity_per_unit FROM northwind.products;
# 2. Write a query to get current Product list (Product ID and name).  
Select northwind.products.id, northwind.products.product_name FROM northwind.products;
# 3. Write a query to get discontinued Product list (Product ID and name).
Select northwind.products.id, northwind.products.product_name FROM northwind.products 
WHERE northwind.products.discontinued = TRUE;
	# There are only values of 0 for discontinued... so none are discontinued?
# 4. Write a query to get most expense and least expensive Product list (name and unit price).  
Select MAX(northwind.products.product_name), MAX(northwind.products.list_price), MIN(northwind.products.product_name), MIN(northwind.products.list_price) FROM northwind.products;
# 5. Write a query to get Product list (id, name, unit price) where current products cost less than $20.  
Select northwind.products.id, northwind.products.product_name, northwind.products.list_price FROM northwind.products 
WHERE northwind.products.list_price < 20;
# 6. Write a query to get Product list (id, name, unit price) where products cost between $15 and $25.  
Select northwind.products.id, northwind.products.product_name, northwind.products.list_price FROM northwind.products 
WHERE northwind.products.list_price < 25 AND northwind.products.list_price > 15;
# 7. Write a query to get Product list (name, unit price) of above average price.  
Select northwind.products.product_name, northwind.products.list_price FROM northwind.products 
WHERE northwind.products.list_price >
	(Select AVG(northwind.products.list_price) FROM northwind.products);
# 8. Write a query to get Product list (name, unit price) of ten most expensive products.  
Select northwind.products.product_name, northwind.products.list_price FROM northwind.products 
order by northwind.products.list_price desc
LIMIT 10;
# 9. Write a query to count current and discontinued products. 
Select northwind.products.discontinued, count(*) FROM northwind.products
group by northwind.products.discontinued;
	# All 45 discontinued product values = 0 so there are no discontinued products?
# 10. Write a query to get Product list (name, units on order, units in stock) of stock is less than the quantity on order.  
Select northwind.products.product_name, northwind.order_details.quantity, northwind.inventory_transactions.quantity
FROM northwind.products, northwind.order_details, northwind.inventory_transactions
WHERE northwind.inventory_transactions.quantity < northwind.order_details.quantity;
