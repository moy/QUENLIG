# -*- coding: latin-1 -*-
#    QUENLIG: Questionnaire en ligne (Online interactive tutorial)
#    Copyright (C) 2007 Thierry EXCOFFIER, Universite Claude Bernard
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
from .configuration_salles import *

add(name="intro",
    before="""Le but de ces 3 heures de TP est de&nbsp;:
    <ul>
    <li> Brancher physiquement un r�seau complexe.
    <li> Configurer les liaisons.
    <li> Mettre en place un routage dynamique.
    <li> Mettre en place un routage statique.
    <li> Effacer les configurations et ranger les cables.
    </ul>
    <p>
    Le plan du r�seau � monter est dans le menu de gauche&nbsp;:
    <em>Aide/Explications</em>
    <p>
    Faites en priorit� les questions en blanc sur noir et celles en caract�res <b>gras</b>.
 
    """,
    question="�tes-vous pr�t pour l'aventure&nbsp;?",
    tests = ( yes("R�pondez OUI s'il vous plait"), ),
    )

add(name="console",
    required=["intro"],
    before="""Dans l'ordre faire les actions suivantes&nbsp;:
    <ul>
    <li> Branchez le cable console entre votre PC et le routeur CISCO
    qui portent la m�me lettre sur le plan.
    <li> Lancez <tt>minicom</tt>
    <li> Configurez <tt>minicom</tt>
    <li> Allumez le routeur CISCO.
    <li> Attendez la fin du d�marrage.
    <b>N'entrez pas dans le dialogue de configuration initiale</b>.
    </ul>""",
    question="""S�lectionnez le cas dans lequel vous �tes&nbsp;:
    {{{!1}}} Le prompt <tt>Router&gt;</tt> appara�t.
    {{{!2}}} Un prompt contenant <tt>rommon</tt> appara�t.
    {{{!3}}} Si un autre prompt se terminant par <tt>&gt;</tt> appara�t.
       ou si on vous demande un mot de passe.
    {{{!4}}} Vous n'arrivez pas � r�initialiser le routeur.
    {{{!5}}} <tt>minicom</tt> ne se lance pas.
    <p>
    Si vous �tes dans un autre cas, appelez un enseignant.
    """,
    tests = (
    require_int(),
    good('1', "Parfait !"),
    bad('2',
        """Cela arrive parfois quand vous lancez <tt>minicom</tt>
        apr�s avoir allum� le routeur.
        Si c'est le cas, alors �teignez/allumez le routeur.
        <p>
        Sinon, votre routeur � un gros probl�me, il faut
        le r�installer (pr�venez un enseignant avant).
        Pour le r�installer, suivez la proc�dure d'installation
        de l'IOS dans la page d'aide du menu de gauche.
        """),
    bad('3',
        """Les �tudiants pr�c�dents n'ont pas fait le m�nage.
        R�initialisez le routeur en faisant la proc�dure
        d'effacement de configuration indiqu�e dans
        la page d'aide du menu de gauche.
        """),
    bad('4',
         """Vous n'arrivez pas � trouver le mot de passe indiqu�
         par les �tudiants pr�c�dent.
         Il faut effacer les mot de passes avec la proc�dure indiqu�e
         dans la page d'aide du menu de gauche.
         """
         ),
    bad('5',
        """Si c'est un probl�me de verrou, d�truisez-le,
        il est dans <tt>/var/lock/minicom</tt>."""),
    ),
    )

    
    

add(name="votre poste",
    required=['console'],
    before="""Vous devez avoir sous les yeux le plan du r�seau que
    vous allez tous configurer.""",
    question="Quel est le nom de votre ordinateur (pas routeur) sur le plan&nbsp;?",
    tests=(
    answer_length_is(2, "La r�ponse est UNE lettre majuscule + UN chiffre"),
    good("{name}", parse_strings=host),
    ),
    )




add(name="combien de r�seaux",
    required=["test branchement"],
    question="Combien de r�seaux IP sont sur le plan&nbsp;?",
    tests = ( require_int(),
              good("{network.nr_networks()}", parse_strings=host),
              ),
    bad_answer = """Remarques :
    <ul>
    <li> Ne comptez pas les liaisons consoles,
    <li> ne comptez pas en double,
    <li> comptez les r�seaux qui ne sont pas encore branch�.
    </ul>""",
    )

