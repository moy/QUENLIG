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

from questions import *
from check import *

add(name="intro",
    required=["manuel:chercher"],
    question="""Quel est le nom de la commande permettant
    d'afficher le nombre de caract�res, mots et lignes
    contenus dans des fichiers ou bien lu dans son entr�e standard&nbsp;?""",
    tests=(
    good("wc"),
    bad("nl", """Cette commande sert � ajouter des num�ros de ligne,
    on veut une commande affichant simplement le nombre de lignes."""),
    bad('count', "Cette commande n'existe m�me pas&nbsp;!"),
    ),
    indices=(
    "C'est l'abr�viation de <em>word count</em>",
    ),
    )

red = """Cette commande affiche le nom du fichier.
Si vous aviez redirig� son entr�e standard,
elle ne l'aurait pas fait (elle ne conna�trait pas le nom du fichier)"""

ind = "Lisez la doc affich�e par&nbsp;: <tt>wc --help</tt> ou <tt>man wc</tt>"

add(name="ligne",
    required=["intro", "variable:lire ligne"],
    question="""Quelle commande devez-vous taper pour afficher
    QUE le nombre de lignes (sans le nom du fichier)
    contenues dans <tt>/etc/passwd</tt>""",
    tests=(
    require('wc', 'On utilise <tt>wc</tt> pour compter'),
    require("/etc/passwd",
            """Le nombre de lignes de <tt>/etc/passwd</tt>,
            pas de l'entr�e standard (ou un autre fichier)."""),
    require('-',
            """Il faut donner une option � <tt>wc</tt>
            pour n'afficher que le nombre de lignes"""),
    shell_bad("wc -l /etc/passwd", red),
    shell_good("wc -l </etc/passwd"),
    reject('|', "On n'utilise pas d'autres commandes que <tt>wc</tt>"),
    Expect('-l', """Je ne vois pas l'option de 'wc' indiquant que l'on
           veut compter le nombre de ligne"""),
    Reject(">", """La commande que vous avez donn� n'affiche rien
           car vous avez redirig� sa sortie standard."""),
    shell_display,
    ),
    indices=(ind, ),
    )

add(name="caract�re",
    required=["ligne"],
    question="""Quelle commande devez-vous taper pour n'afficher
    que le nombre d'octets contenus dans <tt>/etc/passwd</tt>""",
    tests=(
    require('wc', 'On utilise <tt>wc</tt> pour compter'),
    require("/etc/passwd", """Le nombre de lignes de <tt>/etc/passwd</tt>"""),
    reject('-m', """L'option <tt>m</tt> compte les caract�res,
    comme un caract�re UTF-8 peut �tre sur plusieurs octets
    cette option ne permet pas de compter le nombre d'octets."""),
    shell_good("wc -c /etc/passwd", red),
    shell_good("wc -c </etc/passwd"),
    reject('-l', "<tt>-l</tt> c'est pour compter le nombre de lignes"),
    shell_display,
    ),
    indices=(ind, ),
    )

add(name="echo",
    required=["caract�re"],    
    question="""Qu'affiche la commande&nbsp;: <tt>echo A | wc --bytes</tt>""",
    tests=(
    good("2", """Il y en a 2 car la commande <tt>echo</tt> affiche
    un <em>linefeed</em> pour indiquer la fin de ligne."""),
    bad("1",
        """Vous venez b�tement de faire un mauvaise r�ponse.
        Il faut tester dans le shell avant de r�pondre"""),
    answer_length_is(1,
                     """On vous demande simplement de recopier ce qu'affiche
                     la commande."""),
    ),
    )

add(name="compte C",
    required = ["intro", "chercher:ex�cuter"],
    question = """Donnez la commande qui affiche le nombre de
    lignes/mots/octets contenu dans chacun des fichiers dont
    le nom se termine par <tt>.c</tt> � partir du r�pertoire courant.
    <p>
    Elle n'a pas besoin de faire la somme pour tous les fichiers.
    <p>
    Elle n'a pas besoin de v�rifier que c'est bien un fichier.
    """,
    tests = (
        Reject('wc -', "Pas besoin d'option pour <tt>wc</tt>"),
        Expect('find'),
        Expect('-name'),
        Expect('*.c'),
        Bad(Comment(~(Contain('"*.c"') | Contain("'*.c'") | Contain("\\*.c")),
                    "Auriez-vous oubli� de prot�ger l'�toile ?")),
        Good(Shell(Equal('wc $(find . -name "*.c")'))),
        Good(Shell(Equal('find . -name "*.c" -exec wc {} \\;'))),
        Good(Shell(Equal('find . -name "*.c" | xargs wc'))),
        Good(Shell(Equal('find . -name "*.c" -print0 | xargs -0 wc'))),
        Bad(Comment(~Contain('-exec') & ~Contain('xargs') & ~Contain('$('),
                    """Les 3 m�thodes accept�es comme r�ponse sont :
<ul>
<li> Utiliser l'action 'exec' de find
<li> Utiliser la commande 'xargs' pour traiter la sorte de 'find'
<li> Utiliser un remplacement de commande
</ul>""")),
        Bad(Comment(Contain('-exec') & ~Contain('\\;'),
                    "Ou est le ';' terminant la commande � ex�cuter ?")),
        Bad(Comment(Contain('-exec') & ~Contain('{}'),
                    "Ou est le '{}' indiquant le fichier � traiter ?")),
        shell_display,
        ),
    good_answer = """La version la plus efficace et fiable est la suivante :
    <pre>find . -name "*.c" -print0  |  xargs -0 wc</pre>
    La plus courte (mais qui ne marche pas en cas d'espace est :
    <pre>wc $( find . -name "*.c" )</pre>
    """,
    )

