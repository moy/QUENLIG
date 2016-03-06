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
    required=["archiver:cr�ation"],
    before="""La compression et la d�compression d'un fichier
    peut �tre faite avec diff�rents outils.
    <table>
    <tbody>
    <tr>
    <th>Extension</th><th>compresseur</th><th>d�compresseur</th><th>Commentaire</th>
    </tr>
    <tr>
    <td>.Z</td><td><tt>compress</tt></td><td><tt>uncompress</tt></td>
    <td>Outils standard unix maintenant totalement obsol�te</td>
    </tr>
    <tr>
    <td>.gz</td><td><tt>gzip</tt></td><td><tt>gunzip</tt></td>
    <td>Outils le plus couramment utilis� (<a href="http://www.gnu.org/licenses/licenses.fr.html">licence GPL</a>)</td>
    </tr>
    <tr>
    <td>.bz2</td><td><tt>bzip2</tt></td><td><tt>bunzip2</tt></td>
    <td>Plus performant que <tt>gzip</tt></td>
    </tr>
    </tbody>
    </table>""",
    question="""Quel compresseur permet d'obtenir des fichiers <tt>gz</tt>&nbsp;?""",
    tests=(
    bad('zip',
        """Cet outil (non propos� dans la liste) est un archiveur/compresseur,
        Ce n'est donc pas un simple compresseur"""),
    good("gzip"),
    ),
    )

add(name="comprimons",
    required=["intro"],
    question="""Quelle commande tapez-vous pour comprimer
    le fichier <tt>toto</tt>""",
    tests=(
    reject(("<",">"), "On veut la version simple sans redirection"),
    reject('tar', """On ne veut pas cr�er une archive contenant
    plusieurs fichiers mais simplement comprimer un fichier"""),
    require("gzip",
            """Je ne trouve pas le nom du compresseur dans votre r�ponse.
            Pourtant vous l'avez donn� dans une question pr�c�dente"""),
    shell_good("gzip toto"),
    shell_bad("gzip -c toto", "L'option <tt>-c</tt> est inutile"),
    shell_display,
    ),
    good_answer="""Vous remarquerez que votre fichier <tt>toto</tt>
    � disparu, il n'y a que <tt>toto.gz</tt>""",
    )

add(name="garde l'original",
    required=["intro", "sh:'Bonjour' dans 'toto'", "variable:lire ligne"],
    question="""Quelle commande tapez-vous pour comprimer
    le fichier <tt>toto</tt> mais en gardant l'original
    et en stockant le r�sultat dans <tt>toto.gz</tt>.""",
    tests=(
    reject('-', "Vous n'avez besoin d'aucune option."),
    expect('toto.gz'),
    expect('gzip'),
    reject(("-c", "-N"),
              """Pourquoi s'emb�ter � apprendre toutes les options&nbsp;?
              Votre commande est peut-�tre juste, mais refaite l� sans
              l'option <tt>-c</tt> ou <tt>-N</tt>"""),
    require(("<",">"),
            """Il suffit de rediriger l'entr�e et la sortie standard
            et de ne donner AUCUN param�tre � la commande <tt>gzip</tt>
            """),
    shell_good("gzip <toto >toto.gz"),
    shell_bad("gzip <toto.gz >toto",
              """Cette commande compresse <tt>toto.gz</tt> (cela sert � rien)
              et stocke le fichier comprim� deux fois dans <tt>toto</tt>"""),
    shell_display,
    ),
    )

add(name="d�comprimons",
    required=["comprimons"],
    question="""Quelle commande tapez-vous pour d�comprimer
    le fichier <tt>toto.gz</tt>""",
    tests=(
    reject(("<",">"), "On veut la version simple sans redirection"),
    require('toto.gz', "C'est <tt>toto.gz</tt> que vous voulez d�comprimer"),
    shell_good("gzip -d toto.gz",
               """La commande que vous avez indiqu�e est excellente
               pour les scripts, mais en interactif <tt>gunzip</tt>
               est plus courte.
               Seul celle-ci sera accept�e dans la suite du TP."""),
    shell_good("gunzip toto.gz"),
    shell_display,
    ),
    good_answer="""Vous remarquerez que votre fichier <tt>toto.gz</tt>
    � disparu, il n'y a que <tt>toto</tt>""",
    )

add(name="garde le compress�",
    required=["d�comprimons","sh:'Bonjour' dans 'toto'","variable:lire ligne"],
    question="""Quelle commande tapez-vous pour d�comprimer
    le fichier <tt>toto.gz</tt> mais en gardant l'original
    et en stockant le r�sultat dans <tt>toto</tt>.""",
    tests=(
    Reject(";", "Une seule commande est n�cessaire, donc pas de ';'"),
    expect('toto.gz'),
    reject("-c",
              """Pourquoi s'emb�ter � apprendre toutes les options&nbsp;?
              Votre commande est peut-�tre juste, mais refaite la sans
              utiliser l'option <tt>-c</tt> (mais en modifiant la commande),
              votre r�ponse sera plus courte."""),
    require(("<",">"),
            "Il suffit de rediriger l'entr�e et la sortie standard"),
    shell_bad("gzip <toto.gz >toto",
              "<tt>gzip</tt> sert � compresser, pas � d�compresser"),
    shell_good("zcat <toto.gz >toto", "Le &lt; est inutile"),
    shell_good("zcat toto.gz >toto"),
    shell_good("gunzip <toto.gz >toto", "<tt>zcat</tt> est plus court"),
    shell_good("gzip -d <toto.gz >toto",
               """Pour ma part, je trouve que c'est plus lisible
               d'utiliser la commande <tt>gunzip</tt> ou <tt>zcat</tt>"""),
    reject(('<toto ','< toto '),
           """Vous redirigez l'entr�e standard vers <tt>toto</tt> alors
           qu'il n'existe pas encore"""),
    shell_display,
    ),
    )

