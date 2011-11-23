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
Quelques questions
"""

from questions import *
from check import *

add(name="liste",
    required = ["idem:chaine", "idem:flottant"],
    question = """D�finissez une liste contenant dans l'ordre les �l�ments :
               <TT>1, "a", 2, "b", 3.5</TT>""",
    tests = ( Good(P(Equal('[1,"a",2,"b",3.5]') ) ),
            ),
    good_answer = "�videmment, une liste peut contenir des listes",
 )

add(name="concatenation",
    required = ["liste", "table:concat�nation"],
    question = "Quel est l'op�rateur permettant de concat�ner 2 listes&nbsp;?",
    tests = ( Good(Equal("+")),
              ),
    good_answer = "Une nouvelle liste est cr��e par recopie des �l�ments.",
)

add(name="sous-liste",
    required = ["liste", "concatenation"],
    question = """Donner le r�sultat de l'expression
               <TT>[l[0]]+l[2:-2]+[l[-1]]</TT> appliqu�e � la liste
               <TT>l=[1,2,3,4,5,6]</TT>""",
    tests = ( Good(P(Equal("[1,3,4,6]"))),
              ) ,
    good_answer = """Effectivement,
   l'expression permet de retirer le deuxi�me et
   l'avant dernier �l�ment de toute liste <TT>l</TT> de longueur sup�rieure
   ou �gale � 3.""",
)

add(name="rotation gauche",
    required = ["liste", "concatenation", "sous-liste"],
    question = """Ecrire l'expression, qui, quelle que soit une liste nomm�e
    <tt>l</tt> <b>non vide</b>, retire le dernier �l�ment et l'ins�re
    en t�te""",
    tests = (
        Reject('[0:',
               """On n'�crit pas <tt>t[0:4]</tt> mais <tt>t[:4]</tt>
                  car c'est plus court."""),
        Good(P(Equal("[l[-1]]+l[:-1]")| Equal("[l[len(l)-1]]+l[:len(l)-1]"))),
        Bad(Comment(
                P(Equal("l[-1]+l[:-1]")| Equal("l[len(l)-1]+l[:len(l)-1]")),
                """Vous ajoutez un �l�ment � une liste alors que vous
                 devez ajouter deux listes""")
            ),
        ),
    good_answer = """On peut bien s�r faire une fonction,
                     mais dans ce cas, attention � la liste vide.""",
   )
    
