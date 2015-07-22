# -*- coding: utf-8 -*-
from django.forms import widgets
from django.forms.utils import flatatt
from django.utils.html import format_html
from django.utils.safestring import mark_safe


WIDGET_="""
<div {}>
</div>
"""
class JSONEditorWidget(widgets.Widget):
    input_type = 'hidden'

    @property
    def media(self):
        return widgets.Media(
            css={
                'all': ('djjsonfieldeditor/jsoneditor.min.css',)
            },
            js=['djjsonfieldeditor/jsoneditor.min.js']
        )

    def render(self, name, value, attrs=None):
        u"""Render CodeMirrorTextarea"""
        final_attrs = self.build_attrs(attrs, name=name)

        output = [
            format_html('<div{}></div>', flatatt(final_attrs)),
            '<script type="text/javascript">new JSONEditor(document.getElementById(%s));</script>' % (
                '"id_%s"' % name,
            )
        ]
        return mark_safe('\n'.join(output))

