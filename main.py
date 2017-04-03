import re

#Function to open the Log file
def Open_log_file() :

	
	log_fh = open ("log.txt", "r")
	print "Log file open succesfully at log_fh : ", log_fh
	BCF_value_find(log_fh)
		
	
#Function to prase the log file

def BCF_value_find(log_fh) :
	
	print "In Fucntion to find the BCF"
	for line in log_fh :
		
		if re.search("BCF=[0-9]{,3}",line, re.I) :
			
			BCF  = re.search("BCF=[0-9]{0,3}", line, re.I)
			BCF = BCF.group()
			BCF_value = re.search("[0-9]{0,3}$", BCF, re.I).group()
			print "The BCF value is : ", BCF_value
			BSC_id_find (log_fh)
			break			
	print "Out of for loop"
	
#Fuction to find the BSC id
def BSC_id_find (log_fh) :

	print "In Function to find the BSC ID"
	
	for line in log_fh :
	
		if re.search("BSC", line, re.I) :
	
			line = line.strip("\n")
			line = line.split(" ")
			  
			for elem in line :
				
				if elem == "" :
				
					line.remove(elem)	 
			line = line[1]
			print "The BSC ID is : ", line
			BTS_id_find (log_fh)
			break
#Function to find the BTS ID			 
def BTS_id_find (log_fh, *args) :

	print "In function to find the BTS ID"
	count = args
	
	if count != 0 :
		for line in log_fh :
	
			if re.search("BTS-[0-9]{0,4}", line, re.I) :
		
				bts_id = re.search("BTS-[0-9]{0,4}", line, re.I).group()					
				print bts_id
				BTS_cilli_name(log_fh)
				TRX_value_find(log_fh)
					
#Function to find the BTS Cilli Name
def BTS_cilli_name(log_fh) :

	print "In function to find the Cilli name"
	
	for line in log_fh :
		
		if re.search("RF/-", line, re.I) :
		
			line = line.strip("\n")
			line = line.strip(" ")
			line = line.split(" ")
			bts_cilli_name = line[0]
			print bts_cilli_name
			break
			
#Fucntion to find the TRX value			
def TRX_value_find(log_fh) :

	print "In fucntion to find the TRX value"
	count = 0
	
	for line in log_fh :
			
		if re.search("[0-9]", line, re.I) :
			
			if re.search("TRX", line, re.I) :
			
				trx_value = re.search("TRX-[0-9]{0,3}", line, re.I).group()
				count = count + 1
				print trx_value	
			
		else :
			
			BTS_id_find(log_fh, count)
			
Open_log_file()











