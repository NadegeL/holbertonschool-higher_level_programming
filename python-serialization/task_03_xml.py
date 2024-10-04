#!/usr/bin/python3

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize a dictionary to XML"""
    root = ET.Element('root')
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    tree = ET.ElementTree(root)
    tree.write(filename)
    return None

def deserialize_from_xml(filename):
    """Deserialize XML data from a file to a Python dictionary"""
    tree = ET.parse(filename)
    root = tree.getroot()
    dictionary = {}
    for child in root:
        dictionary[child.tag] = child.text
        
    return dictionary

if __name__ == '__main__':
    dictionary = {
        'name': 'John',
        'age': 23,
        'city': 'San Francisco'
    }
    filename = 'data.xml'
    serialize_to_xml(dictionary, filename)
    print(deserialize_from_xml(filename))
