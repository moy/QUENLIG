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

add(name="domaine",
    required=["intro:avantages", "intro:inconv�nients"],
    before = """Vous choisirez comme nom de domaine <tt>tpR1_nisdomain</tt>
    ou <tt>tpR2_nisdomain</tt> selon votre emplacement
    <tt>(tpR1A_nisdomain</tt> ou <tt>tpR1B_nisdomain</tt>
    si vous �tes plusieurs bin�mes NIS dans la salle TPR1...)""",
    question = "Quel est votre nom de domaine NIS&nbsp;?",
    tests = (good_if_contains(''),),
    )

# 4.1

add(name="purge",
    required=["domaine"],
    before = """Effacez les installations pr�c�dentes du package NIS
    afin de partir d'une configuration propre : <pre>dpkg --purge nis</pre>""",
    question = "C'est fait&nbsp;?",
    tests = (good_if_contains(''),),
    )

add(name="install",
    required=["purge"],
    before = """Installez le package nis n�cessaire � la mise en place
    du serveur NIS (faites &lt;CTRL-C&gt; quand le message
    � <em>Starting NIS services...</em> � appara�t)""",
    question="Quelle commande avez-vous tap� pour installer le package&nbsp;?",
    tests = (good_if_contains(''),),
    )

add(name="kill",
    required=["install"],
    before = """Tuez les d�mons yp qui tournent encore avec <tt>kill</tt>
    (faire un <tt>ps -fe</tt> pour v�rifier).""",
    question="Quel sont les noms des d�mons que vous avez tu�&nbsp;?",
    tests = (good_if_contains(''),),
    )

add(name="start",
    required=["kill"],
    before = """Red�marrez le <em>portmapper</em> (peut �tre long) :
    <pre>/etc/init.d/portmap restart</pre>""",
    question="� quoi sert le <em>portmapper</em>&nbsp;?",
    nr_lines = 5,
    tests = (good_if_contains(''),),
    )

add(name="nom du domaine",
    required=["start"],
    before = """Positionnez/v�rifiez le nom de votre domaine NIS.""",
    question="Comment avez-vous fait&nbsp;?",
    nr_lines = 2,
    tests = (good_if_contains(''),),
    )

add(name="NISSERVER",
    required=["nom du domaine"],
    before = """Renseignez la variable <tt>NISSERVER</tt> du fichier
    <tt>/etc/default/nis</tt> (vous pourrez
    �diter le fichier <tt>/etc/init.d/nis</tt>
    pour voir quelle valeur lui assigner).""",
    question="Quelle valeur lui avez-vous donn�&nbsp;?",
    tests = (good_if_contains(''),),
    )

add(name="aussi client",
    required=["NISSERVER"],
    before = """Configurez votre machine pour qu'elle soit aussi
    client NIS&nbsp;: vous ferez en sorte que le client NIS ne recherche pas
    les serveurs NIS par <em>broadcast</em> mais plut�t qu'il interroge
    directement votre serveur NIS.""",
    question="Comment avez-vous fait&nbsp;?",
    nr_lines = 2,
    tests = (good_if_contains(''),),
    )


add(name="ypinit",
    required=["aussi client"],
    before = """Cr�ez la base NIS � l'aide de la commande <tt>ypinit</tt>""",
    question="Comment avez-vous proc�d�&nbsp;?",
    nr_lines = 5,
    tests = (good_if_contains(''),),
    )

add(name="ypinit ?",
    required=["ypinit"],
    question="Que fait la commande <tt>ypinit</tt>&nbsp;?",
    nr_lines = 5,
    tests = (good_if_contains(''),),
    )

add(name="lancement",
    required=["ypinit"],
    before = """D�marrez votre serveur NIS ma�tre et v�rifiez que les bons
    d�mons sont bien lanc�s.""",
    question="Quelle commande utilisez-vous pour lancer le serveur NIS&nbsp;?",
    tests = (good_if_contains(''),),
    )

add(name="d�mons ma�tre",
    required=["lancement"],
    question = "Quels d�mons doivent tourner sur le serveur NIS ma�tre&nbsp;?",
    nr_lines = 5,
    tests = (good_if_contains(''),),
    )

add(name="d�mons client",
    required=["lancement"],
    question = "Quels d�mons doivent tourner sur les clients NIS&nbsp;?",
    nr_lines = 5,
    tests = (good_if_contains(''),),
    )

add(name="client actif",
    required=["d�mons client"],
    question="Les d�mons du client NIS sont-ils actifs&nbsp;?",
    tests = (yes("Ils devraient l'�tre."),),
    )

add(name="lance client",
    required=["client actif"],
    question="Quelle commande a lanc� les d�mons pour �tre un client&nbsp;?",
    tests = (good_if_contains(''),),
    )

add(name="d�marrage",
    required=["lancement"],
    question = """Une fois que le serveur NIS est d�marr�, comment faites-vous
    pour v�rifier que les bons d�mons sont lanc�s&nbsp;?""",
    nr_lines = 5,
    tests = (good_if_contains(''),),
    )

