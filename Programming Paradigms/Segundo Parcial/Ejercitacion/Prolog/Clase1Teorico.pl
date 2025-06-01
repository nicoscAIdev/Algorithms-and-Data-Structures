alumno(jose).
aprobo_primer_parcial(jose).
aprobo_segundo_parcial(jose).
alumno_regular(X) :- alumno(X), aprobo_primer_parcial(X), aprobo_segundo_parcial(X).
