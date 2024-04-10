Zadanie 1
a) stałe indywiduowe: Markus, Cezar
predykaty: człowiek(x), obywatel(x, y) [x jest obywatelem y], władca(x), lojalny(x, y) [x jest lojalny wobec y], proba_zamachu(x, y) [x próbował dokonać zamachu na y], nienawidzi(x, y) [x nienawidzi y]

1. człowiek(Markus)
2. obywatel(Markus, Pompeje)
3. ∀x obywatel(x, Pompeje) -> obywatel(x, Rzym)
4. władca(Cezar)
5. ∀x obywatel(x, Rzym) -> lojalny(x, Cezar) ∨ nienawidzi(x, Cezar)
6. ∀x∃y lojalny(x, y)
7. ∀x∀y władca(y) ∧ proba_zamachu(x, y) -> ~lojalny(x, y)
8. proba_zamachu(Markus, Cezar)
 
b) Z formuły 4, 7, 8 można wyprowadzić dowód, że Markus nie był lojalny wobec Cezara. 

c) CNF

1. człowiek(Markus)
2. obywatel(Markus, Pompeje)
3. ~obywatel(x, Pompeje) ∨ obywatel(x, Rzym)
4. władca(Cezar)
5. ~obywatel(x, Rzym) ∨ lojalny(x, Cezar) ∨ nienawidzi(x, Cezar)
6. lojalny(x, y)
7. ~władca(y) ∨ ~proba_zamachu(x, y) ∨ ~lojalny(x, y)
8. proba_zamachu(Markus, Cezar)

d) dowód metodą rezolucji - zakładamy, że Markus jest lojalny Cezarowi

1. władca(Cezar) | przesłanka
2. proba_zamachu(Markus, Cezar)	| przesłanka
3. ~władca(Cezar) ∨ ~proba_zamachu(Markus, Cezar) ∨ ~lojalny(Markus, Cezar) | przesłanka 
4. lojalny(Markus, Cezar) | przesłanka
5. ~proba_zamachu(Markus, Cezar) ∨ ~lojalny(Markus, Cezar) | rezolwenta 1. i 3.
6. ~lojalny(Markus, Cezar) | rezolwenta 5. i 2. 
7. □ | rezolwenta 6. i 4.

Pusta rezolwenta oznacza, że Markus nie może być lojalny wobec Cezara.


Zadanie 2

a)

1. ∀x pozywienie(x) -> lubi(Jan, x)
2. pozywienie(jabłka)
3. pozywienie(kurcza)
4. ∀x∀y je(x, y) ∧ ~zabija(y, x) -> pozywienie(y)
5. je(Adam, orzeszki)  ∧ ~zabija(orzeszki, Adam)
6. ∀x je(Adam, x) -> je(Basia, x)

b) CNF

1. ~pozywienie(x) ∨ lubi(Jan, x)
2. pozywienie(jabłka)
3. pozywienie(kurcza)
4. ~je(x, y)  ∨ zabija(y, x)  ∨ pozywienie(y)
5. je(Adam, orzeszki)  ∧ ~zabija(orzeszki, Adam)
6. ~je(Adam, x) ∨ je(Basia, x)

c) dowód metodą rezolucji - zakładam, że Jan nie lubi orzeszków

1. ~pozywienie(orzeszki) ∨ lubi(Jan, orzeszki) | przesłanka
2. ~je(Adam, orzeszki)  ∨ zabija(orzeszki, Jan)  ∨ pozywienie(orzeszki) | przesłanka
3. je(Adam, orzeszki)  | przesłanka
4. ~zabija(orzeszki, Adam) | przesłanka
4. ~lubi(Jan, orzeszki) | przesłanka
5. zabija(orzeszki, Jan)  ∨ pozywienie(orzeszki) | rezolwenta 2. i 3. 
6. pozywienie(orzeszki) | rezolwenta 5. i 4.
7. lubi(Jan, orzeszki) | rezolwenta 1. i 6.
8. □ | rezolwenta 7. i 4.

Pusta rezolwenta oznacza, że Jan lubi orzeszki.

d) dowód metodą rezolucji - jakie pożywienie je Basia

1. je(Adam, orzeszki) | przesłanka
2. ~je(Adam, x) ∨ je(Basia, x) | przesłanka
3. je(Basia, orzeszki) | rezolwenta 1. i 2.

Końcowa rezolwenta to je(Basia, orzeszki), oznacza to, że pożywieniem, które je Basia są orzeszki.

Zadanie 3

1. urodził(Markus, 40)
2. obywatel(Markus, Pompeje)
3. zyje(x, y) [x zyje w roku y]
5. ∀x obywatel(x, Pompeje) ∧ zyje(x, 79) -> ~zyje(x, 80)
6. ∀x∀t1∀t2 urodzil(x, t1) ∧ >(t2 - t1, 150) -> ~zyje(x, t2) [t1 - rok narodzin, t2 - czy w t2 x zyje?]

Czy markus żyje jeśli mamy rok 2021?

Sposób I - wybuch Wezuwiusza

1. urodzil(Markus, 40) | przesłanka
2. ∀x∀t1∀t2 urodzil(Markus, 40) ∧ >(2021 - 40, 150) -> ~zyje(Markus, 2021)

Poprzedniki implikacji są prawdziwe, czyli następnik musi być prawdziwy. Markus musiał umrzeć przed rokiem 2021.

Sposób II - żaden człowiek nie żył dłuzej niż 150 lat

1. obywatel(Markus, Pompeje)
2. urodził(Markus, 40)
3. ∀x obywatel(Markus, Pompeje) ∧ zyje(Markus, 79) -> ~zyje(Markus, 80)

Zakładając, że brak informacji o śmierci Markusa oznacza, że żył on w roku 79 - poprzedniki implikacji sa prawdziwe, czyli następnik musi być prawdziwy. Markus musiał umrzeć przed lub w roku 79.
