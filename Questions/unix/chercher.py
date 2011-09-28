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
    required=["manuel:chercher", "sh:r�pertoire courant",
              "sh:r�pertoire connexion"],
    question="""Quel est le nom de la commande permettant de trouver
    des fichiers dans une hi�rarchie de fichier&nbsp;?""",
    tests=(
    reject('ls', "<tt>ls</tt> permet de les voir, pas de les chercher"),
    reject('grep', "<tt>grep</tt> cherche dans les fichiers pas les fichiers"),
    good("find"),
    ),
    indices=("C'est le mot 'trouver' en anglais",
             ),
    )

find_required = require("find",
                        "Pour chercher des fichiers on utilise <tt>find</tt>")

find_dot_required = require("find .",
                            """On demande � <tt>find</tt> de chercher partout
                            dans le r�pertoire courant.
                            <p>
                            Les premiers arguments de <tt>find</tt> sont
                            les endroits o� l'on cherche.
                            Il est possible de chercher � un seul endroit.
                            <p>
                            Ne pas indiquer l'endroit ou l'on cherche
                            fonctionne peut-�tre sous linux,
                            mais pour beaucoup d'autres syst�mes UNIX
                            cela ne fonctionnera pas.
                            """)

find_usr_lib_required = require("find /usr/lib",
                                """On demande � <tt>find</tt> de chercher
                                partout dans <tt>/usr/lib</tt>""",
                                replace=(('  ',' '),))

find_name_required = require(
    "-name",
    """Il faut indiquer que le crit�re de recherche est le nom""")

find_dash_required = reject(
    (" type", " name", " o", " size"),
    """Vous oubliez le <tt>-</tt> devant l'option""")

find_pattern_protect_required = reject(
    " *",
    """Il faut prot�ger le <em>pattern</em> sinon c'est le shell
    qui fait la substitution et le <tt>find</tt> ne verra
    pas le <em>pattern</em>""")

find_tilde_required = require("~",
                              "On cherche dans le r�pertoire de connexion.")

dumb_replace = (
    ("./ ", ". "),
    ("~/ ", "~ "),
    ("GIF", "gif"),
    ("PNG", "png"),
    ("JPG", "jpg"),
    ("Gg", "gG"), ("Ii", "iI"), ("Ff", "fF"),
    ('-or', '-o'),
    ('-and', '-a'),
    (' -print', ''),
    (' a-x ', ' -x '),
    (' a+x ', ' +x '),
    )

dumb_replace_remove_type_f = list(dumb_replace) + [('-type f', '')]

add(name="simple",
    required=["intro"],
    question="""Quelle ligne de commande permet d'afficher
    les noms des r�pertoires et fichiers (de n'importe quel type)
    qui se nomment <tt>toto</tt>
    dans la hi�rarchie dont la racine est le r�pertoire courant&nbsp;?""",
    tests=(
    shell_good("find . -name toto", dumb_replace=dumb_replace),
    shell_bad(("find toto", "find ./toto"),
              """<tt>toto</tt> est la hi�rarchie ou la commande <tt>find</tt>
              va lister tous les fichiers quelque soit leurs noms.
              <p>
              Elle ne va donc pas chercher les fichiers nomm�s
              <tt>toto</tt> dans le r�pertoire courant"""),
    shell_bad("find -name toto",
              """Cette ligne de commande fonctionne peut �tre
              sur votre machine, mais pas sur un Unix standard.
              Vous devez sp�cifier le(s) r�pertoires o� chercher.
              """),
    reject("-iname",
           """On ne veut pas trouver les fichiers TOTO en majuscule.
           Il ne faut donc pas utiliser <tt>-iname</tt>"""),
    find_required, find_dot_required, find_name_required,
    reject("*",
           """On veut les fichiers qui se nomment <tt>toto</tt>
           pas ceux qui commence ou finissent par <tt>toto</tt>"""),
    reject("./", """Utilisez <tt>.</tt> plut�t que <tt>./</tt>"""),
    shell_display,
    ),
    indices=("Le test doit �tre r�alis� sur le nom (<em>name</em>) du fichier",
             ),
    )

