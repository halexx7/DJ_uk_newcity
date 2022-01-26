from xml.etree import ElementTree as ET

from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(name="tel_to")
def tel_to(np):
    """
    Create link `tel:`
    """
    phone = ET.Element("a", {"href": f"tel:{np}"})
    phone.text = f"+{np[:1]} ({np[1:4]}) {np[4:7]}-{np[7:9]}-{np[9:11]}"
    return mark_safe(ET.tostring(phone, encoding="unicode"))
