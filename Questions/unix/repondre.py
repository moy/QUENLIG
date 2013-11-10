# -*- coding: latin-1 -*-
#    QUENLIG: Questionnaire en ligne (Online interactive tutorial)
#    Copyright (C) 2005-2006 Thierry EXCOFFIER, Universite Claude Bernard
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

add(name="bonjour",
    before="""<IMG SRC="Sunrise_over_the_sea.jpg" align="right">
    <p>
    Bonjour.
    <p>
    Pour r�pondre aux questions, c'est tr�s simple&nbsp;:
    vous tapez le texte de votre r�ponse dans le champ texte
    ci-dessous et vous tapez sur la touche qui s'appelle
    &lt;Return&gt;
    ou &lt;Enter&gt;
    ou &lt;Entr�e&gt;
    <p>
    Normalement, vous n'avez besoin de la souris que pour
    faire le copier/coller.
    En effet, s'il n'y a pas de r�ponse � donner,
    le lien sur la prochaine question est activ� (il a le <em>focus</em>)
    et il vous suffit de taper &lt;Return&gt;
    pour suivre le lien.""",
    question="R�pondez 'bonjour' � cette question.",
    tests=(
    good('bonjour'),
    good("'bonjour'",
     """Je vous accorde la r�ponse mais les apostrophes
     �taient l� uniquement pour s�parer le mot du reste de la phrase.
     """),
    good("Bonjour",
     """Je vous accorde la r�ponse, mais vous ne deviez
     pas mettre de majuscule.
     """),
    reject("echo", "Ce n'est pas une question Unix"),
    ),
    indices=(
    """Vous devez taper la r�ponse dans
    la zone de saisie qui normalement est blanche et qui est
    juste au dessus.""",
    ),
    good_answer="""La r�ponse attendue � toutes les questions
    que vous aurez � donner par la suite sera <b>la plus courte</b>.
    Les r�ponses qui ne sont pas minimales en nombre de caract�res
    seront refus�es.""",
    )

add(name="intro",
    required=["bonjour"],
    question="""Ces exercices ne sont pas not�s.
    N�anmoins, si vous trichez en utilisant une liste de bonnes r�ponses
    vous n'apprendrez rien du tout.
    <p>
    R�pondez OUI si vous avez compris.
    """,
    tests = (
    yes("""Alors appelez un enseignant pour qu'il vous explique."""),
    ),
    )


add(name="combien de titres",
    required=["intro"],
    question="""Combien y-a-t-il de titres de boites dans la colonne
    de gauche de cette page web&nbsp;?""",
    tests=(
    good("5"),
    bad("4", """N'oubliez pas de faire d�filer la fen�tre pour voir si
    vous n'en oubliez pas"""),
    require_int(),
    ),
    )


class check_nr_possible_questions(TestWithoutStrings):
    def test(self, student_answer, string, state=None):
        if state:
            return len(state.student.answerables()) == int(student_answer)


add(name="questions possibles",
    required=["intro"],
    question="""Combien y-a-t-il de questions diff�rentes
    dans la liste des questions que vous avez le droit
    de choisir maintenant (en comptant celle-ci)&nbsp;?""",
    tests=(
    require_int(),
    check_nr_possible_questions(),
    ),
    )

class check_nr_questions(TestWithoutStrings):
    def test(self, student_answer, string, state=None):
        if state:
            return len(questions) == int(student_answer)

add(name="questions en tout",
    required=["intro"],
    question="""Quel est le nombre total de questions
    qui sont pr�vues dans ce sujet de TP&nbsp;?""",
    tests=(
    require_int(),
    check_nr_questions(),
    ),
    indices=(
             "C'est indiqu� dans les statistiques",
             "C'est le nombre de questions en tout."
             ),
    )

class check_nr_items(TestWithoutStrings):
    def test(self, student_answer, string):
        import server
        nb = server.get_file("help.html").content.count('<li')
        nb2 = server.get_file("help.html").content.count('<li ')
        a = int(student_answer)
        if a == nb:
            return True
        if a == nb - nb2:
            return True, "Mais vous avez oubli� les puces de deuxi�me niveaux"
        return False, "Recomptez, vous vous �tes tromp�"