add(name="r�seaux directs",
    required=["test branchement"],
    question="""Lister les adresses des r�seaux directement connect�s
    � votre routeur sous la forme&nbsp;:
    <pre>
N.N.N.N/X
M.M.M.M/Y
...
</pre>""",
    nr_lines = 5,
    tests = (
    good("""{C0.remote_port.host.S0.network_plus_bits}
{C0.remote_port.host.S1.network_plus_bits}
{C0.remote_port.host.E0.network_plus_bits}""", parse_strings=host, sort_lines=True),
    number_of_is('/', 3, "Il y a 3 r�seaux."),
    ),
    )

ipbroadcast = reject_endswith(('0','2','4','6','8'),
                    """Vous avez rentr� une adresse de <em>broadcast</em>
                    dont le dernier bit est 0 (nombre pair).
                    Je vous conseille de s�rieusement relire votre cours
                    car ou vous ne savez pas compter en binaire ou
                    vous ne savez pas ce qu'est une adresse
                    de <em>broadcast</em>""")

add(name="broadcast eth0",
    required=["test branchement"],
    question="""Quelle est l'adresse de <em>broadcast</em> du r�seau
    sur lequel votre ordinateur est branch� avec l'interface E0&nbsp;?""",
    tests = (
    require_ip(),
    good("{E0.broadcast}", parse_strings=host),
    ipbroadcast,
    ),
    )

add(name="broadcast eth1",
    required=["test branchement"],
    question="""Quelle est l'adresse de <em>broadcast</em> du r�seau
    sur lequel votre ordinateur est branch� avec l'interface E1&nbsp;?""",
    tests = ( require_ip(),
              good("{E1.broadcast}", parse_strings=host),
              ipbroadcast,             
              ),
    )


    

add(name="test branchement",
    required=["hard:tout brancher"],
    question="""Quelle commande tapez-vous pour voir l'�tat
    de tous les interfaces du routeur&nbsp;?""",
    tests = (
    good("show interfaces"),
    bad("show interface",
        "Aucune abbr�viation ne sera tol�r�, il manque un 's'"),
    expect('show'),
    expect('interfaces'),
    ),
    )


for i in (0,1):
    add(name="Et Hop s%d" % i,
        required=["lien:remote s%d OK" % i],
        question="""Quelle commande tapez-vous sur votre routeur
        pour pinguer le port ethernet
        du routeur qui est connect� au votre via votre port s�rie %d&nbsp;?
        <p>
        Donnez votre r�ponse m�me si le ping �choue.
        """ % i,
        tests = (
        good("ping {C0.remote_port.host.S%d.remote_port.host.E0.port.ip}" % i,
             parse_strings=host),
        expect('ping'),
        ),
        )
    add(name="Et Hop s%d ?" % i,
        required=["Et Hop s%d" % i],
        question="""Le ping du port ethernet du routeur distant (via s%d)
        a-t-il fonctionn�&nbsp;?""" % i,
        tests = (
        no("""C'est impossible. Votre routeur ne sait pas � qui envoyer
        les donn�es car il n'y a pas de table de routage"""),        
        ),
        highlight = True,
        )

add(name="d�montage",
    required=["pc:vitesse", "rip:table de routage"],
    before="""Attendez que les autres personnes aient termin�es leur test de vitesse""",
    question="""
    Affichez r�guli�rement la table de routage toute les secondes.
    <p>
    Ne vous arr�tez pas de le faire tout en d�branchant
    le cable s�rie partant de votre routeur
    et qui est le plus long sur le plan du r�seau.
    <p>
    Au bout d'une minute,
    r�pondez par un chiffre pour indiquer ce qu'il se
    passe avec la table de routage&nbsp;:
    <ol>
    <li> Elle ne change pas.
    <li> Elle prend imm�diatement la bonne valeur.
    <li> Elle se met � jour en plusieurs it�rations.
    </ol>""",
    tests = (
    require_int(),
    good("3"),
    good("2", """C'est un r�sultat tr�s tr�s improbable,
    vous avez du attendre tr�s longtemps pour regarder la table de routage
    apr�s avoir d�branch� le cable."""),
    bad("1", "Impossible, certaines des routes doivent avoir disparu"),
    ),
    )

