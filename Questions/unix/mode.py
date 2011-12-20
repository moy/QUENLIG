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
    question="""Quelle commande permet de changer les droits
    d'acc�s � des fichiers et r�pertoires.""",
    tests=(
    good("chmod"),
    ),
    )

class mode_display(TestExpression):
    def do_test(self, student_answer, state=None):
        n = int(student_answer, 8)
        s = ''
        for i in range(9):
            if n & (1<<(9-i-1)):
                s += 'rwxrwxrwx'[i]
            else:
                s += '-'
        return True, "Le mode num�rique <tt>%s</tt> repr�sente <tt>%s</tt>"%(
            student_answer, s)


add(name="num�rique",
    required=["intro"],
    question="""A quelle valeur num�rique �crite en octal correspond
    le mode <tt>rwxr-x---</tt>""",
    tests=(
    good("750"),
    require_int(),
    answer_length_is(3, "Le mode en octal vu en cours est sur 3 chiffres"),
    reject(('8','9'), "En octal, les chiffres 8 et 9 n'existent pas"),
    Bad(mode_display()),
    ),
    indices=(
    """Remplacez les lettres par des 1 et les - par des z�ros.
    Convertissez le nombre binaire en octal (base 8) :
    <tt>101010011 = 101 010 011 = 523</tt>
    """,
    ),
    )

b = """De nombreuses r�ponses correctes sont possibles.
Toutes ne sont pas accept�es.
Pour augmenter vos chances vous devez donnez la r�ponse la plus courte.
Si vous utilisez les modes 'r', 'w' et 'x' il faut qu'ils
soient utilis�s de pr�f�rence dans cet ordre."""

chmod_required = require("chmod", "Vous devez utiliser <tt>chmod</tt>")

umask = """Cela marche peut-�tre pour votre configuration,
mais pas dans tous les cas.
<p>
En effet quand vous utilisez <tt>+x</tt> le mode 
est modifi� en tenant compte de la valeur courante du <tt>umask</tt>.
<p>
Pour plus d'informations, regardez <tt>man 2 umask</tt>"""

add(name="simple",
    required=["num�rique"],
    before=b,
    question="""Quelle ligne de commande permet d'affecter
    le mode <tt>rwxr-xr-x</tt> au fichier <tt>essai.sh</tt>
    en utilisant la syntaxe en octal.""",
    tests=(
    shell_good((
    "chmod 755 essai.sh",
    "chmod u=rwx,go=rx xxx essai.sh",
    "chmod a=rx,u+w essai.sh",
    )),
    chmod_required,
    shell_bad(("chmod rwxr-xr-x essai.sh",
               "chmod u=rwx go=xr essai.sh"),
              "Vous n'avez m�me pas essay� la commande elle fait une erreur"),
    shell_bad("chmod essai.sh 755",
              """La syntaxe de <tt>chmod</tt> est simple : le premier
              argument est le mode, les autres sont des noms d'entit�s"""),
    require("essai.sh", "On veut modifier le mode de <tt>essai.sh</tt>"),
    require("755", "Vous vous �tes tromp� en calculant le mode en octal."),
    shell_display,
    ),
    good_answer="""Le plus court est <tt>chmod 755 essai.sh</tt>""",
    indices=("""R��crire la suite de lettre en rempla�ant les '-'
    par des '0' et les lettres par des '1' et convertir le nombre
    binaire en octal (base 8)""",),
    )


add(name="ajouter",
    required=["simple"],
    question="""Quelle ligne de commande permet d'ajouter le droit
    d'ex�cuter pour l'utilisateur au fichier <tt>essai.sh</tt>""",
    tests=(
    shell_good("chmod u+x essai.sh"),
    shell_bad("chmod +x essai.sh", umask),
    shell_bad("chmod u+X essai.sh",
              """Le droit d'ex�cution ne sera ajout� que si
              <tt>essai.sh</tt> est un r�pertoire"""),
    chmod_required,
    require("essai.sh",
            """Vous voulez changer le mode de <tt>essai.sh</tt>
            le minimum est de l'indiquer"""),
    reject('[', """Les crochets utilis�s pour donner la syntaxe de la commande.
    indiquent que le contenu est facultatif.
    Vous ne devez pas avoir de crochets dans votre r�ponse."""),
    require("+",
            """Vous ne voulez pas modifier compl�tement la valeur
            du mode mais seulement <b>ajouter</b> un droit
            supl�mentaire"""),
    reject("+ ", "Il ne faut pas d'espace apr�s le <tt>+</tt>"),
    require("+x",
            """Vous voulez ajouter le droit d'ex�cution,
            pas de faire autre chose"""),
    require("u+",
            """C'est seulement pour l'utilisateur que vous
            voulez ajouter le droit d'ex�cution"""),
    shell_display,
    ),
    indices=("""On ne connais pas l'ancien mode, on utilise donc
    la syntaxe <tt>[u][g][o][a][+|-][r][w][x]</tt>""",
             ),
    )


