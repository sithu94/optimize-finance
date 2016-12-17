# Share Data Module
# Date: 1st December 2016
# Function: Return the data related to the portfolio shares
##########################################################
from yahoo_finance import Share
import time
class share_update:
	# Share price
	def return_share_price(company_code):
		while (1):
			company = Share(company_code)
			name = company.get_name()
			price = company.get_price()

			return(name,price)
			
			# return name,price