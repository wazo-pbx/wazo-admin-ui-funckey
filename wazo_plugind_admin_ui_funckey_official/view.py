# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from flask_babel import lazy_gettext as l_
from flask_menu.classy import classy_menu_item

from wazo_admin_ui.helpers.classful import BaseView

from .form import FuncKeyTemplateForm


class FuncKeyTemplateView(BaseView):

    resource_name = 'funckey_template'
    form = FuncKeyTemplateForm
    resource = l_('FuncKey')

    @classy_menu_item('.funckeys', l_('Function Keys Templates'), order=1, icon="th-list")
    def index(self):
        return super(FuncKeyTemplateView, self).index()
