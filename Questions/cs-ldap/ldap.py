# -*- coding: latin-1 -*-
#    QUENLIG: Questionnaire en ligne (Online interactive tutorial)
#    Copyright (C) 2008 Thierry EXCOFFIER, Olivier GL�CK, Universite de Lyon
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

general = """
    On souhaite mettre en place un annuaire LDAP qui permette&nbsp;:
    <ul>
    <li> la gestion et l'authentification sous Unix des utilisateurs de
    votre salle de TP&nbsp;;
    <li> la gestion de groupes d'utilisateurs sous Unix&nbsp;;
    <li> la gestion des noms et adresses des machines de la salle.
    </ul>
    <p>
    R�fl�chissez au mod�le d'information de votre annuaire
    (c'est-�-dire les objets dont vous avez besoin et les sch�mas LDAP
    que vous allez utiliser) ainsi qu'� l'organisation du DIT (Directory
    Information Tree) que vous allez mettre en place (mod�le de nommage).
    """

add(name="informations",
    required=["intro:avantages", "intro:inconv�nients"],
    before = general,
    question = """R�flexions sur le mod�le d'information&nbsp;:
    Pour chaque type d'objet que vous allez stocker indiquez
    ce qu'ils contiennent et � quoi cela sert.""",
    nr_lines = 5,
    tests = (good_if_contains(''),),
    )

add(name="DIT ?",
    required=["informations"],
    before = general,
    question = """Expliquez avec vos mots ce qu'est le DIT.""",
    nr_lines = 5,
    tests = (good_if_contains(''),),
    )


add(name="DIT",
    required=["DIT ?"],
    question = """Proposez une architecture du DIT&nbsp;:
    Pourquoi ce choix&nbsp;?
    Combien de niveaux&nbsp;?""",
    nr_lines = 5,
    tests = (good_if_contains(''),),
    )

add(name="DN",
    required=["informations"],
    question = """Quelle caract�ristique essentielle doit respecter le DN
    (<em>Distinguish Name</em>) d'une entr�e&nbsp;?""",
    nr_lines = 2,
    tests = (good_if_contains(''),),
    )

add(name="schema ?",
    required=["informations"],
    question = "Expliquez avec vos mots ce qu'est un <em>schema</em>&nbsp;?",
    nr_lines = 2,
    tests = (good_if_contains(''),),
    )

add(name="DN racine",
    required=["DN"],
    before = """Pour le choix de votre DN racine, on vous demande de
    respecter les conseils de l'IETF qui sont de le construire � partir
    des <tt>dc</tt> (<em>domain components</em>)
    correspondant � l'identit� de votre zone DNS.
    Renseignez-vous aupr�s des bin�mes en charge du DNS&nbsp;!
    Entendez-vous �galement avec les autres bin�mes �ventuels mettant un
    annuaire LDAP en place dans la m�me zone DNS
    (par exemple, si deux bin�mes font LDAP dans la salle <tt>tpR1</tt>, l'un
    prendra <tt>dc=tpR1A</tt> et l'autre <tt>dc=tpR1B</tt> comme
    <tt>DN</tt> racine).""",
    question = """Que choisissez-vous comme DN racine&nbsp;?
    Pourquoi ce choix&nbsp;?""",
    nr_lines = 5,
    tests = (good_if_contains(''),),
    )

add(name="le DIT",
    required=["DIT"],
    question = """Indiquez les DN que vous avez choisis pour les diff�rentes
    entit�s du DIT.""",
    nr_lines = 15,
    tests = (good_if_contains(''),),
    )

for i in range(5):
    add(name="DIT entr�e %d" % i,
        required=["le DIT"],
        question = "Donnez les informations sur une sorte d'entr�e (ou ne r�pondez pas si vous avez d�j� expliqu� toutes les sortes d'entr�e).",
        nr_lines = 5,
        default_answer = """DN de l'entr�e :
C'est un conteneur ou une feuille :
Objet structurel :
Autres objets :
Sch�ma(s) N�cessaire(s) :""",
        tests = (good_if_contains(''),),
        )


add(name="sch�ma",
        required=["le DIT", "schema ?"],
        question = "Comment voir dans quel sch�ma un objet est stock�&nbsp;?",
        nr_lines = 5,
        tests = (good_if_contains(''),),
        )

