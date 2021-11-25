go:-write('write the numbers'),nl,
read(X),nl,
read(Y),nl,
com(X,Y).
com(X,Y):-X>Y,write('x is bigger value');
X<Y,write('y is bigger value').

