:- discontiguous pozywienie/1.
:- discontiguous zyje/2.
:- discontiguous obywatel/2.
%zadanie 1

czlowiek(markus).
obywatel(markus).
wladca(cezar).
proba_zamachu(markus, cezar).

nienawidzi(X, Y) :- \+(lojalny(X, Y)).
obywatel(X, rzym) :- obywatel(X, pompeje).
obywatel(X, rzym) :- lojalny(X, cezar); nienawidzi(X, cezar).
lojalny(X, Y) :- obywatel(X), wladca(Y), \+(proba_zamachu(X, Y)).

%lojalny(Markus, Cezar) == false

%zadanie 2

pozywienie(jablka).
pozywienie(kurczak).
zabija(cos, kogos).
%zabija(orzeszki, adam).
trujace(X) :- je(Y, X), zabija(X, Y).
pozywienie(X) :- \+trujace(X).
lubi(jan, X) :- pozywienie(X).
je(adam, orzeszki).
je(basia, X) :- je(adam, X).

% lubi(jan, orzeszki) == true
% 
%je(basia, X).
%X = orzeszki

%zadanie 3

urodzil(markus, 40).
obywatel(markus, pompeje).

%sposob I + II

zyje(X, Y) :- 
    (Y>=80,(obywatel(X, pompeje), urodzil(X, Z), Z>=80, Z > Y-150, Y >= Z));   
    (urodzil(X, Z), Z > Y-150, Y >= Z).

%sposob I

zyje(X, Y) :- Y>=80, ((obywatel(X, pompeje), urodzil(X, Z), Z>=80); (\+obywatel(X, pompeje))).

%zyje(markus, 80) == false

%sposob II

zyje(X, Y) :- urodzil(X, Z), Z > Y-150, Y >= Z.

%zyje(markus, 2021) == false





