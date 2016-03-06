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

image = "<img src='boxes.png'>"

add(name="intro",
    required=["repondre:r�pondre"],
    before="""
    Voici une repr�sentation du syst�me de fichier.
    Les cases noires contiennent les noms courts des fichiers.
    Les vertes sont des fichiers de donn�es ex�cutables
    ou non et les jaunes des fichiers repr�sentant des p�riph�riques.
    La plus grande boite est la racine et ne porte pas de nom.
    Les cases <tt>.</tt> et <tt>..</tt> apparaissent
    dans tous les r�pertoires.
    <p>
    """ + image,
    question="""Combien de r�pertoires <b>diff�rents</b> sont visibles
    sur la figure&nbsp;?""",
    tests=(
    good("11"),
    bad(("6","7"),
        "Vous avez compt� que les r�pertoires directement sous la racine"),
    bad("10", "Avez-vous compt� le r�pertoire racine&nbsp;?"),
    bad("12", "Presque !"),
    require_int(),
    ),
    indices=("""Ne comptez pas les cases <tt>..</tt> et <tt>.</tt> vous les
    avez d�j� compt�es par ailleur.""",
             ),
    )

reject_double_slash = reject("//",
           """Mettre plus d'un '<tt>/</tt>' revient � en mettre un seul,
           Comme dans la suite des questions on vous demande tous
           le temps la r�ponse la plus courte,
           celle-ci ne sera pas accept�e""")

reject_space = reject(" ","On fait les concat�nations sans ajouter d'espaces.")

reject_dot = reject(".",
                    """On vous a dit d'enlever tous les
                    <tt>.</tt>, <tt>..</tt> pour que cela soit court."""
                    )

reject_trailing_slash = reject_endswith(
    '/',
    """Mettre un <tt>/</tt> � la fin d'un nom n'est utile
    que dans le cas du lien symbolique
    quand on veux sp�cifier ce qui est point�
    par le lien symbolique plut�t que le lien symbolique lui-m�me.
    <p>
    Ce <tt>/</tt> final n'est pas incorrecte mais vos r�ponses
    seront n�anmoins refus�es si vous le mettez"""
    )

require_absolute_name = require_startswith(
    "/", "Un chemin absolu commence par <tt>/</tt>")

require_relative_name = reject_startswith(
    "/", "Un chemin relatif ne commence pas par <tt>/</tt>")

add(name="nom absolu",
    required=["intro"],
    before="""
    Pour obtenir un nom absolu, vous partez de la boite la plus ext�rieure
    jusqu'� celle qui vous int�resse.
    Le nom absolu est la concat�nation de tous les noms courts
    de ces boites en les s�parant par un caract�re '<tt>/</tt>'
    <p>
    """ + image + """
    <p>
    Bien que la boite ext�rieur ne porte pas de nom court
    son nom absolu n'est pas vide, c'est&nbsp;: <tt>/</tt>
    """,
    question="""Quel est le nom absolu de la boite dont le nom est <tt>etc</tt>
    sur la figure&nbsp;?""",
    tests=(
    good("/etc"),
    bad("//etc",
        """Cette r�ponse fonctionne mais est � �viter car elle
        est non-portable."""),
    require("etc",
            """Je ne vois pas <tt>etc</tt> comment
            est-ce que cela peut le d�signer&nbsp;?"""),
    require_absolute_name,
    reject_trailing_slash,
    reject_double_slash,
    reject_space,
    ),
    indices=(
    """Comme <tt>etc</tt> est dans la plus grande boite
    la r�ponse est&nbsp;: <tt>nom court de la racine/nom court de la boite etc</tt>""",
    """Le nom court de la racine est une chaine de caract�re vide.""",
    ),
    )

