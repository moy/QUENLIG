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
from .check import *

require_passwd = require("/etc/passwd",
                         "Vous devez indiquer le nom du fichier � trier")

dumb_replace=( ('-g', '-n'), )

add(name="intro",
    required=["manuel:chercher"],
    question="""Quelle est la commande permettant de trier les lignes
    contenues dans des fichiers&nbsp;?""",
    tests=(
    good("sort"),
    reject("ls", "<tt>ls</tt> ne regarde pas le contenu des fichiers"),
    ),
    indices=(
    "Le nom de la commande veut dire 'trier' en anglais",
    ),
    )

add(name="simple",
    required=["intro"],
    question="""Donner la commande la plus simple permettant
    de trier les lignes du fichier <tt>/etc/passwd</tt>
    dans l'ordre standard (celui des codes ASCII)""",
    tests=(
    reject((';','|'), "Vous n'avez besoin que d'une seule commande."),
    shell_good("sort /etc/passwd"),
    shell_bad("sort </etc/passwd",
              "�a marche, mais il y a un poil plus simple"),
    reject('-', "Pas besoin d'option pour un simple tri"),
    require_passwd,
    shell_display,
    ),
    good_answer="""Le r�sultat tri� s'affiche sur la sortie standard
    donc l'�cran""",
    )

add(name="nombre",
    required=["intro"],
    question="""Donner la commande la plus simple permettant
    de trier les nombres suivants du plus petit au plus grand.
    Cette liste est ici comme exemple de donn�e � traiter,
    <b>seule la commande</b> figure dans votre r�ponse.
    <pre>456
45
786
1
768
31
8
343</pre>
N'oubliez pas de taper <tt>^D</tt> pour terminer la liste
dont vous venez de faire le copier/coller dans l'entr�e standard
de la commande <tt>sort</tt>""",
    tests=(
    shell_good("sort -n", dumb_replace=dumb_replace),
    reject(("0","1","2","3","4"),
           """On vous a dit de ne mettre que la commande dans la r�ponse.
           Pas la liste de nombres."""),
    bad("sort", """Vous auriez essay�, vous auriez vu que
    le tri n'est pas fait dans l'ordre num�rique."""),
    require('sort', "On veut la ligne de commande compl�te"),
    ),
    )


add(name="dans fichier",
    required=["simple", "sh:redirection sortie"],
    question="""Donner la commande la plus simple (courte) permettant
    de trier les lignes du fichier <tt>/etc/passwd</tt>
    dans l'ordre des codes ASCII</b> et de les stocker dans le fichier
    <tt>xxx</tt> (en le vidant) du r�pertoire courant.""",
    tests=(
    shell_good("sort /etc/passwd >xxx"),
    shell_bad("sort /etc/passwd >>xxx", "Et si vous vidiez le fichier&nbsp;?"),
    reject("-", "Il n'y a pas besoin de sp�cifier d'option"),
    require(">",
            """Je ne vois pas de redirection de la sortie standard
            dans le fichier <tt>xxx</tt>"""),
    require_passwd,
    reject("|", "Il n'y a pas besoin de pipeline"),
    reject('./xxx', "Il y a plus court que <tt>./xxx</tt>"),
    require('xxx', "Je ne vois pas de r�f�rence � <tt>xxx</tt>"),
    expect('sort'),
    shell_display,
    ),
    )


