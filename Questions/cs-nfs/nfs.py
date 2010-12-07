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


add(name="install-paquet",
    required=["intro:avantages", "intro:inconv�nients"],
    before = """Pour �viter tout probl�mes, tapez les commandes&nbsp;:
    <pre>cp �a /etc /tmp/etc
cp �a /home /tmp/home</pre>
    Ce sont ces r�pertoires que vous exporterez via NFS.
    """,
    question = """Comment v�rifiez-vous que les paquets
    <tt>nfs-kernel-server</tt> et <tt>nfs-common</tt>
    sont bien install�s&nbsp;?""",
    nr_lines = 5,
    tests = (good_if_contains(''),),
    )

add(name="install-export",
    required=["install-paquet"],
    question = """Comment configurer-vous votre machine pour exporter&nbsp;:
    <ul>
    <li> le r�pertoire <tt>/tmp/etc</tt>
    en lecture � l'ensemble des machines de votre salle
    <li> le r�pertoire <tt>/tmp/home</tt> en lecture-�criture
    � l'ensemble des machines de votre salle
    ayant une adresse IP sup�rieure � .128.
    </ul>""",
    nr_lines = 5,
    tests = (good_if_contains(''),),
    )


add(name="exportfs",
    required=["install-paquet"],
    question = "Que fait la commande <tt>exportfs �rv</tt>",
    nr_lines = 5,
    tests = (good_if_contains(''),),
    )

# Mise en place


add(name="d�marrage",
    required=["install-export"],
    question = "Comment d�marrez-vous le serveur NFS&nbsp;? D�marrez-le.",
    nr_lines = 5,
    tests = (good_if_contains(''),),
    )

add(name="export",
    required=["d�marrage", "exportfs"],
    question = """Le lancement du serveur NFS d�clenche-t-il
    l'ex�cution de la commande <tt>exportfs</tt>&nbsp;?
    <p>
    Comment le savez-vous&nbsp;?""",
    tests = (good_if_contains(''),),
    )

add(name="log",
    required=["d�marrage"],
    question = "O� se trouvent les logs du serveur NFS&nbsp;?",
    tests = (good_if_contains(''),),
    )

add(name="interdire",
    required=["log"],
    question = """Comment faites-vous pour interdire l'acc�s NFS
    aux stations <tt>.130</tt> et <tt>.131</tt>&nbsp;?""",
    nr_lines = 5,
    tests = (good_if_contains(''),),
    )


add(name="rpc",
    required=["d�marrage"],
    question = """Quelle commande (sur le client ou le serveur&nbsp;?)
    permet de v�rifier quels sont les services RPC disponibles sur
    votre serveur&nbsp;?""",
    tests = (good_if_contains(''),),
    )

add(name="nfs",
    required=["d�marrage"],
    question = """Quelle commande (sur le client ou le serveur&nbsp;?)
    permet de v�rifier que le service NFS est bien pr�sent sur
    votre serveur&nbsp;?""",
    tests = (good_if_contains(''),),
    )

add(name="partitions",
    required=["d�marrage"],
    question = """Quelle commande (sur le client ou le serveur&nbsp;?)
    permet de conna�tre l'ensemble des syst�mes de fichier NFS
    actuellement export�es par votre serveur&nbsp;?""",
    tests = (good_if_contains(''),),
    )

add(name="mount-test",
    required=["rpc", "nfs", "partitions"],
    before = """Puisque vous aurez besoin de changer d'adresse IP cliente
    pour faire vos tests, vous utiliserez comme client NFS une machine qui
    n'est ni serveur NFS, ni serveur NIS, ni serveur DNS, ni
    serveur LDAP (donc une machine inoccup�e !).
    <p>
    Sur le serveur NFS, vous taperez la commande&nbsp;:
    <pre>chmod 600 /tmp/etc/passwd</pre>
    vous pourrez dans vos tests v�rifier si vous pouvez lire ce
    fichier ou non � partir du client NFS.""",
    question = """Quelle ligne de commande tapez-vous
    pour faire une montage du <tt>/tmp/etc</tt> sur le serveur
    sur <tt>/nfsetc</tt> sur la machine locale&nbsp;?""",
    tests = (good_if_contains(''),),
    )

