
'''
fruits = ["apple", "pear", "apple", "kiwi", "apple"]
counts = {}
for fruit in fruits: 
    counts[fruit] = counts.get(fruit, 0) + 1


users = [
    {"name": "anna", "age": 25},
    {"name": "boris", "age": 31},
    {"name": "gleb", "age": 31}
]
for user in users:
    if user["age"] > 30:
        print(user["name"])
'''

def count_levels(path):
    with open(path) as f:
        counts = {}
        for lines in f:
            parts = lines.split()
            try: 
                counts[parts[2]] = counts.get(parts[2], 0) + 1       
            except IndexError: 
                continue
            except FileNotFoundError: 
                print('file not found')
                return None
            except Exception as e:
                def get_errors(path):
                    print('произошла ошибка:', e)
                    
                    
        return counts

count_levels("app.log")



    
