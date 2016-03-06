# -*- coding: latin-1 -*-
#    QUENLIG: Questionnaire en ligne (Online interactive tutorial)
#    Copyright (C) 2005-2010 Thierry EXCOFFIER, Universite Claude Bernard
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
import random
from . import remplacer

add(name="console",
    before="""Pour faire la suite de ce TP vous devrez taper des commandes
    shell ou bien dans une console texte accessible par Controle-Alt-F1
    ou bien dans un �mulateur de terminal comme :
    <ul>
    <li> xterm (je recommande vivement celui-ci)
    <li> gnome-terminal
    <li> eterm
    </ul>
    <p>
    Vous pouvez lancer le terminal :
    <ul>
    <li> � partir d'un clique bouton droit sur le fond d'�cran,
    <li> un clique bouton gauche sur un icone �mulateur de terminal
    <li> � partir du menu contenant toutes les applications.
    </ul>
    <p>Je vous conseille de mettre le navigateur web cote � cote
    avec le terminal comme cela vous pouvez voir les 2 en m�me
    temps et faire du copi� coll�.
    """,
    question="""
    Lancez un �mulateur de terminal, quelle est la cha�ne
    de caract�re exacte qu'il y a � gauche du curseur&nbsp;?
    """,
    bad_answer = """Auriez-vous par hasard chang� votre environnement
    pour qu'il affiche autre chose que le <em>prompt</em> standard
    en modifiant la variable <tt>PS1</tt> dans vos scripts <tt>.profile</tt>
    ou <tt>.bashrc</tt>&nbsp;?
    <p>
    Pour revenir au <em>prompt</em> standard, tapez EXACTEMENT :
    <pre>. /etc/profile</pre>
    """,
    good_answer = """Ce que vous venez de taper s'appel un <em>prompt</em>,
    il vous indique que le shell est pr�t � lire la commande que vous
    allez taper.""",
    indices=("""Cette cha�ne se termine g�n�ralement par un $ et un espace.""",),
    tests=(
    good("###$", "C'est le prompt par d�faut dans l'UFR informatique, le vrai prompt par d�faut est historiquement `$&nbsp;�"),
    require_endswith('$'),
    good_if_contains(''),
    ),
    required = ["intro:final", "navigation:final"]
    )

add(name="configurer",
    required=["console", "intro:copier coller"],
    before="""Editez avec <tt>vi</tt> ou <tt>emacs</tt> ou <tt>xemacs</tt>
    le fichier <tt>.bashrc</tt> � la racine de votre
    compte (n'oubliez pas le point, cr�ez le fichier s'il n'existe pas).
    Et ajoutez dedans&nbsp;: <tt>export LC_COLLATE=C</tt>
    <p>
    <b>Fermer votre terminal et ouvrez en un autre pour que
    cette modification soit prise en compte</b>.
    <p>
    Si vous avez bien fait cette manipulation alors les tris
    seront faits dans l'ordre des codes ASCII et non l'ordre
    des lettres en fran�ais.
    Si cela vous g�ne pour d'autres TP, enlevez cette ligne
    de votre <tt>.bashrc</tt>.
    """,
    question="""La r�ponse � cette question est : ce que
    la commande suivante affiche&nbsp;:
    <tt>echo -e 'a\\nB' | sort</tt>""",
    nr_lines = 3,
    tests=(
    good("B\na"),
    reject("a\nB",
        """La commande que vous avez mise dans le <tt>.bashrc</tt>
        ne s'est pas ex�cut�e.
        Si vous avez vraiment suivi toutes les indications
        et que vous n'arrivez pas � trouver le probl�me
        demandez � un enseignant."""),
    reject(("echo","sort"),
        """La r�ponse n'est pas la commande elle m�me mais
        ce qu'elle affiche.
        Il vous suffit de faire un copier/coller dans la console
        pour voir le r�sultat puis le recopier dans la r�ponse"""),
    reject('Done',
           "Relancez la commande pour voir si cela affiche la m�me chose"),
    ),
    )

casse = "Majuscule et minuscule sont diff�rentes"


add(name="change r�pertoire",
    question="""Quelle est la commande (builtin) permettant
    de changer de r�pertoire courant&nbsp;?""",
    tests=(
    good("cd"),
    bad(("Cd", "CD"), casse),
    bad("pwd", "Cela affiche le r�pertoire courant, cela ne le change pas"),
    ),
    )

add(name="aller dans",
    question="""Quelle commande tapez-vous pour que le
    r�pertoire courant devienne <tt>/usr/bin</tt>&nbsp;?""",
    tests=(
    shell_good("cd /usr/bin"),
    shell_bad("cd /usr/bin/", "Le / final ne sert � rien dans ce cas."),
    shell_bad("cd usr/bin",
              """Cette commande ne fonctionne que si votre r�pertoire courant
              est sur la racine, il faut un chemin absolu."""),
    require("/usr/bin",
            "Je ne vois pas l'endroit ou vous devez allez dans la commande"),
    shell_display,
    ),
    )

add(name="r�pertoire connexion",
    required=["aller dans", "navigation:r�p. connexion"],
    question="""Quelle est la cha�ne de caract�re la plus
    courte repr�sentant le fichier nomm� <tt>a</tt> dans votre r�pertoire
    de connexion&nbsp;?""",
    tests=(
    good("~/a"),
    bad("$HOME/a", "Il y a plus court"),
    bad('/a', "Cela repr�sente le fichier <tt>a</tt> � la racine"),
    bad('~a/', """Cela repr�sente le r�pertoire de connexion
        de l'utilisateur <tt>a</tt>"""),
    bad(('./a','a'),
        "Cela repr�sente le fichier <tt>a</tt> du r�pertoire courant"),
    require("~",
            """Je ne vois pas le symbole qui repr�sente votre
            r�pertoire de connexion"""),
    reject(" ", """On ne demande pas une commande, seulement le nom
    du r�pertoire"""),
    bad('~a', """Vous venez de donner le nom du r�pertoire
    de connexion de l'utilisateur nomm� <tt>a</tt> au lieu de
    celui de l'utilisateur tapant la commande."""),
    expect('a'),
    ),
    )

add(name="r�pertoire connexion 2",
    required=["aller dans", "navigation:r�p. connexion"],
    question="""Quelle est la commande la plus courte vous permettant
    d'aller dans votre r�pertoire de connexion&nbsp;?""",
    tests=(
    good("cd"),
    expect('cd'),
    answer_length_is(2, "La r�ponse est en 2 lettres&nbsp;!"),
    ),
    )

