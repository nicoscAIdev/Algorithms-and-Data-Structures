Object subclass: #CasetaPeaje25
	instanceVariableNames: 'col'
	classVariableNames: ''
	package: 'Parcial22_MiVersion'!

!CasetaPeaje25 methodsFor: 'adding' stamp: 'Nicosabena 4/22/2025 21:55'!
add: unVehiculo
	
	(unVehiculo cantEjes >= 2)ifTrue:[col add: unVehiculo. ^true.]
													ifFalse:[^false].													
																									
	! !


!CasetaPeaje25 methodsFor: 'accessing' stamp: 'Nicosabena 4/21/2025 18:16'!
col: anObject
	col := anObject! !

!CasetaPeaje25 methodsFor: 'accessing' stamp: 'Nicosabena 4/21/2025 18:50'!
col
	^ col size.! !


!CasetaPeaje25 methodsFor: 'as yet unclassified' stamp: 'Nicosabena 4/22/2025 21:56'!
listadoVehiculosSuv
	^ (col select: [:vehiculo | 
			(vehiculo isKindOf: Familiar) and: [vehiculo esSuv]])
		asSortedCollection: [:a :b | a patente < b patente].

	
	! !


!CasetaPeaje25 methodsFor: 'initialization' stamp: 'Nicosabena 4/22/2025 19:49'!
initialize 

	col := OrderedCollection new.
! !


Object subclass: #Vehiculo25
	instanceVariableNames: 'patente cantEjes precioBase telePase'
	classVariableNames: ''
	package: 'Parcial22_MiVersion'!

!Vehiculo25 methodsFor: 'converting' stamp: 'Nicosabena 4/21/2025 19:32'!
asString

	|s|
	
	s:= patente asString, ' ', cantEjes asString, ' ', precioBase asString, ' ',  telePase asString.
	
	^s.! !


!Vehiculo25 methodsFor: 'as yet unclassified' stamp: 'Nicosabena 4/21/2025 18:51'!
precioAPagar
self subclassResponsibility.! !


!Vehiculo25 methodsFor: 'accessing' stamp: 'Nicosabena 4/21/2025 18:17'!
precioBase
	^ precioBase! !

!Vehiculo25 methodsFor: 'accessing' stamp: 'Nicosabena 4/21/2025 18:17'!
cantEjes: anObject
	cantEjes := anObject! !

!Vehiculo25 methodsFor: 'accessing' stamp: 'Nicosabena 4/21/2025 18:17'!
patente: anObject
	patente := anObject! !

!Vehiculo25 methodsFor: 'accessing' stamp: 'Nicosabena 4/21/2025 18:17'!
patente
	^ patente! !

!Vehiculo25 methodsFor: 'accessing' stamp: 'Nicosabena 4/21/2025 18:17'!
telePase
	^ telePase! !

!Vehiculo25 methodsFor: 'accessing' stamp: 'Nicosabena 4/21/2025 18:17'!
telePase: anObject
	telePase := anObject! !

!Vehiculo25 methodsFor: 'accessing' stamp: 'Nicosabena 4/21/2025 18:17'!
precioBase: anObject
	precioBase := anObject! !

!Vehiculo25 methodsFor: 'accessing' stamp: 'Nicosabena 4/21/2025 18:17'!
cantEjes
	^ cantEjes! !


!Vehiculo25 methodsFor: 'initialization' stamp: 'Nicosabena 4/21/2025 18:04'!
initialize

	patente:= 'AA000'.
	cantEjes := 0.
	precioBase := 0.
	telePase := false.! !


Vehiculo25 subclass: #Carga
	instanceVariableNames: 'cargaMaxima'
	classVariableNames: ''
	package: 'Parcial22_MiVersion'!

!Carga methodsFor: 'accessing' stamp: 'Nicosabena 4/21/2025 18:17'!
cargaMaxima: anObject
	cargaMaxima := anObject! !

!Carga methodsFor: 'accessing' stamp: 'Nicosabena 4/21/2025 18:17'!
cargaMaxima
	^ cargaMaxima! !


!Carga methodsFor: 'initialization' stamp: 'Nicosabena 4/21/2025 18:06'!
initialize 
super initialize.

	cargaMaxima := 0.! !


!Carga methodsFor: 'as yet unclassified' stamp: 'Nicosabena 4/21/2025 19:40'!
precioAPagar 

	|precioTotal|

	precioTotal := cantEjes * precioBase.
	(cantEjes * precioBase > 5000) ifTrue: [ precioTotal := precioBase * 1.15 ].
	telePase ifTrue: [ precioTotal := precioTotal * 0.95 asFloat ].
	^precioTotal.

! !


!Carga methodsFor: 'converting' stamp: 'Nicosabena 4/21/2025 19:41'!
asString 

	|s|
	
	s := super asString, cargaMaxima asString, ' ', self precioAPagar asString.
	
	^s.! !


Vehiculo25 subclass: #Familiar
	instanceVariableNames: 'esSuv'
	classVariableNames: ''
	package: 'Parcial22_MiVersion'!

!Familiar methodsFor: 'converting' stamp: 'Nicosabena 4/21/2025 19:33'!
asString 

	|s|
	
	s := super asString, ' ', esSuv asString , ' ', self precioAPagar asString.
	
	^s.! !


!Familiar methodsFor: 'as yet unclassified' stamp: 'Nicosabena 4/21/2025 19:17'!
precioAPagar

	|precioTotal|

	precioTotal := esSuv ifTrue:[telePase ifFalse:[precioBase * 1.20.]
														ifTrue:[precioBase ]]
								ifFalse:[precioBase].
								
	^precioTotal.! !


!Familiar methodsFor: 'accessing' stamp: 'Nicosabena 4/21/2025 18:17'!
esSuv
	^ esSuv! !

!Familiar methodsFor: 'accessing' stamp: 'Nicosabena 4/21/2025 18:17'!
esSuv: anObject
	esSuv := anObject! !


!Familiar methodsFor: 'initialization' stamp: 'Nicosabena 4/21/2025 18:07'!
initialize 
super initialize.

	esSuv := false.
	
! !
