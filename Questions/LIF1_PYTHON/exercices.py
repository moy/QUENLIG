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
Exercices simples
"""

from questions import *
from check import *

add(name="len",
    required = ["control:def", "control:for", "table:len",
                "idem:incr�menter"],
    question = """La r�ponse � cette question est la d�finition de la fonction
   <tt>longueur</tt> qui retourne la longueur du tableau pass� en param�tre.
   <p>
   La d�finition de la fonction est la suivante&nbsp;:
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
        Good(P(Replace((('nb_elements=nb_elements+1', 'nb_elements+=1'),
                        ('nb_elements=1+nb_elements', 'nb_elements+=1'),
                        ),
                       Equal('def longueur(table):\n nb_elements = 0\n for i in table:\n  nb_elements += 1\n return nb_elements')))),
        expects(('for', 'nb_elements', '1', 'return', '=', ' in ', 'def ',
                 'longueur', ':')),
        Expect(' i ', "L'indice de boucle doit �tre <tt>i</tt>"),
        ),
    good_answer = """La fonction <tt>len</tt> ne fait pas de boucle,
    elle est donc beaucoup plus rapide que votre version.""",
    )

add(name="sum",
    required = ["control:def", "control:for", "table:sum"],
    question = """La r�ponse � cette question est la d�finition de la fonction
   <tt>somme</tt> qui retourne la somme des �l�ments d'un tableau
   pass� en param�tre.
   <p>
   La d�finition de la fonction est la suivante&nbsp;:
   <ul>
   <li>On d�clare <tt>somme</tt> comme une fonction avec un param�tre
        <tt>table</tt>
   <li>On met 0 dans la variable <tt>la_somme</tt>.
   <li>Pour chaque �l�ment <tt>i</tt> du tableau <tt>table</tt> :
       <ul>
       <li> On ajoute <tt>i</tt> � la variable <tt>la_somme</tt>
       </ul>
   <li> On retourne la valeur de <tt>la_somme</tt>
   </ul>
   """,
    nr_lines = 5,
    tests = (
        Good(P(Replace((('la_somme=la_somme+i', 'la_somme+=i'),
                        ('la_somme=i+la_somme', 'la_somme+=i'),
                        ),
                       Equal('def somme(table):\n la_somme = 0\n for i in table:\n  la_somme += i\n return la_somme')))),
        expects(('for', 'la_somme', 'return', '=', ' in ', 'def ',
                 'somme', ':')),
        Expect(' i ', "L'indice de boucle doit �tre <tt>i</tt>"),
        ),
    good_answer = """Si vous ne l'avez pas fait : v�rifier que votre
    fonction donne le bon r�sultat dans l'interpr�teur Python.
    <p>
    Que donne <tt>somme([0.5, 1.3, 0.1])</tt>&nbsp;?""",
    )

add(name="ajoute complexe",
    required = ["control:def", "structure:attributs"],
    before = """En Python il n'y a pas de proc�dures, seulement des fonctions.
    <p>
    Si il n'y a pas de <tt>return<tt> dans une fonction alors
    la valeur <tt>None</tt> est automatiquement retourn�e
    <p>
    On peut consid�rer qu'une proc�dure est une fonction sans <tt>return<tt>
    """,
    question = """D�finissez la proc�dure <tt>ajoute_au_premier</tt>
    qui a comme param�tres <tt>a</tt> et <tt>b</tt> qui sont des complexes
    et qui ajoute <tt>a</tt> et <tt>b</tt> et stocke le
    r�sultat dans <tt>a</tt>""",
    default_answer = """def ajoute_au_premier(a, b):
    """,
    nr_lines = 4,
    tests = (
        Good(P(Replace((
            ('b.imaginaire+a.imaginaire', 'a.imaginaire+b.imaginaire'),
            ('b.reel+a.reel', 'a.reel+b.reel'),
            ('a.reel=a.reel+', 'a.reel+='),
            ('a.imaginaire=a.imaginaire+', 'a.imaginaire+='),
            ),
                       Equal('def ajoute_au_premier(a,b):\n a.reel+=b.reel\n a.imaginaire+=b.imaginaire')
                        | Equal('def ajoute_au_premier(a,b):\n a.imaginaire+=b.imaginaire\n a.reel+=b.reel')
                       ))),
        Bad(Comment(~ NumberOfIs('\n', 2),
                    """La r�ponse est en 3 lignes : le <tt>def</tt>
                    et les deux affections (parties r�elle et imaginaire)""")),
        expects(('def', ':', '=', '+', 'imaginaire', 'reel',
                'a.imaginaire', 'a.reel', 'b.imaginaire', 'b.reel')),
        ),
    good_answer = """Il est tout � fait possible d'�crire
    <tt>a += b</tt> au lieu de <tt>ajoute_au_premier(a, b)</tt>.
    <p>
    Mais pour cela on d�finit une <em>m�thode</em> et cela d�passe
    l'objectif de ce cours.""",
    )