add(name="client",
    required=["mount-test"],
    before = """Puisque vous aurez besoin de changer d'adresse IP cliente
    pour faire vos tests, vous utiliserez comme client NFS une machine qui
    n'est ni serveur NFS, ni serveur NIS, ni serveur DNS, ni
    serveur LDAP (donc une machine inoccup�e !).
    <p>
    Sur le serveur NFS, vous taperez la commande&nbsp;:
    <pre>chmod 600 /tmp/etc/passwd</pre>
    vous pourrez dans vos tests v�rifier si vous pouvez lire ce
    fichier ou non � partir du client NFS.""",
    question = """Comment configurez-vous le client pour qu'il monte
    les syst�mes de fichier suivants � chaque d�marrage.
    <ul>
    <li> <tt>/tmp/etc</tt> sur <tt>/nfsetc</tt>
    <li> <tt>/tmp/home</tt> sur <tt>/nfshome</tt>
    </ul>
    """,
    nr_lines = 5,
    tests = (good_if_contains(''),),
    )

##add(name="erreurs",
##    required=["client"],
##    question = """Proposez un ou plusieurs sc�narii permettant de tester
##    toute la configuration avec v�rifications exhaustives des droits d'acc�s
##    et messages d'erreurs NFS rencontr�s avec explications&nbsp;:""",
##    nr_lines = 20,
##    tests = (good_if_contains(''),),
##    )

add(name="auto",
    required=["client"],
    question = "Que signifie l'option de montage <tt>auto</tt>&nbsp;?",
    nr_lines = 5,
    tests = (good_if_contains(''),),
    )

add(name="mount",
    required=["client"],
    question = "Que fait la commande : <tt>mount -a -t nfs</tt>&nbsp;?",
    nr_lines = 5,
    tests = (good_if_contains(''),),
    )

add(name="root_lit",
    required=["client"],
    question = """Sur le client, en tant qu'utilisateur <tt>root</tt>,
    quels fichiers de <tt>/tmp/etc</tt> sont lisibles&nbsp;?""",
    nr_lines = 5,
    tests = (good_if_contains(''),),
    )

add(name="moi_lit",
    required=["client"],
    question = """Sur le client, en tant qu'utilisateur <tt>moi</tt>,
    quels fichiers de <tt>/tmp/etc</tt> sont lisibles&nbsp;?""",
    nr_lines = 5,
    tests = (good_if_contains(''),),
    )

add(name="root_ecrit",
    required=["client"],
    question = """Sur le client, en tant qu'utilisateur <tt>root</tt>,
    quels fichiers de <tt>/tmp/etc</tt> et <tt>/tmp/home</tt>
    sont modifiables&nbsp;?""",
    nr_lines = 5,
    tests = (good_if_contains(''),),
    )

add(name="moi_ecrit",
    required=["client"],
    question = """Sur le client, en tant qu'utilisateur <tt>moi</tt>,
    quels fichiers de <tt>/tmp/home</tt> sont modifiables&nbsp;?""",
    nr_lines = 5,
    tests = (good_if_contains(''),),
    )

add(name="lecture",
    required=["root_lit", "moi_lit"],
    question = """Expliquez les diff�rences d'acc�s en lecture
    pour <tt>root</tt> et </tt>moi</tt>&nbsp;?""",
    nr_lines = 5,
    tests = (good_if_contains(''),),
    )

add(name="superroot",
    required=["lecture"],
    question = """Comment modifier la configuration du serveur pour lire
    tous les fichiers en tant que <tt>root</tt>&nbsp;?""",
    nr_lines = 5,
    tests = (good_if_contains(''),),
    )

# Protocole

