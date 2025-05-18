Object subclass: #Carta
	instanceVariableNames: 'palo figura'
	classVariableNames: ''
	package: 'clase-SimulacroParcial'!

!Carta methodsFor: 'metodos de negocio' stamp: 'Nicosabena 4/15/2025 20:08'!
valor
	^self subclassResponsibility.! !


!Carta methodsFor: 'initialization' stamp: 'Nicosabena 4/15/2025 10:06'!
initialize 
	"Inicializa los valores de los atributos de la Clase"
	
	figura := 'vacio'.
	palo := 'vacio'.! !


!Carta methodsFor: 'converting' stamp: 'Nicosabena 4/15/2025 10:15'!
asString 
	
	"Retorna una cadena con la informacion del objeto"
	"asString tranforma al elemento en una cadena"
	|salida|
	
	salida := 'Palo: ', palo, ' Figura: ', figura.
	
	^salida.! !


!Carta methodsFor: 'accessing' stamp: 'Nicosabena 4/15/2025 10:03'!
figura
	^ figura! !

!Carta methodsFor: 'accessing' stamp: 'Nicosabena 4/15/2025 10:03'!
figura: anObject
	figura := anObject! !

!Carta methodsFor: 'accessing' stamp: 'Nicosabena 4/15/2025 10:03'!
palo: anObject
	palo := anObject! !

!Carta methodsFor: 'accessing' stamp: 'Nicosabena 4/15/2025 10:03'!
palo
	^ palo! !


Carta subclass: #CartaLetra
	instanceVariableNames: 'letra'
	classVariableNames: ''
	package: 'clase-SimulacroParcial'!

!CartaLetra methodsFor: 'metodos de negocio' stamp: 'Nicosabena 4/15/2025 20:55'!
valor
	|v|
	((letra = 'A') or: (letra = 'J'))ifTrue:[v := 65.]
	ifFalse:[v:= 74.].
	^v.! !


!CartaLetra methodsFor: 'accessing' stamp: 'Nicosabena 4/15/2025 20:50'!
letra: anObject
	letra := anObject! !

!CartaLetra methodsFor: 'accessing' stamp: 'Nicosabena 4/15/2025 10:19'!
letra
	^ letra! !


!CartaLetra methodsFor: 'initialization' stamp: 'Nicosabena 4/15/2025 10:20'!
initialize 
	super initialize.
	
	letra := 'n/a'.
	
! !


!CartaLetra methodsFor: 'converting' stamp: 'Nicosabena 4/15/2025 10:34'!
asString

	|salida|
	
	salida := super asString, ' Letra: ', letra.
	
	^salida.! !


Carta subclass: #CartaNumerica
	instanceVariableNames: 'numero'
	classVariableNames: ''
	package: 'clase-SimulacroParcial'!

!CartaNumerica methodsFor: 'metodos de negocio' stamp: 'Nicosabena 4/15/2025 20:10'!
valor
	^numero * 10.! !


!CartaNumerica methodsFor: 'accessing' stamp: 'Nicosabena 4/15/2025 10:17'!
numero
	^ numero! !

!CartaNumerica methodsFor: 'accessing' stamp: 'Nicosabena 4/15/2025 19:46'!
numero: anObject
	
	(anObject isNumber)
	ifTrue:[
		(anObject between: 2 and: 10)
		ifTrue:[
			numero := anObject.
				].
			] ! !


!CartaNumerica methodsFor: 'initialization' stamp: 'Nicosabena 4/15/2025 19:43'!
initialize 
	
	super initialize.
	numero := 'Nula'.! !


!CartaNumerica methodsFor: 'converting' stamp: 'Nicosabena 4/15/2025 20:13'!
asString 

	|salida|
	salida := super asString, ' Numero: ', numero asString.
	
^salida.! !


Object subclass: #Partida
	instanceVariableNames: 'numero cartas'
	classVariableNames: ''
	package: 'clase-SimulacroParcial'!

!Partida methodsFor: 'adding' stamp: 'Nicosabena 4/17/2025 19:01'!
addCarta: unaCarta

cartas add: unaCarta.! !


!Partida methodsFor: 'initialization' stamp: 'Nicosabena 4/17/2025 11:37'!
asString 

	|salida|
	
	salida:= 'La partida es la numero: ', numero asString, self mostrarCartas.
	
	^salida.! !

!Partida methodsFor: 'initialization' stamp: 'Nicosabena 4/17/2025 11:23'!
initialize

	numero := 0.
	cartas := OrderedCollection new.! !


!Partida methodsFor: 'as yet unclassified' stamp: 'Nicosabena 4/17/2025 19:23'!
listarCartasPalo: unPalo

	|cartasDelPalo cartasDelPaloPares s|
	cartasDelPalo := cartas select: [ :c| (c palo) = unPalo.].
	cartasDelPaloPares := cartasDelPalo select: [:c| (c valor) even. ].
	s := ''.
	cartasDelPaloPares do: [:c | s := s,  String cr, String tab, c asString, ' Valor: ', c valor asString.].
	^s.! !

!Partida methodsFor: 'as yet unclassified' stamp: 'Nicosabena 4/17/2025 19:40'!
existe_cartas_Picas
    | carta |
    carta := cartas detect: [:c | ((c palo) = 'Pica') and: ((c valor) >= 100)]ifNone:[^false.].
    carta ifNil: [^false.] ifNotNil: [^true.].
! !


!Partida methodsFor: 'metodos de negocio' stamp: 'Nicosabena 4/17/2025 18:59'!
mostrarCartas

	|salida|
	salida := ''. "Se inicializa"
	cartas do: [:c | salida := salida, String tab, c asString, String cr.].
	
	^salida.! !


!Partida methodsFor: 'accessing' stamp: 'Nicosabena 4/17/2025 11:22'!
cartas: anObject
	cartas := anObject! !

!Partida methodsFor: 'accessing' stamp: 'Nicosabena 4/17/2025 11:22'!
numero
	^ numero! !

!Partida methodsFor: 'accessing' stamp: 'Nicosabena 4/17/2025 11:22'!
numero: anObject
	numero := anObject! !

!Partida methodsFor: 'accessing' stamp: 'Nicosabena 4/17/2025 11:22'!
cartas
	^ cartas! !