add(name="carte",
    required=["ypinit"],
    question = """Qu'est ce qu'une carte (<em>map</em>)&nbsp;?""",
    nr_lines = 5,
    tests = (good_if_contains(''),),
    )

add(name="cat carte",
    required=["carte"],
    question = """Les cartes (<em>maps</em>)
    sont-elles lisibles par la commande <tt>cat</tt>&nbsp;?""",
    tests = (good_if_contains(''),),
    )

add(name="ypmake",
    required=["ypinit"],
    question="Que fait la commande <tt>make</tt> dans <tt>/var/yp</tt>&nbsp;?",
    nr_lines = 5,
    tests = (good_if_contains(''),),
    )

# 4.2


add(name="client",
    required=["d�marrage"],
    before = """Puisque vous aurez besoin de changer d'adresse IP cliente
    pour faire vos tests, vous utiliserez comme client NIS une machine
    qui n'est ni serveur NFS, ni serveur NIS, ni serveur DNS, ni
    serveur LDAP (donc une machine inoccup�e !).""",
    question = """Configurez un client NIS sur une autre machine.
    Quelles sont les manipulations effectu�es&nbsp;?""",
    nr_lines = 5,
    tests = (good_if_contains(''),),
    )

add(name="rpc",
    required=["client"],
    question = """Quelle commande permet de v�rifier quels sont les services
    RPC disponibles sur votre serveur&nbsp;?
    <p>
    Indiquez sur quelle machine vous faites tourner la commande.""",
    nr_lines = 2,
    tests = (good_if_contains(''),),
    )

add(name="service",
    required=["client"],
    question = """Quelle commande permet de v�rifier qu'un serveur NIS
    est bien joignable sur votre serveur&nbsp;?<p>
    Indiquez sur quelle machine vous faites tourner la commande.""",
    nr_lines = 2,
    tests = (good_if_contains(''),),
    )

add(name="password",
    required=["client"],
    question = """Quelle commande permet de v�rifier que le service
    permettant le changement de mot de passe via les NIS est disponible&nbsp;?
    <p>Indiquez sur quelle machine vous faites tourner la commande.""",
    nr_lines = 2,
    tests = (good_if_contains(''),),
    )

add(name="bind",
    required=["client"],
    question = """Quelle commande permet de savoir si un client NIS
    tourne sur une machine&nbsp;?
    <p>Indiquez sur quelle machine vous faites tourner la commande.""",
    nr_lines = 2,
    tests = (good_if_contains(''),),
    )

add(name="serveur",
    required=["client"],
    question = """Quelle commande permet de conna�tre, � partir d'une machine
    cliente, le serveur NIS auquel elle est associ�e&nbsp;?""",
    nr_lines = 2,
    tests = (good_if_contains(''),),
    )

add(name="affiche carte",
    required=["client"],
    question = """Quelle commande permet d'afficher, � partir d'une machine
    cliente, le contenu de la carte <tt>passwd</tt> du serveur NIS&nbsp;?
    <p>Indiquez sur quelle machine vous faites tourner la commande.""",
    nr_lines = 2,
    tests = (good_if_contains(''),),
    )

#

add(name="carte des noms",
    required=["affiche carte"],
    question = """D�crivez pr�cisemment un sc�narii qui permette de tester
    le bon fonctionnement de votre serveur NIS en ce qui
    concerne la <b>carte des noms de machine</b>.""",
    nr_lines = 5,
    tests = (good_if_contains(''),),
    )

add(name="carte passwd",
    required=["affiche carte"],
    question = """D�crivez pr�cisemment un sc�narii qui permette de tester
    le bon fonctionnement de votre serveur NIS en ce qui
    concerne la <b>carte passwd/group</b>.""",
    nr_lines = 5,
    tests = (good_if_contains(''),),
    )

# 4.3

add(name="utilisateur",
    required=["affiche carte"],
    question = """
Sur le serveur NIS, ajoutez un utilisateur <tt>titi</tt> et donnez un nom
� votre machine cliente (<tt>nisclient_xxxx</tt> o� <tt>xxxx</tt> sont
les initiales du bin�me).
<p>
Indiquez ce qu'il faut faire pour
ajouter l'utilisateur et la machine et que ces informations
soient accessibles depuis le client NIS.""",
    nr_lines = 5,
    tests = (good_if_contains(''),),
    )

add(name="filtre",
    required=["affiche carte"],
    question = """Echanges entre le client et le serveur NIS.
    Quel filtre de capture utilisez-vous dans <tt>wireshark</tt>&nbsp;?""",
    tests = (good_if_contains(''),),
    )

add(name="ypwhich",
    required=["filtre"],
    question = """R�sum� des �changes observ�s (nombre de messages, noms
    et param�tres des proc�dures distantes ex�cut�es, ...)
    suite � la commande <tt>ypwhich</tt>""",
    tests = (good_if_contains(''),),
    nr_lines = 5,
    )


