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
    required=["sh:console"],
    question="""Quel est le nom de la commande permettant
    de faire dispara�tre (d�truire) les fichiers&nbsp;?""",
    tests=(
    good("rm"),
    bad("kill", "C'est pour envoyer un signal � une processus"),
    bad("rmdir", "C'est pour d�truire un r�pertoire vide, pas des fichiers"),
    ),
    indices=("En anglais cela vient du mot <em>remove</em>",
             """Elle est dans la liste affich�e par :
             <tt>man -k 'remove.*file'</tt>""",
             ),
    )

add(name="simple",
    question="""Quelle commande permet de d�truire les
    deux fichiers nomm�s :
    <ul>
    <li><tt>a</tt> (donc dans le r�pertoire courant)
    <li><tt>/tmp/a</tt>
    </ul>""",
    tests=(
    shell_good("rm a /tmp/a"),
    shell_good("rm /tmp/a a", "Pourquoi avez-vous chang� l'ordre&nbsp;?"),
    reject('-', "On a pas besoin d'options"),
    shell_require("<argument>a</argument>",
                  "On veut d�truire <tt>a</tt> dans le r�pertoire courant."),
    shell_require("<argument>/tmp/a</argument>",
                  "On veut d�truire <tt>a</tt> dans le r�pertoire <tt>/tmp</tt>"),
    shell_require("<argument>rm</argument>",
                  "On utilise la commande <tt>rm</tt>"),
    reject((";","|","&"), "On veut lancer qu'une seule commande"),
    reject("~/a",
           "<tt>a</tt> dans le r�pertoire courant, pas celui de connexion"),
    reject("./a",
           """Il y a plus court que <tt>./a</tt> pour indiquer <tt>a</tt>
           dans le r�pertoire courant"""),
    shell_display,
    ),
    )
    

add(name="probl�mes",
    required=["simple", "sh:affiche �toile", "lister:sp�cial"],
    question="""Quelle commande permet de d�truire les
    fichiers (pas r�pertoire) nomm�s <tt>*</tt> et <tt>-z</tt>""",
    tests=(
    shell_good("rm '*' -z"),
    shell_good("rm '*' ./-z",
               """Le <tt>./</tt> devant <tt>z</tt>
               est inutile car on consid�re qu'il n'y a plus d'options
               apr�s la premi�re chose qui n'est pas une option (<tt>*</tt>
               dans cet exemple)"""),
    shell_good("rm ./-z '*'",
               "La r�ponse attendue �tait <tt>rm '*' -z</tt>"),
    expect('rm'),
    number_of_is('rm', 1, "On lance la commande une seule fois."),
    shell_reject("<argument>./*</argument>",
                 "Le <tt>./</tt> devant l'�toile ne sert � rien"),
    shell_reject("<pattern_char>*</pattern_char>",
                 "Il faut prot�ger l'�toile car <tt>rm</tt> doit la voir"),
    reject((" ./* ", " * "),
           "Cela d�truit tous les fichiers du r�pertoire&nbsp;!"),
    shell_require("<argument>*</argument>",
                   """La commande <tt>rm</tt> ne voit pas l'�toile"""),
    reject(" -- ",
           """C'est bien d'avoir trouv� l'astuce du <tt>--</tt>
           mais elle n'est pas portable..."""),
    require("-z", "Il faut d�truire <tt>-z</tt>"),
    shell_display,
    ),
    )
    

add(name="pattern",
    required=["simple", "pattern:final"],
    question="""Donnez la ligne de commande permettant de d�truire
    tous les fichiers dont le nom se termine par <tt>.o</tt>
    dans le r�pertoire courant""",
    tests=(
    shell_good("rm *.o"),
    shell_bad("rm '*.o'",
              """Comme vous avez prot�g� le <em>pattern</em> la commande
              essaye de d�truire un fichier dont le nom est vraiment
              <tt>*.o</tt>"""),
    expect(".o"),
    reject("./*.o", """On peut faire un <em>pattern</em> plus court."""),
    reject('-f',
           """L'option <tt>f</tt> de <tt>rm</tt> est dangereuse.
           Il faut l'utiliser en connaissance de cause."""),
    reject('-', "On a besoin d'aucune option pour r�pondre."),
    reject('/', """Le caract�re <tt>/</tt> indique que l'on
    indique une nom dans un autre r�pertoire, hors les fichiers � d�truire
    sont dans le r�pertoire courant, ce n'est donc pas la peine"""),
    answer_length_is(6, "La r�ponse � cette question est en 6 caract�res"),
    expect('rm'),
    shell_display,
    ),
    )

