def safe_divide(a, b): 
	try: 
		return a/b
	except TypeError:
		print('можно использовать только числа')
		return None 
	except ZeroDivisionError: 
		print('на ноль делить нельзя')
		return None 


print(safe_divide(10, 2))    
print(safe_divide("10", 2))
print(safe_divide(7, 0)) 
print(safe_divide(7.5, 2))
print(safe_divide(None, 2))