add(name="somme 2 d�s",
    required=['table:range', 'control:for', 'table:multiplication',
              'io:print'],
    nr_lines = 6,
    question = """La r�ponse � cette question est la suite de lignes Python
    que vous devez taper pour calculer et afficher le nombre de tirage
    de 2 d�s qui donnent la m�me somme.
    Votre programme devra donc afficher tr�s exactement&nbsp;:
    <pre>[0, 0, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]</pre>
    Ceci veut dire que pour obtenir la somme des deux d�s �gale �&nbsp;:
    <ul>
    <li> 0 : Il n'y a aucun tirage possible
    <li> 1 : Il n'y a aucun tirage possible
    <li> 2 : Il y a 1 seul tirage possible
    <li> 3 : Il y a 2 tirages possible
    <li> ...
    <li> 7 : Il y a 6 tirages possible
    <li> ...
    <li> 12 : Il y a 1 seul tirage possible
    </ul>
    Pour que votre r�ponse soit accept�e :
    <ul>
    <li> Le premier d� tir� s'appelle <tt>a</tt>
    <li> Le deuxi�me d� tir� s'appelle <tt>b</tt>
    <li> Les valeurs prises par les 2 d�s sont entre 1 et 6
    <li> Le tableau qui est calcul� et affich� s'appellera <tt>nb</tt>
    <li> Vous utilisez un simple <tt>print</tt> pour afficher <tt>nb</tt>
    </ul> """,
    tests = (
        Good(P(Replace((
            ('b+a', 'a+b'),
            ('nb[a+b]=nb[a+b]+1', 'nb[a+b]+=1'),
            ('nb[a+b]=1+nb[a+b]', 'nb[a+b]+=1'),
            ('13*[0]', '[0]*13'),
            ),
                       Equal('''nb = [0]*13
for a in range(1, 7):
  for b in range(1, 7) :
    nb[a+b] += 1
print(nb)''')))),
        Expect('13', """Vous devez initialiser <tt>nb</tt> avec un tableau
        contenant 13 entiers nul en utilisant la multiplication de tableau"""),
        Reject('range(6)', """Les variables repr�sentant les d�s doivent
        prendre des valeurs entre 1 et 6 inclu (pas entre 0 et 5).
        Utilisez <tt>range(1,7)</tt>."""),
        Reject('range(1,6)', """Les variables repr�sentant les d�s doivent
        prendre des valeurs entre 1 et 6 inclu (pas entre 1 et 5)"""),
        P(Replace((('b+a', 'a+b'),),
                  Expect('a+b',
                         "O� additionnez-vous les valeurs des 2 d�s&nbsp;?",
                         canonize=False),
                  )),
        Expect('nb[', """Je ne vois pas dans votre programme l'endroit
        o� vous modifiez un �lement de <tt>nb</tt> pour lui ajouter un"""),
        P(expects(('nb', ' a ', ' b ', 'nb', 'print', 'for', 'range',
                 'range(1,7)', '[0]'
                 ))),
        ),
    )


