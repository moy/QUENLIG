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

from questions import *
from check import *

add(name="print",
    required = ["idem:chaine", "idem:multiplication"],
    before = """La fonction <tt>print</tt> en Python affiche sur l'�cran
    ses param�tres&nbsp;:""" + python_html("""
    >>> a = 6
    >>> print("a=", a, "!")
    a= 6 !
    >>> """),
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