add(name="nom absolu 2",
    required=["nom absolu"],
    before=image,
    question="""Quel est le nom absolu de la boite
    dont le nom est <tt>xemacs</tt> sur la figure&nbsp;?""",
    tests=(
    good("/usr/bin/xemacs"),
    bad("/bin/xemacs", "Dans la boite <tt>/bin</tt> il n'y a que <tt>ls</tt>"),
    reject("etc", """Le chemin qui m�ne � <tt>xemacs</tt>
    ne passe pas par <tt>etc</tt>"""),
    require_absolute_name,
    reject_trailing_slash,
    reject_double_slash,
    reject_space,
    require("xemacs", "O� est <tt>xemacs</tt> dans votre r�ponse&nbsp;?"),
    require("bin/xemacs", "Dans quel r�pertoire se trouve <tt>xemacs</tt>&nbsp;?"),
    ),
    indices=(
    """La r�ponse est&nbsp;:
    <tt>nom court racine/nom court 1/nom court 2/nom court xemacs</tt>""",
    ),
    )

add(name="point",
    required=["nom absolu 2"],
    before="""Le contenu de la boite <tt>.</tt> est le m�me que
    celui de la boite qui la contient.
    C'est � dire que <tt>/etc/.</tt> est la m�me chose que
    <tt>/etc</tt><p>""" + image,
    question="""Donnez le chemin absolu le plus court qui
    repr�sente la m�me chose que <tt>/./home/././p0123456/Toto/.</tt>
    """,
    tests=(
    reject_trailing_slash,
    reject_double_slash,
    reject_space,
    reject_dot,
    good("/home/p0123456/Toto"),
    good("~p0123456/Toto"),
    require("Toto",
            """Quand on dit <tt>Toto</tt>, c'est pas <tt>toto</tt>
            ni <tt>TOTO</tt> ni <tt>ToTo</tt> ni ..."""),
    require(("home", "p0123456", "Toto"),
            "Il manque des noms courts dans votre chemin"),
    reject('~', """N'utilisez pas le tilde s'il vous plais"""),
    require_absolute_name,
    ),
    )

add(name="point point",
    required=["nom absolu 2"],
    before="""Le contenu de la boite <tt>..</tt> est la m�me que
    celui de la boite qui la contient.
    C'est-�-dire que <tt>/usr/include/..</tt> est la m�me boite que
    <tt>/usr</tt>
    <p>
    Et <tt>/..</tt> est un cas particulier car il n'y a pas
    de boite au dessus et il repr�sente la m�me
    chose que <tt>/</tt>
    <p>
    """ + image,
    question="""Donnez le nom absolu le plus court qui
    repr�sente la m�me chose que <tt>/home/p0123456/Toto/..</tt>
    m�me si vous n'�tes pas l'utilisateur <tt>p0123456</tt>""",
    tests=(
    good("/home/p0123456"),
    good("~p0123456"),
    reject(('~','$HOME'), """Votre identit� n'est pas <tt>p0123456</tt> donc
    vous ne devez pas utiliser le tilde ou <tt>$HOME</tt>."""),
    reject_trailing_slash,
    reject_double_slash,
    reject_space,
    reject_dot,
    bad("/home/p0123456/Toto",
        "C'est la m�me chose que <tt>/home/p0123456/Toto/.</tt>"),
    expect('p0123456'),
    number_of_is('/',2, """Il doit y avoir 2 / dans votre r�ponse
    puisqu'en remontant d'un niveau on perd un /"""),
    ),
    )
    
add(name="point point 2",
    required=["point point", "point"],
    before=image,
    question="""L'utilisateur veut cr�er le fichier <tt>/./home/./p0123456/../../toto</tt>
    <p>
    Donnez le nom absolu le plus court qui
    repr�sente le nom du fichier cr��.""",
    tests=(
    good("/toto"),
    reject_trailing_slash,
    reject_double_slash,
    reject_space,
    reject_dot,
    bad("/home/toto", "Presque... Soyez rigoureux."),
    bad("/home/p0123456/toto",
        """Le <tt>..</tt> fait remonter au p�re, vous ne l'avez pas fait"""),
    require_absolute_name,
    require("toto",
            "Le nom de fichier que vous donnez doit contenir <tt>toto</tt>"),
    
    ),
    )

