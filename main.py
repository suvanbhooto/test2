#!/usr/bin/env python

def add_num(a,b):
	sum=a+b;
	return sum;
	
def mul_num(a,b):
	product=a*b;
	return product;
	
def main():
	import sys
	print(sys.argv)
	i=(len(sys.argv)-1)
	print("le nombre d'arguments : ",i)
	
	ans=str(input("Voulez vous ajouter 2 entier?[y/n]:")) 
	
	if (ans=='y'):
		if (i==0):
			n1=int(input("Inserer le premier argument : "))
			n2=int(input("Inserer le deuxieme argument : "))
			x = int (n1)
			y = int (n2)
			print(add_num(x,y))	
		elif (i==1):
			n1=int(input("Inserer le deuxieme argument : "))
			x = int (sys.argv[1])
			y = int (n1)
			print(add_num(x,y))	
		elif (i==2):
			x = int (sys.argv[1])
			y = int (sys.argv[2])
			print(add_num(x,y))
		else:
			print("erreur : veuiller inserer que deux arguments")
	else:
		print("")
	
main()