add(name="r�pertoire courant",
    required=["r�pertoire connexion", "navigation:ici"],
    question="""Quel que soit l'endroit ou vous vous trouvez
    dans le syst�me de fichier&nbsp;:<br>
    Quelle est la chaine de caract�res (toujours la m�me)
    qui est un des noms du r�pertoire dans lequel vous �tes&nbsp;?""",
    tests=(
    good("."),
    good("./", "Accept�, mais <tt>.</tt> est plus court"),
    bad(("/.",'/'), "Non, �a c'est la racine"),
    bad('..', "Non, �a c'est le p�re de l'endroit ou vous �tes"),
    bad(("~", "~/"), "Non, �a c'est le r�pertoire de connexion"),
    bad("$PWD", """Ceci n'est pas portable, de plus cela ne
    fonctionne pas quand on programme en C par exemple car
    c'est du shell"""),
    reject(("pwd", "cd"), "C'est une commande, pas un nom de fichier"),
    reject('~', """Le tilde indique votre r�pertoire de connexion
    pas l'endroit ou vous �tes"""),
    answer_length_is(1, "La r�ponse tient en 1 caract�re"),
    ),
    )

add(name="p�re",
    required=["aller dans", "navigation:p�re"],
    question="""Quelle commande tapez-vous pour
    changer de r�pertoire courant afin que celui ci devienne
    le p�re (le conteneur) du r�pertoire courant actuel&nbsp;?""",
    tests=(
    shell_good("cd .."),
    shell_bad("cd",
              "Cette commande vous envoit dans votre r�pertoire de ocnnexion"),
    bad("..", "Ceci n'est pas une commande mais le nom du p�re"),
    bad("cd..",
        """Vous auriez lanc� cette commande vous auriez vu qu'elle
        affiche <em>cd.. : command not found</em>
        <p>
        Il faut s�parer les arguments par des espaces."""),
    require("cd", """Je ne vois pas le nom de la commande permettant
    de changer de r�pertoire courant"""),
    shell_bad("cd /..", "Vous n'allez pas dans le p�re mais � la racine"),
    shell_bad("cd ../", "Un caract�re plus court s'il vous pla�t."),
    shell_bad(("cd .", "cd ./"), "Vous restez sur place&nbsp;!"),    
    shell_bad("cd ../.", "Deux caract�res plus court s'il vous pla�t."),
    shell_display,
    )
    )

add(name="directory courant",
    before="Changez votre r�pertoire courant en tapant <tt>cd /usr/include</tt>",
    question="""Quelle est la commande la plus courte affichant
    sur la sortie standard (l'�cran par d�faut)
    le texte qui suit&nbsp;:
    <pre>/usr/include</pre>""",
    tests=(
    good("pwd"),
    bad( ("PWD", "Pwd"), casse),
    reject("/usr/include",
           """Dans cet exercice,
           <tt>/usr/include</tt> est votre r�pertoire courant,
           pas besoin de l'indiquer sur la ligne de commande
           pour l'afficher."""),
    reject("cd",
           """On ne vous demande pas de changer de r�pertoire mais
           d'afficher le r�pertoire courant"""),
    reject("echo",
           """Pas besoin de la commande <tt>echo</tt>,
           la commande que l'on vous demande affiche elle m�me."""),
    ),
    indices=("C'est une commande ``builtin��",
             "C'est l'abbr�viation de <em>Print Working Directory</em>",
             ),
    )

def echo_text():
    c = "0123456789abcdefghijklmnopqrstuvwxyz"
    s = ""
    for a in range(40):
        s += c[random.randrange(len(c))]
    return s

def echo_simple_question():
    return "Quelle est la ligne commande qui lorsque elle est ex�cut�e affiche :<pre>%s</pre>Pensez � faire un copi�/coll�" % echo_text()

class echo_simple_answer(TestShell):
    def test(self, student_answer, string):
        if parse_only_not_commented('echo '+echo_text()) == student_answer[0]:
            return True, self.comment + student_answer[1]

add(name="affiche param�tre",
    question=echo_simple_question,
    tests=(
    echo_simple_answer(),
    bad("echo",
        """Quand vous tapez <tt>echo</tt> tout seul cela n'affiche pas
        la chaine de caract�res demand�e mais une ligne vide."""),
    shell_display,
    ),
    required=["intro:copier coller", "console"],
    indices=("C'est une commande ``builtin��",
             "Quand vous criez et qu'un instant apr�s ce cri revient, c'est un ...",
             )
    )

add(name="affiche param�tres sp�ciaux",
    question="""Quel commande permet d'afficher le texte suivant
    sur la sortie standard (l'�cran)&nbsp;:
    <pre>avant    apr�s</pre>
    Il y a 4 espaces entre les deux mots.
    <p>
    Testez la commande avant de donner la r�ponse.""",
    tests=(
    require('echo ', "On utilise la commande <tt>echo</tt>"),
    shell_good("echo 'avant    apr�s'"),
    shell_good( ( "echo avant \\ \\ \\ apr�s",
                  "echo avant\\ \\ \\  apr�s",
                  "echo avant \\ \\  apr�s",
                  "echo avant '    ' apr�s"
                  ),
                "Il est beaucoup plus simple de tout mettre entre guillemets"
                ),
    require( ("avant", "apr�s"), "Je ne vois pas les deux mots du texte !"),
    shell_require("avant    apr�s",
                  """D�bouchez-vous les yeux,
                  il y a 4 espaces entre les deux mots.
                  C'est �a la difficult�"""),
    shell_display,
    ),
    bad_answer="""
    Attention, il y a quatre espaces entre les deux mots.
    Comme la commande 'echo' ne voit que les param�tres et pas
    leur s�parateur elle affiche simplement un blanc
    entre les param�tres, alors qu'il y en a quatre.
    """,
    required=["affiche param�tre", "intro:guillemet"],
    )

add(name="affiche �toile",
    question="""Quelle commande permet d'afficher le texte suivant
    sur la sortie standard (l'�cran)&nbsp;:
    <pre>*</pre>""",
    tests=(
    shell_good("echo '*'"),
    shell_bad(("echo *", "echo '\*'"),
              """Essayez la commande que vous avez indiqu�,
              cela ne va pas afficher une �toile..."""),
    shell_display,
    ),
    bad_answer="""
    L'�toile est sp�ciale, elle repr�sente une suite de caract�res
    quelconques.
    """,
    )

