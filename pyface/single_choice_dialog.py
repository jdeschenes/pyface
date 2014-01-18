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
""" Single choice dialog. """

from __future__ import absolute_import

# Convenience functions.
def single_choice(parent, choices, message, title):
    """ Convenience function to show an information message dialog. """

    dialog = SingleChoiceDialog(
        parent=parent, choices=choices, message=message, title=title,
    )
    dialog.open()

    return dialog.choice

# Import the toolkit specific version.
from .toolkit import toolkit_object
SingleChoiceDialog = toolkit_object('single_choice_dialog:SingleChoiceDialog')

#### EOF ######################################################################