add(name="r�pertoire courant",
    required=["nom absolu 2"],
    before="""
    Tous les processus ont un r�pertoire courant,
    le r�pertoire courant permet d'�crire des noms
    de fichier relatif qui sont beaucoup plus court
    � �crire que les noms de fichier absolu.
    <p>
    Le chemin absolu du fichier indiqu� en relatif
    est la concat�nation du chemin absolu du r�pertoire
    courant d'un <tt>/</tt> et du chemin relatif.
    <p>
    Les chemins relatifs ont l'avantage de pouvoir �tre exprim�s
    sans r�f�rence � l'endroit ou sont stock�s les fichiers.
    <p>
    Si <tt>/usr</tt> est le r�pertoire courant
    alors le chemin relatif <tt>include</tt>
    indique le r�pertoire <tt>/usr/include</tt>.    
    <p>
    """ + image,
    question="""Si <tt>/usr</tt> est le r�pertoire courant,
    quel est le chemin relatif le plus court indiquant
    <tt>/usr/bin</tt>&nbsp?""",
    tests=(
    good("bin"),
    require_relative_name,
    reject_trailing_slash,
    reject_dot,
    reject_space,
    expect('bin'),
    ),
    )

add(name="relatif",
    required=["r�pertoire courant"],
    before=image,
    question="""Si <tt>/usr</tt> est le r�pertoire courant,
    quel est le chemin relatif le plus court indiquant
    <tt>/usr/bin/xemacs</tt>""",
    tests=(
    reject_double_slash,
    reject_space,
    reject_dot,
    bad("/bin/xemacs",
           """Premi�rement votre chemin est absolu et non relatif.
           et deuxi�mement, il n'y a aucun fichier <tt>xemacs</tt>
           dans <tt>/bin</tt>"""),
    require_relative_name,
    reject("usr/xemacs",
           "Il n'y a aucun fichier <tt>xemacs</tt> dans <tt>usr</tt>"),
    require('xemacs', "Il y a forc�ment <tt>xemacs</tt> dans la r�ponse"),
    bad('xemacs', """Le chemin complet du fichier que vous venez
    d'indiquer est <tt>/usr/xemacs</tt> et non <tt>/usr/bin/xemacs</tt>"""),
    
    good("bin/xemacs"),
    ),
    )


add(name="ici",
    required=["r�pertoire courant", "point"],
    question="""Donnez le nom relatif le plus court indiquant le r�pertoire courant""",
    tests=(
    good("."),
    bad("/",
        "C'est la racine du syst�me de fichier, pas le r�pertoire courant"),
    bad("/.", "C'est la m�me chose que <tt>/</tt> la racine"),
    bad("~",
        "Ce n'est pas le r�pertoire courant mais le r�pertoire de connexion"),
    bad("pwd",
        """C'est le nom d'une commande affichant le r�pertoire courant.
        On vous demande un nom de fichier, pas une commande � ex�cuter"""),
    reject_trailing_slash,
    ),
    indices=("La r�ponse tient sur un caract�re",
             ),
    )

add(name="p�re",
    required=["r�pertoire courant", "point point"],
    question="""Donnez le nom relatif le plus court indiquant le p�re du r�pertoire courant""",
    tests=(
    good(".."),
    reject("/..", "�a c'est le p�re de la racine, donc... la racine :-)"),
    bad(('/',"/."), "C'est la racine du syst�me de fichier."),
    reject_trailing_slash,
    reject('.', "C'est le r�pertoire courant, pas son p�re."),
    ),
    indices=("La r�ponse tient sur deux caract�res",
             ),
    )

add(name="relatif 2",
    required=["relatif", "point point"],
    before=image,
    question="""Si <tt>/usr/include</tt> est le r�pertoire courant,
    quel est le chemin relatif le plus court indiquant
    <tt>/usr/bin/xemacs</tt>""",
    tests=(
    good("../bin/xemacs"),
    reject("usr", "Essayez de ne pas �crire <tt>usr</tt>"),
    expect('xemacs'),
    require_relative_name,
    reject_double_slash,
    reject_space,
    reject_trailing_slash,
    require('..', """<tt>/usr/bin/xemacs</tt> n'est pas au dessous
    de <tt>/usr/include</tt>, il faut donc remonter dans la hi�rarchie
    en utilisant le <tt>..</tt>"""),
    ),
    )

