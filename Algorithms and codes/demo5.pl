population(china,100).
population(india,85).
population(usa,30).
population(bhutan,9).

area(china,10).
area(india,4).
area(usa,12).
area(bhutan,2).

density(X,Y):-population(X,Pop),area(X,Ar),Y is Pop/Ar.
