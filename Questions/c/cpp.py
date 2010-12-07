# -*- coding: latin-1 -*-
#    QUENLIG: Questionnaire en ligne (Online interactive tutorial)
#    Copyright (C) 2007 Thierry EXCOFFIER, Universite Claude Bernard
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

from questions import *

add(name="include",
    required=["main:puts"],
    before = """Le pr�processeur C est un programme qui transforme
    le texte des programmes C (ou d'autres langages).
    <p>
    La directive <tt>#include</tt> indique au pr�pocesseur C
    remplacer la ligne par le contenu du fichier nomm�.
    <p>
    Inserrez la ligne <tt>#include &lt;stdio.h&gt;</tt> au
    d�but du fichier <tt>mon-programme.c</tt>""",
    question = """L'ex�cution de <tt>make</tt> doit normalement
    se passer <em>sans erreurs</em> car maintenant le prototype
    de <tt>puts</tt> est d�fini (vous pouvez le trouver
    dans <tt>/usr/include/stdio.h</tt>).
    <p>
    Combien de lignes sont affich�es&nbsp;?""",
    tests = ( Good(Comment(Int(5),
                           "Votre programme vous a dit bonjour&nbsp;!")),
              Comment("""Cherchez le probl�me, normalement
              ce qui s'affiche est&nbsp;:
<pre>D�but compilation � Sat Nov 24 21:43:23 CET 2007
gcc -Wall -g  -Werror    mon-programme.c  -lm -o mon-programme
mon-programme arg1 arg2 arg3
Bonjour
Fin compilation � Sat Nov 24 21:43:27 CET 2007</pre>"""),
              ),
    )
