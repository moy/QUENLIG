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
Les "list" Python
"""

from questions import *
from check import *

add(name="cr�ation",
    required = ["idem:affectation", "idem:chaine", "idem:flottant"],
    before = """Un tableau Python est d�fini par une liste de valeurs
    entre crochets. Voici quelques exemples&nbsp;:
    <ul>
    <li> Un tableau vide : <tt>[]</tt>
    <li> Un tableau contenant un entier : <tt>[5]</tt>
    <li> Un tableau des chaines de caract�res : <tt>["oui", "non"]</tt>
    <li> Un tableau contenant des tableaux :
    <tt>[["zero", "zero"], ["one", "un"], ["two", "deux"]]</tt>
    </ul>
    """,
    question="""Contrairement au langage C, les tableaux Python
    peuvent contenir des choses de natures diff�rentes.
    <p>
    Affectez dans la variable <tt>r</tt> un tableau contenant
    l'entier <tt>5</tt>, la chaine de caract�res <tt>toto</tt>
    et le nombre flottant <tt>1 virgule 2</tt>.
    """,

    tests = (
        Good(P(Equal('r = [5,"toto",1.2]'))),
        Expect('r'),
        Expect('='),
        Expect('5'),
        Expect('1.2'),
        Expect('"toto"'),
        Expect('['),
        Expect(']'),
        ),

    good_answer = """N'ayez pas peur, il y a des moyens simples pour
    cr�er de grand tableaux vides sans avoir � tout �crire&nbsp;!""",
    )

add(name="acc�s",
    required = ["cr�ation", "idem:affectation"],
    before = """Comme en langage C, on d�signe un �l�ment d'un tableau
    en ajoutant <tt>[la position]</tt> apr�s le tableau.
    <p>
    Comme en langage C, la position du premier �lement est <tt>0</tt>
    """,
    question = """La variable <tt>t</tt> contient un tableau,
    comment stockez vous dans la variable <tt>i5</tt> le cinqui�me
    �lement du tableau <tt>t</tt>&nbsp;?""",
    tests = (
        Good(P(Equal('i5 = t[4]'))),
        Bad(Comment(P(Equal('i5 = t[5]')),
                    """ATTENTION : la position du premier �lement est
                    <tt>0</tt>. Vous avez donc pris le sixi�me �lement
                    du tableau <tt>t</tt>""")),
        Expect('i5'),
        Expect('t'),
        Expect('['),
        Expect(']'),
        Expect('='),
        ),   
    good_answer = """Contrairement au langage C, si vous essayez de lire un
    �lements en dehors du tableau, il y a une erreur.""",
    )

add(name="stocke �l�ment",
    required = ["acc�s"],
    question = """Comment stocker la valeur <tt>10</tt> dans le centi�me
    �l�ment du tableau <tt>x</tt>&nbsp;?""",
    tests = (
        Good(P(Equal('x[99] = 10'))),
        Bad(Comment(P(Equal('x[100] = 10')),
                    """ATTENTION : la position du premier �lement est
                    <tt>0</tt>. Vous avez donc indiqu�
                    le 101<sup>�me</sup> �l�ment.""")),
        Expect('99'),
        Expect('10'),
        Expect('['),
        Expect(']'),
        Expect('='),
        Expect('x'),
        ),
    good_answer = """Contrairement au langage C, si vous essayez d'�crire
    dans un �lement en dehors du tableau, il y a une erreur.""",
    )

add(name="range",
    required = ["cr�ation"],
    before = """La fonction <tt>range</tt> permet de cr�er des tableaux
    contenant des entiers successifs.""",
    question = """Tapez <tt>range(10)</tt> dans votre interpr�teur Python.
    <p>
    Quel est le dernier nombre affich� dans le tableau&nbsp;?
    """,
    tests = (
        Good(Int(9)),
        ),
    good_answer = """<tt>range</tt> permet aussi de g�n�rer un tableau
    contenant les entiers entre 2 bornes : <tt>range(100, 200)</tt>""",
    )

add(name="len",
    required = ["cr�ation"],
    question = "Qu'affiche la commande Python : <tt>len([6, 7, 8, 9])</tt>",
    tests = (
        Good(Int(4)),
        ),
    good_answer = "Bien entendu, <tt>len(range(1000))</tt> affiche 1000",
    )

add(name="sum",
    required = ["cr�ation"],
    question = "Qu'affiche la commande Python : <tt>sum([2000, 11, -1])</tt>",
    tests = (
        Good(Int(2010)),
        ),
    good_answer = """Bien entendu, <tt>sum(range(4))</tt> affiche 6.
    <p>
    Et <tt>sum([])</tt> donne <tt>0</tt>.
    """,
    )

add(name="concat�nation",
    required = ["cr�ation", "range"],
    before = """On peut concat�ner des tables en utilisant
    l'op�rateur <tt>+</tt>, les tables utilis�es ne sont pas modifi�es,
    une nouvelle table est cr��e.<p>
    <tt>[1, 2] + ["x", "y"]</tt> donne <tt>[1, 2, "x", "y"]</tt>
    """,
    question = """Proposez une commande qui cr�e la table&nbsp;:<br>
    <tt>[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]</tt>""",
    tests = (
        Good(P(Equal('range(10)+range(10)'))),
        Good(P(Equal('range(10)*2')|Equal('2*range(10)'))),
        Reject('3', """Vous devez utilisez <tt>range</tt> pour cr�er la table
        des entiers de 0 � 9"""),
        P(expects(('range', '+', 'range(10)'))),
        ),
    good_answer = "� votre avis, que donne <tt>[5] + [] + [6]</tt>&nbsp;?",
    )

add(name="affectation",
    required = ["cr�ation", "sum"],
    before = """Contrairement au langage C, l'affectation n'est pas une recopie
    mais un nommage.
    Vous pouvez donc donner plusieurs noms � la m�me chose.""",
    question = "Que va afficher le programme suivant&nbsp;?" + python_html(
        """a = [1, 2]
