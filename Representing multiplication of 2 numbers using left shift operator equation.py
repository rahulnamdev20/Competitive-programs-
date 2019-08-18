
def multiply(n, m): 
	ans = 0
	count = 0
	while (m): 
		
		if(m==1):
		    print("(",n,"<<",count,")")
		    break
		if (m % 2 == 1): 
			ans += n << count
			print("(",n,"<<",count,") +",end=" ")
            
		
		count += 1
		m = int(m/2) 

	return ans 

# Driver code 
if __name__ == '__main__': 
	n = 5
	m = 4
	print(multiply(n, m)) 
	

