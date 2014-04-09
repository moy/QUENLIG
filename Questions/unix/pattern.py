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

etc_required = require("/etc", "On cherche dans <tt>/etc</tt>")
echo_required= require("echo", "On vous dit d'utiliser <tt>echo</tt>")

add(name="intro",
    required=["sh:affiche param�tre", "sh:configurer"],
    question="""En utilisant la commande <tt>echo</tt>&nbsp;:
    Donner la commande affichant la liste des fichiers et
    r�pertoires contenus dans <tt>/etc</tt> dont le nom
    commence par la lettre 'a'""",
    tests=(
    shell_good("echo /etc/a*"),
    shell_bad(("echo /etc/*a", "echo /etc/*a*"),
              "On vous a dit : <b>commence par la lettre <tt>a</tt></b>"),
    etc_required, echo_required,
    reject('|', """On utilise que la commande <tt>echo</tt>, aucune autre
    commande n'est utile"""),
    reject("ls",
           """On a pas besoin de <tt>ls</tt> car le
           remplacement du <em>pattern</em> fait
            le m�me travail"""),
    reject("find",
           """<tt>find</tt> cherche en profondeur
           ici on veut simplement les fichiers
           qui sont directement dans <tt>/etc</tt>"""),
    expect('a'),
    require('*', """Vous avez besoin de l'�toile pour indiquer la chaine
    de caract�res quelconque qui est apr�s le 'a'"""),
    reject('-', "Pas besoin d'arguments"),
    number_of_is(' ', 1, "Il y a un seul espace dans la r�ponse"),
    ),
    )

require_star = require("*",
                       """Il faut utiliser un <em>pattern</em>
                       repr�sentant une chaine de caract�res
                       quelconques de longueur quelconque.
                       On peut l'utiliser plusieurs fois.""")

reject_dot_slash = reject("./",
                           """Pourquoi indiquer le r�pertoire courant avec
                           <tt>./</tt>&nbsp;?,
                           par d�faut, les noms des fichiers sont relatifs
                           par rapport � lui.""")

star_indice = """Le symbole repr�sentant une chaine de quelconque
    est <tt>*</tt>"""

add(name="tout",
    required=['intro'],
    question="""En utilisant la commande <tt>echo</tt>&nbsp;:
    Donner la commande affichant la liste des fichiers et
    r�pertoires contenus dans le r�pertoire courant.
    <p>
    On ne tiendra pas compte des fichiers cach�s.""",
    tests=(
    shell_good("echo *"),
    shell_bad("echo *.*", "Seul les noms contenant un point seront affich�s"),
    echo_required,
    require_star,
    reject_dot_slash,
    reject('~', "Dans le r�pertoire courant, pas celui de connexion"),
    ),
    indices=(star_indice,
             ),
   )

add(name="d�but fin",
    question="""En utilisant la commande <tt>echo</tt>&nbsp;:
    Donner la commande affichant la liste des fichiers et
    r�pertoires contenus dans <tt>/etc</tt> qui commencent
    par une majuscule et qui se terminent par un chiffre.
    """,
    tests=(
    shell_good("echo /etc/[A-Z]*[0-9]"),
    etc_required, echo_required,
    reject("[1-9]", "Z�ro est un chiffre&nbsp;!"),
    reject('Q', "Vous n'allez quand m�me pas lister tout l'alphabet&nbsp;!"),
    reject('2', "Vous n'allez quand m�me pas lister tous les chiffres&nbsp;!"),
    require(('[',']'), """On utilise les crochets pour indiquer une liste
    de caract�res"""),
    require('-', """On utilise le tiret pour indiquer un interval
    de caract�res"""),
    require("[0-9]", "On cherche un chiffre"),
    require("[A-Z]", "On cherche une lettre majuscule"),
    reject('.*', """La syntaxe <tt>.*</tt> est pour les expressions r�gul�eres,
    par pour les <em>pattern</em>"""),
    ),
   )

add(name="0 au milieu",
    question="""En utilisant la commande <tt>echo</tt>&nbsp;:
    Donner la commande affichant la liste des fichiers et
    r�pertoires contenus dans <tt>/etc</tt> qui contiennent
    le chiffre '0' n'importe ou dans leur nom.
    """,
    tests=(
    shell_good("echo /etc/*0*"),
    shell_good("echo /etc/*[0]*", "<tt>echo /etc/*0*</tt> �tait plus simple"),
    shell_bad("echo /etc/*0",
              """Cela n'affiche que les fichiers dont le nom ce termine par
              un caract�re <tt>0</tt>"""),
    shell_bad("echo /etc/0*",
              """Cela n'affiche que les fichiers dont le nom commence par
              un caract�re <tt>0</tt>"""),
              
    etc_required, echo_required,
    require("0", "Ne confondez pas z�ro avec la lettre 'o'"),    
    reject("[0]",
           "Pourquoi mettre <tt>[0]</tt> alors que <tt>0</tt> suffit&nbsp;?"),
    ),
   )