b = a
b[0] = 3
print(sum(a) + sum(b))"""),
    tests = (
        Int(10),
        ),
    good_answer = """Cela donne ce r�sultat car la variable <tt>a</tt>
    et <tt>b</tt> repr�sentent le m�me tableau.
    Si vous modifiez le tableau cela modifie les deux variables.
    <p>
    Vous n'avez pas ce probl�me avec les nombres et les chaines de caract�res
    car <b>on ne peut pas les modifier</b> une fois qu'ils ont �t� utilis�s.
    On appelle cela des <em>immutables</em>.
    """,
    )

add(name="matrice",
    required = ["cr�ation", "stocke �l�ment"],
    before = """Une table peut contenir des tables :
    <tt>matrice = [ [1,2], [3,4] ]</tt>
    <p>
    Pour identifier une case de la matrice on va d'abord indiquer
    un �lement du premier tableau (c'est �l�ment est un tableau)
    et un �lement de cet �l�ment.
    <p>
    <tt>matrice[0][1]</tt> donne <tt>2</tt>
    """,
    question = """Que tapez-vous pour remplacer dans la matrice donn�e
    en exemple le <tt>3</tt> par <tt>5</tt>&nbsp;?""",
    tests = (
        Good(P(Equal('matrice[1][0] = 5'))),
        P(expects(('matrice', '[', ']', '5', '=',
                   'matrice[1]', 'matrice[1][0]'))),
        ),
    good_answer = """On peut bien s�r faire des matrices de matrices&nbsp;!""",
    )

add(name="multiplication",
    required = ["concat�nation", "idem:multiplication", "matrice"],
    before = "<tt>3 * [5, 7]</tt> donne <tt>[5, 7, 5, 7, 5, 7]</tt>",
    question = "Cr�ez une table contenant 1000 z�ros (l'entier 0)&nbsp;?",
    tests = (
        Good(P(Equal("1000*[0]") | Equal('[0]*1000'))),
        P(expects(('1000', '*', '[', ']', '[0]'))),
        ),
    good_answer = """ATTENTION au pi�ge : le contenu de la tableau
    n'est pas recopi�, les �l�ments sont tous les m�mes.
    <p>
    Regardez bien le programme suivant&nbsp;:""" + python_html(
        """
        t = [[1,2]] * 3
        print(t)             # Cela affiche [[1, 2], [1, 2], [1, 2]]
        t[0][0] = 5
        print(t)             # Cela affiche [[5, 2], [5, 2], [5, 2]]
        """),
    )
        
    
    
    
    
    
    