add(name="exec pattern",
    required=["ajouter", "pattern:0 au milieu"],
    before=b,
    question="""Quelle ligne de commande permet <b>d'ajouter</b>
    le mode 'x' pour l'utilisateur, le groupe et les autres
    � tous les fichiers du r�pertoire courant dont
    le nom se termine par <tt>.sh</tt>
    """,
    tests=(
    shell_good("chmod a+x *.sh"),
    shell_good(("chmod u+x,g+x,o+x *.sh", "chmod ugo+x *.sh", ),
               "<tt>chmod a+x *.sh</tt> est plus court"),
    shell_bad("chmod o+x *.sh",
              "Cela n'a pas ajout� le droit d'ex�cution � l'utilisateur"),
    shell_bad("chmod u+x *.sh",
              """Cela n'a pas ajout� le droit d'ex�cution au groupe
              et aux autres"""),
    shell_bad("chmod +x *.sh", umask),
    reject(";",
           "On ne veux utiliser <tt>chmod</tt> qu'une seule fois"),
    require("+",
            "Il faut indiquer que vous <b>ajoutez</b> des droits"),
    require('x',
            "Je ne vois pas le <tt>x</tt> indiquant le droit d'ex�cution"),
    reject("find",
           """On veux changer les droits dans le r�pertoire courant
           pas dans toute la hi�rarchie"""),
    reject("./*",
           "Le <tt>./</tt> ne sert � rien ici"),
    reject("-R", """On ne veux pas changer le mode sur toute la hi�rarchie,
    seulement dans le r�pertoire courant."""),
    shell_require("<argument><pattern_char>*</pattern_char>.sh</argument>",
                  """Je ne vois pas le <em>pattern</em> indiquant tous
                  les fichiers se terminant par <tt>.sh</tt> dans
                  le r�pertoire courant"""),
    number_of_is(' ', 2, """Il y a normalement seulement 2 espaces
    dans votre commande car elle a 2 param�tres&nbsp;: le changement
    de mode et le <em>pattern</em>"""),
    reject(('r', 'w'),
           "On ne veux pas ajouter le mode <tt>r</tt> ou <tt>w</tt>"),
    reject('uga', 'Petit rappel : u=user g=group o=other a=u+g+o'),
    
    shell_display,
    ),
    )

add(name="exec pattern 2",
    required=["exec pattern"],
    before=b,
    question="""Quel ligne de commande permet <b>d'ajouter</b>
    le mode 'w' pour l'utilisateur, le groupe et les autres
    � tous les fichiers du r�pertoire courant dont
    le nom se termine par <tt>.sh</tt>,
    """,
    tests=(
    shell_good("chmod a+w *.sh"),
    shell_good(("chmod u+w,g+w,o+w *.sh", "chmod ugo+w *.sh", ),
               "<tt>chmod a+w *.sh</tt> est plus court"),
    shell_bad("chmod +w *.sh",
               """Cela ne l'ajoute qu'� l'utilisateur"""),
    expect('chmod'),
    comment("""Il vous suffit de remplacer un <tt>x</tt> par
    un <tt>w</tt> dans la r�ponse que vous aviez donn� pour
    ajouter le droit d'ex�cution dans une question pr�c�dente."""),
    shell_display,
    ),
    )

add(name="r�cursif",
    required=["ajouter"],
    before="""Il ne faut jamais dire au syst�me que
    des fichiers de donn�es sont ex�cutables
    car cela cr�e des probl�mes de s�curit� et en plus
    le double clique pour �diter le fichier l'ex�cutera
    au lieu de l'�diter...""",
    question="""Ajouter r�cursivement � partir du r�pertoire courant
    le mode '<tt>x</tt>' pour le propri�taire, le groupe et tout
    le monde, s'il <b>�tait d�j� pr�sent</b> pour quelqu'un.
    <pre>
    rwx------ devient rwx--x--x
    r-xr-xr-- devient r-xr-xr-x
    rw-r--r-- reste inchang�</pre>
    <p>
    On n'a pas besoin d'une commande autre que <tt>chmod</tt>.
    """,
    tests=(
    reject("find", "Pas besoin de <tt>find</tt> seulement <tt>chmod</tt>"),
    reject('ugo', 'On veut <tt>a</tt> � la place de <tt>ugo</tt>'),
    reject('/', "Pourquoi un <tt>/</tt>&nbsp;?"),
    reject(('1','3','5','7'),
           """Vous ne pouvez pas utiliser de mode num�riques car
           les modes des fichiers modifi�s ne sont pas tous les m�mes."""),
    require('+', "On veut ajouter un droit, il faut donc utiliser <tt>+</tt>"),
    reject('+x', "Non car les fichiers de donn�es vont devenir ex�cutables") ,
    require('.', 'Et le r�pertoire courant, il est o�&nbsp;?'),
    shell_require("-R","Il faut donner une option pour indiquer la r�cursion"),
    reject(" +X", """Relisez bien la documentation, cela ne fait
    pas comme <tt>a+X</tt>, il y a un <em>mais</tt> dans la phrase."""),
    shell_bad("chmod -R o+X .",
              "Cela n'ajoute pas le mode <tt>x</tt> au propri�taire"),
    shell_good("chmod -R a+X ."),
    shell_good("chmod a+X -R .",
               """Ceci n'est pas portable sur d'autres Unix,
               v�rifiez l'ordre des options"""),
    require_endswith(' .',
                     """Le dernier argument de <tt>chmod</tt> doit �tre
                     le r�pertoire courant"""),
    shell_display,
    ),
    )


    