add(name="racine carr�",
    required=["control:while", "idem:abs"],
    nr_lines = 8,
    question = """Donnez la d�finition de la fonction <tt>racine_carree</tt>,
    qui a un param�tre de type flottant nomm� <tt>nombre</tt> et qui retourne
    la racine carr�e de ce nombre.
    <p>
    Cette fonction utilisera deux variables locales :
    <tt>racine_courante</tt> qui contiendra l'approximation de la racine
    et <tt>racine_precedente</tt> qui contiendra la valeur pr�c�dente.
    <p>
    Voici l'algorithme <b>� respecter scrupuleusement</b> :
    <ul>
    <li> On initialise la racine pr�c�dente � 0.
    <li> On initialise la racine courante avec le nombre divis� par 2.
    <li> Tant que la valeur absolue (fonction <tt>abs</tt>)
         de la diff�rence entre la racine pr�c�dente
         et la nouvelle racine est sup�rieure � un milli�me&nbsp;:
    <ul>
         <li> La racine pr�c�dente prend la valeur de la racine courante.
         <li> La racine courante prend pour valeur la moyenne de
              la racine courante et du nombre divis� par la racine courante.
              Cette op�ration est faite en une ligne.
    </ul>
    <li> On retourne la racine courante.
    </ul>
""",
    tests = (
        expects(('def', 'racine_carree', 'nombre', 'racine_precedente',
                 'racine_courante', 'while', 'abs', '/', '+')),
        P(Expect('racine_courante=nombre/2',
                 "Je ne vois pas l'initialisation de la racine courante.",
                 canonize = False)),
        P(Expect('racine_precedente=0',
                 "Je ne vois pas l'initialisation de la racine pr�c�dente.",
                 canonize = False)),
        P(Expect('nombre/racine_courante',
                 "Je ne vois pas le nombre divis� par la racine courante",
                 canonize = False)),
        P(Expect(')/2',
                 "Comment faites-vous la moyenne sans diviser par 2",
                 canonize = False)),
        Bad(P(Comment(~(Contain('racine_precedente-racine_courante',
                                canonize = False)
                        | Contain('racine_courante-racine_precedente',
                                  canonize = False)
                        ),
                       """Je ne vois pas la diff�rence entre la racine
                       pr�c�dente et la nouvelle""",
                       ))),
        Good(RemoveSpaces(Replace((('racine_courante-racine_precedente',
                         'racine_precedente-racine_courante'),
                        ('racine_courante+nombre/racine_courante',
                         'nombre/racine_courante+racine_courante'),
                        ('>=', '>'),
                        ('2.', '2'),
                        ('1.', '1'),
                        ('1000.', '1000'),
                        ('1/1000', '0.001'),
                        ('1e-3', '0.001'),
                        ('10**-3', '0.001'),
                        ),P_AST(Equal(
                        """def racine_carree(nombre):
  racine_precedente = 0
  racine_courante = nombre / 2
  while abs(racine_precedente - racine_courante) > 0.001:
     racine_precedente = racine_courante
     racine_courante = (nombre/racine_courante + racine_courante) / 2
  return racine_courante"""))))),
                
        ),
    )