add(name="pre-installation",
    required=["le DIT"],
    before = """Installez les packages n�cessaires � la mise en place
    d'un serveur LDAP.
    <p>
    En cas de mauvaise configuration suite � l'installation des packages,
    vous pouvez reconfigurer votre serveur LDAP avec la commande
    <tt>dpkg-reconfigure slapd</tt>""",
    question = """Quelles informations avez-vous donn�es lors de
    l'installation des <em>packages</em>)&nbsp;?""",
    nr_lines = 5,
    tests = (good_if_contains(''),),
    )

add(name="fichier config",
    required=["pre-installation"],
    question = """O� est stock�e la configuration du serveur&nbsp;?""",
    tests = (good_if_contains(''),),
    )

add(name="configuration",
    required=["fichier config"],
    before = """Configurez votre machine pour qu'elle devienne serveur LDAP.
    Prenez garde � modifier, si n�cessaire, les champs d�j�
    pr�-remplis lors de l'installation des packages.""",
    question = """Quelles modifications avez-vous faites dans le
    fichier de configuration du serveur&nbsp;?""",
    nr_lines = 5,
    tests = (good_if_contains(''),),
    )

add(name="red�marrer",
    required=["pre-installation"],
    question = "Comment red�marrer le serveur LDAP&nbsp;?",
    nr_lines = 5,
    tests = (good_if_contains(''),),
    )

add(name="quand",
    required=["red�marrer"],
    question = "Quand est-il n�cessaire de red�marrer le serveur LDAP&nbsp;?",
    nr_lines = 5,
    tests = (good_if_contains(''),),
    )

add(name="log",
    required=["pre-installation"],
    question = "O� se trouvent les logs du serveur LDAP&nbsp;?",
    tests = (good_if_contains(''),),
    )


add(name="gq",
    required=["log"],
    before = """Pour voir si votre serveur LDAP fonctionne,
    essayez de vous y connecter avec l'utilitaire <tt>lima</tt>.
    <p>
    Pour savoir comment configurer un client LDAP,
    vous pouvez consulter la page de manuel de <tt>ldap.conf</tt>.
    """,
    question = "Donnez les param�tres de connexion avec <tt>lima</tt>&nbsp;:",
    nr_lines = 5,
    tests = (good_if_contains(''),),
    )


add(name="contenu",
    required=["gq"],
    question = "Quelles sont les entr�es pr�sentes dans l'annuaire juste apr�s l'installation (c'est-�-dire avant d'ajouter des entr�es)&nbsp;?",
    nr_lines = 5,
    tests = (good_if_contains(''),),
    )

add(name="ldif",
    required=["gq"],
    question = """Ecrivez un fichier au format LDIF
    contenant la description d'une entr�e pour chaque type de feuilles
    <p>
    Vous aurez 0 points si vous d�passez 50 lignes dans la r�ponse.
    """,
    nr_lines = 50,
    tests = (good_if_contains(''),),
    )

add(name="ldapadd",
    required=["ldif"],
    before = """Utilisez la commande <tt>ldapadd</tt> pour ajouter dans
    l'annuaire les entr�es que vous venez de d�crire dans le fichier LDIF.""",
    question = """Ligne de commande que vous avez utilis�&nbsp;:""",
    tests = (good_if_contains(''),),
    )

add(name="tester",
    required=["ldapadd"],
    question = """Proposez un m�thode pour v�rifier que les entr�es
    ont effectivement �t� ajout�es&nbsp;?""",
    nr_lines = 5,
    tests = (good_if_contains(''),),
    )

add(name="ajout binome",
    required=["tester"],
    before = """Avec l'utilitaire <tt>lima</tt>
    et en vous appuyant sur les entr�es pr�c�dentes,
    ajoutez dans l'annuaire une entr�e par bin�me pr�sent
    dans votre salle de TP et un groupe correspondant � l'ensemble de ces
    bin�mes.
    <p>
    Vous prendrez comme <em>uid</em> <tt>b1</tt> pour le bin�me1, <tt>b2</tt>
    pour le bin�me2, ...
    <p>
    Vous prendrez comme r�pertoire de connexion <tt>/nfshome/b1</tt>
    pour le bin�me1...
    <p>
    Pour l'instant, vous mettrez comme mot de passe, l'<em>uid</em>
    du bin�me en clair.""",
    question = "Comment proc�dez-vous&nbsp;?",
    nr_lines = 5,
    tests = (good_if_contains(''),),
    )

add(name="ajout machines",
    required=["tester"],
    before = """Ecrivez un programme ou script qui g�n�re un fichier LDIF
    d�crivant toutes les machines de <b>votre</b> zone DNS.
    <p>
    Quelques exemples d'adresse IP&nbsp;:
    <ul>
    <li> <tt>m7.tpR1/192.168.1.7</tt>
    <li> <tt>m9.tpR2/192.168.2.9</tt>
    </ul>""",
    question = """Indiquez le nom de votre zone DNS, le nom canonique
    de votre machine et donnez votre programme ou script&nbsp;:""",
    nr_lines = 15,
    tests = (good_if_contains(''),),
    )