add(name="chemin",
    question="""Dans '/etc' il y a des r�pertoires dont le nom commence
    par 'rc', ces r�pertoires contiennent des fichiers
    dont le nom commence par 'S2'.
    <p>
    Utilisez la commande <tt>echo</tt> et le <em>globbing</em>
    pour afficher la liste de ces fichiers.
    """,
    tests=(
    reject('cd', "Vous n'avez besoin que de <tt>echo</tt>"),
    shell_good("echo /etc/rc*/S2*"),
    etc_required, echo_required,
    require("/rc", "Le nom du deuxi�me niveau commence par <tt>rc</tt>"),    
    require("/S2", "Le nom du troisi�me niveau commence par <tt>S2</tt>"),
    reject("/rc/", """Le nom du r�pertoire n'est pas <tt>rc</tt> mais
    commence par <tt>rc</tt>"""),    
    require('S2*', """Le nom des fichiers n'est pas <tt>S2</tt> mais commence
    par <tt>S2</tt>"""),
    ),
    )

add(name="sous r�pertoires",
    question="""En utilisant la commande <tt>echo</tt>.
    Donner la commande affichant la liste des r�pertoires
    contenus dans <tt>/etc</tt> (<em>pas les fichiers,
    seulement les r�pertoires</em>).
    """,
    tests=(
    shell_good( ("echo /etc/*/.", "echo /etc/*/") ),
    etc_required, echo_required,
    shell_bad("echo /etc/*",
              "Cela affiche aussi les fichiers dans <tt>/etc</tt>"),
    shell_bad("echo /etc/.", "Cela affiche <tt>/etc/.</tt>"),
    reject('ls', 'On a pas besoin de <tt>ls</tt>'),
    reject('-', "On a pas besoin d'option"),
    ),
    indices=("Seul un r�pertoire peut contenir un fichier nomm� '.'",
             """On peut mettre une �toile entre deux <tt>/</tt> elle
             sera alors remplac�e par tous les noms de r�pertoires.""",
             ),
   )

add(name="fini par tilde",
    required=['intro'],
    question="""En utilisant la commande <tt>echo</tt>&nbsp;:
    Donner la commande affichant la liste des fichiers et
    r�pertoires contenus dans le r�pertoire courant dont le nom se
    termine par <tt>~</tt> (tilde)""",
    tests=(
    reject('echo ~',
           'Dans le r�pertoire courant, pas le r�pertoire de connexion'),
    shell_good("echo *~"),
    echo_required,
    require_star,
    reject_dot_slash,
    reject('/', "Pas besoin de / c'est dans le r�pertoire courant"),
    ),
   )

add(name=".c et .h",
    required=['fini par tilde'],
    question="""En utilisant la commande <tt>echo</tt>&nbsp;:
    Donner la commande affichant la liste des fichiers et
    r�pertoires contenus dans le r�pertoire courant dont le nom se
    termine par <tt>.c</tt> ou bien <tt>.h</tt>""",
    tests=(
    reject(('C','H'), "La casse compte"),
    shell_good(("echo *.[ch]", "echo *.[hc]")),
    shell_bad(("echo *.c *.h", "echo *.h *.c"),
              """Il y a plus court, avec une seule �toile."""),
    shell_bad('echo *[.c.h]',
              """Cela affiche les noms qui se terminent par un
              caract�re '<tt>.</tt>' ou '<tt>c</tt>' ou '<tt>h</tt>'
              <p>
              De plus les crochets repr�sentent un ensemble,
              cela ne sert � rien de mettre deux fois le m�me symbole dedans.
              """),
    reject(('[c]', '[h]'),
           """� quoi cela sert d'avoir une liste contenant
           un seul caract�re&nbsp;?
           Autant taper le caract�re lui m�me."""),
    echo_required,
    require_star,
    reject_dot_slash,
    number_of_is('*', 1,
                 """On attend une r�ponse avec une seule �toile
                 suivie d'un caract�re qui est un <tt>c</tt>
                 ou un <tt>h</tt>"""),
    shell_bad("echo *[ch]",
              """S'il y a un fichier <tt>tic</tt> il sera affich�,
              et ce n'est pas ce que l'on demande"""),
    shell_bad("echo *.c .h",
              """Affiche la liste des fichiers dont le nom se termine
              par <tt>.c</tt><p> suivi de la chaine de caract�re <tt>.h</tt>
              qui ne repr�sente pas un fichier."""),
    shell_bad(("echo *[.ch]", "echo *[.hc]"),
              """Affiche les noms de fichier se terminant
    par <tt>.</tt> ou <tt>c</tt> ou <tt>h</tt>"""),
    reject("[c h]", """<tt>[c h]</tt> repr�sente un <tt>c</tt> ou un
    <tt>espace</tt> ou un <tt>h</tt>"""),
    reject('|',
           """Le pipe (<tt>|</tt>) ne fait pas parti des <em>pattern</em>
           du <em>shell</em> mais des expressions r�guli�res"""),
    require('.', "Il doit y avoir un caract�re '.' dans le nom du fichier"),
    reject('{', "Les acolades ne sont pas standard. Ne les utilisez pas"),
    reject(',',
           "Il n'y a pas de virgule dans la syntaxe des <em>pattern</em>"),
    
    answer_length_is(11, "La r�ponse attendue fait 11 caract�res"),
    ),
    indices=(star_indice,
             """Utilisez le pattern d�signant un ensemble de caract�res
             pour indiquer qu'apr�s le <tt>.</tt> il y a <tt>c</tt>
             ou <tt>h</tt>""",
             """Il faut utiliser les crochets.""",
             ),
   )

