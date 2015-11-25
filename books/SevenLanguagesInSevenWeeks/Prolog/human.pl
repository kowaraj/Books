human_type(socrat, human).
human_type(dostoevsky, nonhuman).
live_type(human, mortal).
mortal(X) :- true(X, human).
