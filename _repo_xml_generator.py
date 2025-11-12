#!/usr/bin/env python3
import os, hashlib, xml.etree.ElementTree as ET
from xml.dom import minidom

def prettify(e): return minidom.parseString(ET.tostring(e,'utf-8')).toprettyxml(indent="  ")

def generate(root_dir):
    addons = []
    for p, _, f in os.walk(root_dir):
        if 'addon.xml' in f:
            addons.append(ET.parse(os.path.join(p, 'addon.xml')).getroot())
    root = ET.Element('addons')
    for a in addons: root.append(a)
    xml = prettify(root)
    out = os.path.dirname(root_dir)
    open(os.path.join(out, 'addons.xml'), 'w', encoding='utf-8').write(xml)
    open(os.path.join(out, 'addons.xml.md5'), 'w').write(hashlib.md5(xml.encode()).hexdigest())

if __name__ == '__main__':
    import sys
    generate(sys.argv[1] if len(sys.argv)>1 else 'repo/omega/addons')
    print("Generated!")
