# -*- coding: latin-1 -*-
#    QUENLIG: Questionnaire en ligne (Online interactive tutorial)
#    Copyright (C) 2006 Thierry EXCOFFIER, Universite Claude Bernard
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

add(name="intro",
    required=["manuel:chercher"],
    question="""Quel est le nom de la commande permettant
    de se connecter � distance de mani�re s�curis�e sur une autre machine
    (<em>remote login</em>)&nbsp;?""",
    tests=(
    good("ssh"),
    bad('login', """Cette commande permet de faire appara�tre
    un login de la machine locale dans la fen�tre courante.
    Elle ne permet pas d'acc�der � une autre machine"""),
    bad("rlogin",
        """Cette commande est standard mais est de moins en moins
        utilis�e car elle n'est pas s�curis�e.
        """),
    bad("telnet",
        """Cette commande est standard mais elle est compl�tement
        obsol�te"""),
    bad("rsh", """Cette commande permet de lancer un commande � distance,
    elle n'est pas faites pour se connecter.
    De plus elle est obsol�te."""),
    bad('slogin',
        "Il est pr�f�rable d'indiquer <tt>ssh</tt> c'est plus court"),
    ),
    indices=(
    """Chercher dans les pages des manuels le mot-clefs 'login'""",
    """Abbr�viation de : <em>Secure SHell</em>""",
    ),
    good_answer="""Testez la connexion � distance&nbsp;:
    <ul>
    <li> V�rifier le nom de la machine avec la commande <tt>hostname</tt>
    <li> V�rifiez que vous arrivez bien � �diter un fichier avec
    <tt>vi</tt> ou <tt>xemacs</tt>
    </ul>""",
    )

dumb_replace = ( ('  ', ' '), ('; ',';'), (' ;', ';'))

add(name="liste processus",
    required=["intro", "processus:tous"],
    before="""La commande <tt>ssh</tt> vous connecte par d�faut avec
    le m�me <em>login</em> sur la machine distante
    que sur la machine locale""",
    question="""Donnez la commande permettant d'afficher sur votre
    �cran la liste de TOUS les processus qui sont sur la machine <tt>b201pc34</tt>.""",
    tests=(
    reject('@', """Vous n'avez pas besoin d'indiquer votre <em>login</em>
    il va reprendre le m�me"""),
    require(('ssh', 'ps'), "Vous devez utiliser <tt>ssh</tt> et <tt>ps</tt>"),
    require("-", "TOUS, il manque une option � <tt>ps</tt>"),
    require(("-e", "-A"), "L'option de <tt>ps</tt> est mauvaise. Regardez la liste des questions auxquelles vous avez d�j� r�pondu.",
            all_agree=True),
    require('b201pc34', "Et le nom de la machine distante, il est o�&nbsp;?"),
    reject((';','|'),
           "Il n'y a qu'une seule commande � lancer sur la machine locale."),
    reject_startswith('ps',
                      """La commande <tt>ssh</tt> prend comme argument
                      ce qu'il faut lancer � distance.
                      Dans votre ligne, la commande <tt>ps</tt>
                      est ex�cut�e localement"""),
    shell_good("ssh b201pc34 ps -e"),
    shell_good("ssh b201pc34 'ps -e'",dumb_replace=dumb_replace),
    shell_good("ssh b201pc34 ps -A"),
    shell_good("ssh b201pc34 'ps -A'",dumb_replace=dumb_replace),
    shell_display,
    ),
    indices=(
    """Apr�s le nom de la machine, on peut mettre une commande shell""",
    ),
    )


add(name="des commandes",
    required=["liste processus", "sh:s�quencielle",
              "sh:affiche param�tres sp�ciaux"],
    question="""Donnez la commande permettant d'afficher sur votre
    �cran le r�sultat de l'ex�cution des commandes <tt>ps</tt> et <tt>date</tt>
    sur la machine <tt>b201pc34</tt>""",
    tests=(
    reject('-e', 'La commande <tt>ps</tt>, pas la commande <tt>ps -e</tt>'),
    reject('-', "On a besoin d'aucune option"),
    reject(('(',')'), """Les parenth�ses vont �tre prises par le shell local
    et non le shell distant. Il va y avoir une erreur de syntaxe.
    De plus, elles ne sont pas utiles pour cet exercice."""),
    expect('b201pc34'),
    number_of_is('ssh', 1, "On ne lance la commande <tt>ssh</tt> qu'une fois"),
    shell_good("ssh b201pc34 'ps;date'", dumb_replace=dumb_replace),
    shell_good("ssh b201pc34 ps ';' date"),
    require(';', "On utilise le point virgule pour s�parer les commandes"),
    number_of_is(';',1, "Un seul point virgule suffit, il s�pare 2 commandes"),
    shell_reject('</pipeline><pipeline',
                 """Vous n'avez pas prot�g� le point virgule,
                 donc deux commandes s'ex�cutent sur votre machine.
                 Seulement <tt>ssh</tt> devrait s'ex�cuter"""),
    shell_display,
    require('JAMAISICI',
            "Auriez-vous invers� la commande <tt>ps</tt> et la command <tt>date</tt>&nbsp;?"),
    ),
    indices=("""Il faut que les deux commandes soient consid�r�es
	comme un param�tre unique de la commande <tt>ssh</tt>""",
	),
    )

