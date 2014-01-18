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

# Major package imports.
from pyface.qt import QtCore, QtGui

# Enthought library imports.
from traits.api import Any, Callable, List, Property, Str, Unicode, provides

# Local imports.
from pyface.i_single_choice_dialog import ISingleChoiceDialog, MSingleChoiceDialog
from .dialog import Dialog


@provides(ISingleChoiceDialog)
class SingleChoiceDialog(MSingleChoiceDialog, Dialog):
    """ A dialog that allows the user to chose a single item from a list."""

    #: a message to display to the user
    message = Unicode

    #: the list of choices presented to the user to choose from
    choices = List(Any)

    #: the choice that the user selected
    choice = Any

    #: a function that formats the choices as strings
    format_func = Callable(str)

    #: an attribute to use on each choice to get the text (for backwards compatibility)
    name_attribute = Str

    #: the message (for backwards compatibility)
    caption = Property(Str, depends_on='message')

    ###########################################################################
    # 'Window' interface.
    ###########################################################################

    def close(self):
        """ Closes the window. """

        # Get the chosen object.
        if self.control is not None:
            choice_index = self._get_text_choices().index(self.control.textValue())
            self.choice = self.choices[choice_index]

        # Let the window close as normal.
        super(SingleChoiceDialog, self).close()

        return

    ###########################################################################
    # Protected 'Window' interface.
    ###########################################################################

    def _create_control(self, parent):
        """ Create the toolkit-specific control that represents the window. """

        dialog = QtGui.QInputDialog(parent)
        dialog.setWindowTitle(self.title)
        dialog.setLabelText(self.message)
        dialog.setComboBoxItems(self._get_text_choices())
        dialog.setModal(self.style == "modal")
        # for compatibility with appearance of Wx version
        dialog.setOption(QtGui.QInputDialog.UseListViewForComboBoxItems)

        return dialog

    def _create_contents(self, parent):
        """ Creates the window contents. """

        # In this case, wx does it all for us in 'wx.SingleChoiceDialog'
        pass

    # Traits handlers #########################################################

    def _get_caption(self):
        return self.message

    def _set_caption(self, value):
        self.message = value

    def _name_attribute_changed(self, new):
        if new != '':
            self.format_func = lambda obj: getattr(obj, new, str(obj))
        else:
            self.format_func = str

#### EOF ######################################################################
