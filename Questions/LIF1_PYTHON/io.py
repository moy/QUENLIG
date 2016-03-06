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
Les entr�es/sorties en Python
"""

from QUENLIG.questions import *
from .check import *

add(name="print",
    required = ["idem:chaine", "idem:multiplication"],
    before = """La fonction <tt>print</tt> en Python affiche sur l'�cran
    ses param�tres&nbsp;:""" + python_html("""
    >>> a = 6
    >>> print("a=", a, "!")
    a= 6 !
    >>> """) + """
    <p>ATTENTION, il ne faut pas mettre les parenth�ses quand on utilise
    Python version 2.
    <p>
    Les r�ponses attendues par ce logiciel
    doivent utiliser les parenth�ses.""",
    question="""Par quoi faut-il remplacer <tt>VOTRE COMMANDE</tt>
    pour que le bout de programme qui suit affiche le bon r�sultat
    quelque soit les valeurs des variables <tt>a</tt> et <tt>b</tt>&nbsp;?
    """ + python_html("""
    >>> a = 6
    >>> b = 7
    >>> VOTRE COMMANDE
    6 * 7 = 42
    >>>"""),

    tests = (
        Good(P(Equal('print(a, "*", b, "=", a*b)'))),
        Expect('print', """Pour faire afficher quelque chose sur l'�cran
        on utilise la fonction <tt>print</tt>"""),        
        Bad(Comment(Contain('6') | Contain('7') | Contain('42'),
                    """On veut que votre r�ponse fonctionne quelque soit les
                    valeurs contenues dans <tt>a</tt> et </tt>b</tt>.
                    Vous ne pouvez donc pas avoir de valeurs num�riques
                    dans votre r�ponse""")),
        Bad(Comment(~Contain('a') | ~Contain('b'),
                    """Votre r�ponse doit utiliser les variables <tt>a</tt>
                    et <tt>b</tt>.
                    Sinon, comment manipule-t-elle leurs valeurs&nbsp;?""")),
        Expect('('),
        Expect(')'),
        Expect(',', """On utilise la virgule pour s�parer les param�tres
        pass�s � la fonction"""),
        Bad(Comment(~NumberOfIs(',', 4),
                    """Vous devez appeler la fonction <tt>print</tt>
                    avec 5 param�tres&nbsp;:
                    <ul>
                    <li> La variable <tt>a</tt>
                    <li> La chaine contenant l'�toile
                    <li> La variable <tt>b</tt>
                    <li> La chaine contenant le �gal
                    <li> La formule donnant le r�sultat
                    </ul>
                    Il doit donc y avoir 4 � , � dans votre r�ponse.
                    """)),
        Bad(Comment(~NumberOfIs('"', 4),
                    """Vous devez afficher 2 chaines de caract�res,
                    La premi�re contient � * � et la deuxi�me � = �""")),
        Bad(Comment(~NumberOfIs('*', 2),
                    """Il doit y avoir deux fois le caract�re � * � dans
                    votre r�ponse, la premi�re fois pour l'afficher
                    et la deuxi�me fois pour faire la multiplication""")),
                
        ),

    good_answer = """ATTENTION, par d�faut un espace est automatiquement
    ajout� entre chacun des param�tres affich�.
    <tt>print("a", "b")</tt> affiche <tt>a b</tt> avec un espace entre les deux
    """,
    )

add(name="lire ligne",
    required = ["control:def", "chaine:strip", "module:math", "print",
                "structure:attributs", "idem:commentaire"],
    before = """Le module nomm� <tt>sys</tt> contient un attribut nomm�
    <tt>stdin</tt> qui repr�sente le clavier.
    <p>
    Et <tt>stdin</tt> lui m�me contient un attribut nomm� <tt>readline</tt>
    qui est une fonction qui retourne une ligne saisie au clavier.
    """ + python_html(
        """
        import sys
        a = sys.stdin.readline() # Lit une ligne et la stocke dans 'a'
        """),
    question = """D�finissez la fonction <tt>lire_ligne</tt>
    sans param�tres qui retourne une ligne saisie au clavier en enlevant les
    caract�res inutiles en d�but et fin.
    <p>
    Vous n'avez pas besoin d'utiliser de variables ou d'affectation.
    <p>
    Ce n'est pas la peine d'indiquer le <tt>import sys</tt>
    """,
    nr_lines = 3,
    tests = (
        Reject("=",
               "Vous ne devez pas utiliser l'affectation pour cette fonction"),
        Good(P_AST(Equal("""
def lire_ligne():
    return sys.stdin.readline().strip()
"""))),
        expects(('def', 'lire_ligne', ':', 'return', 'sys', 'stdin',
                 'readline', 'strip', '.')),
        Bad(Comment(~NumberOfIs('(',3) | ~NumberOfIs(')',3),
                    """Dans votre r�ponse il y a un appel � la fonction
                    <tt>readline</tt>, un appel � <tt>strip</tt> et la
                    d�claration des param�tres de <tt>lire_ligne</tt>.
                    Il doit donc y avoir 3 fois <tt>()</tt> dans votre r�ponse.
                    """)),
        Bad(Comment(~NumberOfIs('.',3),
                    """Dans <tt>sys.stdin.readline</tt> il y a deux fois
                    le caract�re '<tt>.</tt>', de plus vous avez besoin
                    de l'attribut <tt>strip</tt> de la chaine de caract�res
                    retourn�e par la fonction <tt>readline</tt>.
                    Il doit donc y avoir 3 '<tt>.</tt>' dans votre
                    r�ponse""")),
        ),
    good_answer = """En Python, une fonction est aussi une valeur&nbsp;!
    Vous pouvez donc �crire&nbsp;:""" + python_html("""
    import sys
    lit_ligne = sys.stdin.readline  # 'lit_ligne' est identique � 'sys.stdin.readline'
    a = lit_ligne()                 # Lit une ligne et la stocke dans 'a'"""),
    )

    
        
