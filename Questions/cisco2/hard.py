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

add(name="mod�le cisco",
    required=["admin:administrateur"],
    question="Quel est le mod�le du routeur CISCO que vous allez utiliser&nbsp;? C'est �crit sur la fa�ade avant...",
    tests=(
    HostCiscoModele(),
    ),
    )

add(name="combien d'interfaces",
    required=["admin:administrateur"],
    question="""Combien d'interfaces <b>r�seau</b> physique allez-vous utiliser
    sur votre routeur&nbsp;?
    <p>
    Regardez sur le plan.""",
    tests = ( require_int(), NrInterfacesUsed() ),
    )

add(name="connecteur ethernet",
    required=["admin:administrateur"],
    question="Quel est le type des connecteurs �thernet sur le routeur et sur le PC&nbsp;?",
    tests = ( good("RJ45", uppercase=True, replace=((' ',''),('-',''))),
              ),
    indices = ("""C'est le m�me connecteur que sur les prises murales""",
               ),
    )

add(name="cable ethernet",
    required=["connecteur ethernet"],
    question="""Quel est le type du cable �thernet � brancher&nbsp;?
    <ul>
    <li> on ne vous demande pas s'il est crois� ou non.
    <li> on veut l'acronyme.
    </ul>""",
    tests = (
    bad('RJ45', "C'est le nom du connecteur, pas du cable", uppercase=True),
    bad(('DCE','DTE'),
        "La notion de DTE/DCE n'existe pas avec ethernet", uppercase=True),
    answer_length_is(3, "La r�ponse est en 3 lettres"),
    good('UTP', uppercase=True),
    good('FTP', uppercase=True),
    ),
    indices = ("<tt>Unshielded Twisted...</tt> ou bien <tt>Foiled Twisted...</tt>", ),
    )

add(name="cable crois�",
    required=["cable ethernet"],
    question="""Le cable �thernet entre le routeur et le
    commutateur (<em>switch</em>) doit-il �tre crois�&nbsp; <tt>oui</tt> ou <tt>non</tt>?""",
    tests = ( no("Il est crois� en interne dans le commutateur"), ),
    )
    


add(name="M | F",
    required=["admin:administrateur"],
    question="""Quel est le genre (M ou F) du c�ble que vous allez connecter
    sur le port s�rie 0 de votre routeur&nbsp;?""",
    tests = (
    answer_length_is(1, "Vous devez r�pondre avec M ou F"),
    good("{C0.remote_port.host.S0.port.type}", uppercase=True,
         replace=(('F','DCE'), ('M', 'DTE')), parse_strings=host),
    ),
    )

add(name="tout brancher",
    required=["admin:nom routeur", "combien d'interfaces",
              "M | F", "cable crois�"],
    question="""R�pondez oui quand vous aurez branch� tous les cables.
    <b>SAUF les cables reliant directement 2 PC
    sans passer par un <em>switch</em></b>,
    ils seront branch�s plus tard.""",
    tests = ( yes("On vous a dit de r�pondre OUI."), ),
    )
