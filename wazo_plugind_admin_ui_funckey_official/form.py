# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from flask_babel import lazy_gettext as l_
from wtforms.fields import (SubmitField,
                            StringField)
from wtforms.validators import InputRequired, Length

from wazo_admin_ui.helpers.form import BaseForm


class FuncKeyTemplateForm(BaseForm):
    name = StringField(l_('Name'), [InputRequired(), Length(max=128)])
    keys = StringField()
    submit = SubmitField()
