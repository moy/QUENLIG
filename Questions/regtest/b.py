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
#

from QUENLIG.questions import *

add(name="A",
    required=["a:a", "a:b(B)"],
    question="a",
    tests=(good("A"),),
    )

add(name="B",
    required=["a:a", "a:b([bB])"],
    question="a",
    tests=(good("A"),),
    )

add(name="C",
    required=["a:c", "a:b"],
    question="a",
    tests=(good("A"),),
    )

add(name="choice",
    required=["a:a", "a:b"],
    question="""Choice :
    {{{a}}} A
    {{{b}}} B
    {{{c}}} C""",
    maximum_bad_answer = 3,
    tests=(good('a'),),
    )

choices = Choice(*[ ("Question %d" % i, Good(Equal("%d" % i)))
                   for i in range(100)
])
add(name="z",
    required=["a:a(unlockCHOICES)"],
    question = choices,
    tests = ( choices, ),
    )

