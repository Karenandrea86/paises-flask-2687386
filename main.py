from flask import Flask, render_template

"""comentario"""
app = Flask(__name__)

@app.route("/hola")
def hola():
    return "Hola"

@app.route('/paises')
def paises():
    '''Diccionario'''
    continentes = [
        {
            "nombre" : "America",
            "paises" : [
                {"nombre" : "Colombia",
                 "capital" : "Bogota",
                 "moneda" : "peso",
                 "poblacion" : 60,
                 "superficie" : 1700000
                 },
                {
                    "nombre" : "Peru",
                    "capital" : "Lima",
                    "moneda" : "Sol",
                    "poblacion" : 32,
                    "superficie" : 1800000
                    }
                ]
            },
        {
            "nombre" : "Europa",
            "paises" : [
                
                {"nombre" : "Francia",
                 "capital" : "Paris",
                 "moneda" : "Euro",
                 "poblacion" : 87,
                 "superficie" : 1600000
                },
                {
                    "nombre" : "Reino Unido",
                    "capital" : "Londres",
                    "moneda" : "Libra",
                    "poblacion" : 58,
                    "superficie" : 1900000
                }
                ]
            },
        {
            "nombre" : "Asia",
            "paises" : [
                {"nombre" : "Japon",
                 "capital" : "Tokio",
                 "moneda" : "yen",
                 "poblacion" : 55,
                 "superficie" : 1500000
                 },
                {
                    "nombre" : "China",
                    "capital" : "Pekin",
                    "moneda" : "Sol",
                    "poblacion" : 84,
                    "superficie" : 1400000
                    }
                ]
            }
        ]
    '''variables de conteo para cada continente'''
    contador_paises_america = 0
    for pais in paises [0][0]["paises"]:
        contador_paises_america = contador_paises_america + 1
        print(contador_paises_america)
        
    contador_paises_europa = 0
    for pais in paises [1][0]["paises"]:
        contador_paises_europa = contador_paises_europa + 1
        print(contador_paises_europa)
    
    contador_paises_asia = 0
    for pais in paises [2][0]["paises"]:
        contador_paises_asia = contador_paises_asia + 1
        print(contador_paises_asia)
    
    
    user = 'Daniela Caro y Karen Velasquez'
    return render_template('paises_listas.html',
                           user = user,
                           continentes  = paises,
                           asia = contador_paises_asia,
                           america = contador_paises_america,
                           europa = contador_paises_europa)