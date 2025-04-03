employees = [{"name": "Alice", "salary": 50000, "rating": 5},{"name": "Bob", "salary": 40000, "rating": 3},{"name": "Charlie", "salary": 35000, "rating": 2}]

updated_employees = list(map(lambda x: {
    "name": x["name"],
    "salary": round(x["salary"] * 1.10 if x["rating"] >=4 else (x["salary"] * 1.05 if x["rating"] == 3 else x["salary"] * 0.97),1),
    "rating": x["rating"]
}, employees))
print(updated_employees)