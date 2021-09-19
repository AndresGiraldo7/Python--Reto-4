import pandas as pd
positivos_C19 = {
    'Colombia ':{
        'Risaralda ': [( 'Pereira ', 45) , (' Dosquebradas ', 15) , ('La Virginia ', 30) ],
'Quindio ': [( 'Armenia ', 75) , ('Montenegro ', 86) ]
},
'Mexico ': {
    'Quintana Roo ': [( 'Benito Juarez ', 101) , (' Solidaridad ',56) ],
'Nayarit ': [( 'Compostela ', 23) , ('San Blas ', 35) , ('Xalisco ', 74) , ('Del Nayar ', 46) ]}
}
    


def analizaPacientes ( opt :int , db:dict , pais :str=''):
    for positivos_C19 in db:
       
     if opt==2:
            db = ('Consulta de la localidad con más pacientes enfermos para un país')
        #max_item= max(positivos_C19, key=int)
        #pt = max_item 
    return  max(positivos_C19 , db)
        #{f'opt': opt, db: db, pais:pais}
    '''if opt == 0:
        db = ('Consulta del promedio de pacientes para todos los países')
        for key in db:
            opt= sum(db[key])/len(db[key])
    if opt == 1:
        db = ('Consulta del promedio de pacientes enfermos para todos los estados de un país')
        for value in db:
            opt= sum(db[value])/len(db[value])'''
                

print ( analizaPacientes (2, positivos_C19 , 'Mexico '))