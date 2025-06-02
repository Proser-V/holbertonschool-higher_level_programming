#!/usr/bin/python3

"""
Description: A module that explore serialization and deserialization using XML
as an alternative format to JSON.
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    A function that serialize a dictionary into XML and save it to the
    given filename.
    """

    root = ET.Element("data")
    for key, value in dictionary.items():
        item = ET.SubElement(root, "item")
        key_elem = ET.SubElement(item, "key")
        key_elem.text = str(key)
        value_elem = ET.SubElement(item, "value")
        value_elem.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """
    A function that read the XML data from that file, and return a
    deserialized Python dictionary.
    """

    tree = ET.parse(filename)
    root = tree.getroot()
    my_dict = {}

    for item in root.findall("item"):
        key = item.find("key").text
        value = item.find("value").text
        my_dict[key] = value

    return my_dict
