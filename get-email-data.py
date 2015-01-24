from towerDataApi import TowerDataApi
import urllib3
import smtplib
import gspread
from gmail_variables import *

urllib3.disable_warnings()

gc = gspread.login(GMAIL_USERNAME, GMAIL_PASSWORD)
wks = gc.open("YOUR SPREADSHEET")
emailSheet = wks.worksheet("Email")

emails = emailSheet.col_values(2) #This will get a list of all the emails in column 2
emails = emails[1:]

def getEmailInfo(email):
	api = TowerDataApi.TowerDataApi(TOWER_DATA_API)
	return api.query_by_email(email)
	{u'gender': u'Male', u'age': u'25-34'}

for i in range(0,len(emails)):
	info = getEmailInfo(emails[i])
	print info
	   
	try:
		emailSheet.update_acell(i+2,4,info["gender"])
	except:
		emailSheet.update_acell(i+2,4,"none")
	 
	try:
		emailSheet.update_acell(i+2,3,info["age"])
	except:
		emailSheet.update_acell(i+2,3,"none")