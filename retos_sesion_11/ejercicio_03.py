
especies = dict((
    ('canino', '🐶'),
    ('felino', '🐱'),
    ('aves', ['🐦', '🦅'])
))

# Eliminar aves
aves = especies.pop('aves')

# Modificar el valor de la clave 'felino' por '🐈'
especies['felino'] = '🐈'

# Cambiar la clave 'canino' por 'caninos' y su valor por ['🐶','🐕']
valor_canino = especies.pop('canino')
especies['caninos'] = ['🐶', '🐕']

print("Diccionario actualizado:")
print(especies)
