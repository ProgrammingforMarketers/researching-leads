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
emails = emails[1:] #This removes the first element of the list (the title of the column)

def getEmailInfo(email):
	api = TowerDataApi.TowerDataApi(TOWER_DATA_API)
	return api.query_by_email(email)
	{u'gender': u'Male', u'age': u'25-34'}

for i in range(0,len(emails)):
	info = getEmailInfo(emails[i]) #This takes every element in "emails" and looks for the gender and age
	print info
	   
	try:
		emailSheet.update_acell(i+2,4,info["gender"]) #This separates the gender element and adds it to your spreadsheet
	except:
		emailSheet.update_acell(i+2,4,"none")
	 
	try:
		emailSheet.update_acell(i+2,3,info["age"]) #This separates the age element and adds it to your spreadsheet
	except:
		emailSheet.update_acell(i+2,3,"none")