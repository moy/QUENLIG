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

add(name="zone",
    required=["intro:avantages", "intro:inconv�nients"],
    before = """On vous propose dans cette partie de :
    <ul>
   <li> mettre en place un serveur DNS primaire qui soit serveur de source
   autoris�e pour la zone de votre salle de TP dont vous avez la charge&nbsp;;
   <li> tester le bon fonctionnement local du serveur � partir des machines
   clientes de la salle&nbsp;;
   <li> mettre en place un serveur racine (primaire ou secondaire)
   et tester l'interrogation du serveur DNS de l'autre salle de TP&nbsp;;
   <li> analyser les �changes de requ�tes/r�ponses DNS entre les diff�rents
   serveurs.
   </ul>
   <p>
   Pour simplifier, les zones DNS seront des TLD (Top Level Domain)
   et les machines seront nomm�es par le biais de leur adresse IP.
   <p>
   Par exemple, les machines de la salle TPR1 seront dans la
   zone <tt>.tpR1.</tt> et seront r�f�renc�es dans le serveur DNS
   de la fa�on suivante&nbsp;;:
   <ul>
   <li> <tt>m1.tpR1</tt> pour <tt>192.168.1.1</tt>
   <li> <tt>m10.tpR1</tt> pour <tt>192.168.1.10</tt>
   </ul>
   <p>
   Si plusieurs bin�mes mettent en place un serveur DNS dans la m�me salle,
   mettez en place une zone par bin�me en vous r�partissant les plages
   d'adresses IP g�r�es de mani�re �quitable.
   <p>
   Si par exemple deux bin�mes sont en charge du DNS dans la salle TPR2&nbsp;:
   <ul>
   <li> Le bin�me A sera en charge de la zone <tt>.tpR2A.</tt>
   son serveur DNS primaire r�f�rencera les machines ayant une adresse
   IP impaire.
   <li> Le bin�me B sera en charge de la zone <tt>.tpR2B.</tt>
   son serveur DNS primaire r�f�rencera les machines ayant une adresse
   IP paire.
   </ul>
   """,
    question = "Quelle est votre zone DNS&nbsp;?",
    tests = (good_if_contains(''),),
    )

add(name="plage",
    required=["intro:avantages", "intro:inconv�nients"],
    question = "Quelle est votre plage d'adresse IP&nbsp;?",
    tests = (good_if_contains(''),),
    )

add(name="install",
    required=["zone", "plage"],
    question = """Quelle commande tapez-vous pour installer les paquets
    n�cessaires � la mise en place d'un serveur DNS&nbsp;?""",
    tests = (good_if_contains(''),),
    )



add(name="named.conf",
    required=["install"],
    question = """Que modifiez-vous dans le fichier <tt>named.conf</tt>
    pour configurer votre machine afin qu'elle soit un serveur DNS&nbsp;?
    <p>
    Vous aurez 0 points si vous d�passez 10 lignes dans la r�ponse.
    """,
    nr_lines = 10,
    tests = (good_if_contains(''),),
    )

add(name="zones",
    required=["install"],
    question = """Que modifiez-vous dans les fichiers de zone.
    Donnez uniquement pour chaque fichier de zone <b>un ou deux</b>
    exemples de chaque type de RR (<em>Resource Record</em>) utilis�.
    <p>
    Vous aurez 0 points si vous d�passez 30 lignes dans la r�ponse.
    """,
    nr_lines = 30,
    tests = (good_if_contains(''),),
    )

add(name="creation zone",
    required=["install"],
    before = """Le nombre de machines � renseigner �tant important,
    on vous sugg�re de g�n�rer automatiquement vos fichiers de zone � l'aide
    d'un petit programme C ou script shell par exemple.
    <p>
    N'oubliez pas de renseigner la zone inverse.""",
    question = """Expliquez comment vous g�n�rez les fichiers de zone,
    donnez l'algorithme ou le programme.""",
    nr_lines = 10,
    tests = (good_if_contains(''),),
    )

add(name="lancement",
    required=["named.conf", "zones", "creation zone"],
    before = """D�marrez le serveur DNS""",
    question = "Quelle commande permet de d�marrer le serveur DNS&nbsp;?",
    tests = (good_if_contains(''),),
    )

add(name="logs",
    required=["named.conf", "zones", "creation zone"],
    question = """O� sont les fichiers de logs du serveur DNS&nbsp;?""",
    indices = ('Cherchez dans <tt>/var/log</tt>',),
    good_answer = '''Pensez � regarder les logs du serveur DNS � chaque d�marrage du serveur.''',
    tests = (good_if_contains(''),),
    )

