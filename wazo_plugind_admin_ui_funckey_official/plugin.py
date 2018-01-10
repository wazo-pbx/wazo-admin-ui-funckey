# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from flask_babel import lazy_gettext as l_
from flask_menu.classy import register_flaskview

from wazo_admin_ui.helpers.funckey import register_funckey_destination_form
from wazo_admin_ui.helpers.plugin import create_blueprint

from .service import FuncKeyTemplateService
from .view import FuncKeyTemplateView
from .form import CustomFuncKeyDestination

funckey = create_blueprint('funckey', __name__)


class Plugin(object):

    def load(self, dependencies):
        core = dependencies['flask']

        FuncKeyTemplateView.service = FuncKeyTemplateService()
        FuncKeyTemplateView.register(funckey, route_base='/funckeys')
        register_flaskview(funckey, FuncKeyTemplateView)

        register_funckey_destination_form('custom', l_('Custom'), CustomFuncKeyDestination)

        core.register_blueprint(funckey)
