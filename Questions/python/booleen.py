# -*- coding: latin-1 -*-
#    QUENLIG: Questionnaire en ligne (Online interactive tutorial)
#    Copyright (C) 2006 Thierry EXCOFFIER, Universite Claude Bernard
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program; if not, write to the Free Software
#    Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
#    Contact: Thierry.EXCOFFIER@bat710.univ-lyon1.fr

from questions import *
from check import *

add(name='intro',
    required=['nombre:addition multiple', 'classeur:multiplication',
              'texte:remplace multiple', 'pour:compter de 2 en 2'],
    before="""Quand quelque chose est vrai, Python l'�crit
    <tt>True</tt> et si c'est faux, il �crit <tt>False</tt>""",
    question="""Fait �crire <tt>True</tt> � Python""",
    tests=(
    print_required,
    space_required,
    apostrophe_rejected,
    require("True", "Je ne vois pas le <tt>True</tt>"),
    python_answer_good('True\n'),
    ),
    )

add(name='�galit� nombres',
    required=['intro', 'nombre:multiplication'],
    before="""Pour demander � Python si deux choses sont �gales,
    on met l'op�ration <tt>==</tt> entre les deux choses.
    Par exemple <tt>print 5 == 7</tt> affiche <tt>False</tt>""",
    question="""Fait afficher � Python si <tt>123*456</tt>
    est �gale � <tt>56088</tt>.""",
    tests=(
    print_required,
    space_required,
    apostrophe_rejected,
    multiply_required,
    do_not_cheat(rejected='True'),
    require(('123', '*', '456'), "Tu dois faire calculer <tt>123*456</tt>"),
    egality_required,
    comment("""Les parenth�ses ne sont pas utiles car le Python
    calcule d'abord les multiplications, puis les additions et enfin
    il fait les comparaisons (<tt>==</tt> et les autres)""",
            require=(')','(')),
    python_answer_good('True\n'),
    ),
    )

add(name='�galit� textes',
    required=['�galit� nombres', 'texte:chien'],
    question="""Fais afficher � Python si <tt>'Bonjour'</tt>
    est �gale � <tt>'bonjour'</tt>.""",
    tests=(
    print_required,
    space_required,
    apostrophe_required,
    do_not_cheat(rejected='False'),
    require(("'Bonjour'", "'bonjour'"),
            "Tu dois comparer les textes <tt>Bonjour</tt> et <tt>bonjour</tt>"
            ),
    egality_required,
    python_answer_good('False\n'),
    ),
    )

add(name='�galit� classeurs',
    required=['�galit� textes', 'classeur:dans classeur',
              'classeur:les entiers'],
    before = """2 classeurs sont �gaux si chacune de leurs pages sont �gales.
    <table class="invisible">
    <tr>
    <td align="right"><tt>[1,2,3]</tt></td>
    <td><tt>==</tt></td>
    <td><tt>[1,2,3]</tt></td>
    <td> donne <tt>True</tt> car ils sont identiques.</td>
    </tr>
    <tr>
    <td align="right"><tt>[1,2,3]</tt></td>
    <td><tt>==</tt></td>
    <td><tt>[1,1+1,1+1+1]</tt></td>
    <td> donne <tt>True</tt> car c'est vrai.</td>
    </tr>
    <tr>
    <td align="right"><tt>[1,2,3,4]</tt></td>
    <td><tt>==</tt></td>
    <td><tt>[1,2]+[3,4]</tt></td>
    <td> donne <tt>True</tt></td>
    </tr>
    <tr>
    <td align="right"><tt>[1,2,3]</tt></td>
    <td><tt>==</tt></td>
    <td><tt>[1,2]</tt></td>
    <td> donne <tt>False</tt> car ils n'ont pas le m�me nombre de pages.</td>
    </tr>
    <tr>
    <td align="right"><tt>[1,2,3]</tt></td>
    <td><tt>==</tt></td>
    <td><tt>[1,2,'3']</tt></td>
    <td> donne <tt>False</tt> car <tt>3</tt> est diff�rent de <tt>'3'</tt></td>
    </tr>
    <tr>
    <td align="right"><tt>[1,2,3]</tt></td>
    <td><tt>==</tt></td>
    <td><tt>[1,3,2]</tt></td>
    <td> donne <tt>False</tt> car l'ordre est diff�rent</td>
    </tr>
    </table>
    """,    
    question="""Fais afficher � Python si <tt>[0,1,2,1+2]</tt>
    est �gale � <tt>range(4)</tt>.""",
    tests=(
    print_required,
    space_required,
    apostrophe_rejected,
    square_bracket_required,
    egality_required,
    do_not_cheat(rejected='True'),
    do_not_cheat(rejected='3'),
    range_required(4),
    python_answer_good('True\n'),
    ),
    )

good_search = """0 * 8 == 72 : False
1 * 8 == 72 : False
2 * 8 == 72 : False
3 * 8 == 72 : False
4 * 8 == 72 : False
5 * 8 == 72 : False
6 * 8 == 72 : False
7 * 8 == 72 : False
8 * 8 == 72 : False
9 * 8 == 72 : True
10 * 8 == 72 : False
11 * 8 == 72 : False
12 * 8 == 72 : False
13 * 8 == 72 : False
14 * 8 == 72 : False
"""

good_search2 = good_search.replace(' ','')

