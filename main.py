import sys
import os 
from src.project1.api import get_parking

if __name__=='__main__':
	args = sys.argv[1:]
	print(args)
	page_size = args[0]
	my_key = os.environ.get('APP_KEY')
	try:
		num_pages = int(args[1])
	except:
		num_pages = 1

	parking_data = get_parking(page_size, my_key, num_pages)
	
	try:
		output_fn = argv[2]
		with open(output_fn, "w") as fw:
			fw.write(str(parking_data))
	except Exception:
		print(parking_data)
	


