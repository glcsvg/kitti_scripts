import xml.etree.ElementTree as ET
import os

base_xml_dir = "/home/dell/Desktop/new_dataset/"
xml_list = os.listdir(base_xml_dir)
kitti_saved_dir = "/home/dell/Desktop/new_dataset/kitti/"


def convert_annotation(file_name):

    print(base_xml_dir,file_name)
    in_file = open(base_xml_dir + file_name)

    tree = ET.parse(in_file)
    root = tree.getroot()

    with open(kitti_saved_dir + file_name[:-4] + '.txt', 'w') as f:
        for obj in root.iter('object'):
            #cls = obj.find('name').text
            xmlbox = obj.find('bndbox')
            """
                4 numbers from 5 to 8: the 2-dimensional bounding box of the object
                xmin，ymin，xmax，ymax
            """
            xmin, ymin, xmax, ymax = xmlbox.find('xmin').text, xmlbox.find('ymin').text, \
                                    xmlbox.find('xmax').text, xmlbox.find('ymax').text
            f.write('head' + " " + '0.00' + " " + '0' + " " + '0.00' + " " + str(xmin) + '.00' + " "
                    + str(ymin) + '.00' + " " + str(xmax) + '.00' + " " + str(ymax) + '.00' + " " +
                    '0.00' + " " + '0.00' + " " + '0.00' + " " + '0.00' + " " + '0.00' + " " + '0.00' + " " + '0.00' + '\n')


for i in xml_list:
    convert_annotation(i)
    print("...........")

print("Finished")