
num_salesmen = 10
num_items = 5

sales_data = []
grand_total = 0


for i in range(num_salesmen):
    name = input("Enter salesman name: ")
    sales = []
    
    for j in range(num_items):
        value = int(input(f"Enter sales for Item {j+1}: "))
        sales.append(value)
    
    total_sales = sum(sales)
    grand_total += total_sales
    
    sales_data.append([name] + sales + [total_sales])


print("\nName\tItem1\tItem2\tItem3\tItem4\tItem5\tTotalSales")
print("--------------------------------------------------------------")

for data in sales_data:
    for value in data:
        print(value, end="\t")
    print()

print("--------------------------------------------------------------")
print("Grand Total:\t", grand_total)