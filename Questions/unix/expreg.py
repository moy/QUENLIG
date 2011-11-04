# -*- coding: latin-1 -*-
#    QUENLIG: Questionnaire en ligne (Online interactive tutorial)
#    Copyright (C) 2005-2006,2011 Thierry EXCOFFIER, Universite Claude Bernard
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


# FAIRe LES QUESTION . * ^ $ +

from questions import *
from check import *

aide = """La m�thode la plus simple pour tester les expressions
    r�guli�re est d'ex�cuter la commande suivante&nbsp;:
    <pre>sed -r 's/votre_expression_reguli�re/(((&)))/g'</pre>
    Vous tapez ensuite du texte au clavier et les cha�nes de caract�res
    reconnues appara�tront dans les triples parenth�ses."""

add(name="intro",
    required=["sh:console", "sh:configurer", "remplacer:intro"],
    before=aide,
    question="""Quelle expression r�guli�re repr�sente une cha�ne
    de caract�re quelconque.""",
    tests=(
    good('.*'),
    bad('*', "Non �a c'est un <em>pattern</em> pour le shell."),
    bad('*.', "L'�toile multiplie ce qui pr�c�de."),
    bad(".", "Cette expression r�guli�re repr�sente un caract�re quelconque"),
    reject("sed",
           """On demande le <em>pattern</em>,
           pas la ligne de commande permettant de le tester"""),
    reject("[",
           """Vous n'allez pas �num�rer tous les
           caract�res possibles&nbsp;!
           N'utilisez pas les crochets."""),
    reject('?', """Le <tt>?</tt> indique un caract�re quelconque pour
    les <em>pattern</em> du shell.
    On vous demande une expression r�guli�re"""),
    require(".",
            """On indique un caract�re quelconque avec un '.'
            Une ligne quelconque est une r�p�tition de caract�res
            quelconques."""),
    reject('+', """Si vous utilisez le <tt>+</tt> pour multiplier ce qui
    pr�c�de cela ne permettra pas de repr�senter une chaine vide
    car dans les expressions r�guli�res <b>�tendues</b> il ne
    multiplie pas par z�ro."""),
    require("*",
            """On indique que l'on r�p�te ce qui pr�c�de
            en utilisant le symbole <tt>*</tt>"""),
    reject("\\.*",
           """<tt>\\.*</tt> repr�sente une s�rie
           de points de longueur quelconque"""),
    reject(("'",'"'),
           """On d�sire l'expression r�guli�re,
           on ne se soucie pas du shell,
           donc on ne veut pas de <tt>'</tt> ou <tt>\"</tt>
           """),
    ),
    good_answer="Par d�faut la cha�ne tient dans une seul ligne",
    indices = (
    """C'est la r�p�tition un nombre ind�termin� de fois
    d'un caract�re quelconque""",
    ),
    )

partie = " Donc la ligne conviendra m�me si elle ne contient pas que des <tt>A</tt> :-("

add(name="ligne de A",
    question="""Quelle expression r�guli�re <b>�tendue</b> repr�sente les
    lignes non vides ne contenant que des caract�res A et rien d'autre""",
    tests=(
    good('^A+$'),
    good(('^[A]+$', '^(A)+$', '^AA*$'),
         "Il est plus simple d'�crire <pre>^A+$</pre>"
         ),
    bad(('^A*$', '^[A]*$', '^(A)*$'),
        "Ce n'est pas bon car cela repr�sente aussi les lignes vides."),
    bad('^A$', "Ceci repr�sente les lignes contenant un seul A"),
    require("^",
            """Si vous n'indiquez pas qu'elle commence au d�but de la ligne,
            l'expression r�guli�re peut commencer n'importe o�.""" + partie),
    require("$",
            """Si vous n'indiquez pas qu'elle finit � la fin
            de la ligne, l'expression r�guli�re peut finir n'importe o�.""" +
            partie),
    reject("[",
           """Pas besoin de sp�cifier une liste de
           lettres car il n'y en a qu'une seule&nbsp;: A"""),
    reject(" ",
           """Si vous mettez un espace cela veut dire que vous d�sirez
           que la chaine de caract�re contienne un espace."""
           ),
    number_of_is('A', 1,
                 """Votre r�ponse ne doit contenir qu'un
                 seul caract�re <tt>A</tt>"""),
    ),
    indices=("Le caract�re <tt>^</tt> indique le d�but de ligne",
    "Le caract�re <tt>$</tt> indique la fin de ligne",
    ),
    )