dumb_replace=(("-R","-r"),("-type f", ""))

import chercher

add(name="pattern arbre",
    required=["simple", "sh:remplacement", "chercher:pattern", "chercher:ex�cuter"],
    question="""Donnez la ligne de commande permettant de d�truire
    tous les fichiers texte dont le nom se termine par <tt>.o</tt>
    dans le r�pertoire courant et toute la hi�rarchie de r�pertoires
    au dessous.""",
    tests=(
    reject('-delete',
           """On vous demande de r�pondre � cette question sans l'option
           <tt>-delete</tt>, en effet le but est d'apprendre � assembler
           des fonctionnalit�s ensemble et non d'apprendre plein
           d'options."""),
    require('rm', "On d�truit les fichiers avec <tt>rm</tt>"),
    require('find',
            "On cherche les fichiers dans la hi�rarchie avec <tt>find</tt>"),
    reject('~', "Pourquoi y-a-t-il un tilde dans votre r�ponse&nbsp;?"),
    reject('|', "On ne veut pas faire de <em>pipe</em>"),
    shell_good("find . -name '*.o' -exec rm {} \;",
               dumb_replace=dumb_replace),
    shell_good( ( "rm $(find . -name '*.o')",
                  "find . -name '*.o' | xargs rm" ),
                """Cette commande est dangereuse dans le cas ou les noms de
                fichiers contiennent des espaces ou des retours � la ligne
                car le shell consid�re que ce sont des s�parateurs""",
                dumb_replace=dumb_replace
                ),
    shell_bad("rm -r '*.o'",
              """La commande <tt>rm</tt> va d�truire r�cursivement
              l'unique fichier nomm� <tt>*.o</tt> qu'il soit un fichier
              ou un r�pertoire.""",
              dumb_replace=dumb_replace,
              ),
    shell_bad("rm -r *.o",
              """Le shell remplace le <tt>*.o</tt> par tous les
              fichiers qui correspondent dans le r�pertoire courant.
              Ensuite <tt>rm</tt> les d�truit r�sursivement.
              Du coup, un r�pertoire nomm� <tt>toto.o</tt> voit
              son contenu d�truit m�me s'il ne se termine pas par <tt>.o</tt>,
              Et le fichier <tt>toto/x.o</tt> n'est pas d�truit.""",
              dumb_replace=dumb_replace,
              ),
    shell_bad("rm *.o",
              """D�truit les fichiers du r�pertoires courant,
              pas des sous r�pertoires.
              Il faut utiliser la commande <tt>find</tt>"""),
    require('*.o',
            """O� est le <em>pattern</em> indiquant que le nom
            du fichier se termine par <tt>.o</tt>&nbsp;?"""),
    shell_require("<argument>*.o</argument>",
                  """<tt>find</tt> ne voit pas le <em>pattern</em>
                  car le shell l'a peut-�tre substitu�."""),
    require("find","Il faut utiliser <tt>find</tt> pour trouver les fichiers"),
    reject(("-R", "-r"), "Pourquoi d�truire r�cursivement&nbsp;?"),
    require('-exec',
            "Il faut utiliser l'option <tt>exec</tt> de <tt>find</tt>"),
    require('{}',
            "Il faut indiquer � <tt>rm</tt> le nom du fichier � d�truire"),
    reject('iname',
           "On ne veut pas d�truire les <tt>.O</tt> en majuscule&nbsp;!"),
    reject('./', """La mani�re la plus courte d'indiquer le r�pertoire courant
    c'est <tt>.</tt>, pas <tt>./</tt>"""),
    expect('\\;'),
    reject('(', "Pas besoin de parenth�sage dans cette exercice."),
    chercher.find_dot_required,
    shell_display,
    ),
    indices=("Il faut utiliser <tt>find</tt> pour trouver les fichiers",
             ),
    )



    

    
