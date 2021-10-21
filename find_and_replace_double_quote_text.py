
old_string= 'sushant"k'

if not old_string == None:
	f_old=old_string.find('"')
	print(f_old)
else:
	f_old=0

if f_old > 0:
	new_string=old_string.replace('"','')
	print(new_string)
else:
	old_string = old_string
	print(old_string)
