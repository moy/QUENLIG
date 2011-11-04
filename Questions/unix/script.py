# -*- coding: latin-1 -*-
#    QUENLIG: Questionnaire en ligne (Online interactive tutorial)
#    Copyright (C) 2011 Thierry EXCOFFIER, Universite Claude Bernard
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

add(name="param�tre",
    required=["variable:intro"],
    before = """G�n�ralement, la premi�re ligne d'un script shell indique
    le nom du programme qui interpr�te les scripts shell,
    c'est g�n�ralement&nbsp:
    <pre>#!/bin/sh</pre>
    Dans toutes les questions concernant les scripts,
    n'�crivez pas cette premi�re ligne""",
    question="""Quel est le script minimal qui affiche
    son premier param�tre&nbsp;?""",
    tests = (
        Expect('echo'),
        Expect('1', """Le premier param�tre du script est dans une variable
        sp�ciale dont le nom est '1' (le chiffre 1)"""),
        Expect('$', """Pour acc�der au contenu d'une variable, on place
        un <tt>$</tt> devant le nom de la variable."""),
        
        Good(Shell(Equal('echo "$1"'))),
        Bad(Comment(Shell(Equal("echo '$1'")),
                    "Vous n'avez pas essay� votre script avant de r�pondre.")),
        Bad(Comment(Shell(Equal('echo $1')),
                          """Essayez votre script avec :
                          <pre>'a     b'</pre>
                          comme premier param�tre..."""
                          )),
        shell_display,
        ),
    )

add(name="tous",
    required=["param�tre"],
    question="""Quel est le script minimal qui affiche
    tous ses param�tres&nbsp;?""",
    tests = (
        Expect('"', "Il ne manquerait pas des guillemets ?"),
        Good(Shell(Equal('echo "$@"'))),
        Bad(Comment(Shell(Equal('echo "$*"')),
                    """La variable <tt>*</tt> est obsolette, il est
                    recommand� d'utiliser la variable <tt>@</tt> qui
                    permet de traiter le cas des param�tres contenant
                    des espaces.""")),
        ),
    )

add(name="shift",
    required=["tous", "sh:ex�cution s�quencielle"],
    before = """La commande <em>builtin</em> <tt>shift</tt> du shell
    d�truit le premier param�tre du script shell.
    Le nouveau premier param�tre est l'ancien deuxi�me,
    tout est donc d�cal� (<em>shifted</em>) vers la gauche.""",
    question = """Quel est le script d'une seule ligne qui affiche
    tous ses param�tres SAUF LE PREMIER&nbsp;?""",
    tests = (
        Expect('shift'),
        Expect(';', """Votre script (d'une seule ligne) comporte 2 commandes,
        vous devez les s�parer avec un..."""),
        Expect('echo'),
        Expect('$@'),
        Expect('"'),
        Good(Shell(Equal('shift ; echo "$@"'))),
        shell_display,
        )
    )

add(name="ifrm",
    required=["param�tre", "test:intro", "sh:si", "detruire:simple"],
    question = """Quel est le script d'une seule ligne qui d�truit
    le fichier dont le nom est pass� en deuxi�me param�tre
    seulement si le fichier dont le nom qui est pass� en premier
    param�tre existe.
    <pre>ifrm dessin.svg dessin.pdf</pre>
    Le fichier <tt>dessin.pdf</tt> est d�truit seulement si
    le fichier <tt>dessin.svg</tt> existe.""",
    tests = (
        Good(Shell(Equal('test -f "$1"  &&  rm "$2"'))),
        Good(Shell(Equal('[ -f "$1" ]  &&  rm "$2"'))),
        Expect('if'),
        Expect('then'),
        Expect('fi'),
        Expect('rm'),
        Expect('$1', "Je ne vois pas la r�f�rence au nom du premier fichier"),
        Expect('$2', "Je ne vois pas la r�f�rence au nom du deuxi�me fichier"),
        Expect('-f', """Je ne vois l'option de <tt>test</tt>
        indiquant que vous testez l'existence d'un fichier."""),
        Bad(Comment(~NumberOfIs('"', 4),
                    """Si vous voulez que votre script fonctionne m�me si
                    les noms des fichiers contiennent des espaces,
                    alors il faut utiliser les guillemets."""
                    )),
        Bad(Comment(~NumberOfIs(';', 2),
                    """Vous avez besoin d'un point-virgule avant le
                    <tt>then</tt> et avant le <tt>fi</tt>.
                    Vous devriez donc avoir 2 points-virgules dans
                    votre r�ponse."""
                    )),
        Good(Shell(Equal('if [ -f "$1" ] ; then rm "$2" ; fi'))),
        Good(Shell(Equal('if test -f "$1" ; then rm "$2" ; fi'))),
        shell_display,
        ),
    )


