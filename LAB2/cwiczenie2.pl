%predykaty: mezczyzna(X), rodzic(X,Y)

%1
kobieta(X) :-
    \+mezczyzna(X).

kobieta(anna).
kobieta(baska).
rodzic(kasia, basia).
rodzic(stasia, kasia).
rodzic(daniel, anna).
rodzic(daniel, piotr).
rodzic(baska, anna).
rodzic(baska, pawel).
rodzic(baska, piotr).
mezczyzna(daniel).
mezczyzna(pawel).
mezczyzna(piotr).
lubi(kasia, anna).
lubi(kasia, daniel).



%2
ojciec(X, Y) :-
    mezczyzna(X),
    rodzic(X, Y).

%3
matka(X, Y) :-
    kobieta(X),
    rodzic(X, Y).

%4
corka(X, Y) :-
    kobieta(X),
    rodzic(Y, X).

%5
brat_rodzony(X, Y) :-
    mezczyzna(X),
    ojciec(Z, X), ojciec(Z, Y),
    matka(W, X), matka(W, Y).

%6
brat_przyrodni(X, Y) :-
    mezczyzna(X),
    ((ojciec(Z, X), ojciec(Z, Y)) ; (matka(W, X), matka(W, Y))),
    \+(((ojciec(Z, X), ojciec(Z, Y)) , (matka(W, X), matka(W, Y)))).

%7 B
kuzyn(X, Y) :-
    dziadkowie(Z, X), dziadkowie(Z, Y).

%8
dziadek_od_strony_ojca(X, Y) :-
    ojciec(Z, Y),
    ojciec(X, Z). 

%9
dziadek_od_strony_matki(X, Y) :-
    matka(Z, Y),
    ojciec(X, Z).

%10
dziadek(X, Y) :-
    rodzic(Z, Y),
    ojciec(X, Z).

%11
babcia(X, Y) :-
    rodzic(Z, Y),
    matka(X, Z).

%12
wnuczka(X, Y) :-
    kobieta(X),
    (babcia(Y, X); dziadek(Y, X)).

%+
wnuk(X, Y) :-
    babcia(Y, X); dziadek(Y, X).

%+
dziadkowie(X, Y) :-
    rodzic(Z, Y),
    rodzic(X, Z).

%13
przodek_do2pokolenia_wstecz(X, Y) :-
    rodzic(X, Y); 
    dziadkowie(X, Y).

%14
przodek_do3pokolenia_wstecz(X, Y) :-
    rodzic(X, Y);
    dziadkowie(X, Y);
    (dziadkowie(Z, Y), rodzic(X, Z)).
%A
rodzenstwo(X, Y) :-
    matka(Z, X), matka(Z, Y),
    ojciec(W, X), ojciec(W, Y).

%E
rodzenstwo_przyrodnie(X, Y) :-
    rodzic(Z, X), rodzic(Z, Y).

%C
wspolny_wnuk(X, Y) :-
    wnuk(Z, X), 
    wnuk(Z, Y).

%D
przybrany_rodzic(X, Y) :-
    true_love(Z, Y),
    rodzic(Z, X),
    \+(rodzic(Y, X)).

%F X to szwagier/bratowa Y
szwagier(X, Y) :-
	true_love(Z, Y), rodzenstwo(Z, X).

%G 
g(X, Y) :-
    rodzic(Z, X), rodzic(Z, Y),
    rodzic(W, X), rodzic(U, Y),
    rodzic(W, U).
    


%predykaty: lubi(X, Y)
przyjazn(X, Y) :-
    lubi(X, Y),
    lubi(Y, X).

nieprzyjazn(X, Y) :-
    \+(lubi(X, Y)),
    \+(lubi(Y, X)).

niby_przyjazn(X, Y) :-
    (lubi(X, Y), \+lubi(Y, X));
    (lubi(Y, X), \+lubi(X, Y)).

loves(X, Y) :-
    lubi(X, Y),
    (kobieta(Y) -> (\+((kobieta(Z), lubi(X, Z), Z \= Y)));
	mezczyzna(Y) -> (\+((mezczyzna(Z), lubi(X, Z), Z \= Y)))).

%związek
true_love(X, Y) :-
    loves(X, Y),
    loves(Y, X).
    


    




    