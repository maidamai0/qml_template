import argparse
import xml.etree.cElementTree as ET
from xml.dom import minidom
import os

parser = argparse.ArgumentParser(description="update qml resource")
parser.add_argument("suffix", nargs="*", action='append')
args = parser.parse_args()
extensions = args.suffix[0]

print(
    f"updating {os.getcwd()}, ends with {extensions} are treated as resource files")

root = ET.Element('RCC')
attrib = {'prefix': '/'}
doc = ET.SubElement(root, 'qresource', attrib)

for _, _, files in os.walk(os.getcwd()):
    for file in files:
        _, ext = os.path.splitext(file)
        if ext[1:] in extensions:
            elem = ET.SubElement(doc, 'file')
            elem.text = file

xmlstr = minidom.parseString(ET.tostring(
    root, 'utf-8')).toprettyxml(indent="    ").split('\n')[1:]
with open("qt_resource.rc", "w") as f:
    for line in xmlstr:
        f.write(f'{line}\n')
