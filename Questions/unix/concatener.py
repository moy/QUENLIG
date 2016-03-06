# -*- coding: latin-1 -*-
#    QUENLIG: Questionnaire en ligne (Online interactive tutorial)
#    Copyright (C) 2005-2011 Thierry EXCOFFIER, Universite Claude Bernard
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
    required=["sh:console"],
    question="""Quelle est la commande permettant d'�crire sur
    la sortie standard le contenu d'un ou plusieurs fichiers&nbsp;?""",
    tests=(
    good("cat"),
    bad((">", ">>"),
        """Ce n'est pas une commande mais un indicateur permettant
        de rediriger la sortie d'une commande dans un fichier"""),
    bad("<",
        """Ce n'est pas une commande mais un indicateur permettant
        de changer l'entr�e standard d'une commande"""),
    reject(("echo", "vi", "ls"),
           "Cette commande ne lit pas le contenu des fichiers"),
    bad('more', "Cela affiche page par page le contenu et c'est interactif"),
    ),
    indices = (
    """Le nom de la commande est cach� dans <em>concatenate</em>""",
    ),
    )

cat_required = require("cat", "On utilise <tt>cat</tt> pour concat�ner")

cat_files_required = require(("/etc/passwd", "/etc/group"),
                             "Il faut indiquer les noms des fichiers !")

cat_once_indices = "Il ne faut appeler <tt>cat</tt> qu'une fois"

add(name="concatener",
    question="""Donner la ligne de commande permettant d'�crire
    le contenu de <tt>/etc/passwd</tt> et <tt>/etc/group</tt>
    sur l'�cran&nbsp;?""",
    tests=(
    shell_good("cat /etc/passwd /etc/group"),
    cat_required,
    shell_bad('cat /etc/{passwd,group}',
              """Cette r�ponse est correcte avec le shell <tt>bash</tt> mais
              ce n'est pas standard."""),
    cat_files_required,
    number_of_is('cat',1,"On n'utilise <tt>cat</tt> qu'une seule fois"),
    reject(">",
           """La concat�nation s'affiche sur l'�cran,
           pas dans un autre fichier"""),
    reject('<', """Pas besoin de changer l'entr�e standard,
    il suffit de dire � <tt>cat</tt> quels sont les fichiers � afficher"""),
    shell_display,
    ),
    indices=(cat_once_indices,
             ),
    )


add(name="concat C",
    required = ["concatener", "chercher:ex�cuter"],
    question="""Donner la commande affichant sur la sortie standard
    le contenu de chacun des fichiers dont le nom se termine
    par <tt>.c</tt> � partir du r�pertoire courant.
    <p>
    Elle n'a pas besoin de v�rifier que c'est bien un fichier.
    """,
    tests = (
        Expect('cat'),
        Expect('find'),
        Expect('-name'),
        Expect('*.c'),
        Reject("-print", """Le '-print' est l'action pas d�faut,
        ce n'est pas la peine de l'indiquer"""),
        Reject(" ./ ", "Cela ne sert � rien de mettre un / apr�s le point"),
        Expect(' . ', "Vous n'avez pas indiqu� le r�pertoire courant"),
        Bad(Comment(~(Contain('"*.c"') | Contain("'*.c'") | Contain("\\*.c")),
                    "Auriez-vous oubli� de prot�ger l'�toile ?")),
        Good(Comment(Shell(Equal('cat $(find . -name "*.c")')),
                     """Votre commande ne fonctionne pas si des noms de
                     fichiers contiennent des espaces.""")),
        Good(Comment(Shell(Equal('find . -name "*.c" | xargs cat')),
                     """Votre commande ne fonctionne pas si des noms de
                     fichiers contiennent des retours � la ligne.
                     Il faut utiliser les options <tt>-print0</tt>
                     de <tt>find</tt> et <tt>-0</tt> de <tt>xargs</tt>""")),
        Good(Comment(Shell(Equal('find . -name "*.c" -exec cat {} \\;')),
                     """Votre commande est lente car elle relance
                     trop souvent la commande <tt>cat</tt>.
                     Il faut utiliser <tt>xargs</tt>""")),
        Good(Shell(Equal('find . -name "*.c" -print0 | xargs -0 cat'))),
        ),
    )


add(name="concatener dans",
    required=["concatener", "sh:redirection sortie"],
    question="""Donner la ligne de commande permettant d'�crire
    le contenu de <tt>/etc/passwd</tt> et <tt>/etc/group</tt>
    dans le fichier <tt>xxx</tt> du r�pertoire courant
    (en le vidant ou cr�ant).""",
    tests=(
    shell_good("cat /etc/passwd /etc/group >xxx"),
    cat_required,
    number_of_is('cat',1,"On n'utilise <tt>cat</tt> qu'une seule fois"),
    cat_files_required,
    reject("./xxx", """Le <tt>./</tt> devant <tt>xxx</tt> est inutile"""),
    reject(">>",
           """Vous devez cr�er <tt>xxx</tt> en une seule fois.
           Donc pas besoin d'ajouter � la fin"""),
    reject("<", """On redirige la sortie, pas l'entr�e"""),
    require("xxx", "Vous devez stocker le r�sultat dans <tt>xxx</tt>"),
    reject('echo', """La commande <tt>cat</tt> affiche,
    pourquoi utiliser <tt>echo</tt>&nbsp;?"""),
    reject('(', """Pas besoin de regroupement de commande,
    vous ne lancez qu'une seule commande"""),
    require('>', "Je ne vois pas la redirection de la sortie standard..."),
    shell_display,
    ),
    indices=(cat_once_indices,
             ),
    )




    
