#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2009 Marc Poulhiès
#
# chronodom
#
# Plopifier is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Plopifier is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Plopifier.  If not, see <http://www.gnu.org/licenses/>.

from distutils.core import setup
import py2exe
 
setup(
    name = 'chronodom',
    description = 'un chrono tout con',
    version = '1.0',
    windows = [{'script': 'chronodom.py'}
              ],
    options = {'py2exe': {'packages':'encodings',
                          'includes': 'cairo, pango, pangocairo, atk, gobject',
                          }
              },
    data_files=['chronodom.glade']
)
