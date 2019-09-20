import json


def sortDict(val):
    return val['date']

pictures = dict()

with open('../db_files/notes.json') as f:
    data = json.load(f)

with open('../db_files/pictures.json') as f:
    json_pictures = json.load(f)

for pic in json_pictures[2]['data']:
    try:
        pictures[pic['noteid']]
    except:
        pictures[pic['noteid']] = dict()
    finally:
        pictures[pic['noteid']][pic['id']] = pic['name']


fw = open('../generated/index.html', 'w')

fw.write('''
<!doctype html>
<html>
<head>
<meta charset="utf-8"><html>
<meta name="description" lang="en" content="Lightbox is a script used to overlay images on the current page. It's a snap to setup and works on all modern browsers."/>
<meta name="author" content="Lokesh Dhakar">
<meta name="viewport" content="width=device-width, initial-scale=1">

<link rel="shortcut icon" href="lightbox/img/demopage/favicon.png">
<link rel="stylesheet" href="http://fonts.googleapis.com/css?family=Karla%7CMontserrat">
<link rel="stylesheet" href="lightbox/css/screen.css">
<link rel="stylesheet" href="lightbox/css/lightbox.css">
<title>lmhedin</title>
</head>
<body>
<center><h3>Linda och Magnus Hedin, renovering av huset</h3></center>

''')

notes = data[2]['data']

notes.sort(key=sortDict, reverse=True)

for note in notes:
    if note['note'] or note['head'] or note['date']:
        string_to_write = "<p>{}, {}</p><br>\n<p>{}</p><br>\n".format(note['date'], note['head'].encode('utf-8'), note['note'].encode('ascii', 'ignore').decode('ascii'))
        #string_to_write = "{}".format(note['head'].encode('ascii', 'ignore').decode('ascii'))
        fw.write("<section id = \"examples\" class = \"examples-section\" > <div class = \"container\" > <div class = \"image-row\" > <div class = \"image-set\" >\n")
        fw.write(string_to_write)
        try:
            pictures[note['id']]
        except:
            pass
        else:
            for key in pictures[note['id']]:
                img_name = pictures[note['id']][key]
                # fw.write("picture: {}, {}<br>".format(key, img_name))
                # fw.write("<img src=\"./pictures/{}\" alt=\"{}\" width=\"42\">\n".format(img_name, "img_name"))
                fw.write(
                    "<a class=\"example-image-link\" href=\"./pictures/{}\" data-lightbox=\"lightbox[1]\"><img class=\"example-image\" src=\"./pictures/{}\"></a>\n".format(img_name, img_name))
        finally:
            fw.write("</div></div></div></section>\n\n")


    # print(string_to_write)


fw.write('''
</body>
</html>
''')
fw.write('''
<script src="lightbox/js/jquery-1.11.0.min.js"></script>
<script src="lightbox/js/lightbox.js"></script>

<script>
var _gaq = _gaq || [];
_gaq.push(['_setAccount', 'UA-2196019-1']);
_gaq.push(['_trackPageview']);

(function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
})();
</script>
''')
fw.close()
