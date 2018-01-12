# Copyright 2017-2018 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from wazo_admin_ui.helpers.service import BaseConfdService
from wazo_admin_ui.helpers.confd import confd


class FuncKeyTemplateService(BaseConfdService):
    resource_confd = 'funckeys'

    def update(self, resource):
        # PUT method for funckey_template is not implemented yet
        pass

    def get_destinations_list(self):
        return confd.funckeys_destinations.get()

    def list_funckeys(self, funckey):
        return confd.funckeys.get(funckey)

    def update_funckeys(self, resource):
        if 'id' in resource:
            template_id = resource['id']

            existing_funckeys = confd.funckeys.get(template_id)['keys']
            for digit, key in existing_funckeys.items():
                confd.funckeys.delete_template_funckey(template_id, digit)

            for key in resource['keys']:
                confd.funckeys.update_template_funckey(template_id, key['digit'], key)
        else:
            resource['keys'] = {}