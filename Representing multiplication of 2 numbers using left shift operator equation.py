
def multiply(n, m): 
	ans = 0
	count = 0
	while (m): 
		
		if(m==1):
		    print("(",n,"<<",count,")")
		    ans += n << count
		    break
		if (m % 2 == 1): 
			ans += n << count
			print("(",n,"<<",count,") +",end=" ")
            
		
		count += 1
		m = int(m/2) 

	return ans 

# Driver code 
if __name__ == '__main__': 
	n = 6
	m = 7
	print("value is ",multiply(n, m)) 
	

