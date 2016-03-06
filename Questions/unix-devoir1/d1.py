# -*- coding: latin-1 -*-
#    QUENLIG: Questionnaire en ligne (Online interactive tutorial)
#    Copyright (C) 2008 Thierry EXCOFFIER, Universite de Lyon
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

"""
Creating session :

QUESTIONS="Questions/unix-devoir1"
SESSION="unix-devoir1"
HOST="proxy710.univ-lyon1.fr"
PORT="10001"
ADMIN="thierry.excoffier"

./main.py $SESSION create $QUESTIONS $PORT url "http://$HOST:$PORT/"
echo "
!gui_smiley
!question_pixel_map_see
" >Students/$SESSION/acls.student
./main.py $SESSION admin $ADMIN start
}

#####################################
Create HTML page for corrections
#####################################
A FAIRE
./corrections.py

"""

from QUENLIG.questions import *

add(name="intro",
    before="""
    Avant de commencer � r�pondre, vous devez avoir lu
    <a href="http://www710.univ-lyon1.fr/~exco/COURS/COURS/UNIX2/unix.html">
    les notes de cours</a> jusqu'� la partie
    �Comment taper plus vite des commandes.�
    <p>
    Si vous r�pondez en recopiant des morceaux venant du cours
    ou bien du web vous n'aurez pas de points.
    """,
    question="R�pondez OUI si vous avez compris et si vous avez lu votre cours.",
    tests = ( yes("R�pondez OUI"), ),
    )

add(name="r�ponse unique",
    before="""
    Une fois que vous aurez r�pondu � une question vous ne pourrez
    plus changer votre r�ponse.
    <p>
    Vous pouvez changer de question sans y r�pondre, mais ce que
    vous aurez tap� sera perdu, et vous devrez le retaper apr�s
    �tre revenu sur la question.
    <p>
    Vous pouvez arr�ter de travailler et reprendre plus tard
    si vous le d�sirez.
    <p>
    Apr�s avoir r�pondu � certaines questions, d'autres appara�tront.
    <p>
    Vous devez r�pondre � toutes les questions jusqu'� ce que cela
    affiche qu'il n'y a plus de questions.
    <p>
    Le logiciel est stupide et affiche �Bonne r�ponse� pour toutes
    vos r�ponses m�me si elles sont fausses.
    """,
    question="R�pondez OUI si vous avez compris",
    tests = ( yes("R�pondez OUI"), ),
    )

add(name="arbre",
    required = ['r�ponse unique'],
    question="Quelles sont les deux grandes classes d'entit�s pr�sentes dans le syst�me de fichier&nbsp;?",
    nr_lines = 2,
    tests = ( Good(Contain('')), ),
    )

add(name="p�riph�riques",
    required = ['r�ponse unique'],
    question="Pourquoi traiter les fichiers textes et les p�riph�riques de la m�me fa�on&nbsp;?",
    nr_lines = 2,
    tests = ( Good(Contain('')), ),
    )

add(name="chemin",
    required = ['arbre'],
    question="Qu'est-ce qu'un chemin&nbsp;?",
    nr_lines = 2,
    tests = ( Good(Contain('')), ),
    )

add(name="absolument relatif",
    required = ['chemin'],
    question="Dans quel cas utiliser des chemins relatifs ou absolus&nbsp;?",
    nr_lines = 2,
    tests = ( Good(Contain('')), ),
    )

add(name="relatif",
    required = ['chemin'],
    question="Comment le syst�me trouve l'entit� indiqu�e par un chemin relatif&nbsp;?",
    nr_lines = 2,
    tests = ( Good(Contain('')), ),
    )



add(name="nom",
    required = ['chemin'],
    question="Donnez des noms de fichiers interdits.",
    nr_lines = 2,
    tests = ( Good(Contain('')), ),
    )

add(name="login",
    required = ['r�ponse unique'],
    question="Quel est votre �login�&nbsp;?",
    nr_lines = 2,
    tests = ( Good(Contain('')), ),
    )

add(name="pratique",
    required = ['r�ponse unique'],
    before = "Pour r�pondre aux questions vous devez avoir acc�s � un UNIX (au b�timent Ariane ou avec un <a href=\"http://www.ubuntu.com/getubuntu/download\">live CD</a> chez vous.",
    question="Avez-vous acc�s � un machine unix&nbsp;?",
    nr_lines = 2,
    tests = ( yes('Vous ne pouvez pas faire ce devoir dans ces conditions'), ),
    good_answer = "Pour les questions suivantes vous aurez besoin d'ouvrir un terminal pour taper des commandes shell dedans.",
    )

add(name="prompt",
    required = ['pratique'],
    question="� quoi sert l'invite de commande&nbsp;?",
    nr_lines = 2,
    tests = ( Good(Contain('')), ),
    )

