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
Les structures de contr�le Python
"""

from questions import *
from check import *

add(name="for",
    required = ["table:range", "idem:flottant", "io:print"],
    before = """La boucle <tt>for</tt> de Python est plus simple
    que celle du C. C'est une boucle permettant de parcourir des ensembles.
    Par exemple&nbsp;:""" + python_html("""
    >>> for element in [45, -5, "coucou", 3.40000000, [7,8]]:
    ...    print(element)
    ...
    45
    -5
    coucou
    3.4
    [7, 8]
    >>> """) + """
    Quelques remarques :
    <ul>
    <li> Affich� en rouge, ce sont les choses � ne pas oublier.
    <li> Pour indiquer que l'on a termin� la boucle, on tape sur
    la touche � Entr�e � sur une ligne vide.
    <li> On peut utiliser n'importe quelle variable comme indice
    de boucle, par forc�ment <tt>element</tt>.
    """,
    question="""Faites un boucle avec <tt>i</tt> comme indice de boucle,
    qui parcourt l'ensemble des nombre entiers de 0 � 9 inclus et
    qui affiche chacun des nombre.
    <p>
    Ne recopiez pas les <tt>&gt;&gt;&gt;</tt> et <tt>...</tt>,
    mais seulement ce que <b>vous</b> avez tap�.
    N'oubliez pas les espaces pour d�caler � droite.
    """,
    nr_lines = 3,
    tests = (
        Good(P(Equal('for i in range(10):\n   print(i)'))),
        Expect("for",
               "On utilise le mot-clef <tt>for</tt> pour faire un boucle"),
        Expect(' i ',
               """Vous devez appeler <tt>i</tt> la variable qui
               est l'indice de boucle"""),
        Expect('range',
               """Vous devez utiliser la fonction <tt>range</tt> pour
               cr�er les nombres entiers de 0 � 9 inclus."""),
        P(Expect('range(10)',
               """Vous devez utiliser <tt>range(10)</tt> pour
               cr�er les nombres entiers de 0 � 9 inclus.""")),
        Expect(':', """Le langage Python impose le � : � qui indique
        le d�but du corps de la boucle"""),
        Expect('print', """Vous devez utiliser la fonction <tt>print</tt>
        pour afficher la valeur de l'indice."""),
        P(Expect('print(i)',
                 """Vous devez simplement afficher la variable <tt>i</tt>.
                 Donc c'est <tt>print(i)</tt>""")),
        Expect(' in ', """Le langage Python est tr�s litt�raire,
        il manque le <tt>in</tt> qui veut dire <b>dans</b> en fran�ais."""),
        ),

    good_answer = """Si l'on veut faire plusieurs actions dans le corps
    de la boucle, il suffit d'�crire plusieurs lignes d'instructions.
    <p>
    ATTENTION :  Et les lignes qui sont dans le corps de la boucle
    ne peuvent pas �tre plus � gauche que la premi�re ligne de la boucle.   
    """,
    )

add(name="for 2",
    required = ["for", "io:print"],
    question = """La r�ponse est le programme qui affiche&nbsp;:
    <pre>0 0
1 1
2 4
3 9
4 16
5 25
6 36
7 49
8 64
9 81</pre>
Vous utiliserez <tt>i</tt> comme indice de boucle.""",
    nr_lines = 3,
    tests = (
        Good(P(Equal('for i in range(10):\n   print(i, i*i)'))),
        expects(('for', ' i ', ' in ', 'range', 'range(10)', ':', 'print')),
        Expect('*', """Pour calculer le carr� de <tt>i</tt> vous devez
        utiliser une multiplication"""),
        expects(('(', ')', ','),
                """Pour afficher <tt>i</tt> et son carr�, vous devez utiliser
                la fonction <tt>print</tt> (n'oubliez pas les parenth�ses)
                avec deux arguments qui sont <tt>i</tt> et <tt>i*i</tt>.
                (n'oubliez pas la virgule entre les deux arguments."""),
        ),
    good_answer = """Quand il n'y a qu'une seule instruction dans le corps
    de la boucle, on peut tout mettre sur une seule ligne&nbsp;:
    <pre>for i in range(10): print(i, i*i)</pre>
    Mais ceci n'est pas recommand� car c'est moins lisible.""",
    )

