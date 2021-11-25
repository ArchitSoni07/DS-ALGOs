owns(john,ai).
owns(mary,ml).
owns(john,book(ai,kelvin)).
owns(mary,book(ml,trever)).
owns(john,book(ai,author(rquel,kelvin))).
owns(mary,book(ml,author(jane,trever))).
owns(john,book(X,author(rquel,kelvin))).
owns(marry,book(_y, author(jane,trever))).

sum(X,Y,Z):-
 S is +(X,*(Z,Y)),
 write(S).
P=sum(7,8,5).
owns(marry,book(+(7,8),X,author(rquel,kelvin))).
