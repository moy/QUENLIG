# -*- coding: latin-1 -*-
#    QUENLIG: Questionnaire en ligne (Online interactive tutorial)
#    Copyright (C) 2011 Thierry EXCOFFIER, Universite Claude Bernard
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
from .check import *

add(name="intro",
    required=["trier:unique", "manuel:chercher"],
    before="""La commande <tt>tr</tt> permet de remplacer un caract�re
    par un autre dans un flux de donn�es.
    Par exemple :
    <ul>
    <li> <tt>tr "a-z" "A-Z"</tt> transforme les minuscules en majuscules
    <li> <tt>tr "XT0-9" "01XXXXXXXXXXX"</tt> transforme X en 0, T en 1 et les chiffres en X
    </ul>
""",
    question="""Quel est le filtre qui � partir d'un texte fourni sur
    l'entr�e standard cr�e la liste des mots utilis�s dans le texte.
    <table>
    <tr><th>Entr�e<th>Sortie attendue</tr>
    <tr><td><pre>Ceci est un texte court,
tr�s court.</pre><td><pre>ceci
court
est
texte
tr�s
un</pre></tr></table>
    La commande <tt>tr</tt> remplacera <b>dans l'ordre indiqu�</b>&nbsp;:
    <ul>
    <li> Les majuscules par des minuscules.
    <li> Les caract�res �,�, �.�, � � par un retour � la ligne
    </ul>

    """,
    nr_lines = 7,
    tests = (
        Reject('text', """Le texte � Ceci est un texte court, tr�s court. �
               ne fait pas parti de votre r�ponse, c'�tait un exemple."""),
        Reject('tr -',
               "Pas besoin d'indiquer d'option � la commande <tt>tr</tt>"),
        Reject('[', "Il ne faut pas indiquer les crochets !"),
        Expect('sort', """On veut la liste des mots utilis�s, il faut donc
        trier la liste"""),
        Expect('tr'),
        Expect('|',
               """Il faut combiner la commande <tt>tr</tt>
               et la commande <tt>sort</tt> dans un pipeline"""),
        Expect('-u', """Utilisez l'option de <tt>sort</tt> pour ne lister
        chaque mot qu'une seule fois."""),
        Expect('a-z'),
        Expect('A-Z'),
        Bad(Comment(~ NumberOfIs('tr', 1),
                      """Vous ne devez lancer la commande <tt>tr</tt> qu'une
                      seule fois.""")),
        Good(Shell(Equal('tr "A-Z,. " "a-z\n\n\n" | sort -u')
                   | Equal('tr "A-Z,. " "a-z\\n\\n\\n" | sort -u')
                   | Equal('tr "A-Z,. " "a-z\\012\\012\\012" | sort -u'))),
        Good(Comment(Shell(Equal('tr "A-Z,. " "a-z\n" | sort -u')
                           | Equal('tr "A-Z,. " "a-z\\n" | sort -u')
                           | Equal('tr "A-Z,. " "a-z\\012" | sort -u')),
                     """Ceci fonctionne, mais il est conseill� de mettre le
                     m�me nombre de caract�res dans les deux param�tres""")),
        shell_display,
        ),
    )
