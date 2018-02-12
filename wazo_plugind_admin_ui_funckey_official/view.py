# Copyright 2017-2018 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from flask import jsonify
from flask_babel import lazy_gettext as l_
from flask_menu.classy import classy_menu_item

from wazo_admin_ui.helpers.classful import BaseView, LoginRequiredView

from .form import FuncKeyTemplateForm


class FuncKeyTemplateView(BaseView):

    resource_name = 'funckey_template'
    form = FuncKeyTemplateForm
    resource = l_('FuncKey')

    @classy_menu_item('.funckeys', l_('Function Keys Templates'), order=1, icon="th-list")
    def index(self):
        return super().index()

    def _map_resources_to_form(self, resource):
        form = self.form(data=resource,
                         keys=self._build_keys(resource['keys']))
        return form

    def _build_keys(self, keys):
        result = []
        for digit, key in keys.items():
            key['digit'] = digit
            result.append(key)
        sorted_keys = sorted(result, key=lambda k: k['digit'])
        return sorted_keys

    def _map_form_to_resources(self, form, form_id=None):
        resource = super()._map_form_to_resources(form, form_id)
        self.service.update_funckeys(resource)

        return resource


class FunckeyDestinationView(LoginRequiredView):

    def list_json(self):
        funckeys_template = self.service.list()
        results = []
        for funckey_template in funckeys_template['items']:
            results.append({'id': funckey_template['id'], 'text': funckey_template['name']})

        return jsonify({'results': results})