add(name="recherche 72",
    required=['�galit� nombres', 'dis:formule et r�sultat',
              'pour:compter de 2 en 2'],
    question="""Fais afficher � Python :<pre>%s</pre>""" % good_search,
    tests=(
    print_required,
    space_required,
    apostrophe_required,
    egality_required,
    for_required,
    range_required(15),
    do_not_cheat(rejected=('False', '10')),
    python_answer_good(good_search2, remove_spaces=True),
    ),
    indices=(
    """Commence par faire une boucle affichant les nombres de 0 � 15,
    puis ajoute la formule, puis ajoute le test d'�galit� pour
    que Python affiche <tt>True</tt> ou <tt>False</tt>""",
    )
    )

add(name='�galit� �trange',
    required=['�galit� textes'],
    question="""Fait afficher � Python si <tt>'True'</tt>
    et �gale � <tt>True</tt>""",
    tests=(
    print_required,
    space_required,
    apostrophe_required,
    egality_required,
    require('True',
            """Je ne trouve pas la texte <tt>'True'</tt> dans
             la phrase Python&nbsp;!"""
            ),
    do_not_cheat(rejected='False'),
    python_answer_good('False\n'),
    ),
    good_answer="""Pour Python le texte <tt>'True'</tt>
    et <tt>True</tt> ne sont pas �gaux car le deuxi�me n'est pas un texte
    mais un bool�en qui indique si quelque chose est vrai ou faux.""",
    )

    
add(name='inf�rieur nombre',
    required=['�galit� nombres'],
    before="""La phrase <tt>a &lt; b</tt> est vraie
    si <tt>a</tt> est plus petit que <tt>b</tt>.
    <p>
    <tt>a</tt> et <tt>b</tt> peuvent �tre des nombres, des textes, ...""",
    question="""Fais afficher si <tt>2*3</tt> est inf�rieur � <tt>6</tt>""",
    tests=(
    print_required,
    space_required,
    apostrophe_rejected,
    do_not_cheat(rejected='False'),
    require(('2','3','6','<','*'),
            "Dans la phrase Python on doit trouver&nbsp;: 2, 3, 6, *, &lt; et 6"
            ),
    less_than_required,
    python_answer_good('False\n'),
    ),
    good_answer = """Et oui, c'est faux car 6 n'est pas inf�rieur � 6....""",
    )

add(name='inf�rieur texte',
    required=['inf�rieur nombre', '�galit� textes'],
    before="""Un texte est inf�rieur (&lt;) � un autre s'il
    est avant lui dans le dictionnaire.""",
    question="""Fais afficher si <tt>'apr�s'</tt> est inf�rieur � <tt>'avant'</tt>""",
    tests=(
    print_required,
    space_required,
    apostrophe_required,
    do_not_cheat(rejected='True'),
    require(("'apr�s'","'avant'", '<'),
            "Dans la phrase Python on doit trouver&nbsp;: 'apr�s', 'avant' et &lt;"
            ),
    less_than_required,
    python_answer_good('True\n'),
    ),
    )

add(name='dans',
    required=['si:cherche', '�galit� nombres'],
    before="""On a souvent besoin de savoir si quelque chose est
    dans un classeur. En fran�ais, on dirait
    <em>truc est-il dans machin&nbsp;?</em>
    en Python on dit <tt>truc in machin</tt>
    On a pas besoin du point d'interrogation.
    <pre>5 in [7,6,5,7]</pre>
    L'expression est vrai car <tt>5</tt> est dnas le classeur.    
    """,
    question="""Fais �crire � Python s'il trouve <tt>'a'</tt>
    dans le classeur <tt>'un grand chat'</tt>""",
    tests=(
    print_required,
    space_required,
    apostrophe_required,
    in_required,
    do_not_cheat(rejected='True'),
    reject('for', """Il faut faire cet exercice sans boucle <tt>for</tt>"""),
    require(("'un grand chat'","'a'"),
            """Dans la phrase Python on doit trouver&nbsp;: 'un grand chat'
            et 'a'"""
            ),
    python_answer_good('True\n'),
    ),
    )
    
add(name='classeur dedans',
    required=['dans', '�galit� classeurs'],
    question = """Fais afficher � Python s'il trouve
    <tt>[1,2]</tt> dans <tt>[ range(3), [2,1], [1,1+1], [1,2,3] ]</tt>""",
    default_answer = '[ range(3), [2,1], [1,1+1], [1,2,3] ]',
    tests=(
    print_required,
    space_required,
    in_required,
    square_bracket_required,
    number_of_is('[', 5),
    number_of_is(']', 5),
    range_required(3),
    do_not_cheat(rejected='True'),
    reject('for', """Il faut faire cet exercice sans boucle <tt>for</tt>"""),
    python_answer_good('True\n'),
    ),
    )


add(name='pas dans',
    required=['dans', 'histoire:enl�ve voyelles'],
    before="""En anglais, <tt>not</tt> veut dire <em>non</em> ou <em>pas</em>.
    L'expression Python <tt>5 not in [4,6]</tt> est <em>vrai</em>
    car <tt>5</tt> n'est pas dans <tt>[4,6]</tt>
    """,
    question="""Fais �crire � Python <tt>'un grand chat'</tt>
    en enlevant les voyelles (<tt>'aeiou'</tt>).
    """,
    nr_lines = 4,
    tests=(
    print_required,
    space_required,
    apostrophe_required,
    in_required,
    not_required,
    for_required,
    do_not_cheat(rejected='ngrndch'),
    require(("'un grand chat'","'aeiou'"),
            """Dans la phrase Python on doit trouver&nbsp;: 'un grand chat'
            et 'aeiou'"""
            ),
    python_answer_good('ngrndcht', remove_spaces=True, remove_newline=True),
    ),
    )