add(name="affiche m�lange",
    required=["affiche �toile", "affiche param�tres sp�ciaux"],
    question="""Affichez le texte&nbsp;: <tt>\"'\\</tt><br>
    (C'est guillemet apostrophe anti-slash)""",
    tests=(
    require("echo", "On affiche avec <tt>echo</tt>"),
    good((r"""echo '"'"'"'\'""",
          r"""echo \"\''\'""",
          )), # Bug shell parser that should accept these one
    bad(r"""echo ""'\"""",
        """Les deux premiers guillemets d�finissent une chaine vide.
        On se retrouve donc avec une apostrophe ouvrant et pas de fermante.
        VOUS N'AVEZ PAS TEST� CETTE LIGNE AVANT DE LA PROPOSER"""),
    shell_good("echo '\"'\"'\"\\\\"),
    shell_display,
    ),
    good_answer=r"""Quelques solutions possibles&nbsp;:
    <pre>echo '"'"'"\\
echo \"\'\\
echo "\"'\\"
</pre>
    """,
    )

add(name="redirection entr�e",
    question="""Quel est le caract�re indiquant que l'on redirige l'entr�e
    standard d'une commande pour qu'elle lise le contenu d'un fichier""",
    tests=(
    good("<"),
    reject(">",
        """Si vous utilisez '&gt;',
        vous perdez ou modifiez le fichier que vous vouliez lire car c'est
        la redirection de sortie."""),
    answer_length_is(1, """Si l'on vous demande quel est <b>LE</b>
    caract�re, c'est que la r�ponse est sur un seul caract�re"""),
    bad('|', """Le pipe redirige l'entr�e standard, mais celle-ci
    vient d'une autre commande (� gauche), pas d'un fichier"""),
    ),
    required=["console"],
    )

add(name="redirection sortie",
    question="""Quel est le caract�re indiquant que l'on redirige la sortie
    standard d'une commande dans un fichier en le vidant d'abord""",
    tests=(
    good(">"),
    bad(">>", "Cela ajoute � la fin du fichier sans le vider"),
    bad("2>", "Cela redirige la sortie d'erreur, pas la standard."),
    reject("<", "C'est une redirection de l'entr�e."),
    ),
    required=["redirection entr�e"],
    good_answer="""Ce caract�re est extremement dangereux car il vide
    le contenu du fichier sans possibilit� de r�cup�ration.
    Il ne faut pas le confondre avec la redirection de l'entr�e standard.
    """
    )

add(name="redirection erreur",
    question="""Quelle est la cha�ne de caract�res indiquant
    que l'on redirige la sortie d'erreur d'une commande dans un fichier
    en le vidant d'abord""",
    tests=(
    good("2>"),
    bad(">", "Vous redirigez la sortie standard, pas la sortie d'erreur"),
    bad("2 >",
        """Comme les deux caract�res ne sont pas coll�s,
        le shell croit qu'il y a un param�tre qui a comme valeur <tt>2</tt>
        qui est suivi par une redirection de la sortie standard."""),
    require("2", "La sortie d'erreur porte le num�ro 2 (<em>fildes</em>)"),
    reject(' ', """Ne mettez pas d'espace, en effet les redirections
    sont des op�rateurs asym�triques"""),
    reject('&',
    """Le <tt>&amp;</tt> est utilis� pour diriger un descripteur vers
    un autre descripteur. Ceci n'est pas le cas ici."""),
    require(">", "C'est une redirection d'une sortie, on utilise donc '&gt;'"),
    bad(">2", "Vous allez cr�er un fichier qui s'appelle <tt>2</tt>"),
    answer_length_is(2, "La r�ponse tient sur 2 caract�res"),
    ),
    )


blanc = "Pour des raisons de lisibilit� on met un espace avant le <tt>&lt;</tt> et le <tt>&gt;</tt>"

add(name="'Bonjour' dans 'toto'",
    question="""Quelle est la ligne de commande la plus simple (courte)
    permettant de stocker
    le mot <tt>Bonjour</tt> dans le fichier <tt>toto</tt>
    (en �crasant ce qu'il y avait dedans).""",
    tests=(
    shell_good("echo Bonjour >toto"),
    shell_good("echo -n Bonjour >toto", "Vous �tes perfectionniste :-)"),
    shell_bad("Bonjour >toto",
    """Cette ligne ex�cute une commande nomm�e <tt>Bonjour</tt>
    qui n'existe normalement pas.
    La sortie standard de cette commande �tant le fichier <tt>toto</tt>"""),
    require("echo",
            """Il faut utiliser la commande qui �crit ses param�tres
            sur la sortie standard et rediriger celle-ci sur le fichier"""),
    reject("<",
           """Si vous m�langer le <tt>&gt;</tt> et le <tt>&lt;</tt>
           vous risquez de perdre beaucoup de fichiers dans l'avenir"""),
    require(">", "Ou la redirection de la sortie standard ?"),
    reject(">>", "On veut vider le fichier"),
    require("Bonjour",
            """Ce que vous devez �crire dans le fichier n'appara�t
            m�me pas dans la commande !
            <b>Respectez la casse</b> (majuscule != minuscule)
            """),    
    shell_display,
    ),
    required=["affiche param�tre", "redirection sortie"],
    )

add(name="ajout en fin",
    required=["redirection sortie"],
    question="""Quelle suite de caract�res utilise-t-on pour
    indiquer que l'on veut rediriger la sortie standard
    vers un fichier sans le vider (en ajoutant � la fin)&nbsp;?""",
    tests=(
    good(">>"),
    bad('>', "Cela vide le fichier, cela n'ajoute pas � la fin"),
    reject('<', "C'est pour changer les entr�es, pas les sorties"),
    reject("2", "Pourquoi parlez-vous de la sortie d'erreur&nbsp;?"),
    ),
    )

add(name="rebonjour",
    required=["'Bonjour' dans 'toto'", "ajout en fin", "paginer:navigation",],
    question="""Vous avez utilis� <tt>echo</tt> pour mettre <tt>bonjour</tt>
    dans le fichier <tt>toto</tt>.
    Donnez la commande pour ajouter <tt>Salut</tt>
    � la fin du fichier <tt>toto</tt>""",
    tests=(
    shell_good("echo Salut >>toto"),
    require(">>",
            """Ou est l'op�rateur indiquant que vous voulez
            ajouter � la fin&nbsp;?"""),
    reject("salut", "On vous dit de mettre une majuscule � <tt>Salut</tt>."),
    require("Salut",
    "Je ne trouve pas le mot <tt>Salut</tt> dans la commande"),
    require("echo",
    "Vous avez besoin de la commande (<em>builtin</em>) <tt>echo</tt>"),
    expect('toto'),
    shell_display,
    ),
    )