add(name="un sp�cial",
    required=["intro"],
    question="""Quelle expression repr�sente le caract�re point (<tt>.</tt>)
    au lieu de repr�senter un caract�re quelconque&nbsp;?""",
    tests=(
    good( ("\\.", "[.]") ),
    require('.', "Je ne vois pas de caract�re <tt>.</tt> dans votre r�ponse"),
    bad( ".", "Cette expression repr�sente un caract�re quelconque"),
    reject(('"',"'"),
           """Une expression r�guli�re n'a pas la m�me syntaxe que le
           shell, les apostrophes et guillemets ne sont pas sp�ciaux"""),
    reject('\\\\', """Votre expressions demande � avoir un caract�re
    <em>backslash</em> car c'est lui que vous avez prot�g�."""),
    ),
    indices=("""Attention le <tt>.</tt> est un caract�re sp�cial,
    il faut annuler sa signification""",
             """Le caract�re d'�chappement dans les expressions
             r�guli�re est \\""",
             ),
    )

add(name="deux sp�cial",
    required=["un sp�cial"],
    question="""Quelle expression r�guli�re repr�sente la chaine de caract�res <tt>2*</tt> (un chiffre deux suivi d'une �toile)&nbsp;?""",
    tests=(
    good( ("2\\*", "2[*]") ),
    bad( "2*", "Cette expression repr�sente une suite de 2"),
    bad('[0-9]\*',
        """Cette expression repr�sente un chiffre suivi d'une �toile,
        on vous demande un <tt>2</tt> suivi d'une �toile."""),
    require('2', 'Je ne vois pas de 2 dans votre r�ponse&nbsp;!'),
    require('*', 'Je ne vois pas de * dans votre r�ponse&nbsp;!'),
    reject(('"',"'"),
           """Guillemets et apostrophes sont reconnus par le shell
           pas par les expressions r�guli�res,
           vous devez utiliser autre chose pour annuler
           la signification de l'�toile"""),
    reject('\\2', "Pourquoi prot�ger le 2, il n'est pas sp�cial"),
    reject('2\\\\*', "Cette expression repr�sente un 2 suivi d'antislashs."),
    reject('[2*]', '<tt>[2*]</tt> repr�sente un <tt>2</tt> ou une �toile'),
    reject('[2\\*]',
           '''<tt>[2\\*]</tt> repr�sente un <tt>2</tt>, un <tt>\\</tt> ou
           une �toile'''),
    ),
    indices=("""Attention le <tt>*</tt> est un caract�re sp�cial,
    il faut annuler sa signification""",
             """Le caract�re d'�chappement dans les expressions
             r�guli�re est \\""",
             ),
    )

add(name="sp�cial",
    required=["un sp�cial", "intro"],
    question="""Quelle expression repr�sente les lignes compl�tes
    contenant un caract�re <tt>.</tt> quelque part&nbsp;?
    """,
    tests=(
    good( (".*\\..*", ".*[.].*") ),
    bad( ("\\.","[.]"),
         """L'expression repr�sente le <tt>.</tt> pas la ligne compl�te"""),
    bad(".*\\.*",
        """Cette expression indique une chaine de caract�res quelconque
        suivie d'une suite de caract�res point."""),
    bad(("*.*", "*'.'*", '*"."*', "*\\.*"),
        """C'est la bonne r�ponse pour les <em>pattern</em>
        du shell. Mais on vous demande une expression r�guli�re"""),
    reject(('[',']'), """Pas besoin de crochets,
    Utilisez plut�t un anti-slash pour annuler les significations
    des caract�res sp�ciaux"""),
    require(".*",
            """On ne veut pas que le '.' mais aussi
            la chaine de caract�res quelconques
            � sa gauche et � sa droite."""),
    reject(("^", "$"),
           """Pas la peine de sp�cifier les indicateurs
           de d�but/fin de ligne car le <tt>.*</tt>
           prend la plus grande chaine possible.
           Donc jusqu'au bout"""),
    number_of_is('.*', 2, """Il y a deux chaines de caract�res quelconques,
    une � gauche et une � droite du point"""),
    number_of_is('\\', 1, """Il y a un seul caract�re sp�cial pour lequel
    la signification doit �tre annul�e, vous n'avez donc besoin
    que d'un seul anti-slash"""),
    
    ),
    indices=(
    """L'expression solution repr�sente une chaine de caract�res quelconques
    suivie d'un point suivie d'une chaine de caract�res quelconques""",
    """La r�ponse la plus courte tient en 6 caract�res""",
    """N'oubliez pas que le <tt>.*</tt> correspond
    � la plus longue cha�ne possible""",
             ),
    )

