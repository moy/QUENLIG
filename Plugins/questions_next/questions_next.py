#!/usr/bin/env python3
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

"""Allow to go to the next question in alphabetical order."""

container = 'questions'
acls = { 'Author': ('executable',), 'Grader': ('executable',) }

def execute(state, plugin, argument):

    answerables = state.student.answerables_typed()

    a = [ i[0] for i in answerables ]

    try:
        plugin.link = answerables[a.index(state.question) + 1][0].url()
        return ''
    except:
        plugin.link = None
        return None




