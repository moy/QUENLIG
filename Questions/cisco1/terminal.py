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

from questions import *
from check import *
from configuration_salles import *

add(name="intro",
    required=['root:sortir'],
    question = """Quand vous �tes en mode privil�gi�.
    Quelle commande permet de passer en mode de configuration
    du routeur&nbsp;?""",
    tests = (
    require('configure', "La commande est <tt>configure</tt> + un param�tre"),
    bad("configure", """Vous pouvez en effet taper <tt>configure</tt>
    puis <tt>Return</tt> pour valider le choix <tt>terminal</tt>.
    Mais on vous demande la r�ponse en une ligne"""),
    good("configure terminal"),
    ),
    indices = (
    """La r�ponse est dans le module 2 de la documentation CISCO.""",
    ),
    good_answer = """Une fois cette commande tap�e,
    vous pouvez modifier la configuration du routeur.""",
    )

add(name="prompt",
    required=['intro'],
    question = """Passez en mode configuration du routeur.
    Quelle est l'invite de commande&nbsp;?""",
    tests = (
    good("Router(config)#"),
    expect('#'),
    expect('Router'),
    expect('(config)'),
    ),
    highlight = True,
    )

add(name="pas de traduction",
    required=['prompt', 'cli:mauvaise commande',
              "tp1_serie:routeur>local s0 OK"],
    before = """En mode configuration du routeur,
    ex�cutez la commande <tt>no ip domain lookup</tt>""",
    question = "Retapez la commande 'coucou'. �tes-vous bloqu�&nbsp;?",
    tests = ( no("Vous avez du mal taper la commande."), ),
    good_answer = """
    <b>
    TOUTE LIGNE DE COMMANDE COMMEN�ANT PAR 'NO' ANNULE
    LA COMMANDE QUI SUIT.
    Ceci est vrai pour toutes les commandes, ne l'oubliez pas.</b>
    <p>
    N'oubliez pas la commande <tt>no ip domain lookup</tt> elle vous
    fera gagner du temps dans les TP.
    """,
    )

add(name="show",
    required=['prompt'], # Au lieu de "pas de traduction"
    before=en_mode_config,
    question = "La commande <tt>show interfaces</tt> fonctionne-t-elle&nbsp;?",
    tests = ( no("Impossible, vous n'�tes pas en mode configuration terminal"), ),
    good_answer = """Malheureusement non.
    <p>
    Cela a certainement �t� d�cid� afin que les administrateurs
    passent le moins de temps possible en mode configuration.
    """,
    )

add(name="quitter",
    required=['prompt', 'cli:? seul'],
    question="""Que tapez-vous pour quitter le mode configuration
    routeur&nbsp;?""",
    tests = (
    good('exit'),
    good('end', 'La commande recommand�e est <tt>exit</tt>'),
    good_if_contains(('z','Z'), """Contr�le-Z n'est pas une commande,
    La commande recommand�e est <tt>exit</tt>"""),
    ),
    )

add(name="password enable",
    required=["intro", "doc:intro"],
    before = """La documentation concernant les mots de passe
    est dans le 'module 2'.
    Une fois dans le module 2, allez dans le menu d�roulant
    et prenez le troisi�me choix.
    <p>""" + en_mode_config,
    question="""Quelle commande tapez-vous pour assigner le mot de passe
    <tt>cisco</tt> au passage en mode privil�gi�
    avec <tt>enable</tt>&nbsp;?""",
    tests = (
    require_startswith("enable",
                       "Il faut utiliser la commande <tt>enable</tt>"),
    require('cisco', "Je ne vois pas le mot de passe"),
    reject('password',
        "Command obsol�te car ins�cure, utilisez <tt>enable secret</tt>"),
    good('enable secret cisco'),
    good('enable secret 0 cisco'),
    good('enable secret 5 cisco'),
    good('enable secret 7 cisco'),
    ),
    )

add(name="config console",
    required=["password enable", "doc:intro"],
    before=en_mode_config,
    question="""Quelle commande tapez-vous pour passer en mode configuration
    de la console de contr�le du routeur&nbsp;?
    <p>
    C'est celle sur laquelle vous �tes en train de taper les commandes.
    """,
    tests = (
    require_startswith("line",
                       "Il faut utiliser la commande <tt>line</tt>"),
    good('line console 0'),
    bad('line console',
        "Le routeur a du vous dire que la commande �tait incompl�te."),
    reject('tty', "C'est pas <tt>tty</tt>"),
    expect('console'),
    ),
    )