add(name="echo fin",
    required=["rebonjour", "concatener:intro"],
    before="""Faites&nbsp;:
    <pre>echo a &gt;toto
echo b &gt;&gt;toto</pre>""",
    question="""Que contient le fichier <tt>toto</tt>&nbsp;?
    vous pouvez utiliser la commande <tt>cat</tt> pour
    regarder le contenu.
    """,
    tests=(
    good("a\nb",
         """En effet, la commande <tt>echo</tt>
         ajoute automatiquement une fin de ligne"""),
    reject(("ab", "a b", "b\na"), "Vous n'avez pas essay�&nbsp;!"),
    reject(" ", """Aucun caract�re espace n'a �t� stock� dans <tt>toto</tt>,
         pourquoi votre r�ponse en contient&nbsp;?"""),
    ),
    nr_lines=4,
    )

add(name="affiche erreur",
    required=["'Bonjour' dans 'toto'"],
    question="""Faites afficher <tt>BUG</tt> sur la sortie d'erreur""",
    tests=(
    require("BUG", "Et le mot <tt>BUG</tt> il est o�&nbsp;?"),
    require("echo", "On fait <tt>echo</tt> pour afficher un texte"),
    require(">", "Il faut rediriger la sortie standard"),
    reject('2>',
    "<tt>2&gt;</tt> redirige la sortie d'erreur, pas la sortie standard"),
         
    reject(">2", "Vous allez cr�er un fichier nomm� <tt>2</tt>"),
    require("&2", "Le nom de la sortie d'erreur est <tt>&amp;2</tt>"),
    reject('2>&2', """Vous redirigez la sortie d'erreur sur la sortie d'erreur,
    vous ne changez donc pas les redirections.
    Il faut rediriger la sortie standard sur la sortie d'erreur"""),
    reject('> &2',
           "Essayez et vous verrez que cela ne fonctionne pas."),
    
    shell_good("echo BUG >&2", dumb_replace=(('bug', 'BUG'),)),
    shell_bad("echo BUG 1>&2",
    "Enlevez un caract�re inutile et vous avez la r�ponse",
    dumb_replace=(('bug', 'BUG'),)),
    shell_display,
    ),    
    )

add(name="cribler erreurs",
    required=["affiche erreur", "cribler:simple", "pipeline:intro"], 
    before="""Il arrive que des commandes affichent de tr�s nombreuses
    erreurs sur l'�cran et que l'on veuille ne pas toutes les afficher""",
    question="""N'affichez que les messages d'erreur de
    <tt>rm -f /etc/*</tt> qui contiennent le mot <tt>time</tt>""",
    default_answer = "rm -f /etc/*  ",
    tests=(
    reject('-e', """N'indiquez pas l'option <tt>-e</tt> de <tt>grep</tt>,
    en effet, il n'y a qu'un seul param�tre"""),
    reject('>&2',
    """Vous redirig� la sortie standard vers la sortie d'erreur.
    Alors qu'il faut rediriger la sortie d'erreur vers la sortie standard"""),
    reject("$", "Pas besoin d'utiliser de remplacement dans cette question."),
    require_startswith('rm -f /etc/*',
    """La ligne de commande commence par <tt>rm -f /etc/*</tt>"""),
    require("grep", "Il faut cribler les lignes avec <tt>grep</tt>"),
    require("time", "On cherche le mot <tt>time</tt>"),
    require("|", "Il faut faire un pipeline"),
    require("2>", """Il faut rediriger la sortie d'erreur de la commande
    <tt>rm</tt> vers la sortie standard"""),
    require("&1","Il faut rediriger vers la sortie standard (<tt>&amp;1</tt>)"),
    reject(">|", """Cette syntaxe est invalide, il faut utiliser
    la chaine <tt>&amp;1</tt> pour nommer la sortie standard."""),
    reject("> ", """Il ne peut y avoir d'espace entre le &gt; et l'endroit
    ou on le dirige"""),
    require("2>&1", """Il faut rediriger la sortie d'erreur vers la sortie
    standard (qui est le pipe dans ce cas)"""),
    shell_good("rm -f /etc/* 2>&1 | grep time"),
    shell_bad("rm -f /etc/* | grep time 2>&1",
    """Vous avez fait la redirection pour la commande <tt>grep</tt> qui
    ne fait pas d'erreur.
    Les messages d'erreur de <tt>rm</tt> vont donc s'afficher sur l'�cran"""),
    shell_display,
    ),
    indices = (
    """Les redirections � gauche du | s'appliquent � la commande de gauche
    et celle � droite � la commande de droite.""",
    ),
    )


    

add(name="remplacement",
    required=["lister:nomm�", "pattern:tout", "variable:affectation"],
    question="""Donner la ligne de commande permettant
    de stocker dans la variable <tt>A</tt>.
    la liste des noms des fichiers et r�pertoires
    du r�pertoire courant.""",
    tests=(
    Bad(Comment(RemoveSpaces(Contain('ls') & ~Contain('ls)')),
                "Si vous utilisez <tt>ls</tt>, pas besoin d'argument")),
    shell_good(("A=$(echo *)", 'A="$(echo *)"')),
    shell_good(("A=$(ls)", 'A="$(ls)"'),
               """On pr�fere utiliser <tt>echo</tt>
               car c'est une <em>builtin</em>,
               la r�ponse recommend�e est <tt>A=$(echo *)</tt>"""),
    require("=",
            "Pour mettre la valeur dans la variable on fait une affectation"),
    shell_bad("A=ls",
              """Vous venez de mettre la chaine de caract�re <tt>ls</tt>
              dans la variable <tt>A</tt>"""),
    shell_bad(('A="echo *"', "A='echo *'"),
              """Si vous croyez que cela fonctionne,
              essayez de taper <tt>echo "$A"</tt> pour voir son contenu"""),
    shell_bad('A=*',
    "V�rifiez le contenu de la variable en tapant : <tt>echo \"$A\"</tt>"),
    shell_require('</replacement>',
                  """Je ne vois pas la syntaxe permettant de remplacer
                  une commande par ce qu'elle affiche.
                  Rappelez-vous, c'est <tt>$(<em>une commande</em>)</tt>
                  """),
    reject("export", "On ne vous a pas demand� d'exporter la variable"),
    reject((' =', '= '), """Il ne faut pas d'espace de chaque
    cot� du signe = pour faire l'affectation"""),
    require('A', "Je ne vois pas le nom de la variable <tt>A</tt>&nbsp;!"),
    shell_display,
    ),
    indices=('''On utilise la syntaxe shell permettant de remplacer
    une commande par la sortie standard de celle-ci.''',
             ),
    )

