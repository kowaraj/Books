type(socrates, human).
type(plato, human).
type(dostoevsky, nonhuman).
type(gogol, nonhuman).
live_type(human, mortal).
live_type(nonhuman, immortal).
mortal(X) :- live_type(Z, mortal), type(X, Z).
