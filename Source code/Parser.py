import xml.etree.ElementTree as ET
import os, os.path

class Parser:
    def __init__(self,path):
        self.file_list = file_list = os.popen("ls "+path).read().split("\n")
        self.data = []
        self.parse_data(path)

    def set_file(self,file):
        file_tree = ET.parse(file)
        file_data = file_tree.getroot()
        return file_data

    def change_path(self,path):
        self.file_list = file_list = os.popen("ls "+path).read().split("\n")
        self.data = []
        self.parse_data(path)

    def parse_data(self,path):
        for file in self.file_list:
            if(file != ""):
                file_data = self.set_file(path+file)
                self.data.append(file_data)