add(name="protocole",
    required=["client"],
    question = """Comment allez-vous espionner les �changes
    entre le client et le serveur&nbsp;?""",
    tests = (good_if_contains(''),),
    )

add(name="filtre",
    required=["protocole"],
    question = """Visualisation des �changes entre le client et le serveur NFS.
    Quel filtre de capture utilisez vous ?""",
    tests = (good_if_contains(''),),
    )

r = """R�sum� (nombre de messages, noms et param�tres des proc�dures distantes ex�cut�es, ...) et commentaires des �changes NFS suite � la commande : """


add(name="mkdir",
    required=["filtre"],
    question = r + "<tt>mkdir /nfshome/moi/TMP</tt>",
    nr_lines = 5,
    tests = (good_if_contains(''),),
    )

add(name="chmod",
    required=["filtre"],
    question = r + "<tt>chmod 777 /nfshome/moi/TMP</tt>",
    nr_lines = 5,
    tests = (good_if_contains(''),),
    )

add(name="cd",
    required=["filtre"],
    question = r + "<tt>cd /nfshome/moi/TMP</tt>",
    nr_lines = 5,
    tests = (good_if_contains(''),),
    )

add(name="�criture",
    required=["filtre"],
    question = r + "<tt>echo \"Bonjour\" &gt;/nfshome/moi/TMP/bj.txt</tt>",
    nr_lines = 5,
    tests = (good_if_contains(''),),
    )


# S'il reste du temps

add(name="new",
    required=["mkdir", "chmod", "cd", "�criture"],
    before = """Configurez une machine qui soit � la fois client NFS,
    client NIS, client LDAP et client DNS.
    <p>
    On suppose que les quatre services sont correctement
    configur�s et que vous �tes promus administrateur de l'ensemble du r�seau.
    Un nouvel utilisateur arrive dans l'organisation avec une
    machine neuve install�e sous Linux.
    <p>
    Citez pr�cis�ment les op�rations que vous devez effectuer afin
    d'int�grer compl�tement ce nouvel utilisateur et sa machine dans
    votre r�seau (vous donnerez un nom de machine et un nom de login
    � ce nouvel arrivant).
    <p>
    Cet utilisateur devra pouvoir s'authentifier sur n'importe quelle machine
    du r�seau et sa machine devra �tre accessible aux autres par son nom.
    """,

    question = "Int�gration d'un nouvel utilisateur et de sa machine dans votre r�seau",
    nr_lines = 5,
    default_answer = """Nom de machine :
Nom de login :
Op�rations � effectuer : 
""",
    tests = (good_if_contains(''),),
    )

add(name="vitesse",
    required=["mkdir", "chmod", "cd", "�criture"],
    question = """�valuez les performances d'NFS par rapport � un acc�s
    au syst�me de fichier local pour&nbsp;:
    <ul>
    <li> La copie d'un gros fichier.
    <li> La creation et l'extraction d'une grosse archive.
    </ul>
    """,
    nr_lines = 10,
    tests = (good_if_contains(''),),
    )

add(name="verrous",
    required=["mkdir", "chmod", "cd", "�criture"],
    question = """Configurez un deuxi�me client et v�rifiez que
    si un client verrouille un fichier l'autre client ne pourra
    pas le verrouiller.
    <p>
    Utilisez la commande <tt>flock</tt> pour verrouiller le fichier.
    <p>
    Quel processus g�re les verrous&nbsp;?
    """,
    tests = (good_if_contains(''),),
    )

add(name="persistent",
    required=["verrous"],
    question = """Red�marrez le serveur NFS, qu'est-ce qui se passe&nbsp;?
    <ul>
    <li> Pour les fichiers en cours d'�criture, est-ce que la copie
    se termine correctement&nbsp;?
    <li> Le client a-t-il besoin de refaire le montage&nbsp;?
    <li> Les verrous sont-ils d�verrouill�s&nbsp;?
    </ul>
    """,
    tests = (good_if_contains(''),),
    )











