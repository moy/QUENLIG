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

cut_required = require("cut",
                       """Comme vous le savez d�j� la commande pour
                       extraire des colonnes d'un fichier est <tt>cut</tt>""")

ordre = """Il est plus logique d'indiquer le s�parateur avant
de sp�cifier la colonne que l'on veut"""

add(name="extraire",
    required=["manuel:chercher"],
    before="""De nombreux fichiers ou r�sultats de commandes
    sont organis�s sous la forme d'un tableau de donn�e avec
    une ligne par donn�e et des champs d�limit�s par un
    s�parateur.
    <p>
    Par exemple le fichier  <tt>/etc/passwd</tt>
    """,
    question="""Quel est le nom de la commande permettant
    d'extraire une colonne (ou plusieurs) d'un fichier&nbsp;?""",
    tests=(
    bad("awk",
        """Cette commande permet de le faire, mais cela n�cessite
        l'�criture d'un programme."""),
    bad("colrm",
        """Cette commande ne comprend pas la notion de champs et de
        d�limiteurs. Elle travaille seulement avec des caract�res."""),
    bad("column", "Cette commande recr�e un tableau � partir de colonnes"),
    good("cut"),
    ),
    indices=("C'est le verbe 'couper' en anglais",
             "C'est en trois lettres",
             "C'est le mot employ� dans l'expression 'couper/coller'",
             ),
    )

add(name="les shells",
    required=["extraire", "manuel:section commande"],
    question="""Commande permettant d'extraire du fichier
    <tt>/etc/passwd</tt> seulement
    la colonne contenant le nom du programme (le shell) qui
    est lanc� au moment de la connexion.""",
    tests=(
    shell_good("cut -d: -f7 /etc/passwd"),
    shell_good("cut -f7 -d: /etc/passwd", ordre),
    cut_required,
    reject("<", "Ne faites pas de redirections inutiles"),
    shell_require("<argument>-d:</argument>",
                  "Vous devez indiquer que ':' est le d�limiteur"),
    shell_require("<argument>-f7</argument>",
                  """Vous devez indiquer la colonne que vous voulez extraire.
                  Le shell est indiqu� dans la derni�re colonne."""),
    shell_require("<argument>/etc/passwd</argument>",
                  """Vous devez indiquer le nom du fichier
                  ou extraire la colonne"""),
    shell_display,
    ),
    )

add(name="utilisateurs",
    required=["les shells", "sh:remplacement"],
    question="""Donnez la commande permettant de stocker
    dans la variable <tt>A</tt> la liste des logins
    d'utilisateurs d�finis dans <tt>/etc/passwd</tt>.""",
    tests=(
    reject("<", "Ne faites pas de redirections inutiles"),
    require("1", "Vous n'indiquez pas que la colonne des utilisateurs est la premi�re"),
    require("$", """Les pr�requis vous indiquent
    qu'il faut faire un remplacement en utilisant <tt>$(...)</tt>"""),
    shell_require('-d:', "O� avez-vous indiqu� que le d�limiteur est ':'"),
    require('A', "O� est indiqu�e la variable A&nbsp;?"),
    shell_good((
    "A=$(cut -d: -f1 /etc/passwd)",
    'A="$(cut -d: -f1 /etc/passwd)"'
                ) ),
    shell_good((
    "A=$(cut -f1 -d: /etc/passwd)",
    'A="$(cut -f1 -d: /etc/passwd)"'), ordre),
    reject((' =', '= '), "Il ne faut pas d'espace autour de l'affectation"),
    shell_display,
    ),
    )

import remplacer

add(name="espaces multiples",
    required=["les shells", "remplacer:intro", "pipeline:intro"],
    question="""Donnez la ligne de commande permettant d'extraire
    la cinqui�me colonne de l'entr�e standard sachant que
    les colonnes sont s�par�es par de multiples espaces et non un seul.""",
    tests=(
    require('sed', "On utilise <tt>sed</tt> pour faire le remplacement"),
    require('/g', """Il y a plusieurs substitutions � faire sur la ligne,
    pas une seule. Il manque donc un 'g' pour <em>global</em> quelque part."""),
    cut_required,
    reject('/ *//',
           """Votre expression r�guli�re remplace un espace par rien.
           Les colonnes vont donc dispara�tre"""),
    reject('/ */ /',
           """Votre expression r�guli�re ajoute un espace entre chaque
           paires de caract�res.
           En effet l'�toile peut r�p�ter z�ro fois."""),
    reject('[ ]', "� quoi servent les crochets autour de l'espace&nbsp;?"),
    
    shell_good("sed 's/  */ /g' | cut -d' ' -f5",
               dumb_replace=remplacer.dumb_replace),
    shell_good("sed 's/ * / /g' | cut -d' ' -f5",
		"""Il est conseill� d'�crire <tt>__*</tt>
		plut�t que <tt>_*_</tt>""",
               dumb_replace=remplacer.dumb_replace),
    shell_good("sed -r 's/ +/ /g' | cut -d' ' -f5",
               dumb_replace=remplacer.dumb_replace),
    shell_bad("sed 's/ +/ /g' | cut -d' ' -f5",
              """Le symbole <tt>+</tt> fait parti des expressions
              r�guli�res �tendues. Mais par d�faut la commande
              <tt>sed</tt> ne les utilise pas.
              <p>
              Ajouter l'option indiquant � <tt>sed</tt> d'utiliser
              les expressions r�guli�res �tendues""",
               dumb_replace=remplacer.dumb_replace),
    require((' *', ' +'),
            "Il faut utiliser l'�toile ou le plus pour r�p�ter l'espace.",
            all_agree=True),
    require("5", "Vous n'avez pas indiqu� le num�ro de la colonne � extraire"),
    shell_require('<argument>-d </argument>',
                  """Vous n'avez pas indiqu� � <tt>cut</tt> que le s�parateur
                  �tait l'espace"""),
    shell_bad(("sed -r 's/\\ +/ /g' | cut -d' ' -f5",
               "sed -r 's/\\ +/\\ /g' | cut -d' ' -f5",
               "sed 's/\\ \\ */ /g' | cut -d' ' -f5",
               "sed 's/\\ \\ */\\ /g' | cut -d' ' -f5",
               ),
              """L'espace n'est pas un caract�re sp�cial pour les expressions
              r�guli�re, donc pas besoin de le prot�ger""",
               dumb_replace=remplacer.dumb_replace),
    require('[', "Vous devez faire un pipeline"),
    Bad(Comment(~End('5'),
                 """Dans la commande <tt>cut</tt>, il est plus intuitif
                    d'indiquer le s�parateur de champs avant d'indiquer
                    le num�ro du champ � extraire""")),
    shell_display,
    ),
    indices=(
    """Utilisez un filtre pour remplacer les suites de blancs
    par un seul blanc et envoyez le r�sultat � la commande
    qui extrait des colonnes.
    Aidez-vous des r�ponses aux questions pr�c�dentes.""",
    ),
    )
    

    
