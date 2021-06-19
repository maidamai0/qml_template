import argparse
import xml.etree.cElementTree as ET
from xml.dom import minidom
import os
import pathlib


parser = argparse.ArgumentParser(description="update qml resource")
parser.add_argument("suffix", nargs="*", action='append')
args = parser.parse_args()
extensions = args.suffix[0]

cur_dir = pathlib.Path(__file__).parent
print(
    f"updating {cur_dir}, ends with {extensions} are treated as resource files")

root = ET.Element('RCC')
attrib = {'prefix': '/'}
doc = ET.SubElement(root, 'qresource', attrib)

cur_dir_name = os.path.split(cur_dir)[1]
for root_dir, dirs, files in os.walk(cur_dir):
    for file in files:
        _, ext = os.path.splitext(file)
        if ext[1:] in extensions:
            elem = ET.SubElement(doc, 'file')
            sub_dir_name = os.path.split(root_dir)[1]
            if sub_dir_name == cur_dir_name:
                elem.text = file
            else:
                elem.text = f'{sub_dir_name}/{file}'

xmlstr = minidom.parseString(ET.tostring(
    root, 'utf-8')).toprettyxml(indent="    ").split('\n')[1:]
with open(f"{cur_dir}/qt_resource.qrc", "w") as f:
    for line in xmlstr:
        f.write(f'{line}\n')