add(name="relatif 3",
    required=["relatif", "point point"],
    before=image,
    question="""Si <tt>/home/p0123456/Toto</tt> est le r�pertoire courant,
    quel est le chemin relatif le plus court indiquant
    <tt>/home/p0123456/.profile</tt>""",
    tests=(
    require(".profile",
            """Le chemin relatif indique forc�ment sa destination&nbsp;:
            <tt>.profile</tt>"""),
    require_relative_name,
    reject_double_slash,
    reject_space,
    reject_trailing_slash,
    bad(".profile", """Le nom que vous venez de donner s'�crit
    <tt>/home/p0123456/Toto/.profile</tt> en absolu."""),
    good("../.profile"),
    bad("~/.profile", "On vous demande un chemin relatif"),
    require_startswith('../',
                       """On veut sortir du r�pertoire courant.
                       Il faut donc aller dans le p�re"""),
    ),
    )

add(name="intrus",
    required=["point point"],
    question="""Quel est l'intrus parmi la liste suivante&nbsp;?
    <ul>
    <li> <tt>/etc/./profile</tt>
    <li> <tt>/usr/../etc/profile</tt>
    <li> <tt>/etc/../profile</tt>
    <li> <tt>/etc/rc2.d/../profile</tt>
    </ul>
    """,
    tests=(
    bad(("/etc/./profile", "/usr/../etc/profile",
         "/etc/rc2.d/../profile"),
        "Ce chemin pointe vers <tt>/etc/profile</tt> et les autres&nbsp;?"),
    good("/etc/../profile",
         "C'est le seul ne repr�sentant pas <tt>/etc/profile</tt>"),
    comment("Votre r�ponse ne figure pas dans la liste des choix possibles."),
    ),
    )




add(name="r�p. connexion",
    required=["nom absolu 2"],
    before="""Quand un param�tre d'une commande commence
    par une certaine suite de caract�res,
    le shell (l'interpr�teur de commande, pas Unix)
    remplace cette s�quence de caract�res par
    le nom absolu du r�pertoire de connexion.""",
    question="""Quelle est la s�quence de caract�res qui
    est remplac�e par le nom du r�pertoire de connexion&nbsp;?""",
    tests=(
    reject_double_slash,
    reject_space,
    reject_dot,
    good("~/"),
    good("~",
        """Non, car dans <tt>~toto/x</tt>, <tt>~toto</tt> est remplac�
        par le r�pertoire de connexion de <tt>toto</tt>.
        Je vous accorde la r�ponse car elle est valide s'il n'y
        a rien apr�s le tilde.
        La bonne r�ponse qui marche dans tous les cas est <tt>~/</tt>
        """),
    bad("$HOME",
        """Non, car si la valeur de la variable <tt>HOME</tt> change,
        cela ne sera plus le r�pertoire de connexion.
        De plus, c'est un peu long � taper."""),
    bad("/", """Ce n'est pas le r�pertoire de connexion mais
    la racine du syst�me de fichier."""),
    ),
    indices=("""La r�ponse est en 2 caract�res, mais une r�ponse
    en un seul est accept�e""",
             ),
    )

image = "<a href='graphe.png'><img src='graphe_small.png'></a>"