add(name="for tous",
    required=["tous", "sh:boucle"],
    question="""Quel est le script d'une seule ligne qui affiche
    ses arguments en en mettant UN par ligne.
    Si votre script est appel� avec comme arguments&nbsp;:<br>
    <tt>un deux "3&nbsp;&nbsp;&nbsp;&nbsp;4"</tt>
     <br>il affichera&nbsp;:
    <pre>un
deux
3    4</pre>
    La variable de boucle s'appelera <tt>I</tt>
    """,
    tests = (
        Reject('$*', """Avec <tt>$*</tt> cela ne fonctionnera pas si les
        arguments contiennent des espaces"""),
        Expect('$@'),
        Expect('for'),
        Expect('do'),
        Expect('done'),
        Expect('I', "Vous devez utiliser <tt>I</tt> comme indice de boucle"),
        Expect('$I',
               "Vous n'utilisez pas le contenu de la variable <tt>I</tt> !"),
        Bad(Comment(NumberOfIs(';', 3),
                    """Auriez-vous mis un <tt>;</tt> apr�s le <tt>do</tt>
                    ou en fin de ligne ?""")),
        Bad(Comment(~ NumberOfIs(';', 2),
                    """N'oubliez pas les <tt>;</tt> quand vous �crivez
                    sur une seule ligne.
                    """)),
        Bad(Comment(~ NumberOfIs('"', 4),
                    """Cela ne fonctionnera pas dans tous les cas, s'il manque
                    les guillemets autour des deux variables utilis�es.""")),
        Good(Shell(Equal('for I in "$@";do echo "$I" ; done'))),
        shell_display,
        ),
    )
    


add(name="ifrm2",
    required=["sh:si", "shift", "detruire:simple", "tous", "ifrm"],
    question="""Quel est le script d'une seule ligne qui d�truit
    les fichiers dont les noms sont indiqu�s dans les param�tres 2, 3...
    seulement si le fichier dont le nom qui est pass� en premier
    param�tre existe.
    <pre>ifrm2 dessin.svg dessin.pdf dessin.ps dessin.gif</pre>
    Les fichiers <tt>dessin.pdf</tt>, <tt>dessin.ps</tt>, <tt>dessin.png</tt>
    sont d�truits seulement si le fichier <tt>dessin.svg</tt> existe.
    <p>
    Vous n'avez pas besoin de modifier de variable pour faire ce script.
    L'algorithme est le suivant&nbsp;: si le premier param�tre est un
    fichier alors on le fait dispara�tre et on
    d�truit tous les fichiers pass�s en param�tre.
    """,
    tests = (
        Reject('$*', "<tt>$*</tt> est obsolette, ne l'utilisez pas."),
        Reject("for", """Les meilleurs programmes sont les plus courts,
        vous n'avez pas besoin de faire de boucle"""),
        Expect('$1', "Vous ne testez pas le premier param�tre ?"),
        Expect('$@', """Vous ne d�truisez pas tous les fichiers dont
        les noms sont pass�s en param�tre ?"""),
        Bad(Comment(~ NumberOfIs('"', 4),
                    """Cela ne fonctionnera pas dans tous les cas, s'il manque
                    les guillemets autour des deux variables utilis�es.""")),
        Expect('shift'),
        Expect('-f'),
        
        Good(Shell(Equal('if test -f "$1" ;then shift;rm "$@";fi'))),
        Good(Shell(Equal('test -f "$1" && shift && rm "$@"'))),
        Good(Shell(Equal('if [ -f "$1" ];then shift;rm "$@";fi'))),
        Good(Shell(Equal('[ -f "$1" ] && shift && rm "$@"'))),
        shell_display,
        ),
    )
    
# find -name '*.pdf' -exec ifrm {}
# d�truire tous les PDF avec un SVG correspondant : n�cessite basename



        
        
    