add(name="tuer",
    required = ['prompt'],
    before = "Pour information : la commande �sleep 10� s'ex�cute sans rien faire pendant 10 seconde",
    question="Comment faites-vous pour arr�ter une commande lanc�e dans le terminal (donnez plusieurs fa�ons)&nbsp;?",
    nr_lines = 2,
    tests = ( Good(Contain('')), ),
    )


add(name="terminer",
    required = ['pratique'],
    question="Indiquez plusieurs moyens de quitter un terminal&nbsp;:",
    nr_lines = 3,
    tests = ( Good(Contain('')), ),
    )

add(name="ou-suis-je",
    required = ['relatif', 'pratique'],
    question="Quelle commande tapez-vous dans le terminal pour afficher le chemin du r�pertoire courant&nbsp;?",
    nr_lines = 2,
    tests = ( Good(Contain('')), ),
    )

add(name="liste",
    required = ['ou-suis-je'],
    question="Comment faites-vous pour lister les entit�s (fichiers/r�pertoires) pr�sentes dans le r�pertoire courant&nbsp;?",
    nr_lines = 2,
    tests = ( Good(Contain('')), ),
    )


add(name="home",
    required = ['ou-suis-je'],
    question="Quel est le chemin absolu de votre r�pertoire de connexion&nbsp;?",
    nr_lines = 2,
    tests = ( Good(Contain('')), ),
    )
add(name="droits",
    required = ['home'],
    question="Quels sont les droits d'acc�s de votre r�pertoire de connexion&nbsp;?",
    nr_lines = 2,
    tests = ( Good(Contain('')), ),
    )

add(name="processus",
    required = ['pratique', 'commande'],
    question="Combien de processus apparaissent quand vous tapez la commande �ps� dans un terminal&nbsp;?",
    nr_lines = 2,
    tests = ( Good(Contain('')), ),
    )

add(name="commande",
    required = ['r�ponse unique'],
    question="� quoi servent les espaces dans les commandes shell&nbsp;?",
    nr_lines = 2,
    tests = ( Good(Contain('')), ),
    )

add(name="r�pertoire",
    required = ['commande'],
    question="Quelle ligne de commande utilisez-vous pour cr�er un r�pertoire �TOTO� dans le r�pertoire courant&nbsp;?",
    nr_lines = 2,
    tests = ( Good(Contain('')), ),
    )

add(name="destruction",
    required = ['commande'],
    question="Quelle ligne de commande utilisez-vous pour d�truire le fichier �truc� qui est dans le r�pertoire �/tmp�&nbsp;?",
    nr_lines = 2,
    tests = ( Good(Contain('')), ),
    )

add(name="option",
    required = ['commande'],
    question="Comment reconna�t-on les options dans les commandes shell&nbsp;?",
    nr_lines = 2,
    tests = ( Good(Contain('')), ),
    )

add(name="builtin",
    required = ['commande'],
    question="Qu'est-ce qu'une commande <em>builtin</em>&nbsp;?",
    nr_lines = 2,
    tests = ( Good(Contain('')), ),
    )

add(name="tabtab",
    required = ['pratique'],
    question="Que se passe-t-il dans le terminal quand vous appuyez 2 fois de suite sur la touche �Tabulation�&nbsp;?",
    nr_lines = 2,
    tests = ( Good(Contain('')), ),
    )

add(name="pattern",
    required = ['pratique', 'commande'],
    question="Qu'est ce que la commande �echo /etc/a*� fait&nbsp;?",
    nr_lines = 2,
    tests = ( Good(Contain('')), ),
    )

add(name="recursion",
    required = ['pattern', 'option', 'liste'],
    question="Qu'est ce que la commande �ls -lR� fait&nbsp;?",
    nr_lines = 2,
    tests = ( Good(Contain('')), ),
    )

add(name="cat",
    required = ['pattern'],
    question="Qu'est ce que la commande �cat /etc� fait&nbsp;?",
    nr_lines = 2,
    tests = ( Good(Contain('')), ),
    )

add(name="cdrom",
    required = ['recursion'],
    question="Qu'est ce que �/dev/cdrom�&nbsp;?",
    nr_lines = 2,
    tests = ( Good(Contain('')), ),
    )

add(name="haut",
    required = ['pratique'],
    question="Qu'est ce que fait la touche clavier �fl�che vers le haut� dans un terminal&nbsp;?",
    nr_lines = 2,
    tests = ( Good(Contain('')), ),
    )




add(name="point point",
    required = ['relatif', 'commande'],
    question="Que fait la commande �cd ..�&nbsp;?",
    nr_lines = 2,
    tests = ( Good(Contain('')), ),
    )








  
    