add(name="filtre",
    required=["tester"],
    question = """Citez trois m�thodes diff�rentes vous permettant
    de voir tout le contenu de l'annuaire.
    Vous indiquerez le filtre utilis� (permettant de lister toutes
    les entr�es).""",
    nr_lines = 15,
    tests = (good_if_contains(''),),
    )

add(name="verif",
    required=["filtre"],
    before = """Essayez une de ces m�thodes pour voir si votre
    annuaire contient bien ce que vous y avez mis jusqu'� pr�sent.""",
    question = "C'est bon&nbsp;?",
    tests = (yes('Et bien trouvez pourquoi cela ne marche pas&nbsp;!!!'),),
    )

navigateur = """Si ce n'est d�j� fait,
Ouvrez un navigateur pour interroger votre annuaire.
<p>
Sous unix, vous pouvez lancer <tt>konqueror</tt>."""


add(name="filtre rdn",
    required=["filtre"],
    before = navigateur,
    question = """URL pour afficher <b>uniquement</b>
    les <tt>rdn</tt> (<em>relative distinguish name</em>)
    r�pertori�es de l'annuaire&nbsp;:""",
    nr_lines = 5,
    tests = (good_if_contains(''),),
    )

add(name="filtre membres",
    required=["filtre"],
    before = navigateur,
    question = """URL pour afficher <b>uniquement</b> les membres (nom, uid)
    du groupe contenant l'ensemble des bin�mes de la salle&nbsp;:""",
    nr_lines = 5,
    tests = (good_if_contains(''),),
    )

add(name="filtre utilisateurs",
    required=["filtre"],
    before = navigateur,
    question = """URL pour afficher <b>uniquement</b> la liste des
    utilisateurs (nom, uid) qui n'appartiennent pas � l'ensemble
    des bin�mes de la salle&nbsp;:""",
    nr_lines = 5,
    tests = (good_if_contains(''),),
    )

add(name="filtre machine",
    before = navigateur,
    required=["filtre"],
    question = """URL pour afficher <b>uniquement</b> la liste des machines
    r�pertori�es dans l'annuaire avec son/ses nom(s)
    et son adresse IP&nbsp;:""",
    nr_lines = 5,
    tests = (good_if_contains(''),),
    )

add(name="mot de passe",
    required=["ajout binome"],
    question = """Donnez la ligne de commande <tt>ldapsearch</tt> avec l'option
    <tt>-LLL</tt> qui permet d'afficher pour chaque utilisateur
    r�f�renc� dans l'annuaire son <tt>uid</tt> et son mot de passe.""",
    nr_lines = 5,
    tests = (good_if_contains(''),),
    )

add(name="mot de passe admin",
    required=["mot de passe"],
    question = """Qu'affiche la commande <tt>ldapsearch</tt> que vous avez
    donn� quand elle est ex�cut�e en tant qu'administrateur&nbsp;:""",
    nr_lines = 5,
    tests = (good_if_contains(''),),
    )

add(name="mot de passe b1",
    required=["mot de passe"],
    question = """Qu'affiche la commande <tt>ldapsearch</tt> que vous avez
    donn� quand elle est ex�cut�e en tant qu'utilisateur <tt>b1</tt>&nbsp;:""",
    nr_lines = 5,
    tests = (good_if_contains(''),),
    )

add(name="mot de passe ?",
    required=["mot de passe admin", "mot de passe b1"],
    question = """Affichage des mots de passe par un admin ou non,
    que constatez-vous ? Expliquez.""",
    nr_lines = 5,
    tests = (good_if_contains(''),),
    )

add(name="autorisation",
    required=["mot de passe"],
    before = """Modifiez le fichier <tt>slapd.conf</tt>
    (<tt>man slapd.access</tt>) afin de faire en sorte que l'attribut
    <tt>homeDirectory</tt>&nbsp;:
    <ul>
    <li> ne soit modifiable que par l'administrateur de la base
    <li> ne soit lisible que par les utilisateurs authentifi�s.
    </ul>
    Testez si vos modifications sont bien entr�es en vigueur
    (vous pourrez utiliser <tt>lima</tt> pour tenter de
    changer la valeur de l'attribut).
    """,
    question = """Quelles sont vos modifications dand <tt>slapd.conf</tt>
    <p>
    Vous aurez 0 points si vous d�passez 10 lignes dans la r�ponse.
    """,
    nr_lines = 10,
    tests = (good_if_contains(''),),
    )