add(name="clef",
    required=["simple", "manuel:section commande", "manuel:voir aussi"],
    before="""Le contenu du fichier <tt>/etc/passwd</tt> contient
    une ligne par utilisateur et chaque ligne contient
    7 champs s�par�s par des ':' pour en savoir plus
    utilisez la commande <tt>man</tt>.""",
    question="""Quelle commande permet de trier <tt>/etc/passwd</tt>
    pour que les noms de r�pertoire de connexion soient
    dans l'ordre alphab�tique&nbsp;?""",
    tests=(
    reject((';','|'), "Vous n'avez besoin que d'une seule commande."),
    reject("<", """Pourquoi voulez-vous rediriger l'entr�e standard,
    cela fait un caract�re de plus � taper"""),
    reject("-d",
           """Avec la commande <tt>sort</tt> le d�limiteur de champs
           est indiqu� par l'option <tt>-t</tt> et non <tt>-d</tt>"""),
    require_passwd,
    shell_require("<argument>-t:</argument>",
                  "Vous devez indiquer que ':' est le d�limiteur"),
    shell_good("sort -t: +5 /etc/passwd",
               "La syntaxe standard est <tt>sort -t: -k 6 /etc/passwd</tt>"),
    shell_good("sort +5 -t: /etc/passwd",
               """On indique normalement le s�parateur avant
               le num�ro du champ � trier.
               De plus, la syntaxe standard est
               <tt>sort -t: -k 6 /etc/passwd</tt>"""),
    shell_good("sort -t: -k 6 /etc/passwd"),
    shell_good("sort -k 6 -t: /etc/passwd",
               """On indique normalement le s�parateur avant
               le num�ro du champ � trier"""),
    reject('+', """N'utilisez pas la syntaxe avec le + pour indiquer
    les colonnes (elle est obsolette) mais l'option <tt>-k</tt>"""),
    require('-k', "Je ne vois pas l'option indiquant la colonne � trier"),
    require('6', "Je ne vois pas le num�ro de la colonne � trier"),
    reject((',','.'), """Vous n'avez pas besoin de virgule ni de point
    pour r�pondre."""),
    
    shell_display,
    ),
    indices=(
    """Indiquez le d�limiteur de colonne avant le num�ro
    de la colonne que vous voulez trier.""",
    """La colonne contenant le r�pertoire de connexion est la sixi�me,
    mais attention au pi�ge, lisez bien la documentation...""",
    ), 
    )

add(name="uid passwd",
    required=["colonne:les shells", "nombre", "pipeline:intro", "manuel:section commande"],
    question="""Tapez la ligne de commande permettant de&nbsp;:
    <ul>
    <li> Extraire la liste des UID du fichier <tt>/etc/passwd</tt>
    <li> Les trier num�riquement et les afficher sur la sortie standard
    </ul>
    """,
    tests=(
    shell_good(("cut -d: -f3 /etc/passwd | sort -n",
                "cut -f3 -d: /etc/passwd | sort -n",
                "cut -d: -f3 </etc/passwd | sort -n",
                "cut -f3 -d: </etc/passwd | sort -n",
                ),
               dumb_replace=dumb_replace
               ),
    shell_require("<argument>sort</argument><argument>-n</argument>",
                  "Je ne vois pas le tri num�rique",
               dumb_replace=dumb_replace
                  ),
    require("3", "Vous n'extrayez pas la colonne des UID du fichier"),
    require_passwd,
    expect('cut'),
    expect('sort'),
    shell_display,
    ),
    indices=(
        """Pour extraire les UID on utilise la commande permettant d'extraire
           une colonne d'un fichier""",
        """La colonne contenant les UID est indiqu�e dans le manuel.""",
    ),
    )

add(name="unique",
    question="""Compl�tez la ligne suivante pour que les
    lignes identiques ne soient pas affich�es plusieurs fois.
    <pre>cut -d: -f7 /etc/passwd | sort</pre>
    Ceci permettra d'afficher la liste de programmes
    qui sont lanc�s au moment de la connexion.""",
    default_answer = "cut -d: -f7 /etc/passwd | sort",
    tests=(
    shell_good("cut -d: -f7 /etc/passwd | sort -u"),
    shell_good("cut -d: -f7 /etc/passwd | sort | uniq",
               "Il suffisait d'ajouter l'option <tt>-u</tt> � <tt>sort</tt>"),
    require("cut -d: -f7 /etc/passwd | sort",
            """Vous avez modifi� la commande, il faut seulement
            la compl�ter"""),
    require_passwd,
    shell_display,
    ),
    indices=("Regardez les options de <tt>sort</tt>",
             "Une seule option est n�cessaire"),
    )

