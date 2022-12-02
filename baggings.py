bezittingen = {
     'goud' : 500,
     'buidel' : ['touw', 'vuursteen', 'zakmes'],
     'rugzak' : ['panfluit', 'dolk', 'slaapzak','appel']
 } 
#ik voeg de 12 zilver toe 
bezittingen['zilver'] = 12

#ik verwijder het zakmes uit de bundel
bezittingen['buidel'].remove('zakmes')

sorted(bezittingen['rugzak'])

print(bezittingen)



