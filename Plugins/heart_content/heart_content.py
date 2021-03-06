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

"""This plugin display the content of the first plugin with
an not empty attribute named 'heart_content'.
This allow plugins in the menu to display their content in the
heart of the page when clicked, for example the 'action_help' plugin.
"""

priority_display = 'title_bar'
priority_execute = '-top'
acls = { 'Wired': ('executable',) }

def execute(state, plugin, argument):

    for a_plugin in state.plugins_list:
        if a_plugin.heart_content:
            return '<DIV CLASS="%s">%s</DIV>' % ( a_plugin.plugin.css_name,
                                                  a_plugin.heart_content )