add(name="inverse",
    required=["0 au milieu", ".c et .h"],
    question="""En utilisant la commande <tt>echo</tt>.
    Donner la commande affichant la liste des fichiers et
    r�pertoires contenus dans <tt>/etc</tt> dont le nom
    contient au moins un caract�re qui ne soit PAS&nbsp;:
    <ul>
    <li> -
    <li> .
    <li>lettre minuscule
    <li>lettre majuscule
    <li>num�rique
    </ul>
    Conservez l'ordre pour que votre r�ponse soit accept�e (j'ai pas
    envie de tester tous les cas possibles).
    <em>Pour que cela fonctionne dans la r�alit�, le tiret doit �tre en premier pour ne pas d�signer un intervalle.</em>
    """,
    tests=(
    shell_good("echo /etc/*[!-.a-zA-Z0-9]*"),
    echo_required, etc_required,
    reject('\\',
           "Pas besoin d'<em>antislash</em> pour r�pondre � cette question"),
    shell_bad("echo /etc/[!-.a-zA-Z0-9]",
              """Vous ne trouvez que des noms de fichier ne comportant
              qu'un seul caract�re"""),
    shell_bad("echo /etc/*[!-.a-zA-Z0-9]",
              """Vous ne trouverez pas <tt>/etc/=a</tt>
              qui contient un caract�re interdit mais se termine
              par un caract�re autoris�"""),
    shell_bad("echo /etc/[!-.a-zA-Z0-9]*",
              """Vous ne trouverez pas <tt>/etc/a=</tt>
              qui contient un caract�re interdit mais commence
              par un caract�re autoris�"""),
    reject(("]]", "]["), "N'imbriquez pas les crochets, une seule paire suffit"),
    reject('![', """Le <tt>!</tt> de la n�gation est juste apr�s
    le crochet ouvrant, pas avant."""),
    require("!", "La n�gation s'indique avec le <tt>!</tt>"),
    number_of_is('!', 1, "Une seule n�gation est suffisante"),
    require("a-z", "Et les minuscules&nbsp;?"),
    require("A-Z", "Et les majuscules&nbsp;?"),
    require("0-9", "Et les nombres&nbsp;?"),
    require("-.", "Et le tiret et le point&nbsp;? Il faut conserver l'ordre."),
    require("-.a-zA-Z0-9", "Il faut conserver l'ordre"),
    ),
    good_answer="Si 'echo' vous affiche <tt>/etc/*[!-.a-zA-Z0-9]*</tt> c'est que '/etc' ne contient pas de tel fichier",
   )

add(name="final",
    required=["inverse", "sous r�pertoires"],
    question="""En utilisant la commande <tt>echo</tt>.
    affichez tous les fichiers avec l'extension <tt>.h</tt>
    qui sont dans des sous r�pertoires <em>directs</em>
    de <tt>/usr/include</tt>""",
    tests=(
    shell_good("echo /usr/include/*/*.h"),
    shell_bad("echo /usr/include/*/./*.h",
              "Il y a 2 caract�res en trop dans votre commande"),
    echo_required,
    reject("/usr/include/*.h",
           """Vous indiquez les <tt>.h</tt> qui sont dans
           <tt>/usr/include</tt>, pas dans ses sous-r�pertoires"""),
    reject("[h]", """Il est plus simple d'�crire <tt>h</tt> que <tt>[h]</tt>
    et cela fait la m�me chose"""),
    require("/usr/include",
            "On vous demande de chercher dans <tt>/usr/include</tt>"),
    number_of_is('*', 2, """Il faut une �toile pour indiquer
    n'importe quel sous r�pertoire, et une autre pour indiquer
    qu'il y a n'importe quoi avant le <tt>.h</tt>"""),
    require_endswith(".h", """On veut lister les noms de fichiers qui
    se terminent par <tt>.h</tt>"""),
    ),
    )