add(name="uid max",
    required=["uid passwd", "variable:lire ligne", "tronquer:derni�re",],
    before="""Nous avons vu que pour lister les UID des utilisateurs
    il fallait lancer la commande suivante&nbsp;:
    <pre>cut -d: -f3 /etc/passwd | sort -n</pre>""",
    question="""Compl�tez la commande pr�c�dente en ajoutant quelque chose
    � la fin pour que cela n'affiche que l'UID le plus grand""",
    default_answer = "cut -d: -f3 /etc/passwd | sort -n | ",
    tests=(
    shell_good(("cut -d: -f3 /etc/passwd | sort -n | tail -1",
                "cut -d: -f3 /etc/passwd | sort -n | tail -n1",
                )),
    require("cut -d: -f3 /etc/passwd | sort -n |",
            """Vous avez modifi� la commande, il faut seulement
            la compl�ter"""),
    reject('-r', "Essayez de r�pondre sans changer l'ordre du tri"),
    reject("head",
           """Si vous n'avez pas chang� les options de <tt>sort</tt>
           le plus grand UID est � la fin, pas au d�but."""),
    require_passwd,
    reject(' -l', "N'auriez-vous pas confondu un UN avec la lettre 'L'&nbsp;?"),
    number_of_is('|', 2, """Il suffit d'allonger le pipeline pour
    filtrer seulement la derni�re ligne � la fin"""),
    shell_display,
    ),
    indices=("Il suffit de tronquer le d�but du fichier",),
    )

add(name="sauve uid max",
    required=["uid max", "sh:remplacement"],
    before="""Nous avons vu que pour afficher le plus grand UID
    il fallait lancer la commande suivante&nbsp;:
    <pre>cut -d: -f3 /etc/passwd | sort -n | tail -1</pre>""",
    default_answer="cut -d: -f3 /etc/passwd | sort -n | tail -1",
    question="""Changer la commande pr�c�dente pour que
    cet UID soit stock� dans la variable shell nomm�e <tt>A</tt>""",
    tests=(
    shell_good("A=$(cut -d: -f3 /etc/passwd | sort -n | tail -1)"),
    shell_good("A=\"$(cut -d: -f3 /etc/passwd | sort -n | tail -1)\""),
    shell_bad(("cut -d: -f3 /etc/passwd | sort -n | tail -1 | read A",
               "cut -d: -f3 /etc/passwd | sort -n | tail -n 1 |read A",
               "cut -d: -f3 /etc/passwd | sort -n -r | read A",
               "cut -d: -f3 /etc/passwd | sort -r -n | read A",
               "cut -d: -f3 /etc/passwd | sort -rn | read A",
               "cut -d: -f3 /etc/passwd | sort -nr | read A",
               ),
              """Si vous avez r�ellement essay� la commande vous auriez vu
              que la variable <tt>A</tt> ne contenait rien
              apr�s l'ex�cution de la ligne.
              <p>
              Ceci est du au fait que le <tt>read A</tt> est dans un pipeline
              et donc qu'il est lanc� dans un processus fils.
              La variable <tt>A</tt> est perdue quand le fils se termine"""
              ),
    require_passwd,
    require('A', "O� est la variable <tt>A</tt>&nbsp;?"),
    reject('<', "On a pas besoin de faire de redirection"),
    require('A=',
            "Regardez les deux questions qui peuvent peut-�tre vous servir"),
    shell_display,
    ),
    indices=("Il suffit d'utiliser l'affectation",
             "Il faut remplacer la commande par le r�sultat de son ex�cution",
             ),
    )

dumb_replace_sed = dumb_replace + ( ('sed -e ', 'sed '), )

add(name="longueur",
    required=["sh:longueurs", "nombre", "remplacer:enl�ve mot"],
    question="""Triez les lignes lues sur l'entr�e standard de la plus courte
    � la plus longue.
    <p>
    Pour ce faire, on combine des commandes que vous avez d�j� faites&nbsp;:
    <ul>
    <li> on pr�fixe chaque ligne par sa longueur,
    <li> puis l'on trie,
    <li> puis on enl�ve le premier mot de chaque ligne.
    </ul>
    """,
    tests=(
    Reject("(while", """La boucle <tt>while</tt> d�fini un bloc d'instruction,
    pas besoin d'ajouter des parenth�ses."""),
    shell_good( 'while read A ; do echo "$(expr length "$A") $A" ; done | sort -n | sed "s/[^ ]* //"', dumb_replace=dumb_replace_sed),
    shell_good( 'while read A ; do echo $(expr length "$A")" $A" ; done | sort -n | sed "s/[^ ]* //"', dumb_replace=dumb_replace_sed),
    shell_good( 'while read A ; do echo $(expr length "$A") "$A" ; done | sort -n | sed "s/[^ ]* //"', dumb_replace=dumb_replace_sed),
    shell_display,
        ),
    )
 

