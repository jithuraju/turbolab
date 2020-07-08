from datetime import date
create_date=input("enter the date of creation of the server in dd-mm-yyyy:")
delete_date=input("enter the date of deletion of the server in dd-mm-yyyy:")

def server_cost(create_date,delete_date):
	dd1,mm1,yy1=create_date.split('-')
	#print(dd1,mm1,yyyy1)
	dd2,mm2,yy2=delete_date.split('-')
	#print(dd2,mm2,yyyy2)
	d1=int(dd1)
	d2=int(dd2)
	m1=int(mm1)
	m2=int(mm2)
	y1=int(yy1)
	y2=int(yy2)
	dcre=date(y1,m1,d1)
	ddel=date(y2,m2,d2)
	temp=ddel-dcre
	#print(temp.days)
	if(temp.days==0):
		cost=20
		print(cost)
	elif(temp.days>365):
		cost=20000
		print(cost)
	elif(temp.days>30 and temp.days<=365):
		cost=1000*(temp.days//30)
		print(cost)
	elif(temp.days<30):
		cost=30*temp.days
		print(cost)	
	
server_cost(create_date,delete_date)		
					
