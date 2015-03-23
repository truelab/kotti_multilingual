import colander
from kotti_multilingual.api import get_source


def i10n_widget_factory(widget_class, **kwargs):
    """ Deferred widget. Turns field into readonly mode
        if the context is a translation.

        Obviously this widget makes sense only on edit forms.
    """
    @colander.deferred
    def deferred_widget(node, kw):
        widget = widget_class(**kwargs)
        request = kw['request']
        context = request.context
        if get_source(context) is not None:
            widget.readonly = True
        return widget
    return deferred_widget