add(name="fichier",
    required=["intro"],
    question="""Quelle ligne de commande permet d'afficher
    tous les fichiers de type texte (qui ne sont pas des r�pertoire,
    ni des liens symboliques, ni des p�riph�riques...)
    dans la hi�rarchie dont la racine est le r�pertoire courant&nbsp;?""",
    tests=(
    shell_good("find . -type f", dumb_replace=dumb_replace),
    find_required, find_dot_required, find_dash_required,
    require("-type",
            """Vous avez oubliez d'imposer le type de fichier recherch�"""),\
    number_of_is('-', 1, """On a besoin que d'un seule option pour cette
    commande&nbsp;: celle qui indique le type de fichier recherch�"""),
    reject(('*', 'name'), "On ne doit pas faire de test sur le nom"),
    reject('!', """Pas besoin de n�gation, on veut seulement
    les objets de type <tt>f</tt> comme fichier"""),
    shell_display,
    ),
    indices=("Le test doit �tre r�alis� sur le type du fichier",
             ),
    )

add(name="taille",
    required=["intro"],
    question="""Quelle ligne de commande permet d'afficher
    tous les noms de fichiers (ou r�pertoires) de plus de 1024ko
    qui sont dans la hi�rarchie
    dont la racine est </tt>/usr/lib</tt>&nbsp;?""",
    tests=(
    find_required, find_usr_lib_required, find_dash_required,
    require("-size",
            """Vous devez mettre l'option indiquant que le crit�re
            de recherche est la taille"""),
    reject("1M", """Avec 1M ce n'est pas portable, c'est-�-dire qu'il y
    a des syst�mes Unix pour lesquels cette option ne fonctionnera pas
    car elle n'est pas standard"""),
    require("1024", "Il faut indiquer la taille"),
    require("1024k", "Il faut indiquer l'unit� de mesure de taille"),
    require("+1024k",
            """Il faut indiquer que vous recherchez les fichiers
            plus grand que <tt>1024k</tt> pas seulement ceux
            qui font exactement cette taille."""),
    reject("ko",
           """L'unit� kilo-octet est sp�cifi� par <tt>k</tt>
           pas par <tt>ko</tt>"""),
    reject("-size 1024",
            """Il faut indiquer que vous �tes int�ress� par
            les fichiers qui sont plus grand que"""),
    reject("*", """Pas besoin d'�toile la commande cherche
    dans toute l'arborescence"""),
    reject("-type", """Pas besoin de chercher un type particulier,
    on veut tous les types de fichiers possibles"""),
    shell_good("find /usr/lib -size +1024k",
               dumb_replace=dumb_replace_remove_type_f),
    shell_display,
    ),
    indices=(
    """Les arguments num�riques de <tt>find</tt> peuvent
    �tre pr�c�d�s de <tt>-</tt> pour dire 'moins de' et
    <tt>+</tt> pour dire 'plus de'.""",
    ),    
    )

add(name="vide",
    required=["taille"],
    question="""Afficher les noms de tous les fichiers de la
    hi�rarchie <tt>/etc</tt> qui sont vides (contiennent 0 octets)""",
    tests=(
    reject(('-0','+0'), """La taille recherch�e n'est ni plus grande
    ni plus petite que 0, donc pas de symbole moins ou plus"""),
    find_required, find_dash_required,
    reject('-empty', """C'est bien, vous avez trouv� l'option <tt>empty</tt>.
    Votre commande marche peut �tre.
    Mais n'est ce pas plus simple d'�crire que la taille est nulle&nbsp;?
    <p>
    Il est plus rapide d'utiliser ce que l'on connait d�j� plut�t
    que de chercher dans la documentation des options
    qui n'existent peut-�tre pas.
    """),
    require('/etc', "On veut chercher dans <tt>/etc</tt>"),
    require('0', "Un fichier vide a une taille de 0 !"),
    number_of_is('/', 1, "Pas besoin de mettre des / inutiles"),
    reject('=', """Il faut un espace, pas un �gale entre le
    param�tre et sa valeur"""),
    shell_good(("find /etc -size 0",
                "find /etc -size 0k",
                "find /etc -size 0b",
                "find /etc -size 0c",
                ),
               dumb_replace=dumb_replace_remove_type_f),
    shell_display,
    ),
    indices=("On n'a pas besoin d'indiquer les unit�s pour z�ro&nbsp!",
             ),
    )


