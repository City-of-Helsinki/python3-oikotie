from lxml import etree

from django_oikotie.xml_models import XMLModel


def obj_to_xml_str(obj: XMLModel) -> str:
    root = obj.to_etree()
    xml = etree.tostring(root, encoding="utf-8", pretty_print=True)
    return xml.decode("utf-8")
