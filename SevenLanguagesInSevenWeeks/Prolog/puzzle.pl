a(dog). a(zebra). a(cat).
d(tea). d(coffee). d(wine).
p(eng). p(esp). p(nor).


diff_a(X, Y, Z) :- a(X) \= a(Y), a(X) \= a(Z), a(Y) \= a(Z).
diff_p(X, Y, Z) :- p(X) \= p(Y), p(X) \= p(Z), p(Y) \= p(Z).

eng_owns_dog(eng, dog).
esp_owns_cat(esp, cat).

people(Owns_dog, Owns_cat, Owns_zebra) :-
    p(Owns_dog), p(Owns_cat), p(Owns_zebra),
    eng_owns_dog(Owns_dog, Dog),
    esp_owns_cat(Owns_cat, Cat),
    diff_a(Dog, Cat, zebra),
    diff_p(Owns_dog, Owns_cat, Owns_zebra).



%    diff_a(Owns_dog, Es, No).
% people(Owns_dog, End, Es_a, Es, No) :- a(En_a), a(Es_a), a(No), ad(En_a, En_d), diff_a(En_a, Es_a, No_a).
%people(En, Es, No) :- p(a(En), d(En)), p(a(Es), d(Es)), p(a(No), d(No)), diff_a(Ennn, Es, No).