add(name="deuxi�me mot",
    required=["remplacement", "variable:lire mots", "regroupement 2",
              "date:intro"],
    question="""Donnez la commande stockant le deuxi�me
    mot affich� par la commande <tt>date</tt> dans la
    variable <tt>Z</tt>.
    <p>
    Si vous avez besoin de variables, appelez les <tt>A</tt>, <tt>B</tt>, ...
    """,
    tests=(
    Bad(Comment(RemoveSpaces(Contain('<date')),
                """Vous demander � lire le contenu d'un fichier qui
                s'appelle <tt>date</tt> au lieu de lire le sorte standard
                de la commande <tt>date</tt>""")),
    shell_good((
    "Z=$(date | (read A B C ; echo $B))",
    "Z=$(date | (read A Z C ; echo $Z))",
    "Z=$(date | (read A Z B ; echo $Z))")),

    shell_good((
    "Z=$(date | (read A B C ; echo \"$B\"))",
    "Z=$(date | (read A Z C ; echo \"$Z\"))",
    "Z=$(date | (read A Z B ; echo \"$Z\"))",
    ),    
    "Les guillemets �taient inutiles car <tt>B</tt> ne contient pas d'espace"),
    shell_bad(("Z=$(date | (read A B ; echo $B))",
    "Z=$(date | (read A Z ; echo $Z))",),
    "Vous n'avez pas essay�"),
    shell_bad("date | read A Z B",
    """Cette commande fonctionne mais � peu d'utilit� car � la ligne suivante
    la variable <tt>Z</tt> a perdu sa valeur"""),
    shell_good("Z=$(date | cut -d' ' -f2)",
               """J'attendais <tt>read</tt> et <tt>echo</tt>,
               mais votre r�ponse fonctionne"""),
    expect('Z='),
    reject(('>','<'), "Pas besoin de redirections autre que le pipeline"),
    shell_bad(("Z=$(date | read A B C ; echo $B)",
    "Z=$(date | read A Z C ; echo $Z)",
    "Z=$(date | read A Z B ; echo $Z)",),
    """La commande <tt>echo</tt> a lieu apr�s que les deux commandes
    dans le pipeline se soient termin�es.
    Elle obtient la valeur de la variable de son p�re et
    non de la commande <tt>read</tt>"""),
    reject('cut', """N'utilisez pas <tt>cut</tt> mais <tt>read</tt>
    comme dans les questions pr�c�dentes."""),
    Bad(Comment(~Start('Z='),
                 """La r�ponse doit commencer par <tt>Z=</tt> si l'on ne
                 veux pas perdre la valeur de Z � la fin du processus""")),
    shell_display,
    ),
    indices=('''Pour afficher le deuxi�me mot,
    On doit faire un pipeline entre la commande <tt>date</tt>
    et un groupe de 2 commandes lisant le deuxi�me mot et l'affichant.''',
             '''Pour le stocker dans la variable, on fait un remplacement
    de commande.'''
             ),
    )


add(name="ex�cution s�quencielle",
    required=["console", "lister:intro", "directory courant",
              "intro:esperluette"],
    question="""Quel caract�re (autre que le retour � la ligne)
    indique que deux commandes
    doivent s'ex�cuter l'une apr�s l'autre.
    M�me si la premi�re s'est mal pass�""",
    tests=(
    good(";"),
    bad("|", "L'ex�cution est parall�le et non s�quentielle"),
    bad("||", """La deuxi�me commande s'ex�cute QUE SI la premi�re s'est
    mal pass�."""),
    bad("&", "Mis � la fin d'un commande, elle s'ex�cute en arri�re plan."),
    bad("&&", """Ex�cution s�quencielle fiable, la deuxi�me s'ex�cute seulement
    si la premi�re c'est bien pass�e."""),
    bad('', """Si je vous comprend bien, si l'on tape <tt>echo bonjour</tt>
    cela devrait ex�cuter la commande <tt>echo</tt> puis la commande
    <tt>bonjour</tt>"""),
    ),
    indices=(
    "Ce caract�re est utilis� pour s�parer deux commandes sur la m�me ligne",
    ),
    )

add(name="s�quencielle",
    question="""Donnez la ligne compos�e d'une suite de commandes
    qui dans l'ordre&nbsp;:
    <ul>
    <li> Change le r�pertoire courant afin d'aller dans le r�pertoire <tt>toto</tt> (qui est dans le r�pertoire courant)
    <li> Affiche la liste des noms de fichiers et r�pertoires contenus dans le r�pertoire courant (donc <tt>toto</tt>).
    <li> Change le r�pertoire courant pour aller dans le p�re, c'est-�-dire
    revenir dans le r�pertoire initial.
    </ul>
    <p>
    Si une commande �choue, les suivantes doivent s'ex�cuter
    (ex�cution non fiable).
    """,
    tests=(
    expect('ls'),
    shell_good("cd toto ; ls ; cd .."),
    shell_bad("cd toto && ls && cd ..",
              """Votre commande est <b>correcte</b>, mais elle en fait plus
              que n�cessaire car elle est fiable.
              C'est la r�ponse � une futur question.
              Donnez la r�ponse non fiable."""),
    reject('/', """Pas besoin de / dans cette commande car tous les noms
     sont relatifs et directement accessibles"""),
     reject('(', "Pas besoin de parenth�ser"),
    shell_require("<command><argument>cd</argument><argument>toto</argument></command>",
                  "On veut aller dans le r�pertoire <tt>toto</tt>"),
    shell_require("<command><argument>ls</argument></command>",
                  "On veut lister les fichiers, on utilisera <tt>ls</tt> sans argument"),
    shell_require("<command><argument>cd</argument><argument>..</argument></command>",
                  "On veut remonter dans le p�re."),
    shell_display,
    ),
    good_answer="""Cette suite de commandes est dangereuse � utiliser.
    En effet le r�pertoire courant apr�s son ex�cution a pu changer
    si le <tt>cd toto</tt> n'est pas accessible.""",
    )