add(name='n�gation',
    before=aide,
    required=["intro"],
    question="""Quelle expression r�guli�re repr�sente un caract�re qui ne soit
    ni une lettre de l'alphabet en minuscule ni un chiffre""",
    tests=(
    reject("!", "La n�gation n'est pas la m�me que celle du shell"),
    reject(".",
           """Vous n'avez pas besoin du caract�re '<tt>.</tt>',
           il n'y a aucun caract�re quelconque ici."""),
    reject(('(', ')'), "Vous n'avez pas besoin de parenth�ses"),
    reject('A', "Pas en minuscule, j'ai pas dis pas en majuscule"),
    reject("^[a", """La n�gation est le premier caract�re apr�s
    le crochet. Sinon elle indique un d�but de ligne."""),
    reject(' ', "Attention, les espaces sont significatifs"),
    reject(('+', '*'), "On cherche un seul caract�re, pas une suite"),
    reject('$', "Le caract�re est n'importe o� sur la ligne"),
    reject(('ab','12'),
           """Ne lister pas tous les caract�res un par un.
           D�finissez un interval de caract�res avec les crochets."""),
    
    require(("[", "]"),
            """Il faut sp�cifier une liste de caract�res en utilisant
            les crochets"""),
    require("-", "Il faut utiliser le <tt>-</tt> pour indiquer un intervalle"),
    require("^", "Je ne trouve pas le caract�re indiquant <em>tout sauf</em>"),
    number_of_is('^',1,
                 """Vous ne devez employer la n�gation qu'une seule fois"""),
    require('0-9', """Je ne trouve pas l'intervalle indiquant tous les
    chiffres de 0 � 9 inclus"""),
    require('a-z', """Je ne trouve pas l'intervalle indiquant toutes les
    lettres de 'a' � 'z' inclus"""),
    good("[^a-z0-9]"),
    good("[^0-9a-z]",
         """J'attendais <tt>[^a-z0-9]</tt>, j'accepte votre
         solution car elle fonctionne mais s'il vous plais
         ne changez pas l'ordre de ce qui es demand� dans l'�nonc�."""),
    expect('a-z0-9'),
    ),
    )

add(name='suite de chiffres',
    before=aide,
    required=["intro"],
    question="""Quelle expression repr�sente des suites de chiffres
           quelconques d'au moins un chiffre (m�me <tt>000</tt>
           ou <tt>01</tt> par exemple)""",
    tests=(
    reject('sed',
           "On ne veut pas la commande, seulement l'expression r�guli�re"),
    bad("[0-9]*", """Cette expression correspond aussi � une chaine vide,
    mais nous recherchons les chaines contenant au moins un chiffre"""),
    bad('[:digit:]+', """C'est une expression r�guli�re qui r�pond
    � la question, mais on vous demande une solution qui n'utilise
    que des connaissances de base."""),
    require(('0-9','[','-',']'),
            "Je ne trouve pas l'intervalle des chiffres de 0 � 9"),
    reject('.', """Une suite de chiffre ne contient pas de caract�res
    quelconques, pourquoi indiquez-vous le caract�re '.'&nbsp;?"""),
    reject(('(',')'), "Pas besoin de parenth�ser"),
    reject(('[0-9]+[0-9]*', '[0-9]*[0-9]+'),
           """Vous pouvez faire deux fois plus court.
           En effet votre expression d�crit deux suites de chiffres
           l'un coll�e � l'autre"""),
    good( "[0-9]+",
    "C'est un expression r�gui�re �tendue car vous utilisez <tt>+</tt>"),
    good( "[0-9][0-9]*" ),
    good( "[0-9]*[0-9]", "On �crit plut�t <tt>[0-9][0-9]*</tt>" ),
    require(('*','+'), """Je ne vois pas le symbole indiquant que l'on r�p�te
    les chiffres""", all_agree=True),
    ),
    )