add(name="password console",
    required=["config console"],
    question="""Une fois en mode configuration de la console,
    quelles commandes tapez-vous pour verrouiller l'acc�s � la console
    par le mot de passe 'cisco' qui sera demand� � chaque connexion
    sur la console de contr�le du routeur&nbsp;?
    <ul>
    <li> Une commande qui indique le mot de passe.
    <li> Une commande indique que l'on veut un acc�s
    avec authentification pour la connexion.
    </ul>
    <p>Ne recopiez pas l'invite de commande&nbsp;!
    """,
    nr_lines = 2,
    tests = (
    require('cisco', "Je ne vois pas le mot de passe"),
    require('login', "La premi�re commande indique que l'on veut un <tt>login</tt>"),
    require('password',
            "La deuxi�me commande indique le mot de passe (c'est <tt>pa...</tt>)"),
    good('login\npassword cisco'),
    good('login\npassword 0 cisco'),
    good('login\npassword 7 cisco'),
    good('password cisco\nlogin'),
    good('password 0 cisco\nlogin'),
    good('password 7 cisco\nlogin'),
    ),
    highlight = True,
    )

add(name="config telnet",
    required=["doc:intro", "password enable", 
              "config console",
              "tp1_route:machine>routeur s1 OK",
              "tp1_route:machine>routeur s0 OK",
              ],
    before="""On peut administrer le routeur avec sa liaison s�rie,
    mais aussi via le r�seau en utilisant <tt>telnet</tt>.
    <p>
    Il suffit de faire <tt>telnet une_adresse_ip_du_routeur</tt> � partir
    de votre ordinateur.
    <p>
    Essayez, mais la connexion sera refus�e...
    Pour quelle soit accept�e, il faut faire cette question
    et la suivante afin de mettre un mot de passe pour
    la connexion <tt>telnet</tt> (elle utilise un VTY).
    """,
    question="""Quelle commande tapez-vous pour passer en mode configuration
    de la console d'administration � distance num�ro 0 (z�ro)&nbsp;?""",
    tests = (
    require_startswith("line",
                       "Il faut utiliser la commande <tt>line</tt>"),
    require('vty', """La console d'administration � distance utilise
    un <em><b>V</b>irtual <b>T</b>elet<b>Y</b>pe</em> (TTY virtuel)"""),
    good('line vty 0'),
    ),
    )

add(name="password telnet",
    required=["config telnet"],
    before="""La connexion avec <tt>telnet</tt> ne sera possible
    que quand vous aurez mis un mot de passe.""",
    question="""Une fois en mode configuration du VTY,
    quelle commande tapez-vous pour mettre le mot de passe <tt>cisco</tt>
    pour bloquer l'acc�s&nbsp;?""",
    tests = (
    good('password cisco'),
    good('password 0 cisco'),
    good('password 7 cisco'),
    expect('password'),
    expect('cisco'),
    ),
    good_answer="""On ne peut pas se connecter � plusieurs
    simultan�ment avec le m�me mot de passe.""",
    highlight = True,
    )

add(name="who",
    required=["password telnet"],
    before="""Faites les choses suivantes :
    <ul>
    <li> Configurer le mot de passe <tt>cisco2</tt> sur VTY 1
    <li> Connectez-vous sur votre routeur en utilisant
    le <tt>telnet</tt> � partir de votre ordinateur.<br>
    <b>Restez connect� pour les questions suivantes</b>.
    <li> Connectez-vous sur un autre routeur.
    </ul>""",
    question="""Quelle commande utilisez-vous pour afficher la liste
    des personnes connect�es sur le routeur&nbsp;?""",
    tests = ( good("who"),
              good("show users", "<tt>who</tt> est plis court"),
              ),
    indices = ("C'est comme sous unix", ),
    )

add(name="combien",
    required=["who"],
    before = """Tapez �entr�e� sur la console s�rie
    et la console <tt>telnet</tt> pour v�rifier que vous �tes bien connect�""",
    question="""Combien de personnes sont connect�es sur votre routeur
    en vous comptant vous m�me&nbsp;?""",
    tests = (
    require_int(),
    good(("2", "3", "4", "5")),
    bad("1", """Normalement vous �tes connect� sur l'interface s�rie
    et aussi avec <tt>telnet</tt> donc il y a un probl�me"""),
    ),
    highlight = True,
    )

    

    

