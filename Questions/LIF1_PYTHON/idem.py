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
Environnement de travail, prise en main de quenlig
et questions sur les choses qui sont identiques en C et Python.
"""

from questions import *
from check import *

add(name="CLIQUEZ-ICI !",
    before="""
    Tout d'abord lancez l'interpr�teur Python XXXXXXXXXXXXXXXXXXXXX
    """,
    question="""R�pondez par <tt>oui</tt> dans le cadre intitul�
    <tt><em>Donnez votre r�ponse ici</em></tt>
    quand vous aurez lanc� l'interpr�teur Python.""",

    tests = (
        Good(Yes()),
        ),
    good_answer = """Choisissez maintenant une autre question
    dans le cadre de gauche intitul� � Les questions �
    <p>
    Vous pouvez aussi simplement taper sur la touche
    � Entr�e � pour passer � la question suivante.
    """
    
    )

add(name="interpr�teur",
    required = ["CLIQUEZ-ICI !"],
    question = """Quand vous tapez <tt>2**10</tt> dans la fen�tre
    de l'interpr�teur Python et que vous validez
    en appuyant sur la touche � Entr�e �.
    <P>
    Qu'est-ce que cela affiche&nbsp;?""",
    tests = (
        Good(Contain('1024')),
        ),
    good_answer = """Vous remarquerez les touches curseurs du clavier
    vous permettent de naviguer dans l'historique et de modifier
    les commandes que vous avez tap�s."""
    )

add(name="affectation",
    required = ["interpr�teur"],
    before="""L'op�rateur <tt>=</tt> en langage C indique qu'il faut
    <b>recopier une valeur</b> � l'emplacement m�moire de la variable.
    <p>
    En Python, cet op�rateur indique que l'on
    <b>donne une nom � la valeur</b>.
    <p>
    Dans un premier temps, faites comme si c'�tait la m�me chose
    car la plupart du temps c'est le cas.
    """,
    question = "Affectez la valeur <tt>3</tt> dans la variable <tt>a</tt>",
    tests = (
        Good(P(Equal("a=3"))),
        Expect('a', 'Je ne vois pas le nom de la variable.'),
        Expect('3', 'Je ne vois pas la valeur 3.'),
        Expect('=', "Je ne vois pas l'op�rateur d'affectation."),
        ),
    good_answer = """
    Vous pouvez maintenant tapez <tt>a=3</tt> dans l'interpr�teur Python.
    <p>
    Pour conna�tre la valeur de <tt>a</tt>, il suffit de taper <tt>a</tt>.
    <p>
    <b>N'oubliez pas de taper sur la touche � Entr�e � pour
    valider chaque ligne de commande et voir le r�sultat.</b>
    """
    )

add(name="multiplication",
    required = ["interpr�teur"],
    question = "Que tapez-vous pour calculer 5 multipli� par 3&nbsp;?",
    tests = (
        Good(P(Equal('5 * 3'))),
        Good(Comment(P(Equal('3 * 5')),
                     """Votre r�ponse est accept�e car la multiplication
                     est associative, mais toutes les op�rations
                     ne le sont pas.""")),
        Expect('3'),
        Expect('5'),
        Expect('*',
               "La multiplication est repr�sent�e par le symbole <tt>*</tt>"),
        ),
    good_answer = """Python sait manipuler de tr�s grands nombres.
    Essayez de faire une grande multiplication&nbsp;!
    <p>
    En langage C, les entiers "normaux" sont entre -2147483648
    et 2147483647 bornes incluses.
    """)