add(name='entier positif',
    before=aide,
    required=["suite de chiffres"],
    question="""Quelle expression r�guli�re �tendue repr�sente
    des suites de chiffres
    ne commen�ant pas par <tt>0</tt> sauf pour le nombre <tt>0</tt>.
    Exemple de ce que l'on doit trouver&nbsp;:
           
           <pre>dfsfd<span class='boxed'>67</span>sdfsfds-<span class='boxed'>0</span>sdfdsf++<span class='boxed'>0</span><span class='boxed'>8090</span>dsfs<span class='boxed'>0</span><span class='boxed'>0</span>ppp</pre>


           """,
    tests=(
    reject('sed', "On veut l'expression r�guli�re, pas la commande"),
    reject('[^0]',
           """<tt>[^0]</tt> indique un caract�re quelconque sauf <tt>0</tt>
           Par exemple <tt>A</tt>"""),
    bad(('[1-9]+[0-9]*|0', '([1-9]+[0-9]*|0)'),
        """Cette solution est correcte mais vraiment pas naturelle.
        Vous obtiendrez la bonne r�ponse en enlevant
        une caract�re de la votre..."""),
        
    reject('^', "On a pas besoin de <tt>^</tt>"),
    reject('+', """N'utilisez pas le <tt>+</tt> il n'est pas utile ici.
    Je pense que vous devriez plut�t utiliser <tt>*</tt>"""),
    reject('.',
           "Un nombre entier, pas un nombre flottant, donc pas de point"),
    reject(' ', """Si vous mettez un espace dans une expression r�guli�re,
    cet espace devra �tre trouv�"""),
    reject('[0]', "Il est plus simple d'�crire <tt>0</tt> que <tt>[0]</tt>"),
    require('|', """Il faut utiliser un <b>ou</b>, en effet,
    c'est z�ro ou un nombre de commen�ant pas par z�ro."""),
    require('[0-9]',
           "Vous n'autorisez pas les nombres � contenir des 0&nbsp;: 608"),
    require('[1-9]', """Vous n'indiquez pas que le premier chiffre est
    entre 1 et 9"""),
    require('*', """Vous n'indiquez pas qu'il y a un nombre ind�fini de
    chiffre apr�s le premier (y compris aucun)"""),

    good( "0|[1-9][0-9]*" ),
    bad( "0|([1-9][0-9]*)",
         "Cela fonctionne, mais les parenth�ses ne sont pas au bon endroit"),
    good( "(0|[1-9][0-9]*)" ),
    good( "[1-9][0-9]*|0" ),
    good( "([1-9][0-9]*|0)" ),
        
    ),
    )

class test_nombre_entier(bad):
    def test(self, a, string):
        if a.find("\\") != -1:
            return False, "Il n'y a pas besoin d'antislash pour cette question"
        if a.find("[1-9]") == -1:
            return False, '''Tous les nombres entiers commencent par un chiffre
            diff�rent de 0 sauf 0.'''
        if " " in a:
            return False, '''Les espaces sont <b>significatif</b>'''
        if a.find("|") == -1:
            return False, "0 est un cas � part car on ne lui met pas un signe"
        if a.count("|") > 1:
            return False, '''Un seul | suffit, ne compliquez pas inutilement'''
        if a[0] != "(" or a[-1] != ")":
            return False, """Je n'accepterais la solution que si vous
            parenth�sez le <tt>ou</tt>,
            �crivez <tt>(a|b)</tt> au lieu de <tt>a|b</tt>"""
        if a.find("[0-9]*") == -1:
            return False, """La fin d'un nombre entier contient un nombre
            ind�fini de nombre entre 0 et 9."""
        if a.find("[+-]") != -1:
            return False, """Si une liste de caract�res entre crochets contient
            '-' il faut le mettre en premier. Sinon il repr�sente un intervalle."""
        if a.find("[-+][0-9]") != -1 or a.find("[-+]?[0-9]") != -1:
            return False, """Un nombre entier ne commence pas par 0 sauf 0"""
        if a.find("[-+][0-9]") != -1:
            return False, """Un nombre entier peut �tre �crit sans signe."""
        return False, """Si apr�s avoir test� votre expression r�guli�re elle
        vous semble juste alors laissez un commentaire pour le faire savoir."""
    
    

