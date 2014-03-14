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

add(name="mod�le cisco",
    required=["tp1:intro"],
    question="""Quel est le mod�le du routeur CISCO
                que vous allez utiliser&nbsp;?
                La r�ponse est �crite sur la face avant.
             """,
    tests=(
    HostCiscoModele(),
    ),
    indices = ("C'est �crit sur la face avant du routeur.", ),
    )

add(name="nb s�rie",
    required=['mod�le cisco'],
    question="""Combien y-a-t-il de ports s�ries permettant de faire des
    liaisons r�seaux sur le routeur CISCO&nbsp;?""",
    tests=(
    require_int(),
    HostCiscoNrSerials(),
    ),
    bad_answer = """Ne comptez pas le port console, c'est une liaison
    s�rie, mais elle ne permet pas de faire du r�seau""",
    )

add(name="nb ethernet",
    required=['mod�le cisco'],
    question="Combien a-t-il de ports ethernet sur le routeur CISCO&nbsp;?",
    tests=(
    require_int(),
    HostCiscoNrEthernet(),
    ),
    indices = ("""Ou vous regardez sur la documentation, ou vous regardez
    derri�re le routeur.
    Attention, ce n'est pas la forme du connecteur qui vous dit si
    c'est ethernet ou non...""", ),
    )

add(name="on off",
    required=['mod�le cisco'],
    question="Le routeur CISCO a-t-il un interrupteur marche/arr�t&nbsp;?",
    tests=(
    HostCiscoOnOff(),
    ),
    )

add(name="console eth",
    required=['nb ethernet'],
    before = """On a besoin de d�trompeur quand les trous dans lesquels
    on met les connecteurs se ressemblent suffisamment (ou sont identiques)
    pour que l'on se trompe.
    Par exemple&nbsp;:
    <ul>
    <li> La forme interne des connecteurs USB emp�che de les brancher � l'envers.
    <li> La forme externe des RJ45, port s�rie (DB-9/DB-25)
    et des cartes m�moires emp�che de les brancher � l'envers.
    <li> Sur les connecteurs IDE/SATA et �lectrique que l'on branche
    � l'int�rieur des PC des trous manquants emp�chent de se tromper.
    <li> Il n'y a pas de d�trompeur sur les prises audio
    et d'alimentation �lectrique en courant continu,
    on peut donc se tromper :-(.
    </ul>""",
    question="""Sur le routeur CISCO,
    y-a-t-il un d�trompeur pour vous emp�cher de connecter
    un cable ethernet RJ45 sur le connecteur nomm� 'console'&nbsp;?""",
    tests=(
    no("Essayez de faire ce branchement pour v�rifier."),
    ),
    good_answer= "Faites attention � ne pas vous tromper dans la suite du TP.",
    )


add(name="show",
    required=['mod�le cisco', 'cli:show liste', 'cli:commande incompl�te'],
    question="""Quelle commande tapez-vous pour voir la configuration
    <b>mat�rielle</b> du routeur CISCO&nbsp;?
    <p>
    Attention, pour des raisons myst�rieuses il est possible
    que <tt>show ha?</tt> n'affiche pas la bonne r�ponse...
    """,
    tests=(
    expect('show'),
    good("show hardware"),
    good("show version",
        "Pas tr�s logique comme r�ponse, comment dit-on mat�riel en anglais?"),
    ),
    indices = ("""Le param�tre est la traduction de <em>mat�riel</em>
    en anglais""", ),
    )


add(name="ram",
    required=['show'],
    before="""RAM : Random Access Memory
    <p>
    <em>Attention, ce que l'on appelle RAM n'est ni la m�moire
    <b>flash</b> ni la m�moire non volatile</em>
    <p>
    Attention, le routeur CISCO n'affiche pas la quantit�
    de RAM totale mais la RAM libre et la RAM utilis�e.
    <p>
    <table>
    <tr><th></th><th>Anglais</th><th>Fran�ais</th></tr>
    <tr><td>Bool�en</td><td>bit</td><td>bit</td></tr>
    <tr><td>8 bits</td><td>byte</td><td>octet</td></tr>
    </table>
    """,
    question="""Combien de RAM (en kilo-octet)
    y-a-t-il dans le routeur CISCO&nbsp;?
    """,
    tests=(
    require_int(),
    HostCiscoRAM(),
    ),
    indices = (
    """Dans la ligne indiquant la quantit� de m�moire,
    le premier chiffre est la m�moire libre, et le deuxi�me
    la m�moire utilis�e par le syst�me.""",
    ),
    )
add(name="nvram",
    required=['ram'],
    before="""NVRAM : Non Volatile RAM.
    <p>
    Cette m�moire est utilis�e par le routeur pour sauvegarder
    sa configuration.
    Elle s'utilise comme de la m�moire normale bien que plus lente d'acc�s.
    """,
    question="""Combien de NVRAM (en kilo-octet)
    y-a-t-il dans le routeur CISCO&nbsp;?""",
    tests=(
    require_int(),
    HostCiscoNVRAM(),
    ),    
    )
add(name="flash",
    required=['nvram'],
    before="""<em>Flash</em> : C'est une sorte de NVRAM qui n'est pas cher mais
    qui lorsque que l'on �crit dedans n�cessite d'effacer et de r��crire
    un gros bloc de donn�e.
    <p>
    De plus les m�moires <em>flash</em> s'usent en quelque dizaines
    de milliers d'�critures.
    <p>
    De fait, dans les routeurs CISCO elles ne servent qu'�
    stocker l'image du syst�me d'exploitation.
    <p>
    <a href="http://en.wikipedia.org/wiki/Flash_memory">wikipedia:flash</a>.
    """,
    question="""Quelle quantit� de m�moire <em>flash</em> (en kilo-octet)
    y-a-t-il dans le routeur CISCO&nbsp;?""",
    tests=(
    require_int(),
    HostCiscoFlash(),
    ),    
    )


 



    