add(name="noms logiques",
    required=["lancement"],
    before = """On vous demande maintenant de donner des noms plus parlants
    � certaines machines telles que les serveurs NFS, les serveurs NIS,
    les serveurs DNS, les serveurs LDAP, et ce sans changer le nom canonique.
    <p>
    On pourra par exemple donner des noms tels que <tt>dns1.tpR1</tt>,
    <tt>nfs1.tpR2</tt>, <tt>nis2.tpR2A</tt>, ...
    <p>
    Pour ce faire, vous demanderez aux bin�mes de votre zone les
    services qu'ils mettent en place et les adresses IP qu'ils utilisent.
    """,
    question = """Comment proc�dez vous&nbsp;?
    <p>
    Mettez en place cettenouvelle configuration.
    <p>
    Vous aurez 0 points si vous d�passez 10 lignes dans la r�ponse.
    """,
    nr_lines = 10,
    tests = (good_if_contains(''),),
    )


add(name="client",
    required=["noms logiques"],
    before = """Configurez un client DNS de votre zone avec comme nom de
    domaine par d�faut celui de votre zone et comme serveur DNS local
    le serveur primaire de la zone (le v�tre !).""",
    question = "Comment avez-vous fait&nbsp;?",
    nr_lines = 10,
    tests = (good_if_contains(''),),
    )

add(name="dig",
    required=["client"],
    question = """Dans la commande <tt>dig @server name type</tt>,
    pr�cisez ce que signifie chaque param�tre.""",
    nr_lines = 5,
    tests = (good_if_contains(''),),
    )

add(name="dig host",
    required=["dig"],
    question = """Donnez la syntaxe �quivalente �
    <tt>dig @server name type</tt>
    avec la commande <tt>host</tt>""",
    nr_lines = 5,
    tests = (good_if_contains(''),),
    )






add(name="connue",
    required=["dig"],
    question = """Quelle ligne de commande permet de v�rifier que votre
    machine cliente est bien enregistr�e dans le serveur DNS
    de votre zone&nbsp;?""",
    nr_lines = 5,
    tests = (good_if_contains(''),),
    )

add(name="inverse",
    required=["dig"],
    question = """Quelle ligne de commande permet de v�rifier que votre
    machine cliente est bien enregistr�e dans la zone inverse&nbsp;?""",
    nr_lines = 5,
    tests = (good_if_contains(''),),
    )

add(name="serveurs",
    required=["dig"],
    question = """Quelle ligne de commande permet de lister les serveurs
    primaire et secondaires de votre zone&nbsp;?""",
    nr_lines = 5,
    tests = (good_if_contains(''),),
    )

add(name="contact",
    required=["dig"],
    question = """Quelle ligne de commande permet de conna�tre l'adresse
    e-mail de l'administrateur de la zone&nbsp;?""",
    nr_lines = 5,
    tests = (good_if_contains(''),),
    )

add(name="alias",
    required=["dig"],
    question = """Quelle ligne de commande permet de lister tous les alias
    de votre zone (et uniquement eux)&nbsp;?""",
    nr_lines = 5,
    tests = (good_if_contains(''),),
    )

add(name="tout",
    required=["dig"],
    question = """Quelle ligne de commande permet de conna�tre l'ensemble
    des enregistrements r�f�renc�s par votre serveur DNS&nbsp;?""",
    nr_lines = 5,
    tests = (good_if_contains(''),),
    )


add(name="commentaire",
    required=["connue", "inverse", "serveurs", "contact", "alias", "tout"],
    question = """Pour les diff�rentes commandes que vous avez essay�
    (elles sont list�es sur cette page)
    indiquez si vous avez bien obtenu le r�sultat escompt�&nbsp;:""",
    nr_lines = 5,
    tests = (good_if_contains(''),),
    )

# 5.3

add(name="racine",
    required=["commentaire"],
    before = """Entendez-vous avec les autres bin�mes s'occupant du DNS
    pour configurer une machine en tant que passerelle entre les deux salles
    de TP.
    <p>
    V�rifier � l'aide de la commande <tt>ping</tt> que vous
    arrivez � joindre le serveur DNS de l'autre salle.
    <p>
    N'oubliez pas de configurer sur les machines clientes la route par
    d�faut vers la passerelle&nbsp;!
    <p>
    Vous prendrez comme passerelle la machine � c�t�
    du switch central avec les adresses IP 192.168.1.1 et 192.168.2.1
    """,
    question = """Indiquez les zones DNS, machines et adresses IP pour
    l'enseble des deux salles&nbsp;:""",
    nr_lines = 20,
    tests = (good_if_contains(''),),
    )

dig = """Pour cette question, vous utiliserez la commande <tt>dig</tt>
    sans PUIS avec l'option <tt>+trace</tt> pour voir plus pr�cis�ment ce qui
    se passe (encha�nement des requ�tes entre les diff�rents serveurs DNS
    potentiels)."""


