#!/usr/bin/env python
# -*- coding: latin-1 -*-
#    QUENLIG: Questionnaire en ligne (Online interactive tutorial)
#    Copyright (C) 2015 Thierry EXCOFFIER, Universite Claude Bernard
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
#    Contact: Thierry.EXCOFFIER@univ-lyon1.fr

"""Display all the questions definition."""

import statistics
import questions

container = 'action'
link_to_self = True
priority_execute = '-question_source'
acls = { 'Default': ('executable',), }
css_attributes = ('TABLE { border: 1px solid black ; }',
                  )

def execute(state, plugin, argument):
    if not argument:
        return ''
        
    s = []
    for question in questions.sorted_questions:
        if not question.courses:
            continue
        q = question.before(state)
        if q == '':
            continue
        s.append('<hr><b><a href="%s">%s</a></b><p>%s' % (question.url(),
                                                          question.name, q))

    plugin.heart_content = '\n'.join(s)
    state.question = None
    return ''