add(name="telnet",
    required=["filtre"],
    question = """R�sum� des �changes observ�s (nombre de messages,
    noms et param�tres des proc�dures distantes ex�cut�es, ...)
    suite � la commande <tt>ssh nis<b>client</b>_xxxx</tt>""",
    tests = (good_if_contains(''),),
    nr_lines = 5,
    )

add(name="id",
    required=["filtre"],
    question = """R�sum� des �changes observ�s (nombre de messages, noms
    et param�tres des proc�dures distantes ex�cut�es, ...)
    suite � la commande <tt>id titi</tt>""",
    tests = (good_if_contains(''),),
    nr_lines = 5,
    )

add(name="yppasswd",
    required=["filtre"],
    question = """R�sum� des �changes observ�s (nombre de messages,
    noms et param�tres des proc�dures distantes ex�cut�es, ...)
    suite � la commande <tt>yppasswd titi</tt>""",
    tests = (good_if_contains(''),),
    nr_lines = 5,
    )

# 4.4

add(name="access",
    required=["yppasswd", "telnet", "ypwhich", "id"],
    before = """Restreignez l'acc�s uniquement � l'ensemble des machines
    de votre salle ayant une adresse IP sup�rieure � .128,
    except�es les stations .132 et .133.""",
    question = "Comment avez-vous fait&nbsp;?",
    tests = (good_if_contains(''),),
    nr_lines = 10,
    )

add(name="permanent nomade",
    required=["access"],
    before = """Les utilisateurs du r�seau sont d�sormais s�par�s en deux
    cat�gories&nbsp;:
    <ul>
    <li> les personnels permanents qui peuvent se connecter depuis
    n'importe quelle machine autoris�e&nbsp;;
    <li> les personnels nomades qui ne peuvent se connecter que sur
    les machines autoris�es ayant une adresse IP multiple de 10
    (.130, .140, ...).
    </ul>""",
    question = """Proposez une solution permettant la mise en oeuvre
de cette architecture et mettez la en place.""",
    tests = (good_if_contains(''),),
    nr_lines = 5,
    )

add(name="tests",
    required=["permanent nomade", "access"],
    question = """D�crivez et faites les tests permettant de v�rifier
    les restrictions d'acc�s des utilisateurs permanents et nomades.""",
    tests = (good_if_contains(''),),
    nr_lines = 5,
    )

# 4.5

add(name="nouvelle machine",
    required=["tests"],
    before = """On suppose que les quatre services sont correctement
    configur�s et que vous �tes promus administrateur de l'ensemble du r�seau.
    <p>
    Un nouvel utilisateur arrive dans l'organisation avec une
    machine neuve install�e sous Linux.
    <p>
    Cet utilisateur devra pouvoir s'authentifier sur n'importe quelle machine
    du r�seau et sa machine devra �tre accessible aux autres par son nom.
    """,
    question = """Citez pr�cis�ment les op�rations que vous devez effectuer
    afin d'int�grer compl�tement ce nouvel utilisateur et sa machine dans
    votre r�seau (vous donnerez un nom de machine et un nom de login
    � ce nouvel arrivant).""",
    tests = (good_if_contains(''),),
    nr_lines = 5,
    )

add(name="totale",
    required=["nouvelle machine"],
    question = """Configurez une machine qui soit � la fois client NFS,
    client NIS, client LDAP et client DNS.
    <p>
    Comment testez-vous que tout fonctionne correctement&nbsp;?""",
    tests = (good_if_contains(''),),
    nr_lines = 5,
    )

add(name="nsswitch.conf",
    required=["nouvelle machine"],
    question = """Qu'indique le fichier <tt>nsswitch.conf</tt>&nbsp;?""",
    tests = (good_if_contains(''),),
    nr_lines = 5,
    )

add(name="ordre",
    required=["nsswitch.conf"],
    question = """Est-ce une bonne/mauvaise id�e de mettre <tt>nis</tt>
    en premier&nbsp;?""",
    tests = (good_if_contains(''),),
    nr_lines = 5,
    )

add(name="secondaire",
    required=["nouvelle machine"],
    question = """Mise en place d'un serveur NIS secondaire,
    configuration d'un client NIS recherchant le serveur NIS par broadcast
    et v�rification que si le serveur NIS associ� au client tombe en panne,
    l'autre serveur prend le relais pour r�pondre au client.
    <p>
    Expliquez comment mettre en place et tester tout cela.""",
    tests = (good_if_contains(''),),
    nr_lines = 10,
    )

add(name="restrictions",
    required=["tests"],
    question = """Expliquez comment configurer des acc�s restreints
    carte par carte (<tt>man ypserv.conf</tt>).""",
    tests = (good_if_contains(''),),
    nr_lines = 10,
    )