add(name="ex�cuter",
    required=["simple", "copier:simple"],
    before="""La commande <tt>find</tt> peut d�clencher l'ex�cution
    d'une ligne de commande shell chaque fois qu'elle trouve
    un fichier.
    La ligne suivante affiche les fichiers trouv�s avec <tt>ls</tt>&nbsp;:
    <pre>find . -name "*.c" -exec ls -ld {} \;</pre>""",
    question="""Modifiez la ligne pr�c�dente, pour faire
    une copie de tous les fichiers qui se terminent par <tt>.c</tt>
    en leur ajoutant l'extension <tt>.bak</tt>.
    Par exemple <tt>toto.c</tt> doit �tre copi� dans <tt>toto.c.bak</tt>
    """,
    tests=(
    require(("find", "-exec", '"*.c"', ' . '),
            "Repartez de la ligne donn�e en exemple"),
    require("cp",
            "Pour faire la copie, on utilise la commande <tt>cp</tt>"
            ),
    require("{}",
            """<tt>find</tt> remplace tous les <tt>{}</tt>
            qui sont apr�s le <tt>-exec</tt>
            et ex�cute la commande pour chacun
            des fichiers qu'il trouve."""
            ),
    require("{}.bak",
            """Le nom du fichier destination n'appara�t pas.
            C'est le nom du fichier trouv� avec <tt>.bak</tt> derri�re.
            C'est donc&nbsp;: <tt>{}.bak</tt>
            """
            ),
    number_of_is("{}", 2,
                 """La commande <tt>cp</tt> utilise 2 arguments,
                 le nom de l'original et le nom de la copie.
                 Vous n'en fournissez qu'un seul"""),
    require("\\;",
            """Vous avez oubli� le <tt>\\;</tt> final
            qui indique la fin de l'action <tt>-exec</tt>"""
            ),
    require(" \\;",
            """Il faut un espace avant le <tt>\\;</tt> final"""),
    reject("ls", """On vous demande pas de lister les informations
    sur les fichiers, on veut les copier"""),
    shell_good("find . -name '*.c' -exec cp {} {}.bak \;",
               dumb_replace=dumb_replace + (('-type f ',''),)),
    shell_display,
    ),
    )

add(name="xargs",
    required=["ex�cuter", "pipeline:intro"],
    before="""Quand il y a beaucoup de fichiers � traiter, utiliser
    l'option <tt>-exec</tt> est long car cela lance un processus � chaque fois.
    <p>
    Pour �viter ce probl�me, on utilise la commande <tt>xargs</tt>
    qui lance la commande pass�e en argument en lui ajoutant les
    valeurs lues sur l'entr�e standard.
    <p>
    S'il y a beaucoup d'arguments, alors la commande sera lanc�es plusieurs
    fois pour ne pas mettre trop d'arguments.
    """,
    question="""Qu'est-ce que la commande suivante affiche&nbsp;?
    <pre>echo 'a
*
b     B
c
d' | xargs echo</pre>
    """,
    tests = (
        Good(Equal('a * b B c d')),
        )
    )

add(name="xargs rm",
    required=["xargs", "detruire:simple"],
    before = """Si vous avez des milliers de fichiers dans un r�pertoire,
    la commande <tt>rm *</tt> ne va pas se lancer car il y en a trop.
    Il faut alors proc�der autrement.""",
    question = """On supposera que les fichiers ne contiennent pas
    de caract�res sp�ciaux.
    <p>
    Donnez la ligne de commande d�truisant tous les fichiers du r�pertoire
    courant, m�me s'il y en a beaucoup&nbsp;:""",
    tests = (
        Good(Shell(Equal("echo * | xargs rm"))),
        Good(Shell(Equal("ls | xargs rm"))),
        Bad(Shell(Comment(Equal("rm *"),
                          "On vous a dit que cela ne fonctionnait pas!"))),
        Expect('rm'),
        Expect('xargs',
               """La commande <tt>xargs</tt> sert � d�couper en morceaux
               plus petits"""),
        Expect('|',
               """On utilise un pipeline pour ne pas passer par un fichier
               interm�diaire."""),
        ),
    )
    