from . import archiver

add(name="comp. archive",
    required=["garde l'original", "archiver:cr�ation", "pipeline:intro"],
    before="""Pour beaucoup de commandes Unix,
    le nom de fichier <tt>-</tt> (tiret ou moins)
    repr�sente l'entr�e ou la sortie standard.""",
    question="""Faites un archivage du r�pertoire <tt>PratiqueUnix</tt>
    et stockez l'archive compress�e dans <tt>PratiqueUnix.tar.gz</tt>.
    <p>
    Attention&nbsp;:
    <ul>
    <li> Vous ne devez pas stocker un fichier non comprim� sur le disque.
    <li> Vous n'avez pas besoin de chercher une nouvelle option
    dans la documentation car vous connaissez d�j� tout ce qui est n�cessaire.
    <b>Surtout pas l'option 'z' qui n'est pas standard</b>
    </ul>
    """,
    tests=(
    reject('<', "Expliquez � un enseignant pourquoi vous utilisez '&lt;'"),
    reject('/',
           """Pas besoin de <tt>/</tt> (� moins que <tt>PratiqueUnix</tt>
           soit un lien symbolique)"""),
    require('-c',
            """Pour <tt>tar</tt>,
            ll faut indiquer l'option de cr�ation <tt>c</tt>,
            N'oubliez pas le tiret avant les options.
            Il faut le mettre m�me si cela marche sans."""),
    reject('gzip -', "Pas besoin d'option pour <tt>gzip</tt>"),
    require('gzip', "On comprime avec <tt>gzip</tt>"),
    require(' - ', """O� est le tiret indiquant que <tt>tar</tt>
    doit �crire l'archive sur la sortie standard&nbsp;?"""),
    require('|', """Il faut connecter la sortie standard de la
    commande <tt>tar</tt> � l'entr�e standard de la commande <tt>gzip</tt>
    avec un <em>pipe</em>"""),
    require('>', """La sortie standard de <tt>gzip</tt> doit
    �tre redirig�e vers le fichier compress� que l'on veut cr�er"""),
    expect('PratiqueUnix.tar.gz'),
    shell_good("tar -cf - PratiqueUnix | gzip >PratiqueUnix.tar.gz",
               dumb_replace=archiver.dumb_replace),
    require('f',
            "Il manque l'option <tt>f</tt> indiquant le fichier de sortie"),
    shell_bad("tar -cf PratiqueUnix - | gzip >PratiqueUnix.tar.gz",
              """Oups, la commande <tt>tar</tt> �crit l'archive du r�pertoire
              <tt>-</tt> dans le fichier <tt>PratiqueUnix</tt>"""),
    reject('<', "Pourquoi redirigez-vous l'entr�e standard&nbsp;?"),

    shell_display,
    ),
    )

add(name="decomp. archive",
    required=["comp. archive", "d�comprimons", "archiver:extraction"],
    question="""D�compressez <tt>PratiqueUnix.tar.gz</tt> et
    extrayez les fichiers dans le r�pertoire courant sans passer
    par un fichier interm�diaire.
    """,
    tests=(
    reject('>', "Expliquez � un enseignant pourquoi vous utilisez '&gt;'"),
    require('|', "Comme pour la compression, il faut un pipeline"),
    require('PratiqueUnix.tar.gz', "Je ne vois pas le nom de l'archive"),
    reject("gunzip PratiqueUnix.tar.gz",
              """Cela ne fonctionne pas, vous venez de d�comprimer
              l'archive dans le r�pertoire courant sans l'extraire.
              En effet, la commande <tt>gunzip xxx.gz</tt> n'�crit rien
              sur la sortie standard.
              """,
              ),
    shell_good("gunzip <PratiqueUnix.tar.gz | tar -xf -",
               dumb_replace=archiver.dumb_replace),
    shell_good("gzip -d <PratiqueUnix.tar.gz | tar -xf -",
               dumb_replace=archiver.dumb_replace),
    shell_bad("gzip -d PratiqueUnix.tar.gz | tar -xf -",
              "<tt>gzip</tt> ne va rien �crire sur sa sortie standard.",
               dumb_replace=archiver.dumb_replace),
    reject((' -c', '-dc'),
              """Pourquoi s'emb�ter � apprendre toutes les options&nbsp;?
              Votre commande est juste, mais refaite l� sans
              l'option <tt>c</tt>"""),
    shell_good("zcat PratiqueUnix.tar.gz | tar -xf -",
               dumb_replace=archiver.dumb_replace),
    require('f -', """Il faut dire � la commande <tt>tar</tt>
    de lire l'entr�e standard (-)"""),
    reject_endswith(' .', """L'extraction de l'archive est faite dans le
    r�pertoire courant, pas besoin d'indiquer le <tt>.</tt> � la fin."""),
    require('-x', """O� est l'option indiquant que l'on veut extraire
    une archive&nbsp;?"""),
    require_endswith(' -',
                     """Lors de l'extraction de l'archive,
                     elle se fait automatiquement dans le r�pertoire
                     courant, pas besoin d'indiquer ou la mettre."""),
    shell_display,
    ),
    good_answer = """La commande <tt>tar</tt> supporte une option
    <tt>z</tt> mais je d�conseille de l'utiliser car elle cache
    le programme utilis� pour comprimer/d�comprimer""",
    )




    
 
