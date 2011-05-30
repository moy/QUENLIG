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

from questions import *
from check import *

add(name="intro",
    before='''La suite de commandes qui vous est propos�e liste
    la hi�rarchie de fichier du r�pertoire courant dans
    un fichier temporaire, puis elle affiche les lignes
    du fichier temporaire contenant ' -> '.''',
    required=["sh:console", "cribler:simple", "intro:pipe"],
    question="""R��crire la suite de commandes suivante
    en utilisant un pipeline
    <pre>ls -lR >/tmp/xxx
grep ' -&gt; ' &lt;/tmp/xxx</pre>""",
    tests=(
    shell_good("ls -lR | grep ' -> '"),
    shell_bad("grep ' -> ' | ls -lR",
              """Les donn�es vont de gauche � droite.
              C'est la commande <tt>ls</tt> qui g�n�re les donn�es
              et le <tt>grep</tt> qui les traite."""),
    reject('xxx',
           '''Comme on utilise un pipeline, on a plus
           besoin du fichier temporaire'''),
    require(('ls', '-lR', "' -> '", "grep"),
            '''Il faut recopier exactement les diff�rents
            morceaux de la commande propos�e'''),
    require('|', "O� est le symbole du pipe&nbsp;?"),
    shell_display,
    ),
    good_answer="""Cette commande est fausse car elle peut trouver
    des fichiers qui ne sont pas des liens symboliques.
    La bonne commande est plut�t&nbsp;:
    <pre>find . -type l</pre>"""
    )

import chercher
import remplacer

add(name="extensions",
    required=["intro", "chercher:pattern", "remplacer:intro",
              "trier:unique", "expreg:sp�cial", "remplacer:enl�ve sans point"],
    question="""Donnez le pipeline permettant d'afficher la liste
    des extensions que vous utilisez dans votre r�pertoire de connexion
    et tous ses sous r�pertoires.
    <ul>
    <li> Il faut d'abord lister les fichiers et r�pertoires
    qui ont une extension dans votre hi�rarchie.
    <li> Dans cette liste, ont enl�ve tout ce qui est � gauche du <tt>.</tt>
    (le caract�re <tt>.</tt> aussi)
    <li> On utilise la commande <tt>sort</tt> pour trier
    et n'afficher qu'une seule fois chaque extension.
    </ul>
    """,
    tests=(
    reject("^", """Le '^' est inutile car le <tt>.*</tt> va prendre
    la plus longue chaine"""),
    reject('-r', "L'option <tt>-r</tt> n'est pas utile"),
    expect('find'),
    expect('sed'),
    expect('sort'),
    expect('-name'),
    reject('-iname',
           """Pas besoin de <tt>iname</tt> il n'y a pas de lettres � trouver,
           donc pas de diff�rences minuscules/majuscules"""),
    
    reject( ('(', ')'), "On a pas besoin des parenth�ses pour r�pondre"),
    require('~', "Je ne vois pas le r�pertoire de connexion"),
    reject('~/', "Mettez <tt>~</tt> au lieu de <tt>~/</tt> s'il vous plais"),
    
    shell_good(("find ~ -name '*.*' | sed 's/.*\\.//' | sort -u",
                "find ~ -name '[!.]*.*' | sed 's/.*\\.//' | sort -u",
                ),
               dumb_replace = list(chercher.dumb_replace) \
               + list(remplacer.dumb_replace)),
    shell_require('<argument>*.*</argument>',
                  """Il faut prot�ger les <em>patterns</em>
                  sinon <tt>find</tt> risque de chercher
                  le mauvais nom...
                  Par exemple, s'il y a <tt>toto.c</tt>
                  dans le r�pertoire courant, il va
                  le chercher dans toute la hi�rarchie.
                  """),
    reject("/g",
           "L'option <tt>g</tt> est inutile car il n'y a qu'une substitution"),
    number_of_is('/', 3, """Quand on fait une substitution avec
    la commande <tt>sed</tt> il doit y avoir 3 <em>slash</em>
    sinon il y a une erreur de syntaxe"""),
    
    shell_display,
    ),
    indices=("""Pour lister les fichiers avec extension il faut
    utiliser la commande <tt>find</tt>""",
             """Pour enlever ce qui est � gauche de l'extension
             on utilise <tt>sed</tt>""",
             ),
    )
    