add(name="aide",
    required=["questions en tout"],
    before="Lisez la page d'aide/explication.",
    question="""Combien de puces (<em>item</em>) sont affich�es
    sur la page d'aide accessible dans le menu de gauche&nbsp;?""",
    tests=(
    require_int(),
    bad('0', """Une puce est un petit dessin � gauche d'un �l�ment
    d'une �num�ration"""),
    check_nr_items(),
    ),
    indices=("""La puce est le petit symbole que l'on trouve
    � gauche d'un paragraphe quand on fait une �num�ration""",
             ),
    good_answer = """Maintenant vous n'aurez pas le droit de dire
    que vous ne savez pas comment ce passe le TP'""",
    )

add(name="commentaire",
    required=["indices"],
    before="""Le cadre �Faites un commentaire� en bas � gauche permet de taper
    des commentaires � propos des questions pour am�liorer ce sujet
    de TP d'une fois sur l'autre&nbsp;:
    <ul>
    <li> L'�nonc� vous pose un probl�me (ambigu, fautes d'orthographe, ...)
    <li> Une r�ponse correcte est refus�e sans explication.
    <li> Les indices ne sont pas suffisants ou faux.
    <li> Il manque des pr�requis.
    <li> ...
    </ul>
    Apr�s avoir tap� un commentaire il faut cliquer
    sur le bouton pour l'envoyer.
    <p>
    <b>Tout</b> ce que vous faites
    est enregistr� afin que les enseignants puissent
    �valuer votre travail.
    """,
    question="""Combien de lignes de commentaires peut-on �crire
    dans la zone de commentaires sans que le texte tap�
    se d�cale vers le haut&nbsp;?
    La zone suivante contient 3 lignes&nbsp;:
    <pre>1
2
3</pre>

    """,
    tests=(
    good( ("10", "11", "12") ),
    require_int(),
    ),
    )

add(name="indices",
    required=["intro"],
    question="""Combien d'indices vous donne-t-on pour r�pondre
    � cette question&nbsp;?""",
    tests=(
    good("2"),
    bad("0", """Si on ne vous donnais pas d'indice pour r�pondre � la question,
    il n'y aurais pas de lien nomm�&nbsp;: �Donnez-moi un indice�"""),
    bad("1",
        """S'il n'y avait qu'un seul indice, le lien se serait nomm�.
        <p>
        <em>Donnez-moi l'indice</em>
        <p>
        Et non :
        <p>
        <em>Donnez-moi un indice</em>
        """),
    require_int(),
    ),
    indices=("Je suis le premier indice",
             "Je suis le deuxi�me indice"),
    )

add(name="humour",
    required=["indices"],
    question="Quelle est la r�ponse � cette question&nbsp;?",
    tests=(
    good("42"),
    bad("humour", "Tr�s astucieux, f�licitation. Mais ce n'est pas �a."),
    require_int(),
    comment("Vous ne pouvez pas r�pondre � la question sans regarder l'indice"),
    ),
    indices=("La r�ponse � cette question est <tt>42</tt>", ),
    )

add(name="meta",
    required=["humour"],
    question="<tt>Quel</tt> est la r�ponse � cette question.",
    tests=(
    good("Quel"),
    good("quel", "Accept�, mais c'�tait avec une majuscule"),
    reject("meta", "Lisez les indices."),
    ),
    indices=(
    """Lisez bien la phrase en s�parant les mots qui font partie
    de la phrase de ceux qui sont le sujet de la phrase.
    <p>
    A ne pas lire pendant la s�ance de TP : <A HREF='http://www.abbottandcostello.net/who.htm'>Who's On First</A>""",
    """Avez-vous remarqu� que les mots de la phrase
    ne sont pas tous dans la m�me fonte&nbsp;?""",
    """La question n'a pas de point d'interrogation, ce n'est
    donc pas une question, mais une r�ponse :-)""",
             ),
    good_answer = """Vous comprenez maintenant qu'il faut faire attention
    � tous les d�tails quand on lit une documentation ou bien
    les questions qui vous sont pos�es.""",
    )


class check_nr_good_answers(TestWithoutStrings):
    def test(self, student_answer, string, state=None):
        if state:
            try:
               return state.student.number_of_good_answers()== int(student_answer)
            except ValueError:
               return False

add(name="r�pondre",
    required=["combien de titres", "questions possibles", "questions en tout",
              "commentaire"],
    before="""Vous savez maintenant utiliser ce programme pour
    r�pondre aux questions.""",
    question="""A combien de questions avez vous r�pondu correctement
    sans compter celle-ci&nbsp;?""",
    tests=(
    check_nr_good_answers(),
    require_int(),
    ),
    )