imaginaire = """A partir d'une machine cliente configur�e pour interroger
votre serveur DNS, que se passe t-il si vous essayez de r�soudre le nom
d'une machine imaginaire (par ex. <tt>www.google.fr</tt>) qui n'est
r�f�renc�e dans aucun des serveurs DNS install�s&nbsp;?"""

add(name="imaginaire",
    required=["commentaire"],
    before = dig,
    question = imaginaire,
    nr_lines = 10,
    tests = (good_if_contains(''),),
    )

autre = """A partir d'une machine cliente configur�e pour interroger
votre serveur DNS, que se passe t-il si vous essayez de r�soudre le nom
d'une machine est r�f�renc�e dans un autre serveur DNS
(par exemple celui de l'autre salle)&nbsp;?"""

add(name="autre",
    required=["commentaire"],
    before = dig,
    question = autre,
    nr_lines = 10,
    tests = (good_if_contains(''),),
    )

directe = """Que se passe t-il si vous essayez de r�soudre le nom
d'une machine est r�f�renc�e dans un autre serveur DNS
(par exemple celui de l'autre salle) en interrogeant directement
l'autre serveur DNS&nbsp;?"""

add(name="directe",
    required=["commentaire"],
    before = dig,
    question = directe,
    nr_lines = 10,
    tests = (good_if_contains(''),),
    )




##add(name="trace",
##    required=["imaginaire", "autre", "directe"],
##    question = "Refaites les commandes avec <tt>+trace</tt>, conclusions&nbsp;?",
##    nr_lines = 10,
##    tests = (good_if_contains(''),),
##    )


add(name="racines",
    required=["imaginaire", "autre", "directe"],
    before = """Sur une autre machine que la v�tre (si possible),
    mettez en place un serveur racine qui r�f�rence l'ensemble des zones DNS
    mises en place.
    <p>
    Entendez-vous avec les autres bin�mes DNS pour savoir si vous �tes serveur
    racine primaire (zone de type <em>master</em>)
    ou secondaire (zone de type <em>slave</em> : <tt>man named.conf</tt>).
    <p>
    Vous prendrez comme adresse IP pour votre serveur racine&nbsp;:
    <ul>
    <li> 192.168.2.19 (ou .18) si vous �tes dans la salle TPR1
    <li> 192.168.1.19 (ou .18) si vous �tes dans la salle TPR2.
    </ul>""",
    question = """Pour votre serveur racine primaire ou secondaire
    indiquez l'adresse IP et les modifications faites dans <tt>named.conf</tt>.
    <p>
    Vous aurez 0 points si vous d�passez 10 lignes dans la r�ponse.
    """,
    nr_lines = 10,
    tests = (good_if_contains(''),),
    )

add(name="racines zone",
    required=["racines"],
    before = """Mettez � jour le fichier de zone racine de votre serveur DNS
    primaire et relancez le.""",
    question = """Contenu du fichier de la zone racine&nbsp;:
    <p>
    Vous aurez 0 points si vous d�passez 20 lignes dans la r�ponse.
    """,
    nr_lines = 20,
    tests = (good_if_contains(''),),
    )

dig = """<b><big>
Maintenant que le serveur DNS racine est configur� et fonctionne</big></b>"""

more = """<p>
Indiquez l'enchainement des requ�tes/r�ponses DNS en pr�cisant bien
la nature des serveurs DNS impliqu�s.
<p>
Vous pr�ciserez �galement la nature des requ�tes/r�ponses
(it�rative ou r�cursive)."""

add(name="imaginaire2",
    required=["racines"],
    before = dig,
    question = imaginaire + more,
    nr_lines = 10,
    tests = (good_if_contains(''),),
    )

add(name="autre2",
    required=["racines"],
    before = dig,
    question = autre + more,
    nr_lines = 10,
    tests = (good_if_contains(''),),
    )

add(name="directe2",
    required=["racines"],
    before = dig,
    question = directe + more,
    nr_lines = 10,
    tests = (good_if_contains(''),),
    )


add(name="d�branche",
    required=["imaginaire2", "autre2", "directe2"],
    question = """Que se passe t-il si vous d�branchez le c�ble r�seau
    du serveur racine primaire et que vous essayez des requ�tes&nbsp;:""",
    nr_lines = 10,
    tests = (good_if_contains(''),),
    )

#

add(name="resolv",
    required=["racines"],
    before = """Sur une machine cliente, ajoutez les suffixes des autres
    zones DNS dans le fichier <tt>/etc/resolv.conf</tt>.""",
    question = """Les modifications que vous avez faites dans le fichier
    <tt>/etc/resolv.conf</tt>&nbsp;:""",
    nr_lines = 5,
    tests = (good_if_contains(''),),
    )

