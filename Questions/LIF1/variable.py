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
from check import C

add(name="variables",
    required = ['intro:intro'],
    before="""En programmation, on manipule des <b>donn�es</b>.
    <p>
    Ces donn�es peuvent �tre des nombres, des cha�nes de caract�res ou
    des structures de donn�es.
    <p>
    Pour pouvoir �tre manipul�es, ces donn�es doivent �tre "stock�es"
    dans la m�moire de l'ordinateur.
    Pour que le programmeur puisse utiliser ces donn�es,
    on va leur associer un <b>nom</b>&nbsp;: c'est ce que l'on appelle
    une <b>variable</b>.
    <p>
    En d'autres termes une <b>variable</b> est un nom que l'on associe
    � une zone m�moire dans laquelle sera cod�e une information
    """,  
    question="""�num�rez les noms des diff�rents types de donn�es du
    langage C (en fran�ais&nbsp;: caract�re, entier, flottant, grand flottant).""",
    tests = (
        Good(Contain("int") & Contain("float") & Contain("double")
             & Contain("char")),
        Bad(Comment(Contain("main"),
                    """<tt>main</tt> n'est pas un mot cl� du langage
                    mais le nom de la fonction principale""")),
        ),
    )

add(name="nom de variable",
    required = ['variables'],
    before="""Les noms de variables sont constitu�s d'une chaine de caract�res.
    Mais attention, toutes les chaines de caract�res ne sont pas valides. 
    Une chaine de carat�re valide doit r�pondre aux crit�res suivants :
    <ul>
    <li>Ne pas contenir de caract�res accentu�s
    <li>Ne pas contenir d'<tt>espace blanc</tt>.
    <small>caract�re blanc, tabulation, fin de ligne</small>
    <li>Ne pas commencer par un chiffre
    <li>Ne pas contenir un <tt>caract�re graphique</tt>.
    <small>tout caract�re du clavier ne repr�sentant ni une lettre
    de l'alphabet latin, ni un chiffre.
    hormis le 'tiret de soulignement' : <b>_</b></small>
    <li>Ne pas porter le m�me nom qu'un :
    <ul>
    <li> <b>mot cl�</b> du langage (i.e un mot r�serv� au langage) ;
    <li> qu'une fonction existante ;
    <li> qu'une autre variable visible.
    </ul>
    </ul>
    On peut le dire autrement : un nom de variable peut �tre compos� uniquement
    de caract�res non accentu�s de l'alphabet latin, de chiffres et de tirets
    de soulignement; un nom de variable ne doit pas commencer par un chiffre.
    """,
    question="""Dans le programme suivant,
    listez les noms de variables qui ne sont pas valides.
    <small>Vous pouvez le v�rifier en copiant ce programme dans un fichier
    et en le compilant.</small>
    <pre>int main(int argc, char **argv)
{
  int a_2 ;
  int 2b, c@d ;
  char _d ;
  float ?x ;
  double y2 ;
 
  return 0 ;
}</pre>
    """, 
    tests = (
        Bad(Comment(Contain('a_2'),
                    "Le soulign� est autoris� dans les noms de variable")),
        Bad(Comment(Contain('y2'),
                    "Les chiffres sont autoris�s dans les noms de variable")),
        Good(Contain("2b") & Contain("c@d") & Contain("?x")),
        Bad(Comment(Contain(''), "Il en manque")),
        ),
    )

add(name="casse variable",
    before="""En langage C,
    on diff�rencie les caract�res �crits en majuscules ou en minuscules.
    <p>
    Ainsi deux variables peuvent porter le m�me nom si la casse
    utilis�e est diff�rente.
    <p>
    Par exemple, la d�claration suivante est valide&nbsp;:
    <pre>int toto, TOTO, ToTo ;</pre>
    Pour le langage C, les trois variables pr�c�dentes portent des noms
    diff�rents.
    <p>
    <b>Remarque</b> : Tous les mots cl�s du langage C sont �crits en caract�res
    minuscules. 
    """,  
    question="""Dans le programme suivant,
    les d�clarations de variables sont-elles correctes&nbsp;?
    <small>R�pondez par oui ou non</small>
    <pre>
int main(int argc, char **argv)
{
  int INT;
  float FLOAT;
  double argv;
  
  return 0 ;
}</pre>
    """, 
   nr_lines=1,     
    tests = (
    Good(Comment(No(),
         """Les d�clarations des variables <tt>INT</tt> et <tt>FLOAT</tt>
         sont correctes (car ces noms sont diff�rents de <tt>int</tt>
         et <tt>float</tt> pour le langage).
         <p>Mais la d�claration <tt>double argv;</tt> est <b>incorrecte</b>,
         car le nom <tt>argv</tt> a d�j� �t� utilis� plus haut dans une
         autre d�claration."""),
         ),
        ),
    )