add(name="authentification",
    required=["mot de passe"],
    before = """On souhaite maintenant permettre aux utilisateurs
    de la salle de s'authentifier <em>via</em> votre annuaire.""",
    question = """Quel(s) fichier(s) modifier et comment&nbsp;?
    Sur le client ou sur le serveur LDAP&nbsp;?""",
    nr_lines = 20,
    tests = (good_if_contains(''),),
    )

add(name="change passwd",
    required=["authentification"],
    before = """On souhaite maintenant permettre aux utilisateurs
    de la salle de changer leur mot de passe.""",
    question = """Quel(s) fichier(s) modifier et comment&nbsp;?
    Sur le client ou sur le serveur LDAP&nbsp;?""",
    nr_lines = 20,
    tests = (good_if_contains(''),),
    )

add(name="v�rification",
    required=["authentification"],
    question = """Contr�le du bon fonctionnement avec les commandes
    <tt>id</tt>, <tt>su</tt> ou <tt>telnet</tt>,
    <tt>chown</tt>, <tt>chgrp</tt>, ...
    <p>
    Expliquez et commentez les tests effectu�s&nbsp;:""",
    nr_lines = 10,
    tests = (good_if_contains(''),),
    )


add(name="passwd",
    required=["change passwd"],
    question = """Apr�s avoir modifi� le mot de passe avec la commande
    <tt>passwd</tt>, regardez le contenu de l'attribut <tt>userPassword</tt>
    avec <tt>ldapsearch</tt>.
    <p>
    Commentaire&nbsp;:""",
    nr_lines = 5,
    tests = (good_if_contains(''),),
    )

add(name="hostname",
    required=["v�rification"],
    before = """On souhaite maintenant permettre la r�solution
    de noms via l'annuaire LDAP.""",
    question = "Que suffit-il de faire&nbsp;?",
    nr_lines = 5,
    tests = (good_if_contains(''),),
    )

add(name="alias",
    required=["hostname"],
    question = """Comment ajoutez-vous un alias sur un nom de machine&nbsp;?
    Le <tt>ping</tt> vers cet alias fonctionne t-il&nbsp;?""",
    nr_lines = 5,
    tests = (good_if_contains(''),),
    )

add(name="wireshark",
    required=["hostname"],
    before = """Mettez en place un moyen de visualiser les �changes entre
    le client et le serveur LDAP.""",
    question = "Quel filtre de capture utilisez-vous&nbsp;?",
    tests = (good_if_contains(''),),
    )

add(name="id",
    required=["wireshark"],
    before = """Ex�cutez la commande <tt>id b1</tt> � partir d'une autre
    machine que votre serveur LDAP qui soit configur�e pour permettre
    l'authentification Unix via votre annuaire.""",
    question = """R�sumez bri�vement et commentez les �changes LDAP observ�s
    entre le client et le serveur (nombre de messages, lisibilit� des donn�es
    v�hiculant dans les requ�tes/r�ponses, ...)&nbsp;:""",
    nr_lines = 20,
    tests = (good_if_contains(''),),
    )

add(name="nouveau",
    required=["id"],
    before = """On suppose que les quatre services sont correctement
    configur�s et que vous �tes promus administrateur de l'ensemble du r�seau.
    <p>
    Un nouvel utilisateur arrive dans l'organisation avec une machine neuve
    install�e sous Linux.
    <p>
    Cet utilisateur devra pouvoir s'authentifier sur n'importe quelle machine
    du r�seau et sa machine devra �tre accessible aux autres par son nom.
    """,
    question = """Citez pr�cis�ment les op�rations que vous devez effectuer
    afin d'int�grer compl�tement ce nouvel utilisateur et sa machine dans
    votre r�seau (vous donnerez un nom de machine et un nom de login � ce
    nouvel arrivant).""",
    nr_lines = 20,
    tests = (good_if_contains(''),),
    )


add(name="total",
    required=["nouveau"],
    before = """Configurez une machine qui soit � la fois client NFS,
    client NIS, client LDAP et client DNS.
    <p>
    Testez le bon fonctionnement des quatre services.
    <p>
    Changez l'ordre d'utilisation des services en configurant le fichier
    <tt>nsswitch.conf</tt>.""",
    question = "Comment testez-vous que tout fonctionne correctement&nbsp;?",
    nr_lines = 20,
    tests = (good_if_contains(''),),
    )














































