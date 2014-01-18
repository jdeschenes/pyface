#------------------------------------------------------------------------------
# Copyright (c) 2014, Enthought, Inc.
# All rights reserved.
#
# This software is provided without warranty under the terms of the BSD
# license included in enthought/LICENSE.txt and may be redistributed only
# under the conditions described in the aforementioned license.  The license
# is also available online at http://www.enthought.com/licenses/BSD.txt
# Thanks for using Enthought open source!
#
# Author: Enthought, Inc.
# Description: <Enthought pyface package component>
#------------------------------------------------------------------------------
""" A dialog that allows the user to chose a single item from a list. """

from __future__ import absolute_import

# Enthought library imports.
from traits.api import Any, Callable, List, Unicode

# local imports
from .i_dialog import IDialog, MDialog

class ISingleChoiceDialog(IDialog):
    """ A dialog that allows the user to chose a single item from a list. """

    #: a message to display to the user
    message = Unicode

    #: the list of choices presented to the user to choose from
    choices = List(Any)

    #: the choice that the user selected
    choice = Any

    #: a function that formats the choices as strings
    format_func = Callable(str)


class MSingleChoiceDialog(MDialog):
    """ The mixin class that contains common code for toolkit specific
    implementations of the ISingleChoiceDialog interface.
    """

    ###########################################################################
    # 'Private' interface.
    ###########################################################################

    def _get_text_choices(self):
        """ Returns the list of strings to display in the dialog. """
        choices = [self.format_func(obj) for obj in self.choices]
        return choices
