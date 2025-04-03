customers = [{"name": "Emma", "age": 22, "total_purchase": 150.0},{"name": "John", "age": 30, "total_purchase": 200.0},{"name": "Grace", "age": 45, "total_purchase": 180.0}]

eligible_customers = filter(lambda x: x["age"] <= 40, customers)

updated_customers = list(map(lambda x: {
    "name": x["name"], 
    "age": x["age"], 
    "total_purchase": x["total_purchase"] * 0.9 if 18<= x["age"] <= 25 else x["total_purchase"] * 0.95}, eligible_customers))

print(updated_customers)