add(name="pattern",
    required=["simple", "sh:affiche �toile", "pattern:fini par tilde"],
    question="""Quelle ligne de commande permet d'afficher
    tous les fichiers et r�pertoires (de n'importe quel type)
    dont le nom se termine par <tt>~</tt> (tilde)
    dans la hi�rarchie dont la racine est le r�pertoire courant&nbsp;?""",
    tests=(
    shell_good("find . -name '*~'", dumb_replace=dumb_replace),
    find_required, find_dot_required, find_name_required,
    find_pattern_protect_required,
    reject("*.*",
           """Vous n'allez pas trouver les fichiers dont
           le nom ne contient pas de caract�re '<tt>.</tt>'"""),
    reject('\\~', """Pas la peine de prot�ger le tilde
    il est sp�cial seulement en premi�re lettre"""),
    reject('[~]', """Pourquoi mettre le tilde entre crochets,
    c'est un caract�re qui n'a pas de signification
    pour les <em>patterns</em>"""),
    require("*~", """Je ne vois pas le <em>pattern</em> indiquant
    que le nom du fichier se termine par <tt>~</tt>"""),
    reject('[*~]', """Le <em>pattern</em> indique que c'est une �toile
    ou un tilde"""),
    number_of_is('.',1, """Votre commande n'a besoin que d'un seul point,
    celui qui indique ou chercher"""),
                 
    shell_display,
    ),
    indices=("""N'oubliez pas que le shell remplace
    les patterns non prot�g�s qui sont sur la ligne de commande.""",
             ),
    )


add(name="et",
    required=["pattern", "taille", "fichier"],
    before="""Vous avez besoin de trouver les plus petites biblioth�ques
    partag�es du syst�me. Comment faire&nbsp;?""",
    question="""Quelle ligne de commande permet d'afficher
    les noms des fichiers qui respectent les crit�res suivants
    (dans l'ordre)&nbsp;:
    <ul>
    <li> dans la hi�rarchie <tt>/usr/lib</tt>
    <li> Des vrais fichiers : de type fichier texte, pas les liens symboliques
    ni les r�pertoires, ...
    <li> La taille est inf�rieure � 6 kilo octets.
    <li> Le nom se termine par <tt>.so</tt> (en respectant la casse).
    </ul>
    <p>
    <b>Respectez l'ordre des conditions sinon votre solution
    sera refus�e.</b>
    """,
    tests=(
    reject('+6', """<b>Moins</b> de 6 kilo-octets on vous a dit, pas plus."""),
    shell_good("find /usr/lib -type f -size -6k -name '*.so'",
               dumb_replace=dumb_replace,
               ),
    shell_good("find /usr/lib -type f -a -size -6k -a -name '*.so'",
               """Les <tt>-a</tt> ou <tt>-and</tt> sont inutiles,
               le ET est fait par d�faut.""",
               dumb_replace=dumb_replace,
               ),
    shell_good("find /usr/lib \\( -type f -a -size -6k -a -name '*.so' \\)",
               """Les <tt>\\(</tt> et <tt>\\)</tt> sont inutiles,
               car il n'y a pas d'ambiguit�""",
               dumb_replace=dumb_replace,
               ),
    find_pattern_protect_required,
    reject("-6 ", """Il faut indiquer l'unit� de mesure pour la taille"""),
    reject(' 6k', """Vous recherchez les fichiers dont la taille est exactement
    de <tt>6k</tt>, on veut les fichiers de taille inf�rieure."""),
    require("-6k", """Il faut indiquer la taille du fichier"""),
    reject('-iname', """On ne veut pas des fichiers avec l'extension <tt>.SO</tt> en majuscule, il faut donc respecter la casse."""),
    require('-name', """O� est l'option pour tester le nom&nbsp;?"""),
    require('-size', """O� est l'option pour tester la taille&nbsp;?"""),
    reject('/usr/lib/', """Le <tt>/</tt> apr�s <tt>/usr/lib</tt>
    ne sert � rien car ce n'est pas un lien symbolique mais un r�pertoire"""),
    require('.so', """On cherche les fichiers dont le nom se termine
    par <tt>.so</tt>"""),
    require('*.so', """Avant le <tt>.so</tt> il peut y avoir n'importe
    quoi, vous avez oubli� quelque chose."""),
    expect('/usr/lib'),
    require(' f ', "Le type d'un fichier texte normal est <tt>f</tt>"),
    reject('-a', "Simplifiez votre commande en enlevant les <tt>-a</tt>"),
    shell_display,
    ),
    bad_answer = """N'oubliez pas de faire les tests dans l'ordre
    indiqu� dans la question""",
    indices=("""N'oubliez pas que le shell remplace les patterns non prot�g�s
    qui sont sur la ligne de commande.""",
             """Avez-vous mis les param�tres dans l'ordre indiqu� dans
             la question&nbsp;?""",
             ),
    )

    
    