add(name="cr�er matrice",
    required=["table:matrice", "table:empiler",
              "table:multiplication", "control:for"],
    question="""D�finissez une fonction <tt>creer_matrice</tt>
    qui a pour arguments
    <tt>nb_lignes</tt>, <tt>nb_colonnes</tt>, <tt>valeur</tt>
    et qui retourne une matrice dont tous les �l�ments sont �gaux
    � la valeur.
    <p>
    <tt>creer_matrice(2, 3, 9)</tt> retourne <tt>[[9, 9, 9], [9, 9, 9]]</tt>
    <p>
    Votre fonction commencera par initialiser une variable <tt>matrice</tt>
    de telle fa�on qu'elle ne contiennent aucune ligne,
    puis une boucle utilisant la variable <tt>numero_ligne</tt> comme indice
    lui ajoutera autant de lignes que n�cessaire.
    Chaque ligne est un tableau de <tt>nb_colonnes</tt> �l�ments
    tous �gaux � <tt>valeur</tt>
    """,
    nr_lines = 6,
    tests = (
        Good(P(Replace((('nb_colonnes*[valeur]',
                         '[valeur]*nb_colonnes'),
                        ),
                       Equal('''
def creer_matrice(nb_lignes, nb_colonnes, valeur):
   matrice = []
   for numero_ligne in range(nb_lignes):
      matrice.append([valeur]*nb_colonnes)
   return matrice'''
    )))),
        expects(('def', 'creer_matrice', 'nb_lignes', 'nb_colonnes',
                 'valeur', 'return', 'numero_ligne')),
        Expect('append', """Dans la boucle vous devez utiliser la
               fonction <tt>append</tt> pour ajouter une ligne �
               la matrice."""),
        Expect('range',
               """Vous devez faire la boucle autant de fois qu'il y a
                  de lignes � cr�er, vous devez donc utiliser <tt>range</tt>
                  pour cr�er l'ensemble sur lequel on va it�rer."""),
        P(Expect('matrice=[]',
                 """O� est l'initialisation de <tt>matrice</tt> comme �tant
                 un tableau vide&nbsp;?""", canonize=False)),
        P(Expect('[valeur]',
                 """Le moyen le plus simple pour cr�er une ligne est
                 d'utiliser un tableau d'un �l�ment (<tt>valeur</tt>)
                 et de le multiplier pour obtenir un tableau
                 avec le nombre d'�l�ments d�sir�.""",
                 canonize=False)),
        Bad(P(Comment(~(Contain('[valeur]*nb_colonnes', canonize=False)
                        | Contain('nb_colonnes*[valeur]', canonize=False)
                        ),
                       """Pour cr�er les lignes contenant les valeurs
                       identiques, vous devez utilisez la multiplication."""))),
        P(expects(('range(nb_lignes)', 'matrice.append',
                   'for numero_ligne in'))),
        ),
    good_answer = """ATTENTION au pi�ge :""" + python_html("""
>>> a = creer_matrice(2,3,[1])
>>> print(a)
[[[1], [1], [1]], [[1], [1], [1]]]
>>> a[0][0] = [3] # Remplace un �l�ment par un autre.
[[[3], [1], [1]], [[1], [1], [1]]]
>>> a[1][1][0] = 2 # Change la valeur d'un �l�ment
[[[3], [2], [2]], [[2], [2], [2]]]"""
    ) + """Ceci est du au fait que la mutiplication de tableau ne recopie
    pas les valeurs, c'est la m�me valeur dans toutes les cases du tableau.""",
)

# XXX a finir ? (structure:instance param�tr�e n'est pas fini non plus)
# add(name="ajoute complexe",
#     required = ["control:def", "structure:instance param�tr�e",
#                 "structure:attributs"],
#     question = """D�finissez la fonction <tt>sum_c</tt>
#     qui a comme param�tres <tt>a</tt> et <tt>b</tt> qui sont des complexes
#     et qui retourne le complexe �gal � la somme des deux.
#     <p>
#     Cette fonction ne doit pas modifier ses param�tres.
#     """,
#     default_answer = """def sum_c(a, b):
#     """,
#     tests = (
#         Good(P('def sum_c(a,b):\n return Complexe(a.reel+b.reel,a.imaginaire+b.imaginaire)')),
#         ),
#     good_answer = """On peut bien s�r faire en sorte d'utiliser <tt>+</tt>
#     pour additionner les complexes.
#     Mais pour cela on d�finit une <em>methode</em> mais cela d�passe
#     l'objectif de ce cours.""",
#     )
#     