add(name="compte tout C",
    required = ["compte C", "concatener:concat C", "ligne", "chercher:xargs"],
    question="""Quelle est la ligne de commande la
    <tt>plus fiable et efficace</tt>
    permettant d'afficher le nombre de lignes contenu dans la concat�nation
    de tous le fichiers dont
    le nom se termine par <tt>.c</tt> � partir du r�pertoire courant.
    <p>
    Quand votre r�ponse s'ex�cute il faut que la commande <tt>wc</tt>
    ne soit ex�cut�e qu'une seule fois.
    Regardez bien les questions qui peuvent vous servir.
    """,
    tests = (
        Reject('total', """Ce n'est pas une bonne id�e de filtrer le mot
        <tt>total</tt> car il est li� � la langue de l'utilisateur"""),
        Good(Shell(Equal('find . -name "*.c" -print0|xargs -0 cat|wc -l'))),
        Reject('-exec', """Quand vous utilisez <tt>-exec</tt> il y a un
        processus lanc� par fichier. C'est trop lent.
        Utilisez la commande <tt>find</tt> seulement pour trouver
        les noms de fichiers"""),
        Bad(Comment(
            Shell(Equal('find . -name "*.c" -exec cat {} \\; | wc -l')),
            """La commande <tt>cat</tt> est lanc�e tr�s souvent.
            Ce n'est donc pas efficace""")),
        Bad(Comment(
            Shell(Equal('cat $(find . -name "*.c") | wc -l')),
            """Cette ligne ne fonctionnera pas s'il y a trop de fichiers
            car la commande 'cat' aura trop d'argument.""")),
        Bad(Comment(
            Shell(Equal('find . -name "*.c" -print0 | xargs -0 wc -l')
                  | Equal('wc -l $(find . -name "*.c")')
                  ),
            """Vous affichez le nombre de lignes de chacun des fichiers,
            pas le nombre total pour l'ensemble des fichiers.""")),
        Expect('find'),
        Expect('xargs',"Pour �tre performant il faut utiliser <tt>xargs</tt>"),
        Expect('-print0',
               """Il faut utiliser <tt>-print0</tt> (probl�mes des
               retours � la ligne dans les noms de fichier)"""),
        Expect('cat', """Il faut utiliser la command 'cat' pour concat�ner
        tous les fichiers avec de compter les lignes"""),
        Expect("wc"),
        Expect("-l", """Vous avez oubli� l'option de 'wc' qui indique que
               l'on veut compter le nombre de lignes"""),
        Bad(Comment(Contain('-print0') & Contain('xargs') & ~Contain('-0'),
                    """Il manque l'option de 'xargs' indiquant que le
                    s�parateur sur l'entr�e standard est le code NULL et
                    non le retour � la ligne.""")),
        shell_display,
        ),
    )

##add(name="Compte tout C",
##    required = ["Compte C", "ligne"],
##    question = """Donnez la commande qui affiche le nombre <b>TOTAL</b> de
##    lignes contenu dans chacun des fichiers se terminant
##    par <tt>.c</tt> � partir du r�pertoire courant.""",
##    tests = (
##        Reject('wc -', "Pas besoin d'option pour <tt>wc</tt>"),
##        Expect('find'),
##        Expect('-name'),
##        Expect('*.c'),
##        Bad(Comment(~ Contain('"*.c"'),
##                    "Auriez-vous oubli� de prot�ger l'�toile")),
##        Good(Shell(Equal('wc $(find . -name "*.c"'))),
##        Good(Shell(Equal('find . -name "*.c" -exec wc {} \\;'))),
##        Good(Shell(Equal('find . -name "*.c" | xargs wc'))),
##        Good(Shell(Equal('find . -name "*.c" -print0 | xargs -0 wc'))),
##        ),
##    )




