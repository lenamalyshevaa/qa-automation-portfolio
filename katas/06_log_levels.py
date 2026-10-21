

def count_levels(path):
    try:
        with open(path) as f:
            counts = {}
            for lines in f:
                parts = lines.split()
                try: 
                    counts[parts[2]] = counts.get(parts[2], 0) + 1       
                except IndexError: 
                    continue
            return counts
    except FileNotFoundError:
        print("file not found")
        return None



def get_errors(path):
    try:
        with open(path) as f:
            errors = []
            for line in f:
                parts = line.split()
                try: 
                    if 'ERROR' == parts[2]:
                        errors.append(' '.join(parts[3:]))
                except IndexError: 
                    continue
            return errors
    except FileNotFoundError:
        print("file not found")
        return None



print(count_levels("app.log"))
print(get_errors("app.log"))
print(count_levels("nope.log"))
print(get_errors("nope.log"))



    
