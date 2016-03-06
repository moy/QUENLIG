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

add(name="intro",
    required=["makefile:makefile", "processus:intro"],
    before="""Copier le programme C suivant dans le fichier nomm�
    <tt>mon-programme.c</tt>
    <pre>int main(int nombre_d_arguments, char *les_arguments[])
{
   return 0 ;
}</pre>
    """,
    question="""Taper � nouveau <tt>make</tt>.
    Combien, de lignes s'affichent&nbsp;?""",
    tests = ( Good(Int(3)),
              Bad(Comment(Int(2), """Vous avez mis le fichier dans le mauvais
              r�pertoire ou bien vous ne lui avez pas donn� le bon nom""")),
              Comment("""Je suppose que vous avez eu des messages d'erreur
              qui se sont affich�s sur l'�cran.<br>
              Faites un copi�/coll� au lieu de recopier le source du programme
              � la main.""" + navigation),
              ),
    good_answer = """La commande <tt>make</tt> a trouv� toute seule
    que pour cr�er la cible <tt>mon-programme</tt> il fallait
    lancer le compilateur C sur le fichier source <tt>mon-programme.c</tt>.
    <p>
    La ligne du milieu indique comment la compilation a �t� faite.""",
    )

add(name="puts",
    required=["makefile:erreur compile"],
    before = """La fonction <tt>puts</tt> affiche sur la sortie standard
    (l'�cran par d�faut) la chaine de caract�res qui lui a �t� pass�e
    en param�tre.
    <p>
    Pour avoir des informations sur <tt>puts</tt> vous pouvez
    tapez la commande <tt>man puts</tt>
    <p>
    Modifiez votre programme <tt>mon-programme.c</tt> pour qu'il dise bonjour
    en ajoutant la ligne
    <pre>puts("Bonjour") ;</pre> avant la
    ligne contenant le <tt>return</tt>.
    """,
    question = """Lancez la commande <tt>make</tt>,
    elle �choue sur quelle cible&nbsp;?""",
    tests = (Good(Comment(Equal('mon-programme'),
                          """En effet, vous utilisez la fonction <tt>puts</tt>
                          dans le programme mais son prototype n'a jamais
                          �t� d�fini.
                          <p>
                          Le prototype permet d'�viter des erreurs
                          de programmations."""
                          )),
             Comment("Avez-vous sauv� votre fichier modifi�&nbsp;?"),
             ),
    )

add(name="table des arguments",
    required=["cpp:include"],
    before = """La fonction <tt>main</tt> 2 arguments.
    <ul>
    <li> Le premier, nomm� <tt>nombre_d_arguments</tt> dans votre source
    est un entier indiquant avec combien de param�tres le programme a �t� lanc�
    <li> Le deuxi�me, nomm� <tt>les_arguments</tt> dans votre source
    est un tableau de chaines de caract�res,
    chaque chaine repr�sentant un argument.
    </ul>
    <p>
    En C, on acc�de � un �l�ment d'un tableau en faisant suivre
    le tableau par l'indice en crochets de l'�l�ment que l'on veut prendre
    dans le tableau.
    <p>
    L'indice 0 correspond au <b>premier</b> �l�ment du tableau.
    <p>
    <tt>les_arguments[1]</tt> est donc la deuxi�me chaine de caract�res
    contenue dans le tableau.
    <p>
    Mettez <tt>puts( les_arguments[1] )</tt> dans les
    sources de votre programme (avant le <tt>return</tt> qui termine
    votre programme).""",
    question = """Quand vous lancez <tt>make</tt> (et qu'il n'y
    pas d'erreur de compilation), qu'est ce que
    ce <tt>puts</tt> affiche&nbsp;?""",
    tests = ( Good(Comment(Equal("arg1"),
                           """Le premier argument (celui � l'indice 0)
                           est le nom du programme qui a �t� lanc�.
                           Dans notre cas&nbsp;: <tt>mon-programme</tt>""")),
              Bad(Comment(Equal("arg2"),
                          """Vous devriez faire l'exp�rience plut�t
                          que de faire confiance � votre
                          esprit de d�duction""")),
              ),
    )

add(name="Hello world",
    question="Affiche 'Hello world'",
    nr_lines=10,
    default_answer="""#include <stdio.h>

int main(int argc, char **argv)
{
return 0 ;
}""",
    tests = (
    Good(C_stdout(UpperCase(Start('HELLO WORLD')))),),
    )

    
add(name="Hello world2",
    question="Affiche 'Hello world'",
    nr_lines=10,
    default_answer="""#include <stdio.h>

int main(int argc, char **argv)
{
char tmp[99];
fgets(tmp, sizeof(tmp), stdin) ;
printf("(%s)\\n", tmp) ;
printf("(%s)(%s)\\n", argv[1], argv[2]) ;

return 0 ;
}""",
    tests = (
    Good(C_stdout(UpperCase(Start('HELLO WORLD')),
                  c_input='xxx', c_args=('a','b')
                  )),
    ),
    )

    

                  
    
    
    
    


    


