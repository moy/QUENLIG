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

add(name="administrateur",
    required=["tp2:votre poste"],
    question="""Passez en mode administrateur du routeur CISCO.
    Et r�pondez � cette question par le chiffre indiqu� dans
    l'�num�ration suivante&nbsp:
    <ol>
    <li> J'ai r�ussi.
    <li> Il y a un mot de passe (autre que %s).
    <li> Je ne me souviens pas comment l'on fait (mauvais point).
    </ol>""" % mots_de_passe,
    tests = (
    require_int(),
    good("1"),
    bad("2",
        """Suivez la <a href="cisco_efface_passwd.html">
        proc�dure d'effacement de mot de passes</a>."""),
    bad("3", "Il faut taper <tt>enable</tt>."),
    ),
    )

add(name="nom routeur",
    required=['administrateur'],
    before = "Attention la casse compte.",
    question="""Quelle ligne de commande tapez-vous pour donner
    son nom � votre routeur&nbsp;?""",
    tests = (
    good("hostname {C0.remote_port.host.name}",
         "N'oubliez pas d'ex�cuter la commande", parse_strings=host),
    expect('hostname'),
    require('{C0.remote_port.host.name}',
            "Je ne vois pas le nom de votre routeur",
            parse_strings=host),
    ),
    )

add(name="sauve configuration",
    required=["rip:RIP"],
    before="""Si jamais il y a un probl�me vous pouvez perdre toute
    la configuration de votre routeur.""",
    question="Quelle commande tapez-vous pour sauver la configuration&nbsp;?",
    tests = (
    good("copy running-config startup-config"),
    expect('copy'),
    expect('running-config'),
    expect('startup-config'),
    ),
    good_answer = "VOUS DEVEZ LE FAIRE",
    )

add(name="relance routeur",
    required=["sauve configuration"],
    question="Quelle commande tapez-vous pour relancer le routeur&nbsp;? (Ne la lancez pas)",
    tests = (
        good("reload"),
        bad('restart', """Cela r�initialise certaines chose mais cela ne
        red�marre pas le routeur"""),
        bad('reboot',
            """Montrez � l'enseignant l'endroit
            o� vous avez trouv� cette commande"""),
        ),
    )

add(name="AVANT DE PARTIR",
    required=["sauve configuration"],
    question=avant_de_partir,
    )



add(name="nommer votre pc",
    required=["tp2:votre poste", "pc:eth0", "rip:RIP"],
    before = "N'oubliez pas de respecter la casse (majuscule/minuscule)",
    question="""Quelle commande tapez-vous sur le routeur pour nommer
    votre PC&nbsp;?""",
    tests = (
    good("ip host {name} {E0.port.ip}", parse_strings=host),
    reject('hostname', "C'est pour se donner un nom � soit-m�me"),
    expect('ip host'),
    require('{name}', "Je ne vois pas le nom de votre machine",
            parse_strings=host),
    require('{E0.port.ip}', "Je ne vois pas l'adresse IP de la machine",
            parse_strings=host),
    ),
    )

add(name="telnet",
    required=["pc:eth0", "rip:Et Hop s0 OK", "rip:Et Hop s1 OK"],
    before="""On peut administrer le routeur avec sa liaison s�rie,
    mais aussi via le r�seau en utilisant <tt>telnet</tt>.
    <p>
    Il suffit de faire <tt>telnet une_ip_du_routeur</tt> � partir
    de votre ordinateur.""",
    question="""Pouvez-vous faire un <tt>telnet</tt> sur votre routeur
    et travailler dessus&nbsp;?""",
    tests = (
    no("Montrez cela � l'enseignant, c'est impossible."),
    ),
    good_answer = """Pour pouvoir utiliser <tt>telnet</tt>
    il faut avoir configur� les mots de passe.""",
    )


add(name="config telnet",
    required=["telnet"],
    question="""Quelle commande tapez-vous dans l'IOS
    pour passer en mode configuration
    de la console d'administration � distance num�ro 0 (z�ro)&nbsp;?""",
    tests = (
    good('line vty 0'),
    good('line VTY 0'),
    require_startswith("line",
                       "Il faut utiliser la commande <tt>line</tt>"),
    require('vty', """La console d'administration � distance utilise
    un <em><b>V</b>irtual <b>T</b>elet<b>Y</b>pe</em> (TTY virtuel)"""),
    Bad(Comment(UpperCase(Equal('line vty 0 4')),
                "Vous �tes en train de configurer les ligne VTY de 0 � 4.")),
    ),
    )

add(name="password telnet",
    required=["config telnet"],
    before="""La connexion avec <tt>telnet</tt> ne sera possible
    que quand vous aurez mis un mot de passe.""",
    question="""Une fois en mode configuration du VTY,
    quelle commande tapez-vous pour mettre
    le mot de passe <tt>cisco</tt>&nbsp;?""",
    tests = (
        good('password cisco'),
        good('password 0 cisco'),
        good('password 7 cisco'),
        Expect('cisco', "Je ne vois pas le mot de passe..."),
        ),
    good_answer="""On ne peut pas se connecter simultan�ment avec le m�me
    mot de passe.<p>
    On ne peut pas se connecter s'il n'y a pas de mot de passe.""",
    )

add(name="config console",
    required=["config telnet", "password telnet"],
    question="""Quelle commande tapez-vous pour passer en mode configuration
    de la <b>console</b> de contr�le du routeur&nbsp;?
    <p>
    C'est celle sur laquelle vous �tes en train de taper les commandes.
    """,
    tests = (
        require_startswith("line",
                           "Il faut utiliser la commande <tt>line</tt>"),
        Expect('console'),
        bad('line console',
            """Il peut y avoir plusieurs consoles branch�e sur le m�me
            routeur. Vous devez indiquer laquelle configurer"""),
        good('line console 0'),
        ),
    )

add(name="password console",
    required=["config console"],
    question="""Une fois en mode configuration de la console,
    quelles commandes tapez-vous pour verrouiller l'acc�s � la console
    par le mot de passe 'cisco' qui sera demand� � chaque connexion
    sur la console de contr�le du routeur&nbsp;?
    <ul>
    <li> Un premi�re commande indique que l'on veut un acc�s
    avec authentification pour la connexion.
    <li> La deuxi�me commande sp�cifie que le mot de passe.
    </ul>
    """,
    nr_lines = 2,
    tests = (
    require('cisco', "Je ne vois pas le mot de passe"),
    require('login', "La premi�re commande indique que l'on veut un 'login'"),
    require('password',
            "La deuxi�me commande indique le mot de passe (pa...)"),
    good('login\npassword cisco'),
    good('login\npassword 0 cisco'),
    good('login\npassword 7 cisco'),
    good('password cisco\nlogin'),
    good('password 0 cisco\nlogin'),
    good('password 7 cisco\nlogin'),
    ),
    )

add(name="password enable",
    required=["password telnet"],
    question="""Quelle commande tapez-vous pour assigner le mot de passe
    (stock� chiffr�) <tt>cisco</tt> au passage en mode privil�gi�
    avec <tt>enable</tt>&nbsp;?""",
    tests = (
    require_startswith("enable",
                       "Il faut utiliser la commande <tt>enable</tt>"),
    require('cisco', "Je ne vois pas le mot de passe"),
    reject('enable password', "Command obsol�te car ins�cure"),
    good('enable secret cisco'),
    ),
    )
