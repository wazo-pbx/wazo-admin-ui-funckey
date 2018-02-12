# Copyright 2017-2018 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from flask_babel import lazy_gettext as l_
from flask_menu.classy import register_flaskview

from wazo_admin_ui.helpers.plugin import create_blueprint
from wazo_admin_ui.helpers.funckey import register_funckey_destination_form
from wazo_admin_ui.helpers.destination import register_listing_url

from .form import (
    CustomFuncKeyDestination,
    ForwardServicesFuncKeyDestinationForm,
    GeneralServicesFuncKeyDestinationForm,
    OnlineRecFuncKeyDestinationForm,
    TransferServicesFuncKeyDestinationForm,
)
from .service import FuncKeyTemplateService
from .view import FuncKeyTemplateView, FunckeyDestinationView


funckey = create_blueprint('funckey', __name__)


class Plugin(object):

    def load(self, dependencies):
        core = dependencies['flask']

        FuncKeyTemplateView.service = FuncKeyTemplateService()
        FuncKeyTemplateView.register(funckey, route_base='/funckeys')
        register_flaskview(funckey, FuncKeyTemplateView)

        register_funckey_destination_form('custom', l_('Custom'), CustomFuncKeyDestination)
        register_funckey_destination_form('transfer', l_('Transfer'), TransferServicesFuncKeyDestinationForm)
        register_funckey_destination_form('service', l_('Service'), GeneralServicesFuncKeyDestinationForm)
        register_funckey_destination_form('forward', l_('Forward'), ForwardServicesFuncKeyDestinationForm)
        register_funckey_destination_form('onlinerec', l_('Online Recording'), OnlineRecFuncKeyDestinationForm)

        FunckeyDestinationView.service = FuncKeyTemplateService()
        FunckeyDestinationView.register(funckey, route_base='/funckey_listing')

        register_listing_url('funckey_template', 'funckey.FunckeyDestinationView:list_json')

        core.register_blueprint(funckey)