add(name="casse insensible",
    required=["pattern", "sh:r�pertoire connexion"],
    question="""Donner la ligne de commande permettant de rechercher
    toutes les images dont le nom se termine par <tt>.GIF</tt>
    dans votre r�pertoire de connexion (et au dessous).
    Malheureusement, la casse n'est pas toujours
    respect�e et peut �tre&nbsp;: <tt>.GIF</tt>, <tt>.gif</tt>,
    <tt>.Gif</tt>, ...
    <p>
    Vous ne devez pas lister tous les cas possibles
    en utilisant les crochets (<tt>[Gg][Ii][Ff]</tt>)
    """,
    tests=(
    reject('-type', "R�essayez sans donner l'option <tt>-type</tt>"),
    shell_good("find ~ -iname '*.gif'", dumb_replace=dumb_replace),
    shell_bad("find ~ -name '*.[gG][iI][fF]'",
              "Cela fonctionne, mais il y a plus simple (<tt>-iname</tt>)",
              dumb_replace=dumb_replace
              ),
    shell_bad(("find ~ -name *.gif", "find ~ -iname *.gif"),
              """On vous a d�j� expliqu� que la command <tt>find</tt>
              ne verrait pas le <em>pattern</em> s'il y avait un <tt>.gif</tt>
              dans le r�pertoire courant car
              le shell ferait la substitution""",
              dumb_replace=dumb_replace
              ),    
    require("find", "Vous devez utiliser la commande <tt>find</tt>"),
    find_tilde_required,
    require('*', """Vous devez donner un <em>pattern</em> indiquant
    qu'il y a n'importe quoi avant <tt>.gif</tt> vous devez
    donc utilisez une �toile"""),
    require("name",
            """Vous n'avez pas indiqu� que le crit�re de recherche
            est le nom du fichier"""),
    reject("-name",
            """<tt>-name</tt> permet de chercher en respectant la casse,
            ce n'est donc pas cette option qu'il faut utiliser"""),
    reject("-ilname",
           """-lname cherche dans le nom du fichier point�
           par le lien symbolique"""),
    reject(("'.gif'", "'.GIF'", '".GIF"', '".gif"'),
           """Vous cherchez les fichiers s'appellant '.gif'
           pas se terminant par '.gif'"""),
    require('.GIF',
            "Vous devez chercher les fichiers se terminant par <tt>.gif</tt>",
            uppercase=True
            ),
    require(' ~ ', """La fa�on la plus courte d'indiquer votre r�pertoire
    de connexion est la chaine de caract�re <tt>~</tt> (tilde)"""),
    reject('wholename',
           """L'option <tt>wholename</tt> n'a pas �t� vue en cours.
           D'autre part cette option teste le chemin complet et pas
           le nom court du fichier"""),
    
    shell_display,
    ),
    )