add(name="for 3",
    required = ["for 2"],
    question = """La r�ponse est le programme qui affiche&nbsp;:
    <pre>i= 0
i*i= 0
i= 1
i*i= 1
i= 2
i*i= 4
i= 3
i*i= 9
i= 4
i*i= 16</pre>
Vous utiliserez <tt>i</tt> comme indice de boucle.
<p>
Comme il y a 2 lignes � afficher pour chaque valeur prise par
la variable <tt>i</tt>, vous utiliserez deux fois la fonction <tt>print</tt>.
""",
    nr_lines = 4,
    tests = (
        Good(P(Equal('for i in range(5):\n   print("i=",i)\n   print("i*i=",i*i)'))),
        P(expects(('for', ' i ', ' in ', 'range', 'range(5)', ':', 'print',
                   'i=', 'i*i='))),
        Expect('*', """Pour calculer le carr� de <tt>i</tt> vous devez
        utiliser une multiplication"""),
        expects(('(', ')', ','),
                "O� sont les param�tres des fonctions <tt>print</tt>&nbsp;?"),
        Bad(Comment(~NumberOfIs('print', 2),
                    """Vous devez <b>imp�rativement</b> utiliser <b>deux</b>
                    fois la fonction <tt>print</tt> pour cet exercice.""")),
        Bad(Comment(~NumberOfIs('"', 4),
                    """Vous devez afficher deux chaines de caract�res
                    qui sont � i = � et � i*i= �,
                    il doit donc y avoir 4 guillemets dans votre r�ponse""")),
        Bad(Comment(~NumberOfIs('(', 3) | ~NumberOfIs(')', 3),
                    """Vous avez 3 appels de fonctions dans ce programme.
                    Il y en a un pour <tt>range</tt> et 2 pour <tt>print</tt>.
                    Il doit donc y avoir 3 parenth�ses ouvrantes
                    et 3 parenth�ses fermantes.""")),
        Bad(Comment(~NumberOfIs(',', 2),
                    """Il n'y a pas le bon nombre de virgules
                    dans votre r�ponse""")),
        ),
    good_answer = r"""On aurait pu faire un seul <tt>print</tt> :
    <pre>for i in range(5):
            print("i=", i, "\ni*i=", i*i)</pre>
    Comme en langage C, le <tt>\n</tt> indique qu'il faut passer
    � la ligne suivante.""",
    )


add(name="def",
    required = ["idem:incr�menter", "idem:multiplication", "idem:soustraction",
                "idem:division enti�re"],
    before = """Une fonction en Python calcule un r�sultat d�pendant
    de ses param�tres. Voici un exemple de fonction&nbsp;:""" + python_html("""
    def modulo(a, b):
       quotient = a // b
       return a - b * quotient""") + """
   Cette fonction � deux param�tres et retourne un entier si on lui
   � pass� deux entiers en param�tre. <tt>modulo(20, 7)</tt>
   affiche <tt>6</tt>
   <p>
   Il faut bien penser � ce qui est en rouge.
   <p>
   Les lignes qui sont dans la fonction ne peuvent pas �tre plus
   � gauche que la premi�re ligne de la fonction.
   """,
    question = """La r�ponse � cette question est la d�finition de la fonction
   <tt>carre</tt> qui retourne le carr� du nombre <tt>x</tt> pass� en param�tre.
   """,
    tests = (
        Good(P(Equal('def carre(x):\n return x*x'))),
        Good(P(Equal('def carre(x):\n return x**2'))),
        expects(('def ', 'carre', 'x', 'return')),
        expects(('(', ')'),
                "Les param�tres de la fonction sont entre parenth�ses"),
        Expect('*',
               """Pour calculer le carr�, vous multipliez le nombre
   par lui-m�me"""),
        ),
    nr_lines = 3,
    good_answer = """Cette fonction <tt>carre</tt> va donner le bon
   r�sultat pour toutes les variables qui contiennent quelque chose
    qui peut �tre multipli� (entier, flottant, imaginaires...)""",
    )
    
add(name="len",
    required = ["def", "for", "table:len"],
    question = """La r�ponse � cette question est la d�finition de la fonction
   <tt>longueur</tt> qui retourne la longueur du tableau pass� en param�tre.
   <p>
   La d�finition de la fonction est la suivante~:
   <ul>
   <li>On d�clare <tt>longueur</tt> comme une fonction avec un param�tre
        <tt>table</tt>
   <li>On met 0 dans la variable <tt>nb_elements</tt>.
   <li>Pour chaque �l�ment <tt>i</tt> du tableau <tt>table</tt> :
       <ul>
       <li> On ajoute 1 � la variable <tt>nb_elements</tt>
       </ul>
   <li> On retourne la valeur de <tt>nb_elements</tt>
   </ul>
   """,
    nr_lines = 5,
    tests = (
        Good(P(Replace((('nb_elements=nb_elements+1', 'nb_elements+=1'),),
                       Equal('def longueur(table):\n nb_elements = 0\n for i in table:\n  nb_elements += 1\n return nb_elements')))),
        expects(('for', 'nb_elements', '1', 'return', '=', ' in ', 'def ',
                 'longueur', ':')),
        Expect(' i ', "L'indice de boucle doit �tre <tt>i</tt>"),
        ),
    good_answer = """La fonction <tt>len</tt> ne fait pas de boucle,
    elle est donc beaucoup plus rapide que votre version.""",
    )