add(name="regroupement",
    required=["s�quencielle", "redirection sortie", "date:intro",
              "concatener:concatener"],
    before="""Les parenth�ses permettent de regrouper des commandes
    ensemble pour qu'elles s'ex�cutent dans le m�me shell
    et que l'on puisse rediriger les entr�es/sorties sur l'ensemble
    des commandes""",
    question="""Donnez la commande permettant de stocker
    dans le fichier <tt>xxx</tt> (en l'effa�ant) la date suivie du contenu
    du fichier <tt>/etc/passwd</tt>""",
    tests=(
    shell_good(("(date;cat /etc/passwd) >xxx",
                "(date;cat </etc/passwd) >xxx",
                )),
    reject(">>",
           """On veut remplacer le contenu du fichier <tt>xxx</tt>,
           pas ajouter � la fin."""),
    reject("$", """Il est possible de faire cette question en utilisant
    des remplacements, mais ce n'est pas ce qui est demand�.
    Vous ne devez pas utiliser la syntaxe <tt>$(commande)</tt>"""),
    require("/etc/passwd", "Et <tt>/etc/passwd</tt>, ou est-il&nbsp;?"),
    require("date", "Et la date&nbsp;?"),
    require("cat", "Utilisez <tt>cat</tt> pour �crire le contenu de <tt>/etc/passwd</tt> sur la sortie standard."),
    require("xxx", "Vous avez oubli� de dire dans quoi vous stockiez le r�sultat"),
    number_of_is(">", 1, """On utilise un regroupement pour ne faire
    la redirection qu'une seule fois."""),
    require(('(',')'), """O� sont les parenth�ses permettant
    de regrouper des commandes&nbsp;?"""),
    require(';',
    """Le regroupement doit contenir 2 commandes � lancer successivement.
    Il faut donc utiliser un ';'"""),
    number_of_is("xxx", 1, """Votre r�ponse ne doit contenir le
    nom du fichier <tt>xxx</tt> qu'une seule fois."""),
    shell_bad("(cat /etc/passwd;date) >xxx",
    "N'auriez-vous pas invers� quelque chose, relisez la question..."),
    shell_display,
    ),
    )

add(name="regroupement 2",
    required=["regroupement", "variable:lire ligne", "variable:intro"],
    question="""Donnez la commande permettant d'afficher
    la deuxi�me ligne du fichier <tt>/etc/passwd</tt>
    en utilisant seulement les commandes <tt>read</tt> et <tt>echo</tt>
    <p>
    Si vous avez besoin d'une variable, appelez-la <tt>A</tt>.
    """,
    tests=(
    shell_good(("(read A ; read A ; echo $A ) </etc/passwd",
                "(read ; read A ; echo $A ) </etc/passwd"),
               "Des guillemets autour de <tt>$A</tt> sont pr�f�rables"),
    shell_good(('(read A ; read A ; echo "$A" ) </etc/passwd',
                '(read ; read A ; echo "$A" ) </etc/passwd')
                ),
    reject("|", "On a pas besoin de pipeline."),
    reject(">", "On a pas besoin de rediriger la sortie standard."),
    number_of_is('read', 2,
    """Il faut lancer deux fois <tt>read</tt>, le premier pour
    lire la premi�re ligne et le second pour lire la deuxi�me"""),
    require('<', """Il faut que l'entr�e standard soit modifi�e
    pour que la commande <tt>read</tt> puisse lire le fichier"""),
    
    number_of_is('<', 1,
    """On ne redirige l'entr�e standard vers <tt>passwd</tt> qu'une
    seule fois. En effet, � chaque fois qu'elle est redirig�e,
    on recommence � lire � partir du d�but."""),
    require('echo', "On utilise <tt>echo</tt> pour afficher la ligne lue"),
    require( ('(', ')'), """Comme indiqu� dans le titre de la question
    vous avez besoin de faire un regroupement pour pouvoir utiliser
    <tt>read</tt> plusieurs fois sur le m�me fichier en l'ouvrant
    qu'une seule fois."""),
    shell_bad(("(read A ; read A) </etc/passwd ; echo $A",
    "(read A ; read A) </etc/passwd ; echo \"$A\"",
    "(read ; read A) </etc/passwd ; echo $A",
    "(read ; read A) </etc/passwd ; echo \"$A\"",
    ), """Quand le processus cr�� par les parenth�ses meurt,
    la variable <tt>A</tt> dispara�t. Donc votre <tt>echo</tt>
    n'affiche pas la bonne valeur."""),
    require('$',
    "Pour afficher le contenu d'une variable, on utilise <tt>$</tt>"),
    expect("/etc/passwd"),
    shell_display,
    ),
    )

    

add(name="s�quencielle fiable",
    question="""Quelle suite de caract�res
    indique que la commande qui suit ne s'ex�cute que
    si la commande pr�c�dente s'est termin�e sans erreur&nbsp;?""",
    tests=(
    good("&&"),
    answer_length_is(2, "R�ponse en 2 caract�res"),
    ),
    indices=("C'est dans votre cours...",),
    )

add(name="fiable",
    required=["s�quencielle fiable"],
    question="""Donnez la ligne compos�e d'une suite de commandes
    qui dans l'ordre&nbsp;:
    <ul>
    <li> Change le r�pertoire courant afin d'aller dans le r�pertoire <tt>toto</tt>
    <li> Affiche la liste des noms de fichier.
    <li> Change le r�pertoire courant pour aller dans le p�re.
    </ul>
    <b>Elle doit �tre �crite de mani�re � garantir
    que le r�pertoire courant n'aura pas
    chang� apr�s son ex�cution,
    et donc que l'on ne va pas dans le p�re si l'on a pas
    pu aller dans <tt>toto</tt>.</b>
    """,
    tests=(
    require("&&",
            """Ou est l'op�rateur indiquant que l'on ne veut ex�cuter
            la commande suivante que si la pr�c�dente
            c'est bien pass�e&nbsp;?"""),
    shell_bad("cd toto && ls ; cd ..",
              "Vous allez dans le p�re dans tous les cas"),
    shell_bad("(cd toto && ls)",
              """Cela fonctionne, mais vous ne faites pas exactement
              ce que l'on vous demande, on vous dit d'aller dans le p�re."""),
    reject(";",
           """Quand vous utilisez <tt>;</tt> la commande suivante
           s'ex�cute m�me si celle d'avant n'a pas fonctionn�e"""),
    shell_good("cd toto && ls && cd .."),
    reject("(", "Pas besoin de regroupement"),
    reject('/', "Pourquoi avez-vous besoin de <tt>/</tt>&nbsp;?"),
    expect('toto'),
    expect("cd"),
    expect("ls"),
    expect(".."),
    shell_display,
    ),
    )