# add(name="cracker",
#     required=["pc:r�par� ?"],
#     before="""Si votre voisin est aussi en train de r�pondre
#     � cette question,
#     alors allez sur sa machine ou son routeur en utilisant
#     <tt>telnet</tt> et d�configurez quelque chose pour que
#     le r�seau ne fonctionne plus.""",
#     question="""Avez-vous trouv� ce que votre voisin a d�configur�
#     sur votre machine&nbsp;?
#     Si <em>oui</em> alors r�parez et indiquez comme r�ponse
#     ce qu'il � fait.""",
#     tests = (
#     bad(""),
#     good_if_contains(""),
#     ),
#     )
# 
class HalfNode(HostTest):
    def test_host(self, student_answer, string, state, host):
        ciscos = [h for h in host.network.hosts.values() if isinstance(h, Cisco)]
        if int(student_answer) == len(ciscos)/2 - 1:
            return True
        return False, ""

add(name="encore plus loin",
    required=["d�montage"],
    question="""Quelle est la plus longue route pour aller d'un routeur
    � un autre en nombre de routeurs travers�s
    si tout le monde a enlev� les cables qui traversent le cercle central&nbsp;?""",
    tests = (
    require_int(),
    HalfNode(),
    ),
    )




add(name="remontage",
    required=["encore plus loin"],
    before = """Faites ce qui suit :
    <ul>
    <li> Rebranchez le cable que vous avez d�branch� pr�c�demment.
    <li> Branchez TOUS les cables indiqu�s sur le plan
    y compris ceux que vous n'aviez pas branch� la premi�re fois.
    Ceux qui connectent les PC entre eux.
    </ul>
    """,
    question = """Donnez la ligne de commande permettant de configurer
    la nouvelle interface (<tt>eth1</tt>) que vous utilisez.""",
    tests = (
    Good(HostReplace(Equal(
        "ip a add {E1.port.ip}/{E1.nr_bits_netmask} dev {E1.port.name}"))),
    Good(HostReplace(Equal(
        "ip addr add {E1.port.ip}/{E1.nr_bits_netmask} dev {E1.port.name}"))),
    good("ifconfig {E1.port.name} {E1.port.ip} netmask {E1.mask}",
         parse_strings=host),
    good("ifconfig {E1.port.name} {E1.port.ip}/{E1.nr_bits_netmask}",
         parse_strings=host),
    require('{E1.port.name}', "Je ne vois pas le nom du port �thernet",
             parse_strings=host),
    require('{E1.port.ip}', "Je ne vois pas l'adresse IP du port �thernet",
             parse_strings=host),
    ),
    )

refus = """

La commande est refus�e lorsque vous la tapez
car les passerelles sont <b>obligatoirement</b> des routeurs
qui sont acccessibles sur le r�seau local.
Hors, l'adresse que vous donnez n'est pas sur le r�seau local.
<p>
On pourrait utiliser un tunnel mais ce n'est pas le sujet du TP.
<p>
Il faut donc que le coeur du r�seau sache router
ces nouvelles adresses.
"""

d = "C0.remote_port.host.S0.remote_port.host.S1.remote_port.host.C0.remote_port.host"

# add(name="route impossible",
#     required=["remontage"],
#     before = """ATTENTION, la r�ponse � cette question est une
#     commande qui NE FONCTIONNE PAS.
#     N�anmoins, il est important que vous compreniez pourquoi
#     cela ne marche pas.""",
#     question=replace_host("""Quelle commande taperiez-vous sur votre PC pour
#     que le ping vers l'adresse {%s.E1.port.ip} fonctionne&nbsp;?
#     """ % d),
#     tests = (
#     reject('ping', """Le ping ne fonctionne pas, on vous demande
#     ce qu'il faut faire sur le PC pour qu'il puisse fonctionner."""),
#     require('route', """Le ping ne fonctionne pas car une fois
#     parti vers la route par d�faut (routeur CISCO) les routeurs
#     ne savent pas quoi en faire car ils ne connaissent pas cette destination.
#     <p>
#     Vous devez donc ajouter une nouvelle route dans le PC en lui indiquant
#     � quelle passerelle envoyer le paquet."""),
#     reject('192.168.128', """Si vous utilisez un routeur CISCO comme passerelle
#     il ne sera pas quoi faire du paquet car il ne connait pas
#     la destination"""),
#     require('{%s.E0.port.ip}' % d,
#             """Vous devriez envoyer le paquet au PC qui connait
#             l'adresse en question. Donc sur son autre interface
#             car elle est connue des routeurs.""",
#             parse_strings=host),
#     require('{%s.E1.network}' % d,
#             """Je ne vois pas (ou elle est fausse) l'adresse du r�seau
#             destination.""",
#             parse_strings=host),
#     require('route add -net',
#             """Pour ajouter une route vers un r�seau,
#             la syntaxe est <tt>route add -net ...</tt>"""),
#     require('gw', "Je ne vois pas le param�tre <tt>gw</tt>"),
#     good('route add -net {%s.E1.network_plus_bits} gw {%s.E0.port.ip}' % (d,d),
#          refus, parse_strings=host),
#     good('route add -net {%s.E1.network} netmask {%s.E1.mask} gw {%s.E0.port.ip}' % (d,d,d),
#          refus, parse_strings=host),
#     ),
# )
 
