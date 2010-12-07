# -*- coding: latin-1 -*-
#    QUENLIG: Questionnaire en ligne (Online interactive tutorial)
#    Copyright (C) 2005-2006 Thierry EXCOFFIER, Universite Claude Bernard
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


add(name="message cod�",
    required=["texte:remplace multiple"],
    question="""Vous recevez le message secret
    <tt>731 4251331 6135421 731 35421 61 42513 13 42531</tt>
    Pour le lire, il faut faire quelques remplacements&nbsp;:
    <ul>
    <li> 1 &#8594; e
    <li> 2 &#8594; h
    <li> 3 &#8594; n
    <li> 4 &#8594; c
    <li> 5 &#8594; i
    <li> 6 &#8594; d
    <li> 7 &#8594; u
    </ul>
    Fais afficher le message d�cod�.
    """,
    default_answer="print '731 4251331 6135421 731 35421 61 42513 13 42531'",
    tests=(
    do_not_cheat(rejected='chien'),
    print_required,
    replace_required,
    python_answer_good('une chienne deniche une niche de chien en chine\n'),
    ),
    )

add(name='10001 = ? * ?',
    required=['pour:d� + d� = 7'],
    question="""Fait afficher les deux nombres plus petits que 200 dont
    le produit est �gal � <tt>10001</tt>.""",
    nr_lines = 4,
    tests=(
    do_not_cheat(rejected='137'),
    for_required,
    print_required,
    number_of_is('for', 2, "Il faut deux boucles pour trouver"),
    python_answer_good('73137', remove_spaces=True, remove_newline=True),
    python_answer_good('13773', remove_spaces=True, remove_newline=True),
    python_answer_good(('7313713773','1377373137') ,
                       """Tu as trouv� que
                       <tt>73 * 137 = 10001</tt>
                       et
                       <tt>137 * 73 = 10001</tt>
                       C'est un peu la m�me chose... Non&nbsp;?
                       <p>
                       Pour �viter cela, on affiche seulement le plus grand
                       nombre en premier.
                       C'est tr�s facile, il faut que la deuxi�me boucle
                       s'arr�te avant de d�pass� la premi�re.
<pre>for d1 in range(200):
 for d2 in range(d1):
   if d1 * d2 == 10001:
     print d1, d2</pre>
     Cette boucle affiche <tt>137 73</tt>contrairement
     � la tienne qui affiche&nbsp;:
     <hr>
     """,                       
                       remove_spaces=True, remove_newline=True),
    ),
    )

def pm(number, prod, summ, n):
    if n == 0:
        if prod == summ:
            print number
    else:
        n -= 1
        for i in range(1,number % 10 + 1):
            pm(number*10 + i, prod*i, summ+i, n)

# for i in range(1,10): pm(i, i, i, 2)

               
add(name="multiplier = sommer",
    required=['pour:d� + d� = 7'],
    question="""Fais afficher par Python le
    <b>plus grand</b> nombre de 3 chiffres qui �
    la particularit� d'avoir la somme de ses 3 chiffres �gale
    au produit de ses trois chiffres.
    <p>
    Avec 6 chiffres la solution � trouver serait <em>621111</em>
    car <em>6+2+1+1+1+1 = 12 = 6*2*1*1*1*1</em>.
    Tu devrais faire afficher � Python <tt>6 2 1 1 1 1</tt>.
    """,
    nr_lines = 6,
    tests=(
    print_required,
    space_required,
    apostrophe_rejected,
    for_required,
    if_required,
    number_of_is('for', 3, "Il faut 3 <tt>for</tt> pour cet exercice"),
    python_answer_reject('1 2 3',
                 """Il faut une seule r�ponse pour cet exercice,
                 regarde les indices pour t'aider"""),
    range_required(),
    python_answer_good('321', remove_spaces=True, remove_newline=True),
    ),
    indices = (
    """Le plus grand nombre est celui qui a les plus gros chiffres
    au d�but.""",
    """Il faut 3 boucles imbriqu�es&nbsp;:
    <ul>
    <li> La premi�re va de 1 � 9 car le premier chiffre ne peut �tre 0.</li>
    <li> La deuxi�me va de 0 jusqu'� la valeur du chiffre pr�c�dent
    pour garantir que le premier sera le plus grand.</li>
    <li> La troisi�me va de 0 jusqu'� la valeur du chiffre pr�c�dent
    pour garantir que le deuxi�me sera le plus grand.</li>
    </ul>""",
    """Le d�but pour t'aider&nbsp;:
    <pre>for premier in range(1,10):
    for deuxieme in range(premier+1):</pre>
    """,
    ),
    )

jean = [36,73, 33, 20, 87, 75, 32, 31, 99, 27, 22, 65, 23, 51, 7, 25, 4, 5, 80]
jacques = [82, 81, 25, 7, 74, 37, 89, 95, 47, 27, 83, 29, 97, 70, 18, 87, 88]

def intersection(a,b):
    s = ''
    for i in a:
        if i in b:
            s += str(i) + '\n'
    return s

add(name="intersection ensembliste",
    required=['pour:cherche 72', 'booleen:dans'],
    question="""<img src="intersection_small.png" align="RIGHT">Deux collectionneurs de livres se rencontrent.
    <ul>
    <li> Jean a les num�ros <tt>""" + str(jean) + """</tt> </li>
    <li> Jacques a les num�ros <tt>""" + str(jacques) + """</tt> </li>
    </ul>
    <p>
    Fais afficher � Python les livres que poss�de Jean et que Jacques
    poss�de aussi (un livre par ligne).""",
    nr_lines = 4,
    tests=(
    print_required,
    space_required,
    apostrophe_rejected,
    for_required,
    if_required,
    in_required,
    number_of_is('[', 2, 'Il faut 2 classeurs pour cet exercice'),
    number_of_is(']', 2, 'Il faut 2 classeurs pour cet exercice'),
    python_answer_good(intersection(jean, jacques)),
    python_answer_good(intersection(jacques, jean)),
    ),
    indices = (
    """Tu fais en Python comme dans la r�alit�.
    Jean prend ses livres 1 par 1 et demande � Jacques s'il
    le poss�de. Si oui, alors c'est un livre en commun.""",
    ),   
    )