add(name="addition",
    required = ["interpr�teur"],
    question = "Que tapez-vous pour calculer 2 plus 1&nbsp;?",
    tests = (
        Good(P(Equal('2 + 1'))),
        Good(Comment(P(Equal('1 + 2')),
                     """Votre r�ponse est accept�e car l'addition
                     est associative, mais toutes les op�rations
                     ne le sont pas.""")),
        Expect('2'),
        Expect('1'),
        Expect('+',
               "L'addition est repr�sent�e par le symbole <tt>+</tt>"),
        ),
    good_answer = """On a le droit de mettre un <tt>+</tt> qui ne sert
    � rien devant les nombres positifs.
    <p>
    +5 c'est la m�me chose que 5
    """)


add(name="soustraction",
    required = ["interpr�teur"],
    question = "Que tapez-vous pour calculer 4 moins 7&nbsp;?",
    tests = (
        Good(P(Equal('4 - 7'))),
        Expect('4'),
        Expect('7'),
        Expect('-',
               "La soustraction est repr�sent�e par le symbole <tt>-</tt>"),
        ),
    good_answer = """La soustraction est un op�rateur binaire.
    Il travaille avec deux valeurs qu'il combine.""",
    )

add(name="oppos�",
    required = ["soustraction", "addition"],
    question = """Que tapez-vous pour <b>ajouter</b> 5
    � l'entier <b>moins</b> 8&nbsp;?""",
    tests = (
        Good(P(Equal('5 + -8'))),
        Good(P(Equal('-8 + 5'))),
        Bad(Comment(P(Equal('5 - 8')),
                    """Votre r�ponse est math�matiquement correcte mais
                    ce n'est pas ce que l'on vous demande""")),
        Expect('5'),
        Expect('8'),
        Expect('+'),
        Expect('-',
               "L'oppos� est repr�sent�e par le symbole <tt>-</tt>"),
        ),
    good_answer = """L'oppos� est un op�rateur unaire.
    Il travaille avec une seule valeur.""",
    )

add(name="oppos� 2",
    required = ["oppos�", "affectation"],
    question = """Que tapez-vous pour mettre l'oppos� de la variable
    <tt>m</tt> dans la variable <tt>p</tt>&nbsp;?""",
    tests = (
        Good(P(Equal('p = -m'))),
        Bad(Comment(P(Equal('m = -p')),
                    """Avec cette commande, vous stockez l'oppos� de
                    la variable <tt>p</tt> dans <tt>m</tt>""")),
        Expect('='),
        Expect('p'),
        Expect('m'),
        Expect('-'),
        ),
     good_answer = """Contrairement au langage C, on a le droit
     de faire l'oppos� de l'oppos�&nbsp;: <tt>--5</tt>
     est �gal � <tt>5</tt>""",
    )

add(name="parenth�ses",
    required = ["multiplication", "addition"],
    question = """Les parenth�ses s'utilisent naturellement.
    Donnez l'expression correspondant � la multiplication de :
    <ul>
    <li> 2 plus 4
    <li> et de 1 plus 6
    </ul>
    Si vous tapez la formule dans Python, il vous r�pondra <tt>42</tt>
    """,
    tests = (
        Good(P(Equal('(2+4)*(1+6)'))),
        Bad(Comment(P(Equal('2+4*1+6')),
                    """L'op�rateur <tt>*</tt> est plus prioritaire que
                    l'op�rateur <tt>+</tt> donc cela ne fait pas ce
                    qui est demand�.
                    <p>
                    Si vous aviez tap� cette formule dans l'interpr�teur
                    Python il aurait affich� <tt>12</tt> et non <tt>42</tt>"""
                    )),
        Expect('2'),
        Expect('4'),
        Expect('1'),
        Expect('6'),
        Expect('*'),
        Expect('+'),
        Bad(Comment(~Contain('(') | ~Contain(')'),
                """Les parenth�ses sont celles des math�matiques&nbsp;:
                <tt>(</tt> et <tt>)</tt>"""))
        ),
    good_answer = """Essayez de taper une formule avec une parenth�se
    fermante manquante dans l'interpr�teur Python.
    <p>
    Avez-vous remarqu� qu'il attend la
    fin de la commande � la ligne suivante&nbsp;?
    <p>
    Vous pouvez au choix finir la commande ou taper � Control - C �
    pour arr�ter la saisie de la commande.
    """
    )