add(name="graphe",
    required=["relatif 3"],
    before=image,
    question="""Votre r�pertoire courant est <tt>/home/p0123456/Toto</tt>,
    quel est le chemin relatif le plus court indiquant
    <tt>/usr/bin</tt>""",
    tests=(
    require_relative_name,
    reject_double_slash,
    reject_space,
    reject_trailing_slash,
    reject('~', "Le <tt>~</tt> indique un chemin absolu et pas relatif"),
    require_startswith('..', """Le chemin doit commencer par <tt>..</tt>
    pour remonter dans le p�re"""),
    require_endswith('bin', """Le chemin doit se finir par <tt>bin</tt>
    car c'est bien de lui dont on parle"""),
    bad("/usr/bin", "On vous demande un chemin relatif, pas absolu."),
    require('usr',
            "Comment sait-il que <tt>bin</tt> est dans <tt>usr</tt>&nbsp?"),
    bad("../../usr/bin", "�a c'est <tt>/home/usr/bin</tt>"),
    bad("../usr/bin", "�a c'est <tt>/home/p0123456/usr/bin</tt>"),
    good("../../../usr/bin",
         """Si vous �tes certain que votre racine ne changera pas
         d'emplacement, <tt>/usr/bin</tt> est plus court.
         Mais dans certain cas, il est int�ressant de tout
         faire en relatif."""),
    ),
    )

image = "<a href='graphe_cercle.png'><img src='graphe_cercle_small.png'></a>"

add(name="r�p. connexion 2",
    required=["r�p. connexion"],
    before=image,
    question="""Donnez le nom absolu
    (bien que ne commen�ant pas par <tt>/</tt>)
    le plus court d�signant le fichier <tt>/home/p0123456/toto</tt>
    si vous �tes l'utilisateur <tt>p0123456</tt>""",
    good_answer="""Ce n'est pas un nom reconnu par Unix.
    C'est le shell qui fait la substitution.
    Cela ne fonctionne donc que dans la ligne de commande ou les scripts.""",
    tests=(
    good("~/toto"),
    bad("toto",
        """Ceci est juste seulement si votre r�pertoire courant
        est votre r�pertoire de connexion.
        Mais si ce n'est pas le cas&nbsp;?"""),
    require("~",
            """Vous savez d�j� que <tt>~/</tt> est remplac�
            par le shell par votre r�pertoire de connexion"""),        
    require("~/",
            """Si le tilde n'est pas suivi d'un slash, alors ce
            qui suis est consid�r� comme un nom d'utilisateur.
            <tt>~jean/toto</tt> est le fichier <tt>toto</tt>
            dans le r�pertoire de connexion de l'utilisateur <tt>jean</tt>"""),
    reject_double_slash,
    reject_space,
    reject_trailing_slash,
    reject_dot,
    reject('~/p0123456/toto', """Le shell traduira cela en&nbsp;:
    <tt>/home/p0123456/p0123456/toto</tt>"""),
    expect('toto'),
    ),
    )

image = "<a href='tree.svg'><img border=0 src='tree_small.png'></a>"

add(name="arbre",
    required=["graphe"],
    before=image,
    question="""Dans la figure,
    combien <tt>/home</tt> contient de r�pertoires (sans compter
    les sous r�pertoires ni <tt>.</tt> et <tt>..</tt>)&nbsp;?""",
    tests=(
    good("1"),
    bad("2",
        """On vous demande le nombre de r�pertoires dans <tt>/home</tt>
        Il ne faut pas compter ceux qui sont dans ses sous r�pertoires."""),
    good("3",
         """J'accepte cette r�ponse car je suppose que vous
         avez compt� <tt>.</tt> et <tt>..</tt> bien qu'ils ne
         soient pas affich�s sur le dessin."""),
    require_int(),
    ),
    )
    
add(name="final",
    required=["point point 2", "p�re", "ici", "arbre",
              "relatif 2", "r�p. connexion 2"],
    question="""Quel est le chemin absolu le plus court valide pour Unix&nbsp;?
    <p>
    �videmment, le chemin vide (sans caract�res) n'est pas valide.
    """,
    tests=(
    good("/"),
    bad("~",
        """Ceci est un pattern du shell,
        il est en effet remplac� par un nom absolu.
        Ce nom n'est pas connu par le noyau Unix.
        """),
    require_absolute_name,
    reject(('/.', '/..'), "Valide, mais il y a plus court"),
    ),
    )

