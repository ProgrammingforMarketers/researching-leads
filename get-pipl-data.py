import piplapis.search
piplapis.search.default_api_key = '6z9w7t9b5de5juzebdpbn2cz'
from piplapis.search import SearchAPIRequest
from piplapis.data import Person, Name, Address, Job
from piplapis.search import SearchAPIError
import gspread
from gmail_variables import *


gc = gspread.login(GMAIL_USERNAME, GMAIL_PASSWORD)
wks = gc.open("Lesson 7 Sample Spreadsheet")
emailSheet = wks.worksheet("Email")
emails = emailSheet.col_values(2) #This will get a list of all the emails in column 2
emails = emails[1:] #This gets rid of the header by removing the first element (the "0th" element)

def getName(emailAddress):
	request = SearchAPIRequest(email=emailAddress)

	try:
    		response = request.send()
	except SearchAPIError as e:
    		print e.http_status_code, e

	return response.person.names[0]
	# You can also use response.person.addresses[0] to get their address, or response.person.jobs[0] to get their job



for i in range(0,len(emails)):
	info = getName(emails[i])
	emailSheet.update_cell(i+2,1,info) #This updates the first column (1) and the "i+2" row with the name info. We need the i+2 row since i starts counting at 0, and we have the header in the first line
