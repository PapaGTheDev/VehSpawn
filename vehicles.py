import os
import re

def extract_model_name(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        match = re.search(r'<handlingName>(.*?)<\/handlingName>', content)
        if match:
            return match.group(1)
        else:
            return None

def process_folder(folder_path):
    vehicles = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('handling.meta'):
                file_path = os.path.join(root, file)
                model_name = extract_model_name(file_path)
                if model_name:
                    vehicles.append({
                        'model': model_name,
                        'name': 'changeme',
                        'brand': 'changeme',
                        'price': 12000,
                        'category': 'changeme',
                        'type': 'automobile',
                        'shop': 'changeme'
                    })
    return vehicles

def write_to_console(vehicles):
    for vehicle in vehicles:
        print(vehicle)

def main():
    folder_path = "Vehicles Folder"
    vehicles = process_folder(folder_path)
    write_to_console(vehicles)

main()
