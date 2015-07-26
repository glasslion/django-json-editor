# -*- coding: utf-8 -*-
from django.forms import widgets
from django.forms.utils import flatatt
from django.template.loader import render_to_string
from django.utils.html import format_html
from django.utils.encoding import force_text
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string


class JSONEditorWidget(widgets.Widget):

    @property
    def media(self):
        return widgets.Media(
            css={
                'all': ('djjsoneditor/jsoneditor.min.css',)
            },
            js=['djjsoneditor/jsoneditor.min.js']
        )

    def render(self, name, value, attrs=None):
        u"""Render the JSON editor"""

        kws = {}
        kws['data_input_id'] = 'id_%s' % name
        kws['data_input_attrs'] = flatatt(self.build_attrs(attrs, name=name))
        kws['json_value'] = value
        kws['editor_div_id'] = 'jsoneditor_id_%s' % name

        return mark_safe(render_to_string('djjsoneditor/editor_widget.html', kws))

