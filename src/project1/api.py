from sodapy import Socrata

def get_parking(val: int, my_key:str, num_pages: int = 1)-> dict:
	client = Socrata(
		"data.cityofnewyork.us", my_key)
	
	#get first 10 results
	df = client.get("nc67-uf89", limit=val)*num_pages
	return df

	#client.get("nc67-uf89", limit=10, offset=10)

	#client.get("nc67-uf89", select='COUNT(*)')


