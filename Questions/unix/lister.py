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
    required=["sh:console", "sh:r�pertoire courant",
              "sh:r�pertoire connexion"],
    question="""Quel est le nom de la commande permettant d'avoir
    des informations sur les fichiers et le contenu des r�pertoires.""",
    tests=(
    good("ls"),
    bad("cat",
        "Cette commande permet d'afficher le <b>contenu</b> des fichiers"),
    bad('file',
        """Cette commande est tr�s utile, mais elle ne permet pas de lister
        le contenu des r�pertoires"""),
    
    reject(" ", "Seulement le nom de la commande, pas d'options"),
    ),
    )

add(name="nomm�",
    required=["intro"],
    question="""Donnez la commande permettant de lister les noms des fichiers (et r�pertoires) qui se trouvent dans <tt>/usr</tt>""",
    tests=(
    shell_good("ls /usr"),
    shell_bad("ls /usr/",
              "Cela fonctionne mais, on peut faire un caract�re plus court"),
    shell_bad("ls usr",
              """Cela ne fonctionne que si votre r�pertoire courant
              est <tt>/</tt>"""),
    shell_bad("ls /usr/*",
              """Cela va trop en lister, en effet cela va lister le contenu
              des r�pertoires qui se trouvent dans <tt>/usr</tt>
              alors que l'on ne veut que leur nom."""),
    require("/usr",
            
            """Comment pouvez-vous lister le contenu de <tt>/usr</tt>
            sans faire r�f�rence � <tt>/usr</tt> dans la
            ligne de commande&nbsp;?"""),
    reject("-", "Il n'y a pas besoin de donner des options � <tt>ls</tt>"),
    shell_display,
    ),
    )

add(name="affichage long",
    required=["intro"],
    question="""Quelle ligne de commande utilisant <tt>ls</tt>
    permet d'afficher plus d'informations sur les fichiers&nbsp;?""",
    tests=(
    shell_good("ls -l"),
    reject("a",
           """L'option <tt>-a</tt> permet de voir les fichiers
           cach�s, cela permet de voir plus de fichier mais ne permet pas
           d'avoir plus d'informations"""),
    require("ls",
            "Donnez la ligne de commande compl�te, pas seulement l'option"),
    answer_length_is(5, """La bonne r�ponse fait 5 caract�res
    en comptant l'espace"""),
    shell_display,
    ),
    indices=("""Pour s'en rappeler&nbsp;: c'est pour afficher une
    <b>l</b>ongue liste d'information sur les fichiers""",
             "Tapez <tt>ls --help</tt> pour lister les options",
             ),
    )


f = """La commande <tt>ls -l /tmp/toto</tt> affiche (si votre langue est le fran�ais)&nbsp;:
    <pre>-rwxr-xr-x   1 exco   liris      18 Jan 19  2005 /tmp/toto</pre>"""

add(name="nom court",
    required=["affichage long"],
    question=f + """Quel est le nom court du fichier (pas le chemin)&nbsp;?""",
    tests=(
    good("toto"),
    reject("/",
           """Un nom court ne peut contenir de <tt>/</tt>
           contrairement au nom relatif ou absolu (un chemin)"""),
    reject('exco', "C'est le propri�taire du fichier"),
    reject('liris', "C'est le groupe propri�taire du fichier"),
    ),
    )

add(name="taille",
    required=["affichage long"],
    question=f + """Quel est le nombre d'octets contenu dans le fichier&nbsp;?""",
    tests=(
    good("18"),
    bad("1", "�a c'est le nombre de noms diff�rents que porte le fichier"),
    bad("2005", "C'est l'ann�e de modification du fichier"),
    bad("19", "C'est date (jour du mois) de modification du fichier"),
    bad("4", "Nombre d'octets dans le fichier, pas dans son nom"),
    bad("10", """Je pense que vous avez un probl�me de vue,
    peut-�tre faut-il augmenter la taille des caract�res&nbsp;?"""),
    bad("0", "Expliquez � votre enseignant pourquoi vous avez r�pondu cela"),
    require_int(),
    ),
    )

