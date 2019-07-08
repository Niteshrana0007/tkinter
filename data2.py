import json
class DataHandler:
    def __init__(self,file_name):
        data_info = open(file_name,'r')
        self.data = json.load(data_info)
        #print(self.data)

    def get_categories(self):
        list_data = []
        for element in self.data["category_list"]:
            list_data.append(element['name'])
        return list_data

    def  get_data_for_category(self,name):
        list_data = []
        for element in self.data["category_list"]:
            if element["name"].lower() == name.lower():
                list_data = element["list"]
        return list_data
        
            


#new = DataHandler('data.json')
#print(new.get_categories())
