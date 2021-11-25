region(ram,1990,1950).
region(mike,1951,1970).
region(john,1971,1985).
region(ravi,1986,2010).

ruler(X,Y):-region(X,A,B),
	Y>=A,
	Y=<B.