add(name="ou simple",
    required=["pattern"],
    question="""Ligne de commande permettant de rechercher
    tous les fichiers/r�pertoires de la hi�rarchie courante dont
    le nom se termine par
    <tt>.sh</tt> ou <tt>.pl</tt> ou <tt>.py</tt>
    (Ne changez pas l'ordre des 3 extensions dans votre commande.)
    """,
    tests=(
    reject('(-', "Il manque un espace apr�s la parenth�se ouvrante"),
    reject(('"\\)',"'\\)"), "La parenth�se fermante est un param�tre. Il manque un espace quelque part..."),
    shell_good(("find . -name '*.sh' -o -name '*.pl' -o -name '*.py'",
                "find . \\( -name '*.sh' -o -name '*.pl' -o -name '*.py' \\)",
                ),
               dumb_replace=dumb_replace),
    shell_good(("find . -name '*.sh' -o -name '*.p[ly]'",
                "find . \\( -name '*.sh' -o -name '*.p[ly]' \\)",
                ),
               """Vous �tes plus fort que le prof, pourquoi
               faites-vous cette UE&nbsp;?""",
               dumb_replace=dumb_replace),
    reject('-iname', """Il ne faut pas utiliser <tt>-iname</tt>
    car celui ci va trouver <tt>toto.SH</tt> et on ne le vous
    demande pas"""),
    find_required, find_dot_required, find_name_required,
    find_pattern_protect_required,
    reject('|', """Le <tt>|</tt> n'existe pas dans les <em>patterns<em>
    utilis�s par <tt>find</tt> et pour le <em>shell</em>, il
    n'est utilis� que pour le <tt>case</tt>."""),
    require(("*.sh", "*.py", "*.pl"),
            """Il manque au moins un <em>pattern</em> indiquant
            l'une des extensions � rechercher"""),
    number_of_is('-name',3,"Il faut r�p�ter 3 fois <tt>-name</tt>"),
    reject("-name -o",
           """<tt>-name -o</tt> indique que l'on recherche un fichier
           nomm� <tt>-o</tt>"""),
    reject('|', """Le <em>ou</em> n'est pas dans le <em>pattern</em>
    donn� comme param�tre de <tt>-name</tt>, c'est un param�tre
    sp�cifique � la commande <tt>find</tt>"""),
    require("-o", """N'oubliez pas d'indiquer que vous faites un ou"""),
    number_of_is(' ', 9,
                 """Dans la solution la plus courte, il y a 9 param�tres
                 qui sont pass�s � la commande <tt>find</tt>
                 (pensez � ne pas oublier d'espaces)"""),
    shell_display,
    ),
    indices=("Lire ce qu'�crit <tt>find --help</tt>",
             "'Ou' c'est <tt>-o</tt> ou <tt>-or</tt>",
             """N'oubliez pas d'indiquer l'option <tt>-name</tt>
             apr�s chaque <tt>-o</tt>""",
             "Faites attention aux espaces",
             ),
    )



add(name="images",
    required=["ou simple", "casse insensible"],
    question="""Donner la ligne de commande permettant d'afficher
    les noms de toutes les images <tt>.GIF</tt>, <tt>.JPG</tt>, <tt>.PNG</tt>
    qui sont dans votre r�pertoire de connexion ou au dessous.
    �videmment on ne tient pas compte de la casse.
    <p>
    Respectez l'ordre <tt>.GIF</tt>, <tt>.JPG</tt>, <tt>.PNG</tt>
    sinon la r�ponse sera refus�e.
    """,
    tests=(
    require("-o", """N'oubliez pas d'indiquer que vous faites un
    <tt>ou</tt>. En effet par d�faut c'est un <tt>et</tt> et aucun
    fichier ne pourra correspondre."""),
    require('*', "S'il n'y a pas d'�toile, vous cherchez un nom exact."),
    shell_good(("find ~ -iname '*.gif' -o -iname '*.jpg' -o -iname '*.png'",
                "find ~ \\( -iname '*.gif' -o -iname '*.jpg' -o -iname '*.png' \\)",
                ),
               dumb_replace=dumb_replace),
    reject("-name", "On va a dit de ne pas tenir compte de la casse"),
    require('-iname', """On a vu dans un exercice pr�c�dent comment
    test sans tenir compte de la casse"""),
    find_tilde_required,
    require(('*.gif', '*.jpg', '*.png'),
                 """Je ne vois pas les 3 <em>pattern</em> testant
                 les 3 extensions""",
            replace=dumb_replace),
    number_of_is('-iname',3,"Je ne vois pas 3 tests sur les noms de fichiers"),
    number_of_is('-o',2, "Je ne vois pas 2 <tt>ou</tt>"),
    reject('(-', "N'auriez-vous pas oubli� un espace apr�s la parenth�se ouvrante&nbsp;?"),
    shell_display,
    ),
    indices=("Lire ce qu'�crit <tt>find --help</tt>",
             "ou = -o = -or",
             "Ne changez pas l'ordre des tests",
             "Faites attention aux espaces",
             ),
    )


    
