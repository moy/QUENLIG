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
Tout sur les chaines de caract�res
"""

from questions import *
from check import *

add(name="conversion",
    required = ["table:chaine", "idem:flottant", "idem:chaine",
                "idem:affectation"],
    before = """En Python on ajoute pas des choux et des carottes.
    Il faut que ce que l'on ajoute soit un minimum compatible,
    par exemple un entier et un nombre flottant.
    On ne peut pas ajouter une chaine de caract�res et un nombre.
    <p>
    Pour convertir quelque chose en une chaine de caract�res,
    il suffit d'utiliser la fonction <tt>str</tt> retourne une chaine
    de caract�res calcul�e � partir de son unique param�tre
    (qui n'est pas modifi�).""",
    question="""Stockez dans la variable <tt>a</tt> l'entier d�sign�
    par la variable <tt>b</tt> entre parenth�ses.
    <p>
    Si <tt>b=76</tt> alors <tt>a</tt> contiendra <tt>(76)</tt>""",

    tests = (
        Good(P(Equal('a="("+str(b)+")"'))),
        Bad(Comment(P(Equal('a=(b)')),
                    """Ici les parenth�ses n'ont aucun effet,
                    c'est comme si vous aviez �crit <tt>a=b</tt>""")),
        Bad(Comment(P(Equal('a="("+b+")"')),
                    """Python ne va pas vouloir ajouter une chaine
                    de caract�re et un entier.""")),
        Expect("str", """Vous devez utiliser la fonction <tt>str</tt>
        pour traduire <tt>b</tt> en chaine de caract�res"""),
        Expect('+', """Vous avez besoin de concat�ner les chaines de
        caract�re contenant <tt>(</tt>, la valeur de <tt>b</tt> en chaine
        de caract�re ainsi que <tt>)</tt>.
        Pour concat�ner les chaines vous avez besoin de l'op�rateur <tt>+</tt>.
        """),
        Bad(Comment(~NumberOfIs('"',4),
                    """Vous avez besoin d'indiquer une chaine de caract�res
                    contenant <tt>(</tt> et une contenant <tt>)</tt>
                    vous avez donc besoin d'�crire 4 guillemets.""")),
        expects(("a", "=", "b", "(", ")", '"("', '")"')),
        ),

    good_answer = """Bien �videmment, si vous passez une chaine
    de caract�res en param�tre de la fonction <tt>str</tt> cette
    chaine sera retourn�e inchang�e.""",
    )

add(name="strip",
    required = ["idem:chaine", "structure:attributs"],
    before = """Toutes les chaines de caract�res ont un attribut
    nomm� <tt>strip</tt> qui est une fonction qui retourne la m�me
    chaine de caract�re mais en sans les espaces qui sont au d�but
    et � la fin de la chaine.
    <p>
    Si <tt>a</tt> contient <tt>" x "</tt> alors <tt>a.strip()</tt> est
    la chaine de caract�re <tt>"x"</tt>.
    <p>
    <tt>" a  b  c    ".strip()</tt> retourne <tt>"a  b  c"</tt>
    en laissant les espaces � l'int�rieur.
    """,
    question = """Si <tt>a</tt> est une chaine de caract�re quelconque,
    quelle est la valeur de l'expression suivante&nbsp;:
    <tt>a.strip() == a.strip().strip()</tt>""",
    tests = (
        Good(Equal("True")),
        Bad(Comment(UpperCase(Equal("True")),
                    """Attention les minuscules et les majuscules sont
                    diff�rentes.""")),
        ),
    good_answer = """La fonction <tt>strip</tt> est fondamentale d�s que
    l'on pose des questions � un utilisateur.
    Il a en effet toujours la tendance � mettre des espaces en trop en d�but
    et fin de saisie""",
    )
