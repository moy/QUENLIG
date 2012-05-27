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
Les objets
"""

from questions import *
from check import *

add(name="cr�er classe",
    required = ["control:def", "idem:flottant", "idem:chaine",
                "module:cr�er"],
    before = """Il n'y a pas de structure comme en langage C en Python.
    N�anmoins, on peut d�finir des <em>classes</em> et les utiliser
    comme des structures&nbsp;:""" + python_html("""
    class Individu:
         nom = "Nom inconnu"
         prenom = "Pr�nom inconnu"
         age = 0""") + """<p>
    On ne d�finit pas le type des champs comme en langage C,
    mais seulement leur valeur par d�faut.
    <p>
    Si vous saisissez cette d�finition directement dans Python
    (sans la mettre dans un fichier).
    Il faut terminer la d�finition de la structure par une ligne vide.
    """,
    question="""Donnez la d�finition d'un structure nomm�e
    <tt>Complexe</tt> qui contient deux champs <tt>reel</tt>
    et <tt>imaginaire</tt> initialis� � 0&nbsp;?""",
    nr_lines = 3,
    tests = (
        Good(P_AST( Equal('class Complexe:\n reel=0\n imaginaire=0')
                   |Equal('class Complexe:\n imaginaire=0\n reel=0')
                   |Equal('class Complexe:\n imaginaire=0.\n reel=0.')
                   |Equal('class Complexe:\n reel=0.\n imaginaire=0.')
                   )),
        P(expects(('class', 'Complexe', 'reel', 'imaginaire', '0', '=', ':',
                   'class Complexe', 'reel=0', 'imaginaire=0'))),
        ),
    good_answer = """La valeur par d�faut peut �tre le r�sultat d'un calcul.
    Par exemple <tt>1024 * a</tt>""",
    )

add(name="cr�er instance",
    required=["cr�er classe", "table:cr�ation"],
    before = """Le nom de la classe est en fait une fonction qui
    retourne un nouvel �l�ment de la classe.
    Quand vous voulez une nouvelle instance, il vous suffit d'appeler
    cette fonction.""",
    question = """Cr�ez un nouveau <tt>Complexe</tt>
    que vous nommerez <tt>a</tt>""",
    tests = (
    Good(P(Equal('a=Complexe()'))),
    expects(('Complexe', 'a', '=')),
    P(Expect('()', """La fonction <tt>Complexe</tt> est appel�e sans param�tres
             donc tout simplement <tt>Complexe()</tt>""", canonize=False)),
             ),
    good_answer = """Si vous �crivez <tt>a = [ Complexe(), Complexe() ]</tt>
    alors <tt>a</tt> est un tableau contenant deux complexes diff�rents
    mais tous les deux �gaux � z�ro.
    Dans le futur les valeurs de ces complexes pourront changer.
    <p>
    Si vous �crivez :""" + python_html(
    """
        b = Complexe()
        a = [b, b]""") + """
    <p>Alors <tt>a</tt> est un tableau contenant deux fois le m�me complexe.
    Si la valeur de <tt>b</tt> change alors les deux �l�ments
    de <tt>a</tt> changent.""",
    )

add(name="attributs",
    required = ["cr�er instance", "module:math"],
    before = """Pour acc�der ou modifier les valeurs des attributs
    d'une instance, on utilise le caract�re '<tt>.</tt>' comme
    en langage C.""" + python_html(
    """
    a = Complexe()
    print("(",a.reel, ",", a.imaginaire, ")")""") + """
    Cet exemple va afficher <tt>( 0 , 0 )</tt>    
    """,
    question = """Si la variable <tt>a</tt> est un <tt>Complexe</tt>,
    que faites-vous pour stocker le complexe <em>3+4i</em> dedans&nbsp;?""",
    nr_lines = 3,
    tests = (
    Good(Replace((('3.','3'),('4.','4')),
                 P(Equal('a.reel=3\na.imaginaire=4')
                  |Equal('a.imaginaire=4\na.reel=3')))),
    expects(('a', 'reel', 'imaginaire', '3', '4', '=', '.', 'a.',
            'a.reel', 'a.imaginaire')),
    Reject('4i',"Vous devez stocker un nombre r�el dans la partie imaginaire"),
    Expect('\n', 'La r�ponse est en deux lignes'),
    
    Comment("""Vous devez mettre 3 dans l'attribut r�el de <tt>a</tt>
            et 4 dans son attribut imaginaire"""),
            ),
    good_answer = """Comme en langage C, si vous tapez <tt>b = a.truc</tt>
    un message d'erreur va vous dire que <tt>a</tt> ne contient pas d'attribut
    <tt>truc</tt>.
    <p>
    Mais ATTENTION, si vous tapez <tt>a.truc = 5</tt> cela va cr�er un
    attribut <tt>truc</tt> dans l'objet que <tt>a</tt> d�signe,
    sans vous pr�venir."""
    )

# XXX A finir ?
# add(name="instance param�tr�e",
#     required = ["cr�er classe", "attributs"],
#     before = """On peut cr�er facilement une instance directement
#     avec les bonnes valeurs.
#     Pour cela on d�finit une fonction d'initialisation de l'instance.
#     Cette fonction d'initialisation est un attribut de la classe,
#     son nom est <tt>__init__</tt>.
#     """,
#     )
# 
    

