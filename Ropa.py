# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 11:54:18 2023

@author: USER
"""

import termcolor
from logic import *
from prueba import Prenda

prenda1 = Prenda("torso","formal","amarillo","camisa")
prenda2 = Prenda("piernas","formal","violeta","jean")

Amarillo = Symbol("amarillo")
Azul = Symbol("azul")
Rojo = Symbol("rojo")
Verde = Symbol("verde")
Naranja = Symbol("naranja")
Violeta = Symbol("violeta")
Negro = Symbol("negro")
Blanco = Symbol("blanco")

if prenda1.color == "azul":
    Azul = Symbol(prenda1.nombre + " " + prenda1.color)
    torso = [Azul]
elif prenda1.color == "amarillo":
    Amarillo = Symbol(prenda1.nombre + " " + prenda1.color)
    torso = [Amarillo]
elif prenda1.color == "rojo":
    Rojo = Symbol(prenda1.nombre + " " + prenda1.color)
    torso = [Rojo]
elif prenda1.color == "verde":
    Verde = Symbol(prenda1.nombre + " " + prenda1.color)
    torso = [Verde]
elif prenda1.color == "naranja":
    Naranja = Symbol(prenda1.nombre + " " + prenda1.color)
    torso = [Naranja]
elif prenda1.color == "violeta":
    Violeta = Symbol(prenda1.nombre + " " + prenda1.color)
    torso = [Violeta]
elif prenda1.color == "negro":
    Negro = Symbol(prenda1.nombre + " " + prenda1.color)
    torso = [Negro]
elif prenda1.color == "blanco":
    Blanco = Symbol(prenda1.nombre + " " + prenda1.color)
    torso = [Blanco]

if prenda2.color == "azul":
    Azul = Symbol(prenda2.nombre + " " + prenda2.color)
    piernas = [Azul]
elif prenda2.color == "amarillo":
    Amarillo = Symbol(prenda2.nombre + " " + prenda2.color)
    piernas = [Amarillo]
elif prenda2.color == "rojo":
    Rojo = Symbol(prenda2.nombre + " " + prenda2.color)
    piernas = [Rojo]
elif prenda2.color == "verde":
    Verde = Symbol(prenda2.nombre + " " + prenda2.color)
    piernas = [Verde]
elif prenda2.color == "naranja":
    Naranja = Symbol(prenda2.nombre + " " + prenda2.color)
    piernas = [Naranja]
elif prenda2.color == "violeta":
    Violeta = Symbol(prenda2.nombre + " " + prenda2.color)
    piernas = [Violeta]
elif prenda2.color == "negro":
    Negro = Symbol(prenda2.nombre + " " + prenda2.color)
    piernas = [Negro]
elif prenda2.color == "blanco":
    Blanco = Symbol(prenda2.nombre + " " + prenda2.color)
    piernas = [Blanco]

symbols = torso + piernas

"""torso = Symbol(prenda1.nombre)
colort = Symbol(prenda1.color)
Buso = Symbol("Buso")
Camisilla = Symbol("Camisilla")
characters = [torso, colort]

piernas = Symbol(prenda2.nombre)
colorp = Symbol(prenda2.color)
sala = Symbol("sala")
juegos = Symbol("juegos")
rooms = [estudio, pasillo, sala, juegos]

revolver = Symbol("revolver")
hacha = Symbol("hacha")
candelabro = Symbol("candelabro")
herramienta = Symbol("herramienta")
weapons = [revolver, hacha, candelabro, herramienta]

symbols = characters + rooms + weapons"""


def check_knowledge(knowledge):
    for symbol in symbols:
        if model_check(knowledge, symbol):
            termcolor.cprint(f"{symbol}: SI", "green")
            
        elif not model_check(knowledge, Not(symbol)):
            termcolor.cprint(f"{symbol}: NO", "red")
            #print(f"{symbol}: TAL VEZ")

            


# There must be a person, room, and weapon.
"""knowledge = And(
    Or(And(Plum,Not(Green),Not(Mustard),Not(Peacock)), And(Green,Not(Plum),Not(Mustard),Not(Peacock)), And(Mustard,Not(Plum),Not(Green),Not(Peacock)), And(Peacock,Not(Plum),Not(Mustard),Not(Green))),
    Or(And(estudio,Not(pasillo),Not(sala),Not(juegos)), And(pasillo,Not(estudio),Not(sala),Not(juegos)), And(sala,Not(estudio),Not(pasillo),Not(juegos)), And(juegos,Not(estudio),Not(pasillo),Not(sala))),
    Or(And(revolver,Not(hacha),Not(candelabro),Not(herramienta)), And(hacha,Not(revolver),Not(candelabro),Not(herramienta)), And(candelabro,Not(revolver),Not(hacha),Not(herramienta)), And(herramienta,Not(revolver),Not(hacha),Not(candelabro)))
)"""

knowledge = And(
    Or(And(Amarillo, Negro)),
    Or(And(Azul, Negro)),
    Or(And(Amarillo, Blanco))
)


print("Base de conocimiento: ", knowledge.formula())
print("¿Qué sé?")
check_knowledge(knowledge)