add(name="boucle",
    required=["affiche param�tres sp�ciaux", "variable:intro"],
    before="""La r�ponse � cette question a peu d'utilit�,
    c'est seulement pour v�rifier que vous savez faire une boucle <tt>for</tt>
    """,
    question="""Donnez la ligne de commande avec une boucle <tt>for</tt>
    affichant avec plusieurs appels � la commande <tt>echo</tt>&nbsp;:
    <pre>Un
Mot
Par
Ligne</pre>
<p>
Vous utiliserez <tt>I</tt> comme variable de boucle.
Tout autre nom de variable sera refus�.
""",
    tests=(
    shell_good("for I in Un Mot Par Ligne ; do echo $I ; done",
               """Par s�curit� on met des guillemets
               autour du <tt>$I</tt>.
               Pensez au cas ou <tt>I</tt> contient une chaine
               de caract�res avec des espaces."""
               ),
    shell_good('for I in Un Mot Par Ligne ; do echo "$I" ; done'),
    reject(("'Un Mot Par Ligne'", '"Un Mot Par Ligne"'),
    """Si vous prot�gez les espaces de la phrase,
    la boucle ne portera pas sur les mots de la phrase"""),

    shell_bad("for I in Un Mot Par Ligne ; do echo '$I' ; done",
              "Vous n'avez m�me pas essay� la commande"),
    reject(" i ", "Un <tt>i</tt> MAJUSCULE comme on vous l'a demand�"),
    reject("*",
    """Pourquoi avez-vous une �toile dans votre r�ponse,
    vous ne voulez pas parcourir la liste des noms de fichier
    du r�pertoire courant mais <tt>Un Mot Par Ligne</tt>"""),
    require(("Un","Mot","Par","Ligne"),
            """Je ne trouve pas l'ensemble de mots � it�rer.
              Avez-vous respect� la casse&nbsp;?"""),
    shell_require(">I</variable>",
                  "Je ne vois pas d'acc�s au contenu de <tt>I</tt>"),
    number_of_is(';', 2,
    """Quand on �crit une boucle <tt>for</tt> sur une seule ligne
    contenant une seule instruction il faut 2 point virgule (;)."""),
    require((' in ', 'for ', 'do ', 'done'),
    """La syntaxe du <tt>for</tt> contient obligatoirement
    les mots clefs : <tt>for</tt>, <tt>in</tt>, <tt>do</tt>, <tt>done</tt>"""),
    reject('<', """Ne recopiez pas b�tement les exemples du cours,
    et testez vos commandes avant de r�pondre"""),
    reject('for $I', """En tapant <tt>for $I</tt> vous dites � la commande
    <tt>for</tt> que le nom de la variable � it�rer est dans
    la variable <tt>I</tt>. Alors que c'est <tt>I</tt> la variable
    que l'on veut it�rer."""),
    shell_display,
    ),
    )

add(name="arri�re plan",
    required=["intro:esperluette", "console"],
    before="""Vous voulez lancer une fen�tre avec une horloge analogique.
    Vous tapez par exemple&nbsp;:
    <pre>xclock</pre>
L'horloge appara�t mais votre invite de commande (<em>prompt</em>)
ne r�appara�t pas car le processus n'est pas encore termin�.
<p>
Si vous tapez <tt>^C</tt> ou si vous fermez la fen�tre le processus
<tt>xclock</tt> va mourir et la fen�tre va se fermer.
""",
    question="""Comment lancer <tt>xclock</tt> en ligne de commande
    pour que l'invite de commande revienne tout de suite&nbsp;?""",
    tests=(
    shell_good("xclock &"),
    require("xclock",
            "C'est <tt>xclock</tt> que je veux lancer en arri�re plan"),
    require("&", """Je ne vois pas le symbole indiquant que l'on
    veut lancer en arri�re plan"""),
    reject('bg', """<tt>bg</tt> est pour mettre en arri�re plan une commande
    lanc�e avant et qui a �t� interrompue par un <tt>^Z</tt>"""),
    shell_display,
    ),
    indices=("""Il faut lancer le programme en arri�re plan
    (tache de fond, ou en <em>background</em> en anglais)""",
             ),
    )

add(name="tant que",
    required=["variable:lire mots", "affiche param�tre", "boucle"],
    question="""Faites une boucle affichant ligne par ligne,
    sans modifications tout ce qui a �t� lu sur l'entr�e standard.
    <p>
    Vous devez utiliser la variable nomm�e <tt>A</tt>
    """,
    tests=(
    shell_good('while read A ; do echo "$A" ; done'),
    shell_bad('while read A ; do echo $A ; done',
               "Les espaces multiples seront perdus"),
    reject('-', "Pas besoin d'options dans la commande"),
    expect('while'),
    expect('read'),
    expect('echo'),
    expect('A'),
    shell_display,
    ),
    good_answer = """Cela ne fonctionnera pas s'il y a une ligne commen�ant
    par tiret, mais on peut encore am�liorer.""",
    )

add(name="longueurs",
    required=['tant que', 'calculer:longueur', 'remplacement'],
    question="""Faites afficher chaque ligne lue dans l'entr�e standard
    en la pr�c�dent par sa longueur suivi d'un espace&nbsp;:
        <pre>1 x
2 yy
6 a    b
0</pre>
    <p>
    Vous devez utiliser la variable nomm�e <tt>A</tt>
""",
    default_answer = 'while read A ; do echo "$A" ; done',
    tests=(
    expect('length'),
    expect('expr'),
    reject('-', "Pas besoin d'options pour cette commande"),
    reject(("$A ", "$A)"),
           "N'oubliez pas les guillemets quand vous acc�dez aux variables"),
    expect("$(", """Vous devez utiliser le remplacement de commande afin
    d'inclure la sortie standard de <tt>expr</tt> comme param�tre de
    <tt>echo</tt>"""),
    shell_good('while read A;do echo "$(expr length "$A") $A" ; done'),
    shell_good('while read A;do echo $(expr length "$A") "$A" ; done'),
    shell_good('while read A;do echo $(expr length "$A")" $A" ; done'),
    shell_bad('while read A;do echo "$(expr length "$A")" "$A" ; done',
              "Vous enlevez 2 caract�res et vous avez trouv�."),
    reject('""', "Pourquoi il y a 2 guillemets � la suite ?"),
    shell_display,
    ),
    )

