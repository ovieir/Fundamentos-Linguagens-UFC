% Fatos: pai(nome_pai, filho)
pai(joao, ana).
pai(joao, pedro).
pai(carlos, marcos).
pai(carlos, julia).
pai(pedro, lucas).
pai(marcos, helena).

% Fatos: mae(nome_mae, filho)
mae(maria, ana).
mae(maria, pedro).
mae(helena, lucas).
mae(sandra, marcos).
mae(sandra, julia).
mae(julia, helena).

% Regras
irmao(X, Y) :- 
    pai(P, X), pai(P, Y), 
    mae(M, X), mae(M, Y), 
    X \= Y.

primo(X, Y) :- 
    pai(P1, X), pai(P2, Y), 
    irmao(P1, P2),
    X \= Y.

avo(X, Y) :- 
    pai(X, P), pai(P, Y).
avo(X, Y) :- 
    mae(X, P), pai(P, Y).

avoh(X, Y) :- 
    pai(X, P), mae(P, Y).
avoh(X, Y) :- 
    mae(X, P), mae(P, Y).
