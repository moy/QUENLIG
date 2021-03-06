#!/usr/bin/env python3
# -*- coding: latin-1 -*-
#    QUENLIG: Questionnaire en ligne (Online interactive tutorial)
#    Copyright (C) 2012 Thierry EXCOFFIER, Universite Claude Bernard
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

"""Display the question graph with statistics for this session.
"""

container = 'action'
link_to_self = True
acls = { 'Teacher': ('executable',), 'Author': ('executable',), }
priority_execute = '-question_source'

from QUENLIG import statistics
from QUENLIG import server

server.do_not_cache.add('xxx_graphe.svg')
server.do_not_cache.add('xxx_graphe.png')

def execute(state, plugin, argument):
    if argument:
        statistics.graph_dot_minimal(True)
        try:
            plugin.heart_content = server.get_file('xxx_graphe.svg').content.decode("utf-8")
        except:
            plugin.heart_content = ""
        state.question = None
    return ''


    




    

