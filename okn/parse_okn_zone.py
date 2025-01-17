import json
from main import write_json_objects_to_file


def parse_okn_zone():
    path_to_file_zone = ''
    with open(path_to_file_zone, encoding='utf-8') as f:
        all_objects = json.load(f)
        all_f = []
        for obj in all_objects:
            for coord in obj['geometry']['coordinates'][0]:
                coord[0], coord[1] = coord[1], coord[0]
            all_f.append(obj)
    write_json_objects_to_file(all_f, 'valid_zashit_zone.json')
