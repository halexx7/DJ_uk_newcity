from xml.etree import ElementTree as ET

from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(name="cool_tel")
def cool_tel(np):
    """
    Create `+7 (982) 123-98-98`
    """
    phone = ET.Element("p")
    phone.text = f"+{np[:1]} ({np[1:4]}) {np[4:7]}-{np[7:9]}-{np[9:11]}"
    return mark_safe(ET.tostring(phone, encoding="unicode"))