Object subclass: #MotorAcceso25
	instanceVariableNames: 'politicas'
	classVariableNames: ''
	package: 'TP1-2025'!

!MotorAcceso25 methodsFor: 'initialization' stamp: 'Nicosabena 4/18/2025 18:33'!
initialize 

	politicas := OrderedCollection new.
! !


!MotorAcceso25 methodsFor: 'accessing' stamp: 'Nicosabena 4/18/2025 18:32'!
politicas
	^ politicas! !

!MotorAcceso25 methodsFor: 'accessing' stamp: 'Nicosabena 4/18/2025 18:32'!
politicas: anObject
	politicas := anObject! !


!MotorAcceso25 methodsFor: 'converting' stamp: 'Nicosabena 4/18/2025 18:35'!
asString 

	|salida|
	 ! !


Object subclass: #Politica25
	instanceVariableNames: 'codigo descripcion habilitada'
	classVariableNames: ''
	package: 'TP1-2025'!

!Politica25 methodsFor: 'initialization' stamp: 'Nicosabena 4/18/2025 18:44'!
initialize

	codigo := 0.
	descripcion := ''.
	habilitada := false.
	
! !


!Politica25 methodsFor: 'accessing' stamp: 'Nicosabena 4/18/2025 18:32'!
descripcion: anObject
	descripcion := anObject! !

!Politica25 methodsFor: 'accessing' stamp: 'Nicosabena 4/18/2025 18:32'!
codigo
	^ codigo! !

!Politica25 methodsFor: 'accessing' stamp: 'Nicosabena 4/18/2025 18:32'!
descripcion
	^ descripcion! !

!Politica25 methodsFor: 'accessing' stamp: 'Nicosabena 4/18/2025 18:32'!
codigo: anObject
	codigo := anObject! !

!Politica25 methodsFor: 'accessing' stamp: 'Nicosabena 4/18/2025 18:32'!
habilitada
	^ habilitada! !

!Politica25 methodsFor: 'accessing' stamp: 'Nicosabena 4/18/2025 18:32'!
habilitada: anObject
	habilitada := anObject! !


Politica25 subclass: #Aplicacion25
	instanceVariableNames: 'nivelPrivilegios'
	classVariableNames: ''
	package: 'TP1-2025'!

!Aplicacion25 methodsFor: 'accessing' stamp: 'Nicosabena 4/18/2025 18:32'!
nivelPrivilegios
	^ nivelPrivilegios! !

!Aplicacion25 methodsFor: 'accessing' stamp: 'Nicosabena 4/18/2025 18:57'!
nivelPrivilegios: anObject
	
	  (1 >= anObject <= 10) ifTrue:[ nivelPrivilegios := anObject]
									ifFalse:[^false].
									
								! !


!Aplicacion25 methodsFor: 'initialization' stamp: 'Nicosabena 4/18/2025 18:56'!
initialize 
super initialize.

	nivelPrivilegios := 0.! !


Politica25 subclass: #Networking25
	instanceVariableNames: 'ipDesde ipHasta'
	classVariableNames: ''
	package: 'TP1-2025'!

!Networking25 methodsFor: 'accessing' stamp: 'Nicosabena 4/18/2025 18:32'!
ipDesde: anObject
	ipDesde := anObject! !

!Networking25 methodsFor: 'accessing' stamp: 'Nicosabena 4/18/2025 18:32'!
ipHasta: anObject
	ipHasta := anObject! !

!Networking25 methodsFor: 'accessing' stamp: 'Nicosabena 4/18/2025 18:32'!
ipHasta
	^ ipHasta! !

!Networking25 methodsFor: 'accessing' stamp: 'Nicosabena 4/18/2025 18:32'!
ipDesde
	^ ipDesde! !


Object subclass: #Usuario25
	instanceVariableNames: 'email clave direccionIP nivelPrivilegios'
	classVariableNames: ''
	package: 'TP1-2025'!

!Usuario25 methodsFor: 'accessing' stamp: 'Nicosabena 4/18/2025 18:32'!
clave: anObject
	clave := anObject! !

!Usuario25 methodsFor: 'accessing' stamp: 'Nicosabena 4/18/2025 18:32'!
email: anObject
	email := anObject! !

!Usuario25 methodsFor: 'accessing' stamp: 'Nicosabena 4/18/2025 18:32'!
direccionIP
	^ direccionIP! !

!Usuario25 methodsFor: 'accessing' stamp: 'Nicosabena 4/18/2025 18:32'!
nivelPrivilegios
	^ nivelPrivilegios! !

!Usuario25 methodsFor: 'accessing' stamp: 'Nicosabena 4/18/2025 18:32'!
direccionIP: anObject
	direccionIP := anObject! !

!Usuario25 methodsFor: 'accessing' stamp: 'Nicosabena 4/18/2025 18:32'!
clave
	^ clave! !

!Usuario25 methodsFor: 'accessing' stamp: 'Nicosabena 4/18/2025 18:32'!
email
	^ email! !

!Usuario25 methodsFor: 'accessing' stamp: 'Nicosabena 4/18/2025 18:32'!
nivelPrivilegios: anObject
	nivelPrivilegios := anObject! !
