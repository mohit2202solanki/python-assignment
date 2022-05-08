class calculation():
	def area(self,p1 = None,p2 = None):
		if (p1 != None and p2 != None): 
			x = p1 * p2  
			return x 
		elif (p1 != None and p2 == None):
			x = 3.14 * p1 * p1 
			return x 
		else :
			x = "No parameters passed"
			return x 

y = calculation()
rectangle = y.area(12,3)
circle = y.area(12)
circle = round(circle,2)

print("Area of Rectangle : ",rectangle)
print("Area of Circle  : ",circle)
