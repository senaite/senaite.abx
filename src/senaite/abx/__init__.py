# -*- coding: utf-8 -*-
#
# This file is part of SENAITE.ABX.
#
# SENAITE.ABX is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation, version 2.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc., 51
# Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# Copyright 2020-2025 by it's authors.
# Some rights reserved, see README and LICENSE.

import logging

from zope.i18nmessageid import MessageFactory

PRODUCT_NAME = "senaite.abx"
PROFILE_ID = "profile-{}:default".format(PRODUCT_NAME)

messageFactory = MessageFactory(PRODUCT_NAME)
logger = logging.getLogger(PRODUCT_NAME)


def initialize(context):
    """Initializer called when used as a Zope 2 product
    """
    logger.info("*** Initializing SENAITE ABX Customization package ***")