add(name="flottant",
    required = ["interpr�teur"],
    before = """Un nombre flottant est une mani�re de repr�senter
    une approximation des nombres r�els dans les langages de programmation.
    <p>
    Comme tous les langages de programmation sont en anglais,
    la virgule est repr�sent�e par le caract�re <tt>point</tt>.
    """,
    question = """Comment �crivez-vous le nombre 5 virgule 2&nbsp;?""",
    tests = (
        Good(P(Equal('5.2'))),
        Expect('5'),
        Expect('2'),
        Expect('.', "La virgule est repr�sent�e par un <b>point</b> : �.�"),
    ),
    )

add(name="division",
    required = ["flottant"],
    question = """Que tapez-vous pour calculer le r�sultat de la
    division de 21 par 11&nbsp;?""",
    tests = (
        Good(P(Equal('21 / 11'))),
        Expect('21'),
        Expect('11'),
        Expect('/',
               "La division est repr�sent�e par le symbole <tt>/</tt>"),
        ),
    good_answer = """ATTENTION : quand vous faites la division de deux
    entiers le r�sultat est&nbsp:;
    <ul>
    <li> un nombre flottant si vous �tes en Python version 3
    <li> un entier pour les versions ant�rieures de Python.
    </ul>
    """,
    )


add(name="division enti�re",
    required = ["division", "oppos�"],
    before = """La division enti�re calcul�e par Python
    � son r�sultat arrondi � l'entier inf�rieur.
    Voici ce que cela donne pour quelques r�sultats de divisions.
    <table class="information_table">
    <tr><th>Division flottante<th>Division enti�re</tr>
    <tr><td>   -0.5           <td>    -1          </tr>
    <tr><td>    0.9           <td>     0          </tr>
    <tr><td>    1.4           <td>     1          </tr>
    <tr><td>    1.9           <td>     1          </tr>
    <tr><td>    2.1           <td>     2          </tr>
    </table>
    L'operateur Python pour calculer la division enti�re est <tt>//</tt>.
    """,
    question = """Que tapez-vous pour calculer le r�sultat de la
    division enti�re de 21 par 11&nbsp;?""",
    tests = (
        Good(P(Equal('21 // 11'))),
        Expect('21'),
        Expect('11'),
        Expect('//',
               "La division enti�re est repr�sent�e par <tt>//</tt>"),
        ),
    good_answer = """ATTENTION : la division enti�re de Python
    donne un r�sultat diff�rent de la division enti�re du langage C.
    <p>
    En langage C <tt>3/-2</tt> donne <tt>-1</tt>""",
    )

add(name="chaine",
    required = ["affectation"],
    before = """Il y a plusieurs mani�res d'�crire des chaines de caract�res
    en Python. Une des mani�res possible est de faire la m�me choses
    qu'en langage C&nbsp;: <b>mettre le texte entre guillemets</b>.""",
    question = """Mettre la chaine de caract�res <tt>D'accord</tt>
    dans la variable nomm�e � b �""",
    tests = (
        Good(P(Equal('b = "D\'accord"'))),
        Bad(Comment(P(Equal('b = "d\'accord"')),
                    "Ne confondez pas les minuscules et les majuscules")
            ),
        Expect("'", "Dans � D'accord � il y a une apostrophe (cote)"),
        Expect('"', 'Le guillemet est le caract�re �"�'),
        Expect("D'accord"),
        Expect('b'),
        Expect('='),
        ),
    good_answer = """Si vous devez mettre des guillemets dans une chaine
    de caract�re, il suffit de les pr�c�der d'un <em>backslash</em>.
    Par exemple&nbsp;:
    <p>
    <tt>b = "Tapez : \\"D'accord\\" !"
    <p>
    Les <em>backslash</em> ne sont pas stock�s dans la chaine.
    """,
    )

