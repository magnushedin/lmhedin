import json

dict_notes = dict()

with open('../db_files/notes.json') as f:
    json_notes = json.load(f)

with open('../db_files/pictures.json') as f:
    json_pictures = json.load(f)

json_new_pictures = json_pictures

for note in json_notes[2]['data']:
    try:
        dict_notes[note['id']]
    except:
        dict_notes[note['id']] = dict()
    finally:
        dict_notes[note['id']] = note['date']

# Debug
# for note in dict_notes:
#     print("id: {}, date: {}".format((note), dict_notes[note]))

for pic in json_new_pictures[2]['data']:
    # Debug print("pic noteid: {}, date from note: {}".format(pic['noteid'], dict_notes[pic['noteid']]))
    pic['name_date'] = dict_notes[pic['noteid']]

fh_new_pictures = open('../db_files/pictures_with_notename.json', 'w')
fh_new_pictures.write(json.dumps(json_new_pictures, indent=4))
fh_new_pictures.close()
