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

add(name="intro",
    required = ["intro:intro"],
    before="""La commande <tt>make</tt> permet de compiler,
    de lancer, de v�rifier et plein d'autres choses sur vos projets,
    que ceux-ci soient du d�veloppement ou autre chose.""",
    question = """Lorsque vous lancez la commande <tt>make</tt>,
    combien cela affiche de lignes � l'�cran&nbsp;?""",
    tests = ( Good(Comment(Int(1),
                           """La ligne qui est affich�e vous indique
                           que la commande <tt>make</tt> n'a pas trouv�
                           la description de votre projet."""
                           )
                   ),
              Comment("""Votre r�ponse est impossible :
              <ul>
              <li> Si le r�pertoire courant est vide, montrez
              cela � un enseignant.
              <li> Si le r�pertoire courant n'est pas vide
              alors allez dans le bon r�pertoire
              (celui que vous venez de cr�er).
              </ul>""" + navigation),
              ),
    )


add(name="makefile",
    required = ["intro"],
    before="""Copiez le texte suivant dans le fichier nomm� <tt>Makefile</tt>
    en utilisant un �diteur de texte (<tt>xemacs</tt> de pr�f�rence).
    <pre># Ce qui est � gauche des deux points est nomm� un 'but' ou 'cible'.
# Ce qui est � droite est ce dont il d�pend.
# Les lignes au dessous (en shell) indiquent comment r�aliser le but/cible,

CFLAGS = -Wall -Werror -g      # Options de compilation par d�faut
LDLIBS = -lm                   # Biblioth�ques de fonctions par d�faut

mon-projet <b>:</b> avant-compilation execute-mon-programme apres-compilation

avant-compilation <b>:</b>
	@echo "D�but compilation � $$(date)"

execute-mon-programme <b>:</b> mon-programme

mon-programme <b>:</b>

apres-compilation <b>:</b>
	@echo "Fin compilation � $$(date)"

</pre>""",
    question = """Lorsque vous lancez la commande <tt>make</tt>,
    combien cela affiche de lignes � l'�cran&nbsp;?""",
    tests = (
    Good(Comment(Int(2),
                 """Les deux lignes que vous avez sur l'�cran indiquent
                 la date de d�but et de fin de compilation.
                 Cela a �t� rapide car il n'y a rien � compiler.
                 <pre>D�but compilation : Sat Nov 24 18:05:18 CET 2007
Fin compilation   : Sat Nov 24 18:05:18 CET 2007</pre>"""
                 )
         ),
    Comment("""Vous n'avez pas r�ussi � faire correctement le copi� coll�
    pour mettre le texte indiqu� sur l'�cran.
    <ul>
    <li> Si le message affich� est du genre : <tt>Makefile:8: *** missing separator (did you mean TAB instead of 8 spaces?).  Stop.</tt>
    cela veut dire que les deux lignes qui commencent par <tt>@echo</tt>
    ne sont pas indent�es avec une caract�re tabulation mais
    avec des espaces.
    <li> Sinon, appelez un enseignant.
    </ul>"""),
    ),
    )

add(name="recompile",
    required = ["main:intro"],
    before = "On vous pose la m�me question de mani�re intentionnelle.",
    question = """Lorsque vous lancez la commande <tt>make</tt>,
    combien cela affiche de lignes � l'�cran&nbsp;?""",
    tests = (
    Good(Comment(Int(2),
                 """La commande <tt>make</tt> s'est rendue compte en regardant
                 les dates de modification des fichiers que le programme
                 avait d�j� �t� compil� et que c'�tait un perte de temps
                 de le recompiler""")),
    Comment("""Ne r�pondez pas au hasard, tapez <tt>make</tt> dans
    le terminal et comptez les lignes"""),
    ),
    )

add(name="ex�cuter",
    required = ["recompile"],
    before = """La commande <tt>make</tt> peut en plus lancer l'ex�cutable
    apr�s la cr�ation si vous lui demandez.
    <p>
    Ajoutez dans votre fichier <tt>Makefile</tt> la ligne en jaune.
    <pre>...
execute-mon-programme <b>:</b> mon-programme
<span style="background:yellow">	mon-programme arg1 arg2 arg3</span>
...""",
    question = """Lorsque vous lancez la commande <tt>make</tt>,
    combien cela affiche de lignes � l'�cran&nbsp;?""",
    tests = (
    Good(Comment(Int(3),
                 """La ligne du milieu indique que la commande
                 <tt>make</tt> a ex�cut� votre programme.
                 Mais celui-ci n'affiche rien :-(""")),
    Comment("""Ne r�pondez pas au hasard, tapez <tt>make</tt> dans
    le terminal et comptez les lignes"""),
    ),
    )

add(name="erreur compile",
    required = ["ex�cuter"],
    before = """Quand la commande <tt>make</tt> rencontre une erreur
    lors de la fabrication d'une cible, elle s'arr�te.""",
    question = """Remplacez le <tt>return</tt> par <tt>Return</tt>
    dans le fichier <tt>mon=programme.c</tt> puis lancez <tt>make</tt>
    <p>
    Combien de lignes sont affich�es&nbsp;?""",
    tests = ( Good(Comment(IntGT(6),
                           """Apr�s le lancement de la compilation C
                           vous voyez de nombreux messages venant
                           du compilateur.
                           <ul>
                           <li> La premi�re est la plus importante car
                           souvent elle d�clenche les suivantes.
                           <li> Sur chaque ligne le nom du fichier
                           source et le num�ro de ligne sont indiqu�s.
                           </ul>
                           
                           <p>
                           La derni�re ligne est affich�e par la commande
                           <tt>make</tt> et indique la cible qui
                           n'a pas pu �tre cr�e.
                           <p>
                           <b>Si vous avez lanc� la commande <tt>make</tt>
                           � partir d'<tt>emacs</tt> ou <tt>xemacs</tt>
                           il vous suffit de taper <u><tt>^X `</tt></u>
                           (control-X puis anti-cote)
                           pour que votre curseur se positionne
                           automatiquement sur la prochaine erreur
                           de compilation</b>
                           <p>
                           <em>N'oubliez pas de remettre <tt>return</tt>
                           au lieu de <tt>Return</tt></em>
                           """)),
              Comment("""Avez-vous :
              <ul>
              <li> Mis une majuscule � <tt>return</tt>&nbsp;?
              <li> Sauvegard� le fichier&nbsp;?
              <li> �dit� le bon fichier&nbsp;?
              </ul>"""),
              ),
    ),
add(name="erreur",
    required = ["ex�cuter"],
    before = """Quand la commande <tt>make</tt> rencontre une erreur
    lors d'une ex�cution, elle s'arr�te.""",
    question = """Remplacez le <tt>return 0</tt> par <tt>return 1</tt>
    dans le fichier <tt>mon=programme.c</tt> puis lancez <tt>make</tt>
    <p>
    Quelle est la cible que la commande <tt>make</tt> n'arrive
    pas � cr�er&nbsp;?""",
    tests = ( Good(Comment(Equal('execute-mon-programme'),
                           """Maintenant remettez le <tt>return 0</tt>
                           car il indique que le programme c'est bien
                           ex�cut�""")),
              Comment("""La cible qui a �chou�e est indiqu� sur la derni�re
              ligne entre les crochets."""),
              ),
    ),
    


   


    
    
