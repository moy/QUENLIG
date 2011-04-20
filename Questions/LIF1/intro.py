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
"""

from questions import *

add(name="intro",
    before="""Tout d'abord, ce tutoriel s'adresse aux d�butants.
Si vous avez d�j� un peu programm� dans un autre langage que le langage C,
il pourra certe vous aider � assimiler plus rapidement la syntaxe de ce
langage mais vous risquez de vous ennuyer un peu.
<p>
Ce  tutoriel doit �tre utilis� comme le compl�ment d'un cours de C.
Il a �t� pens� pour vous aider � assimiler la syntaxe de ce langage
et vous donner de bonnes habitudes de programmation.
<p>
ATTENTION : la casse compte ! Donc attention aux minuscules et majuscules.
""",
    question="""Allez, on commence!
<p>
Avez-vous lu la totalit� des informations contenues dans cette page web&nbsp;?
R�pondez par <tt>oui</tt> ou <tt>non</tt> dans le cadre intitul�
<tt><em>Donnez votre r�ponse ici</em></tt>.""",

    tests = (
        Good(Yes()),
        ),
    )

