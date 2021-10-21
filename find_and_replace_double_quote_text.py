old_string= "sushant'k"
if not old_string == None:
	if old_string.find('"') > 0:
		f_old=10
		print(f_old)
	elif old_string.find("'") > 0:
		f_old=20
		print(f_old)
else:
	f_old=0

if f_old == 10:
	new_string=old_string.replace('"','')
	print(new_string)
elif f_old == 20:
	new_string=old_string.replace("'",'')
	print(new_string)
else:
	old_string = old_string
	print(old_string)
    
