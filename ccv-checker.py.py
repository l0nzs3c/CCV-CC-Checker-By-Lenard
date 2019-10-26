import random
import requests
import requests as reqs
import time

#CODED BY LENARD

print("[+] Establishing Secure Connection")
time.sleep(1)
print("[+] Connection Status: Connected!")
time.sleep(1)
print("[!] Database Braintree Checking!")
time.sleep(1)
print("[+] Braintree API")
time.sleep(0.1)
print("[+] Connected to API")
time.sleep(1)
print("[*] Enter your Bin mga lodi! HAHAHAHAHA")





def BinChecker():
	FBin = (raw_input("Enter the BIN : "))
	Bin = FBin.replace(' ' , '')
	Bin = Bin.replace('x' ,'')
	Bin = Bin.replace('X', '')
	Bin = Bin[:6]

	url = "https://www.lookupbin.com/bin?bin=" + Bin

	response = reqs.get(url)

	if "is not a known BIN" in (response.text):
		print "\n", Bin, "is not a known BIN"

		check = raw_input("\nWARNING....!..The BIN is not proper BIN. CC with these BIN may not works properly \n Do you want to change the BIN (yes/no | Default:yes): ")
		if check in ['n', 'N', 'No', 'no', 'NO']:
			quit()
		else:
			BinChecker()
	else:
		if "BIN" in (response.text):
			BIN = ((response.text).split("BIN:",2)[-1]).split("</div></div>", 1)[0][28:]
			print "\nBIN:", BIN

		if "Network" in (response.text):
			Network = str((response.text).split("Network:",2)[-1]).split("</div></div>", 1)[0][28:]
			print "Network:", Network

		if "Brand" in (response.text):
			Brand = str((response.text).split("Brand:",2)[-1]).split("</div></div>", 1)[0][28:]
			print "Brand:", Brand

		if "Type" in (response.text):
			Type = str((response.text).split("Type:",2)[-1]).split("</div></div>", 1)[0][28:]
			print "Type:", Type

		if "Prepaid" in (response.text):
			Prepaid = (response.text).split("Prepaid:",2)[-1].split("</div></div>", 1)[0][28:]
			print "Prepaid:", Prepaid

		if 'Country:' in (response.text):
			Country = str((response.text).split("Country:",2)[-1]).split("</div></div>", 1)[0][28:]
			print "Country:", Country

		if "Bank:" in (response.text):
			Bank = ((response.text).split("Bank:",2)[-1]).split("</div></div>", 1)[0][28:]
			print "Bank:", Bank
		print "\nWARNING....!we are not responsible for your malicious activities..!"
		ccgen(FBin, Network)

def ccgen(FBin, Network):
	if (len(FBin) < 16):
		FBin = FBin+((16-(len(FBin)))*'x')
	
	TBin = FBin
	nocc = input("\nHow many Card needed : ")

	print "\nGenerated Credit Cards"
	print "Credit Card No | Month | Years | CVV | Card Status"
	for i in range(nocc):
		for i in range(len(TBin)):

			n = str(random.randint(0, 9))
			m = str(random.randint(01, 12))
			if (len(m) == 1):
				m = '0' + m
			y = str(random.randint(2021, 2025))
			
			if (Network == 'amex'):
				cv = str(random.randint(1000, 9999))
			else:
				cv = str(random.randint(100, 999))	

			c = TBin[i]
			if (c == 'x' or c == 'X'):
				FBin = FBin[:i] + str(n) + FBin[i+1:]

		cc = FBin + '|' + m + '|' +  y + '|' + cv
		ccchecker(cc)

def ccchecker(cc):

	url = "https://mrchecker.net/card/ccn1/alien07.php"
	
	form = {
		'ajax':'1',
		'cclist':cc,
		'do':'check'
	}

	response = reqs.post(url, form, stream = True)

	if 'Live' in (response.text):
		print cc, "| Live"
	elif 'Unknown' in (response.text):
		print cc, "| Unknown"
	else :
		print cc, "| Die"

BinChecker()

print '\nIf there is no Live BINs try once again by increasing the number of Card needed'
