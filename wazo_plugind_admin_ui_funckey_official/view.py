# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from flask_babel import lazy_gettext as l_

from wazo_admin_ui.helpers.classful import BaseView


class FuncKeyTemplateView(BaseView):

    resource_name = 'funckey_template'
    resource = l_('FuncKey')