# XXX Faire une question pour enlever le premier caract�re de la ligne

add(name="refaire cat",
    required=["tant que", "remplacer:intro", "pipeline:intro"],
    question="""Faites une boucle affichant ligne par ligne,
    sans modifications tout ce qui a �t� lu sur l'entr�e standard.
    <p>
    <b>Y compris quand la ligne commence par un tiret</b>.
    Pour ce faire :
        <ul>
        <li> Afficher un espace en d�but de chaque ligne lue.
        <li> Puis remplacez l'espace par rien du tout.
        </ul>
    <p>
    Vous devez utiliser la variable nomm�e <tt>A</tt>
    """,
    default_answer = 'while read A ; do echo "$A" ; done',
    tests=(
    shell_good('while read A ; do echo " $A" ; done | sed "s/ //"',
               dumb_replace=remplacer.dumb_replace),
    shell_good('while read A ; do echo " $A" ; done | sed "s/.//"',
               dumb_replace=remplacer.dumb_replace),
    shell_good('while read A ; do echo " $A" | sed "s/ //" ; done',
    """Votre r�ponse est correcte mais fonctionne trop lentement car
    vous lancez un processus pour chaque ligne lue.
    Il faut lancer une seule fois la commande <tt>sed</tt>.""",
    dumb_replace=remplacer.dumb_replace),
    reject('^', """Pas la peine d'indiquer que l'on veut enlever le premier
    espace/caract�re de la ligne, c'est ce qui est fait par d�faut."""),
    reject('/g', "Vous allez enlever tous les espaces de la ligne !"),
    expect('while'),
    expect('sed'),
    expect('read'),
    expect('echo'),
    expect('A'),
    Expect(' $A', "O� ajoutez-vous l'espace avant le contenu de A&nbsp;?"),
    shell_display,
    ),
    )


add(name="valeur de retour",
    required=["fiable", "variable:intro"],
    before="""La variable shell nomm�e <b><tt>?</tt></b> contient
    la valeur retourn�e par la derni�re commande que vous avez lanc�.""",
    question="""Quelle ligne de commande fait afficher la valeur de
    retour de la derni�re commande&nbsp;?""",
    tests=(
    shell_good(('echo $?', 'echo "$?"')),
    expect('echo'),
    require('$', "On utilise $ pour avoir le contenu d'une variable"),
    shell_display,
    ),
    )

add(name="grep trouve",
    required=["valeur de retour", "cribler:simple"],
    question="""Quelle est la valeur retourn�e par le processus
    <pre>grep -q b /etc/passwd</pre>
    Rien n'est affich� sur l'�cran, c'est normal.
    """,
    tests = (
    Int(0),
    ))
    
add(name="grep trouve pas",
    required=["valeur de retour", "cribler:simple"],
    question="""Quelle est la valeur retourn�e par le processus
    <pre>grep coucou /etc/passwd &gt;/dev/null</pre>""",
    tests = (
    Int(1),
    ))


add(name="si",
    required=["grep trouve", "grep trouve pas"],
    question="""Donnez la ligne de commande utilisant un <tt>si</tt>
    qui affiche OUI ou NON suivant que le fichier <tt>/etc/passwd</tt>
    contienne le texte <tt>root</tt> ou non.""",
    tests = (
    reject('<', "On a pas besoin de rediriger l'entr�e standard"),
    reject('[', "On a pas besoin la commande <tt>test</tt> (<tt>[</tt>)"),
    Reject('expr'),
    Reject('$?'),
    Reject("$(", "Pas besoin de remplacement avec $(...)"),
    expect('if'),
    expect('/etc/passwd'),
    expect('OUI'),
    expect('NON'),
    expect('then'),
    expect('fi'),
    expect('else'),
    expect('root'),
    shell_bad('if grep root /etc/passwd ; then echo OUI ; else echo NON ; fi',
    """Le mot OUI est m�lang� apr�s la sortie de la commande <tt>grep</tt>,
    faites en sorte que seulement OUI s'affiche."""),
    shell_bad('if grep root /etc/passwd ; then echo OUI ; else echo NON ; fi >/dev/null',
    """Cette commande n'affiche rien !"""),
    shell_good((
    'if grep -q root /etc/passwd ; then echo OUI ; else echo NON ; fi',
    'if grep root /etc/passwd >/dev/null ; then echo OUI ; else echo NON ; fi',
    )),
    shell_display,
    ),
    
    )

add(name="boucle si",
    required=["si", "remplacer:remplacer hi�rarchie"],
    question="""Quelle ligne de commande affiche pour tous les fichiers
    du r�pertoire courant dont le nom se termine par <tt>.c</tt>
    <ul>
    <li> OUI si le fichier contient le texte <tt>Copyright</tt>
    <li> et NON sinon.
    </ul>
    Elle affichera par exemple :
    <pre>OUI
NON
NON
OUI
OUI
OUI</pre>
    <p>
    On nommera <tt>F</tt> la variable de boucle.
    """,
    tests = (
    reject('<'),
    expect('for'),
    expect('F'),
    expect('$F'),
    expect('in'),
    expect('*.c'),
    expect('do'),
    expect('if'),
    expect('Copyright'),
    expect('then'),
    expect('else'),
    expect('echo'),
    expect('OUI'),
    expect('NON'),
    expect('done'),
    expect('grep'),
    reject(' $F', """Cette commande ne fonctionne pas quand il y des espaces
           dans les noms de fichier."""),
    shell_good(('for F in *.c ; do if grep -q Copyright "$F" ; then echo OUI ; else echo NON ; fi ; done',
    'for F in *.c ; do if grep Copyright "$F" >/dev/null ; then echo OUI ; else echo NON ; fi ; done')),
    Bad(Comment(~Contain('-q') & ~Contain('/dev/null'),
                "Votre commande affiche des choses en plus de OUI et NON")),
    shell_display,
    ),
    
    )


