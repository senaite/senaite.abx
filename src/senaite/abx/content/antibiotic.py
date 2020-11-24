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
# Copyright 2020 by it's authors.
# Some rights reserved, see README and LICENSE.

from bika.lims.catalog import SETUP_CATALOG
from plone.dexterity.content import Item
from plone.supermodel import model
from senaite.abx import messageFactory as _
from zope import schema
from zope.interface import implementer


class IAntibiotic(model.Schema):
    """Antibiotic content interface
    """
    abbreviation = schema.TextLine(
        title=_(u"Abbreviation"),
        required=True,
    )

    antibiotic_class = schema.Choice(
        title=_(u"Antibiotic class"),
        vocabulary="senaite.abx.vocabularies.antibiotic_classes",
        required=False,
        missing_value=[],
    )


@implementer(IAntibiotic)
class Antibiotic(Item):
    """Antibiotic content
    """
    # Catalogs where this type will be catalogued
    _catalogs = [SETUP_CATALOG]