add(name="propri�taire",
    required=["affichage long"],
    question=f + """Qui est l'utilisateur propri�taire de ce fichier&nbsp;?""",
    tests=(
    good("exco"),
    bad('liris', "Non, �a c'est le groupe propri�taire"),
    ),
    )

add(name="jour",
    required=["affichage long"],
    question=f + """Quel jour du mois de janvier ce fichier a �t� modifi�&nbsp;?""",
    tests=(
    bad("18", "Vous venez d'indiquer la taille du fichier en octet"),
    good("19"),
    require_int(),
    ),
    )

w = "Les \" ou ' ne changent pas le fait que <tt>-z</tt> est compris comme une option par la commande."

add(name="sp�cial",
    required=["intro"],
    question="""Donnez la ligne de commande pour lister
    avec l'option <tt>-l</tt> les informations sur
    le fichier nomm� <tt>-z</tt>
    <p>
    Vous n'avez pas besoin de lire les manuels pour r�pondre
    � cette question.
    """,
    tests=(
    reject('--',
           """Le -- n'est pas standard, on ne le trouve que dans
           les commandes cr��es par la FSF (GNU).
           Trouver une autre astuce portable."""),
    shell_good("ls -l ./-z"),
    reject((" '-z'", ' "-z"', ' \\-z'),
           """Les \" ou ' ou \\ ne changent pas le fait que <tt>-z</tt>
           soit compris comme une option par la commande car
           elle ne voit pas les caract�res d'�chappement du shell.
           En effet, le tiret n'est pas un caract�re sp�cial pour le shell.
           """),
    shell_bad("ls -l -z", "<tt>ls</tt> croit que <tt>-z</tt> est une option"),
    reject(("*z", "?z", "[-]z"),
           """Le fait d'utiliser un <em>pattern</em> ne change rien.
           En effet, apr�s la substitution faite par
           le shell la commande <tt>ls</tt> recevra
           un argument <tt>-z</tt> qu'elle prendra
           pour une option"""),
    require("-l", "Ou est pass�e l'option <tt>-l</tt>&nbsp;?"),
    require("-z", "Je ne vois nulle part le nom du fichier <tt>-z</tt>"),
    reject(' /', """Vous faites r�f�rence � un fichier dans la racine,
    ce n'est pas le cas de <tt>-z</tt>"""),
    reject(';', """Vous n'avez pas besoin d'utilisez d'autre commandes
    que <tt>ls</tt>"""),
    reject('\\-', """Cela ne sert � rien de prot�ger le tiret car
    ce n'est pas un caract�re sp�cial vis � vis du shell"""),
    answer_length_is(len("ls -l ./-z"),
                     """La r�ponse attendue fait %d caract�res""" % len("ls -l ./-z")),
    shell_display,
    ),                 
    indices=("Utilisez un autre nom pour ce fichier afin qu'il ne commence pas par un caract�re <tt>-</tt>",
             "Le r�pertoire courant est <tt>.</tt>",
             "Faites un chemin relatif au r�pertoire courant",
             ),
    )

f = """La commande <tt>ls -l</tt> affiche&nbsp;:
    <pre>lrwxrwxrwx   1 exco   liris      13 Jan 19  2005 /tmp/toto -> ../etc/passwd</pre>"""


