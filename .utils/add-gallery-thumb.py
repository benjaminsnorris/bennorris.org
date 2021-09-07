import os
import re

def adjustFiles(directory):
    counter = 0
    for file in os.scandir(directory):
        if counter > 25:
            return
        if file.is_file():
            adjustFile(file)
            counter = counter + 1
    print('adjusted',counter,'files', sep=' ')

def adjustFile(file):
    if file.path.__contains__('.DS_Store'):
        return

    image_regex = re.compile('(https://media.bennorris.org/images/.+?\.(jpg|png|jpeg))')
    file_read = open(file, 'r', encoding='utf-8')
    file_name = file_read.name
    contents = file_read.read()
    search = image_regex.search(contents)
    file_read.close()

    # If the post does not contain an image, no need to continue
    if not search or not contents.__contains__('- sketchnotes'):
        return

    image_url = search.group(0)
    thumb = 'gallery_thumb: ' + image_url + '\n'
    adjusted_contents = re.sub('date:',thumb + 'date:',contents)

    file_write = open(file, 'w')
    file_write.write(adjusted_contents)
    file_write.close()

    print('added gallery thumbnail in '+file_name)

def main():
    directory = "_posts"
    adjustFiles(directory)
    # adjustFile('_posts/2019-04-07-general-conference-3-cook-sketchnote.md')
    # adjustFile('_posts/2021-08-11-linkedin-live-sketchnote.md')

main()
