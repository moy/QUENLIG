# -*- coding: latin-1 -*-
# QUENLIG: Questionnaire en ligne (Online interactive tutorial)
# Copyright (C) 2011 Thierry EXCOFFIER, Eliane PERNA Universite Claude Bernard
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
# Contact: Thierry.EXCOFFIER@bat710.univ-lyon1.fr
#

"""
Les "dict" Python
"""

from QUENLIG.questions import *
from .check import *

add(name="cr�ation",
    required = ["table:cr�ation", "idem:chaine", "table:stocke �l�ment"],
    before = """Un dictionnaire est un tableau dont les indices sont
    presque ce que vous voulez.
    Les indices des dictionnaires sont appel�s des � clefs �.
    G�n�ralement ce sont des chaines de caract�res, mais pas seulement.
    <p>
    Le dictionnaire <tt>nombres = {"un":1, "deux": 2}</tt>
    peut-�tre cr�� de la mani�re suivante&nbsp;:<pre>
nombres = {}          # Dictionnaire vide
nombres["un"] = 1     # La valeur de la clef 'un' est 1
nombres["deux"] = 2   # La valeur de la clef 'deux' est 2</pre>
    """,
    question="""Donnez l'�criture sous la forme <tt>{clef1: valeur1, clef2: valeur2...}</tt>
    du dictionnaire dont la valeur de la clef � nom � est
    la chaine de caract�re � thierry �
    et la valeur de la clef � age � est l'entier � 21 �.
    <p>
    Les symboles '�' et '�' ne font bien s�r pas parti de votre r�ponse.
    """,

    tests = (
        Good(P(End('{"nom":"thierry","age":21}'))),
        P(expects(('nom', 'thierry', 'age', '21', ':', '{', '}', ',', '"',
                   '"nom":', '"age":', '"nom":"thierry"',
                   '"age": 21'))),
        ),

    good_answer = """Les clefs que l'on peut utiliser dans un dictionnaire
    sont&nbsp;:
    <ul>
    <li> Les entiers et flottants.
    <li> Les chaines de caract�res.
    <li> Les tuples (ce sont des tableaux non modifiables)
    <li> D'autres choses, mais c'est rarement utile.
    </ul>""",
    )

add(name="keys",
    required = ["cr�ation", "control:for"],
    before = """La boucle <tt>for</tt> de Python parcourt les �l�ments
    d'un ensemble.
    Quand on parcourt un dictionnaire on obtient chacune des clefs
    du dictionnaire.""",
    question = """Quelle boucle d'indice <tt>key</tt> �crivez-vous pour
    afficher les clefs du dictionnaire appel� <tt>dico</tt> les unes
    apr�s les autres&nbsp;?""",
    nr_lines = 3,
    tests = (
        Good(P_AST(Equal('''
for key in dico:
    print(key)
'''))),
        P(expects(('for', 'key', 'in', 'dico', ':', 'print', '(', ')',
                   'print(key)'))),
        ),
    good_answer = """ATTENTION : l'ordre de parcours des clefs du dictionnaire
    n'est pas forc�ment celui dans lequel vous avez mis les �l�ments dans le
    dictionnaire.
    <p>
    ATTENTION : Il ne faut pas changer le dictionnaire pendant qu'on
    le parcourt, sinon le r�sultat est impr�dictible.""",
    )

add(name="values",
    required = ["keys"],
    before = """Si <tt>d</tt> est un dictionnaire.
    Alors <tt>d.keys()</tt> est un tableau contenant toutes
    les clefs et <tt>d.values()</tt> est un tableau contenant
    toutes les valeurs.""",
    question = """Quelle boucle d'indice <tt>value</tt> �crivez-vous pour
    afficher les valeurs contenues dans le dictionnaire
    appel� <tt>dico</tt> les unes apr�s les autres&nbsp;?""",
    nr_lines = 3,
    tests = (
        Good(P_AST(Equal('''
for value in dico.values():
    print(value)
'''))),
        P(expects(('for', 'value', 'in', 'dico', ':', 'print', '(', ')',
                 'values', 'values()', '.values()', 'dico.values()'))),
        ),
    good_answer = """Quand on fait cette boucle, il n'y a aucun moyen
    facile pour trouver la/les clefs qui ont permis d'obtenir la valeur.""",
    )