import chercher

add(name="r�paration",
    required=["ajouter", "chercher:ex�cuter", "chercher:images"],
    before="""Un administrateur maladroit � rendu tous vos fichiers
    ex�cutables&nbsp;: les fichiers texte, les images, les pages HTML, ...""",
    question="""Quelle ligne de commande permet d'enlever le bit <tt>x</tt>
    des images PNG et JPG de votre compte.
    <ul>
    <li> Il ne faudra pas tenir compte de la casse,
    <li> la solution la plus courte est recherch�e.
    <li> dans votre r�ponse indiquez d'abord PNG puis JPG,
    <li> cela n'a pas de sens d'enlever le mode <tt>x</tt> � l'utilisateur
    et le laisser aux autres. Donc il faut l'enlever � tous.
    </ul>
    """,
    tests=(
    reject('/', "Vous n'avez pas besoin de <tt>/</tt> dans la r�ponse"),
    shell_good(
    (
    "find ~ \( -iname '*.jpg' -o -iname '*.png' \) -exec chmod -x {} \\;",
    "find ~ \( -iname '*.jpg' -o -iname '*.png' \) -exec chmod a-x {} \\;",
    ),
    "J'accepte la r�ponse, mais on vous avais dis d'abord PNG et apr�s JPG",
    dumb_replace=chercher.dumb_replace),
    shell_good(
    (
    "find ~ \( -iname '*.png' -o -iname '*.jpg' \) -exec chmod -x {} \\;",
    "find ~ \( -iname '*.png' -o -iname '*.jpg' \) -exec chmod a-x {} \\;",
    ),
    dumb_replace=chercher.dumb_replace),
    shell_bad(
    ("find ~ -iname '*.png' -o -iname '*.jpg' -exec chmod -x {} \\;",
     "find ~ -iname '*.png' -o -iname '*.jpg' -exec chmod a-x {} \\;",
     ),
    """Le <tt>-exec</tt> va s'ex�cuter seulement pour les JPG
    pas pour les PNG. Vous devez parenth�ser""",
    dumb_replace=chercher.dumb_replace),
    require("find", "Il faut utiliser <tt>find</tt>"),
    reject('$(', "N'utilisez pas <tt>$()</tt> mais <tt>-exec</tt>"),
    require("~",
            """Vous devez changer tous les fichiers
            � partir de la <b>racine de votre compte</b>"""),
    reject("ugo", "Utilisez <tt>a</tt> plut�t que <tt>ugo</tt>"),
    reject("regex",
           "Utilisez <tt>-iname</tt> plut�t qu'une expression r�guli�re"
           ),
    require("-o", "Il faut faire un 'ou', donc il vous faut un <tt>-o</tt>"),
    require(("(", ")"),
            """Il faut parenth�ser le 'ou' pour que le <tt>exec</tt>
            s'applique au deux"""),
    Bad(Comment(~(Contain("\\(") | Contain("'('") | Contain('"("'))
                | ~(Contain("\\)") | Contain("')'") | Contain('")"')),
    """N'oubliez pas de prot�ger les parenth�ses,
    car elles sont sp�ciales pour le shell""")),
    Bad(Comment(~(Contain(" \\( ") | Contain(" '(' ") | Contain(' "(" '))
                | ~(Contain(" \\) ") | Contain(" ')' ") | Contain(' ")" ')),
            """N'oubliez pas les espaces autour des parenth�ses.""")),
    shell_require(('png','jpg'), "Pour les images PNG et JPG on a dit.",
            dumb_replace=chercher.dumb_replace),
    number_of_is('-iname', 2, "Je ne vois pas deux <tt>-iname</tt>"),
    reject('u-x', """On ne veut pas enlever le droit d'ex�cution
    seulement � l'utilisateur, mais au groupe et aux autres"""),
    number_of_is(' ', 13, "Il y a 13 espaces dans la bonne solution"),
    require('-x', """Je ne vois pas l'option de <tt>chmod</tt> indiquant
    que vous voulez enlever le mode d'ex�cution"""),
    reject('xargs', 'Pas besoin de <tt>xargs</tt>'),
    
    
    shell_display,
    ),
    indices=("Il faut utiliser la commande <tt>find</tt>",
             """On veut enlever le mode <tt>x</tt> � l'utilisateur,
             au groupe et aux autres.
             N'oubliez pas, la r�ponse doit �tre la plus courte.""",
             ),
    )
