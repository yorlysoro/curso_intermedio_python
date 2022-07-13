def run():
	my_list = [1 , "Hello", True, 5.8]
	my_dict = {
		'first_name' : "Fulanito",
		'last_name' : "Garcia"
	}

	super_list = [
	{
		'first_name' : "Fulanito",
		'last_name' : "Garcia"
	},
	{
		'first_name' : "Juan",
		'last_name' : "Garcia"
	},
	{
		'first_name' : "Jose",
		'last_name' : "Garcia"
	},
	{
		'first_name' : "yorlys",
		'last_name' : "Garcia"
	},
	]

	super_dict = {
		'natural_nums' : [1,2,3,4],
		'integer_nums' : [-1,-2,0,1,2],
		'float_nums' : [1.5,4.5,8.5]
	}

	for key, value in super_dict.items():
		print(key, "-", value)

	



if __name__ == '__main__':
	run()