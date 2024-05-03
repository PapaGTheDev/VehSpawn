import os
import xml.etree.ElementTree as ET

def extract_vehicle_info(file_path):
    vehicle_info = {}
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        for handling_node in root.findall('.//handlingName'):
            model_name = handling_node.text.strip()
            vehicle_info[model_name] = {
                'coords': f'vector4(0.0, 0.0, 0.0, 0.0)',
                'defaultVehicle': model_name,
                'chosenVehicle': model_name
            }
    except Exception as e:
        print(f"Error processing file {file_path}: {e}")
    return vehicle_info

def search_and_process_directories(root_dir):
    vehicle_info = {}
    for root, _, files in os.walk(root_dir):
        for file_name in files:
            if file_name == 'handling.meta':
                file_path = os.path.join(root, file_name)
                vehicle_info.update(extract_vehicle_info(file_path))
    return vehicle_info

def write_config_file(vehicle_info, output_file):
    with open(output_file, 'w') as f:
        f.write("Config = {\n")
        f.write("    ['Shop'] = {\n")
        f.write("        ['Job'] = 'none',\n")
        f.write("        ['ShopLabel'] = 'Premium Deluxe Motorsport',\n")
        f.write("        ['showBlip'] = true,\n")
        f.write("        ['blipSprite'] = 326,\n")
        f.write("        ['blipColor'] = 3,\n")
        f.write("        ['TestDriveTimeLimit'] = 0.5,\n")
        f.write("        ['Location'] = vector3(-45.67, -1098.34, 26.42),\n")
        f.write("        ['ReturnLocation'] = vector3(-44.74, -1082.58, 26.68),\n")
        f.write("        ['VehicleSpawn'] = vector4(-56.79, -1109.85, 26.43, 71.5),\n")
        f.write("        ['TestDriveSpawn'] = vector4(-56.79, -1109.85, 26.43, 71.5),\n")
        f.write("        ['FinanceZone'] = vector3(-29.53, -1103.67, 26.42),\n")
        f.write("        ['ShowroomVehicles'] = {\n")
        for idx, (model_name, info) in enumerate(vehicle_info.items(), start=1):
            f.write(f"            [{idx}] = {{\n")
            f.write(f"                ['coords'] = vector4(0.0, 0.0, 0.0, 0.0),\n")
            f.write(f"                ['defaultVehicle'] = '{model_name}',\n")
            f.write(f"                ['chosenVehicle'] = '{model_name}',\n")
            f.write("            },\n")
        f.write("        },\n")
        f.write("    },\n")
        f.write("}\n")

if __name__ == "__main__":
    root_dir = "vehicledirectory"
    output_file = "config.lua"
    vehicle_info = search_and_process_directories(root_dir)
    write_config_file(vehicle_info, output_file)
    print(f"Config file '{output_file}' has been created.")