def soustraction(a,b):
    s = ''
    for i in a:
        if i not in b:
            s += str(i) + '\n'
    return s

add(name="soustraction ensembliste",
    required=['intersection ensembliste', 'booleen:pas dans'],
    question="""<img src="soustraction_small.png" align="RIGHT">Deux collectionneurs de livres se rencontrent.
    <ul>
    <li> Jean a les num�ros <tt>""" + str(jean) + """</tt> </li>
    <li> Jacques a les num�ros <tt>""" + str(jacques) + """</tt> </li>
    </ul>
    <p>
    Fais afficher la liste des livres que Jean poss�de et
    qui manquent � Jacques (un livre par ligne).
    """,
    nr_lines = 4,
    tests=(
    print_required,
    space_required,
    apostrophe_rejected,
    for_required,
    if_required,
    in_required,
    not_required,
    number_of_is('[', 2, 'Il faut 2 classeurs pour cet exercice'),
    number_of_is(']', 2, 'Il faut 2 classeurs pour cet exercice'),
    python_answer_good(soustraction(jean, jacques)),
    python_answer_bad(soustraction(jacques, jean),
                      """Tu viens d'afficher la liste des livres
                      que Jacques poss�de et qui manquent � Jean"""),
    ),
    indices = (
    """Tu fais en Python comme dans la r�alit�.
    Jean prend ses livres 1 par 1.
    Si le livre n'est pas dans la collection de Jacques
    alors il faut l'afficher.""",
    ),
    )

def union(a,b):
    s = ''
    for i in a:
        s += str(i) + '\n'

    for i in b:
        if i not in a:
            s += str(i) + '\n'
    return s


add(name="union ensembliste",
    required=['soustraction ensembliste' ],
    question="""<img src="union_small.png" align="RIGHT">Deux collectionneurs de livres se rencontrent.
    <ul>
    <li> Jean a les num�ros <tt>""" + str(jean) + """</tt> </li>
    <li> Jacques a les num�ros <tt>""" + str(jacques) + """</tt> </li>
    </ul>
    <p>
    Jean et Jacques d�cident de mettre ensemble leur deux collections.
    �videmment, ils ne gardent pas les livres qu'ils ont en double.
    <p>
    Fais afficher le contenu de leur collection commune (un livre par ligne).
    """,
    nr_lines = 5,
    tests=(
    print_required,
    space_required,
    apostrophe_rejected,
    for_required,
    if_required,
    in_required,
    not_required,
    reject('+', """Utiliser l'addition de classeur est une bonne id�e,
    mais essaye de r�soudre le probl�me sans l'utiliser."""),
    number_of_is('[', 3, 'Il faut 3 classeurs pour cet exercice'),
    number_of_is(']', 3, 'Il faut 3 classeurs pour cet exercice'),
    number_of_is('for', 2, 'Il faut 2 boucle <tt>for</tt> pour cet exercice'),
    python_answer_good(union(jean, jacques)),
    python_answer_good(union(jacques, jean)),
    ),
    indices = (
    """Tu fais en Python comme dans la r�alit�.
    On part de la collection de Jean,
    puis Jacques prend ses livres 1 par 1&nbsp;:
    si Jean n'a pas le livre on l'ajoute � sa collection.
    <p>
    On obtiendra le m�me r�sultat si l'on fait l'inverse.""",
    ),
    )


message = [[1,' '],[2,'#'],[2,'-'],[2,'#'],[2,'\n'],[2,' '],[4,'#'],[2,'\n'],[3,' '],[2,'#']]
message_str = str(message).replace(', ',',')

def formate(m):
    s = ''
    for p in m:
        for i in range(p[0]):
            s += p[1] + ' '
    return s.replace(' ','')


add(name="dessin cach�",
    required=['classeur:une page', 'classeur:dans classeur',
              'classeur:les entiers', 'dis:m�me ligne'],
    question="""On a le classeur suivant&nbsp;:
    <pre><small>%s</small></pre>
    Pour afficher, le message, il faut prendre chacun des petits classeurs,
    la premi�re page indique le nombre de fois que l'on doit r�p�ter le
    texte qui est dans la deuxi�me page.
    Le message commence donc par&nbsp;: afficher '#', afficher '#', afficher '-', afficher '-', afficher '-', afficher '-', afficher '#', ...
    <p>
    Pour pouvoir lire le message, il faut tout afficher sur la m�me ligne.
    """ % message_str,
    nr_lines = 4,
    default_answer = '%s' % message_str,
    tests=(
    print_required,
    space_required,
    for_required,
    python_answer_good(formate(message) + '\n', remove_spaces=True),
    ),
    indices=(
    """Il faut d'abord faire une boucle pour parcourir le grand classeur""",
    """La premi�re page du petit classeur indique le nombre de fois,
    que l'on doit afficher le texte qui est dans la deuxi�me page.""",
    """Pour afficher plusieurs fois le texte, on peut par exemple
    faire une boucle sur l'ensemble des entiers avec <tt>range</tt>""",
    ),
    )
    
    