add(name="�galit�",
    required = ["chaine"],
    before = """Le test d'�galit� est le m�me en Python et en C.
    C'est un op�rateur binaire qui retourne une valeur bool�enne.""",
    question = """Qu'est-ce que l'interpr�teur Python affiche quand vous
    tapez <tt>5 == "5"<tt>&nbsp;?""",
    tests = (
        Good(Contain('False')),
        ),
    good_answer = """En langage Python, m�me si les variables ne sont
    pas d�clar�es, il tient compte du type et ne m�lange pas les choses
    qui ne vont pas ensemble.""",
    )

add(name="in�galit�",
    required = ["�galit�"],
    before = """Le test d'in�galit� est le m�me en Python et en C.
    C'est un op�rateur binaire qui retourne une valeur bool�enne.""",
    question = """Qu'est-ce que l'interpr�teur Python affiche quand vous
    tapez <tt>5 != "5"<tt>&nbsp;?""",
    tests = (
        Good(Contain('True')),
        ),
    good_answer = """Si deux choses ne sont pas �gales,
    il est logique qu'elles soient diff�rentes""",
    )


add(name="inf�rieur",
    required = ["in�galit�", "flottant"],
    before = "On suppose que les variables utilis�es existent",
    question = """Que tapez-vous pour savoir si le contenu de la
    variable <tt>a</tt> est plus petit que le contenu
    de la variable <tt>b</tt>&nbsp;?""",
    tests = (
        Good(P(Equal("a < b"))),
        Expect("<", "L'op�rateur inf�rieur est <tt>&lt;</tt>"),
        Expect('a'),
        Expect('b'),
        ),
    good_answer = """L'op�rateur <tt>&lt;</tt> est un op�rateur binaire.
    <p>
    Quand on demande � comparer des choses incomparables
    il retourne <tt>False</tt>.
    <table class="information_table">
    <tr><td>5 &lt; 6<td>True</tr>
    <tr><td>5.5 &lt; 6<td>True</tr>
    <tr><td>5.5 &lt; "6"<td>False</tr>
    </table>""",
    )

add(name="inf�rieur ou �gal",
    required = ["inf�rieur"],
    question = """Que tapez-vous pour savoir si le contenu de la variable
    � d � est plus petit ou �gale � <tt>2</tt>&nbsp;?""",
    tests = (
        Reject('< =', "Il ne doit pas y avoir d'espace entre le &lt; et le ="),
        Good(P(Equal("d <= 2"))),
        Expect("<=", "L'op�rateur inf�rieur est <tt>&lt;=</tt>"),
        Expect('d'),
        ),
    good_answer = """Bien s�r, les op�rateurs sup�rieur et sup�rieur
    ou �gal sont <tt>&gt;</tt> et <tt>&gt;=</tt>""",
    )

add(name="incr�menter",
    required = ["affectation", "addition"],
    question = """Que tapez-vous pour ajouter <tt>1</tt>
    � la variable <tt>a</tt>&nbsp;?""",
    tests = (
        Good(Comment(P(Equal("a = a + 1")),
                     """On peut �crire la m�me op�ration comme ceci&nbsp;
                     <tt>a += 1</tt>""")),
        Good(Comment(P(Equal("a = 1 + a")),
                     """Il est recommend� d'�crire
                     <tt>a = a + 1</tt>
                     car la tradition veut que l'on mettre les constantes
                     � droite des variables.
                     <p>
                     On peut �crire la m�me op�ration comme ceci&nbsp;
                     <tt>a += 1</tt>""")),
        Good(P(Equal("a += 1"))),
        
        Reject('++', "L'op�rateur <tt>++</tt> n'existe pas en Python"),
        Expect('='),
        Expect('+'),
        Expect('1'),
        Expect('a'),
        ),
    )