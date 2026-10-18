import json 
from pathlib import Path 

def total_by_client(path):
	ppath = Path(path)
	try:
		with open(ppath) as f:
			data = json.load(f)
			c_sum = {}
			for c in data: 
				name = c["client"]
				amount = c["amount"]
				if name in c_sum:
        					c_sum[name] += amount 
				else:
						c_sum[name] = amount  
			for client, amount in c_sum.items():
				return(c_sum)
	except:
		print("Something went wrong when opening the filea")
		return None


print(total_by_client("orders.json"))