# May be 2 gateways because destination network contains 2 hosts
def find_gateway(host, destination_network):
    n = host.inflate_max()
    gateways = []
    for h in n:
        for i in h.interfaces.values():
            if i.mask and str(i.network) == destination_network:
                gateways.append( (h.distance, h.min_path) )
    gateways.sort()
    return gateways

def path_table(p):
    path = "<table><tr><th>Host D�part</th><th>IP local</th><th>IP Destination</th><th>Host Destination</th></tr>"
    for link in p:
        path += "<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>" % (
            link.port.host.name,
            link.port.ip.ip,
            link.remote_port.ip.ip,
            link.remote_port.host.name,
            )
    path += "</table>"
    return path

def path_ip(path):
    for link in path:
        if link.remote_port.ip:
            return str(link.remote_port.ip)

def test_gateway(student_answer, string, g):
    if student_answer.startswith("ip route %s %s" % (
        string,
        path_ip(g[0][1]))):
        if student_answer != "ip route %s %s %d" % (
            string,
            path_ip(g[0][1]),
            g[0][0]
            ):
            return False, """La route est bonne, mais il manque
            la distance ou bien elle est fausse"""
        if g[0][0] == g[1][0]:            
            return True, """Une autre route �tait possible
            avec la m�me distance, elle passait par : %s"""%path_table(g[1][1])
        if g[1][1][0] != g[0][1][0]:
            return True, """Une autre route plus longue existait.
            On pouvait l'indiquer pour augmenter la fiabilit�.
            """+path_table(g[1][1])
        return True
    return None
        
class RouteTest(HostTest):
    def test_host(self, student_answer, string, state, host):
        g = find_gateway(host.C0.remote_port.host, string.split(' ')[0])
        answer = test_gateway(student_answer, string, g)
        if answer != None:
            return answer
        if g[0][0] == g[1][0]:
            answer = test_gateway(student_answer, string, (g[1], g[0]))
            
        if answer == None:
            return False, """Je ne vois pas l'adresse de la passerelle
            ou elle est fausse""" # + path_table(g[0][1])
        return answer
        




for h in network.hosts.values():
    if not isinstance(h, Host):
        continue
    if str(h.E1.port.ip) < str(h.E1.remote_port.ip):
        continue
    s = str(h.E1.network)
    ss = str(h.E1.network_plus_bits)

    add(name="vers %s" % s,
        required=["remontage"],
        before = """Vous indiquerez la distance en nombre de composants
        actifs travers�s (routeur, switchs et <b>PC</b>).
        On ne compte pas la machine de d�part mais on compte la passerelle
        finale (cela revient � compter le nombre de liens).
        <p>
        Vous indiquerez la route la plus courte
        <p>
        La passerelle peut aussi bien �tre un routeur CISCO qu'un PC.
        En effet le PC peut router sur les r�seaux sur lesquels
        il est directement connect�.
        <p>
        Vous avez tout int�r�t � d�rouler l'algorithme de calcul
        de distance sur le plan pour �valuer la longueur de toutes
        les routes.
        """,
        question = """
        Quelle ligne de commande tapez-vous sur votre routeur pour indiquer
        une route statique la plus courte
        qui permettrait d'atteindre le <b>r�seau</b> %s&nbsp;?
        """ % ss,
        tests = (
        require("ip route", "La commande est <tt>ip route</tt>"),
        require(str(h.E1.network),
                """Je ne vois pas l'adresse du r�seau destination
                ou bien elle est fausse"""),
        require(str(h.E1.mask),
                """Je ne vois pas le netmask du r�seau destination
                ou bien il est faux"""),
        RouteTest("%s %s" % (str(h.E1.network), str(h.E1.mask))),
        ),
        )
        