add(name="lien symbolique",
    required=["nom court", "propri�taire"],
    before="""Si le raccourci est un chemin relatif,
    alors il est �valu� en fonction du r�pertoire
    dans lequel se trouve le lien.""",
    question=f + """Quel est le nom (chemin) absolu du fichier point�
    par ce raccourci (<tt>../etc/passwd</tt>) &nbsp;?""",
    tests=(
    good("/etc/passwd"),
    good("/tmp/../etc/passwd", "Une r�ponse plus courte est '/etc/passwd'"),
    bad("../etc/passwd",
        """C'est bien le chemin relatif par rapport � <tt>/tmp</tt>
        mais on vous demande le chemin <b>absolu</b>"""),
    bad("/tmp/toto", """Non, �a c'est le nom du lien, pas le nom
    de la chose point�e"""),
    require("passwd",
            """Le nom court du fichier point� est <tt>passwd</tt>
            Cela n'appara�t pas dans votre r�ponse"""),
    reject("toto",
            """Il n'y a <tt>toto</tt> nulle part dans le
            nom du fichier point� par <tt>/tmp/toto</tt>"""),
    require("/",
            """On vous demande un chemin absolu,
            cela commence donc forc�ment par <tt>/</tt>"""),
    bad("/tmp/etc/passwd",
        """Votre r�ponse ne correspond pas � <tt>../etc/passwd</tt>
        en relatif par rapport � <tt>/tmp</tt>"""),
    bad("/passwd",
        """R�fl�chissez encore.
        Le raccourci est vers <tt>../etc/passwd</tt>"""),
    require_startswith('/',
                       """On vous demande un chemin absolu,
                       il commence donc par un slash"""),
    expect('etc'),
    shell_display,
    ),
    bad_answer="C'est le chemin absolu le plus court qui est la bonne r�ponse",
    indices=(
    """Votre r�ponse ne d�pend pas de votre r�pertoire courant""",
    """Pour trouver la r�ponse&nbsp;:
    <ul>
    <li> Concat�nez le nom absolu du r�pertoire contenant le lien symbolique
    avec la valeur du lien symbolique.
    <li> Raccourcicez le nom du fichier en enlevant les <tt>..</tt>
    sans changer sa destination.
    </ul>""",
    ),
   
    )

ls_is_required=require("ls","""Vous devez utiliser la commande <tt>ls</tt>""")

add(name="tri� par date",
    required=["jour"],
    question="""Quelle ligne de commande permet de lister les noms
    des fichiers (sans afficher les autres informations) en les triant
    par date de modification du contenu.""",
    tests=(
    shell_good("ls -t"),
    shell_bad("ls -c",
              """Cela trie par date de modifications des 'meta-informations'
              comme le propri�taire, le mode, ...
              Cela ne trie pas par date de modification du contenu"""
              ),
    ls_is_required,
    reject("-l",
           """Que les noms des fichiers, rien d'autre.
           Enlevez l'option inutile."""),
    reject('|', """N'utilisez pas un <em>pipe</em> cherchez la bonne option
    de la commande <tt>ls</tt>"""),
    shell_bad('ls', "Sans options ils sont tri�s dans l'ordre alphab�tique"),
    reject('--sort', """Les options longues (avec 2 tirets) ne sont pas
    standards."""),
    shell_display,
    ),
    indices=("""Pour s'en rappeler&nbsp;: c'est pour
    trier par <em><b>t</b>ime</em> les fichiers""",
             "Tapez <tt>ls --help</tt> pour lister les options",
             ),
    )

add(name="tri� par taille",
    required=["taille"],
    question="""Quelle ligne de commande permet d'afficher les noms fichiers
    en les triant par taille""",
    tests=(
    shell_good( ("ls -S",) ),
    ls_is_required,
    reject("-t", """L'option <tt>-t</tt> trie par date, pas par taille"""),
    reject("-l", """On ne vous demande pas d'afficher plein d'information
    sur les fichiers, seulement de les trier par taille"""),
    shell_bad("ls -s", "Cela affiche la taille mais ne trie rien"),
    reject('--size', """Les options longues (avec 2 tirets) ne sont pas
    standards."""),
    shell_display,
    ),
    indices=("""Pour s'en rappeler&nbsp;: c'est pour
    trier par <em><b>S</b>ize</em> les fichiers""",
             "Tapez <tt>ls --help</tt> pour lister les options",
             ),
    )

    

   
                  