add(name='nombre entier',
    required=["entier positif"],
    before=aide,
    question="""Quelle expression r�guli�re �tendue repr�sente les nombres
    entiers avec leur signe&nbsp;:
    <pre>dfsfd<span class='boxed'>+6</span>sdfsfds-<span class='boxed'>0</span>sdfdsf++<span class='boxed'>0</span>sdfs<span class='boxed'>89</span>dsfs<span class='boxed'>-45</span>sdff+<span class='boxed'>-342</span>fd<span class='boxed'>56</span>ssfsdf<span class='boxed'>0</span><span class='boxed'>76</span>werwer-<span class='boxed'>0</span><span class='boxed'>89</span>sdf\\<span class='boxed'>106</span></pre>
    Les boites indiquent les nombres que votre expression r�guli�re doit trouver.
    """,
    tests=(    
    good( ('([-+]?[1-9][0-9]*|0)',
           '(0|[-+]?[1-9][0-9]*)',
           '((-|+|)[1-9][0-9]*|0)',
           '(0|(-|+|)[1-9][0-9]*)',
           '((+|-|)[1-9][0-9]*|0)',
           '(0|(+|-|)[1-9][0-9]*)'
           ) ),
    good( '(0|+[1-9][0-9]*|-[1-9][0-9]*)',
          "Il est plus court d'�crire : <pre>(0|[-+]?[1-9][0-9]*)</pre>"),
    bad( ('(0|[-+][1-9][0-9]*)', '([-+][1-9][0-9]*|0)'),
          "Cela ne trouve pas les nombre sans signe."
          ),
    reject('[1-9]+', "Il y a un + qui n'est pas n�cessaire..."),
    bad( ('(0|([-+]?[1-9][0-9]*))', ),
          "Cela fonctionne, mais faites plus court (parenth�ses en trop)."
          ),
    test_nombre_entier(),
    ),
    )
    
    
add(name="identique",
    question="""Quelle expression r�guli�re �tendue repr�sente les
    lignes ne contenant <b>que</b> des caract�res identiques au premier
    de la ligne.
    """,
    tests=(
    reject(('a','A'),
           "Que vient faire un <tt>a</tt> dans votre r�ponse&nbsp;?"),
    require(('(',')'),
            """Vous devez grouper des caract�res et r�utiliser le texte
            trouv� par le groupe"""),
    require(('^', '$'),
            """Vous devez indiquer le d�but et la fin de ligne sinon
            l'expression pourra correspondre � une suite de caract�res
            identiques en plein milieu"""),
    require('\\1', """Vous devez utiliser les caract�res trouv�s par le groupe
            pour indiquer que le reste de la ligne est identique"""),
    good('^(.)\\1*$'),
    good('(^.)\\1*$', "Je pr�f�re : <tt>^(.)\\1*$</tt>"),
    bad('^(.)\\1+$', """Presque, mais cela ne trouve pas
    les lignes d'un seul caract�re"""),
    reject('+', """Vous ne devez pas utiliser le <tt>+</tt>
    car une ligne contenant un seul caract�re contient que des caract�res
    identiques !"""),
    require_startswith('^', """Pour ce probl�me,
    le <tt>^</tt> doit �tre en d�but d'expression r�guli�re""") ,
    require_endswith('$', """Pour ce probl�me,
    le <tt>$</tt> doit �tre en fin d'expression r�guli�re""") ,
    bad('^(.)\\1$', """Vous trouvez seulement les lignes contenant
    deux caract�res identiques"""),
    ),
    indices=("""Il faut mettre le premier caract�re de la ligne dans
    un groupe et dire que le reste de la ligne est la r�p�tition
    du contenu de ce groupe""",
             """Les groupes sont d�finis par les parenth�ses&nbsp;:
             <tt>a(.*)b(.*)c</tt>
             <p>
             Cette expression d�finit 2 groupes sans les utiliser.
             """,
             """Les groupes sont nomm�s anti-slash num�ro de groupe.
             <tt>\\1</tt> est le num�ro du premier groupe.
             """,
             """Pour cette exercice, le premier groupe est un caract�re
             quelconque et la suite de la ligne est une r�p�tition
             du premier groupe.
             """,
             ),
    )


