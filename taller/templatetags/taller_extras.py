from django import template
# from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(name="add_class")
def add_class(field, class_name):
    return field.as_widget(attrs={
        "class": " ".join((field.css_classes(), class_name))
    })