add(name="ping",
    required=["resolv"],
    question = """Faites <tt>ping m138</tt> et notez l'adresse
    IP correspondante&nbsp;:""",
    tests = (good_if_contains(''),),
    )

add(name="ping2",
    required=["resolv"],
    before = """Changez l'ordre des suffixes dans <tt>/etc/resolv.conf</tt>
    puis refaites <tt>ping m138</tt>""",
    question = "Notez l'adresse IP correspondante.&nbsp;:""",
    tests = (good_if_contains(''),),
    )

add(name="diff�rence",
    required=["ping", "ping2"],
    question = "Expliquez les cons�quences du changement d'ordre des suffixes&nbsp;:",
    nr_lines = 5,
    tests = (good_if_contains(''),),
    )

#


add(name="exp�rience 1",
    required=["resolv"],
    before = """Vous pouvez exp�rimenter un �change de zones entre un serveur
    de noms racine primaire et un serveur racine secondaire.
    <p>
    Modifiez sur le serveur primaire le num�ro de s�rie dans l'enregistrement
    SOA (comme si vous aviez modifi� le fichier de zone) et relancez
    le service.
    <p>
    Relancez ensuite le service sur le serveur de noms secondaire.
    """,
    question = """Que constatez-vous dans le fichier de zone du serveur
    secondaire&nbsp;?
    <p>
    Regardez �galement les dates de derni�re modification du fichier.""",
    nr_lines = 10,
    tests = (good_if_contains(''),),
    )

add(name="exp�rience 2",
    required=["resolv"],
    before = """Vous pouvez exp�rimenter une autre proc�dure d'�change,
    mais cette fois sans relancer le serveur de noms secondaire.
    <p>
    Modifiez d'abord sur les deux serveurs le d�lai de rafra�chissement
    (refresh) et mettez-le � 2 minutes.
    <p>
    Relancez les services.
    <p>
    Modifiez sur le serveur primaire le num�ro de s�rie et relancez le
    service.""",
    question = """Que constatez-vous au bout de 2 minutes
    sur le serveur secondaire&nbsp;?""",
    nr_lines = 10,
    tests = (good_if_contains(''),),
    )

# 5.4

add(name="wireshark",
    required=["resolv"],
    before = """Visualiser avec <tt>wireshark</tt> les �changes de
    requ�tes/r�ponses DNS correspondant � une r�solution de nom vers
    une machine de l'autre salle pour laquelle vous n'avez encore jamais
    effectu� la r�solution de nom.""",
    question = """Indiquez le nombre de requ�tes/r�ponses pour
    cette r�solution ainsi que les fanions de la r�ponse DNS.""",
    nr_lines = 10,
    tests = (good_if_contains(''),),
    )

add(name="wireshark 2",
    required=["wireshark"],
    before = """Visualiser avec <tt>wireshark</tt> les �changes de
    requ�tes/r�ponses DNS correspondant � la
    <b>deuxi�me</b> r�solution du
    <b>m�me nom</b> de machine qu'� la question pr�c�dente.""",
    question = """Indiquez le nombre de requ�tes/r�ponses pour
    cette r�solution ainsi que les fanions de la r�ponse DNS.""",
    nr_lines = 10,
    tests = (good_if_contains(''),),
    )



add(name="nouvelle",
    required=["resolv"],
    before = """On suppose que les quatre services sont correctement
    configur�s et que vous �tes promus administrateur de l'ensemble du r�seau.
    Un nouvel utilisateur arrive dans l'organisation avec une machine neuve
    install�e sous Linux.""",
    question = """Citez pr�cis�ment les op�rations que vous devez effectuer
    afin d'int�grer compl�tement ce nouvel utilisateur et sa machine dans
    votre r�seau (vous donnerez un nom de machine et un nom de login � ce
    nouvel arrivant).
    <p>Cet utilisateur devra pouvoir s'authentifier sur n'importe quelle
    machine du r�seau et sa machine devra �tre accessible aux
    autres par son nom.""",
    default_answer = "Nom de machine : .......... Nom de login : ........\n",
    nr_lines = 10,
    tests = (good_if_contains(''),),
    )

add(name="totale",
    required=["nouvelle"],
    question = """Configurez une machine qui soit � la fois client NFS,
    client NIS, client LDAP et client DNS.
    <p>
    Changez l'ordre d'utilisation des services en
    configurant le fichier <tt>nsswitch.conf</tt>.
    <p>
    Comment testez-vous que tout fonctionne correctement&nbsp;?""",
    nr_lines = 10,
    tests = (good_if_contains(''),),
    )




















