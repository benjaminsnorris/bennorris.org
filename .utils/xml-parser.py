import xml.etree.ElementTree as ET
import urllib.parse
import re

def parseXML(xmlfile, config):
    tree = ET.parse(xmlfile)
    root = tree.getroot()
    posts = []
    wp = '{http://wordpress.org/export/1.2/}'
    allTags = {}

    postType = 'all'
    if 'postType' in config:
        postType = config['postType']
    requireTag = False
    if 'requireTag' in config:
        requireTag = config['requireTag']

    for item in root.findall('./channel/item'):
        post = {}
        shouldInclude = True
        tags = ''
        excludeTags = ''
        if 'excludeTags' in config:
            excludeTags = config['excludeTags']
        removeTags = ''
        if 'removeTags' in config:
            removeTags = config['removeTags']

        for child in item:
            if child.tag == wp+'post_type' and child.text == 'attachment':
                shouldInclude = False
            elif child.tag == wp+'post_date':
                post['date'] = child.text+'-0000'
                post['filedate'] = child.text.split(' ')[0]
            elif child.tag == 'title' and child.text:
                post['title'] = child.text
            elif child.tag == '{http://purl.org/rss/1.0/modules/content/}encoded':
                if child.text:
                    post['content'] = child.text
            elif child.tag == 'category':
                tag = child.text.lower()
                allTags[tag] = True
                if tag in excludeTags:
                    shouldInclude = False
                elif tag not in removeTags:
                    if tags:
                        tags += ',' + tag
                    else:
                        tags = tag
        
        if postType != 'all':
            if 'title' in post:
                if postType != 'post':
                    shouldInclude = False
            elif postType != 'micro':
                shouldInclude = False

        if 'category' in config:
            if config['category'] == "Gospel Sketcher" or config['category'] == "Sketchnotable":
                if tags:
                    tags = "sketchnotes," + tags
                else:
                    tags = "sketchnotes"

        if tags:
            post['tags'] = tags
        elif requireTag:
            shouldInclude = False

        if shouldInclude:
            posts.append(post)

    # for tag in allTags:
    #     print(tag)

    return posts

def createPostFiles(posts, config):
    filenames = []
    for post in posts:
        filename = createPostFile(post, config)
        filenames.append(filename)
    return filenames
        
def createPostFile(post, config):
    filename = post['filedate'] + '-'
    frontmatter = '---\n'
    category = ''
    if 'category' in config:
        category = config['category']
    text = post['content']

    if 'title' in post:
        frontmatter += 'title: "' + post['title'] + '"\n'
        title = post['title'].lower()
        title = title.replace('’','')
        title = title.replace("'", '')
        title = re.sub('\A[^a-zA-Z]*|\W*\Z','',title)
        title = re.sub('[^a-z0-9]+','-',title)
        title = urllib.parse.quote(title)
        filename += title + '.md'
    else:
        title = post['date']
        title = re.sub('[^0-9]','',title)
        filename += title + '.md'
    frontmatter += 'date: ' + post['date'] + '\n'
    if 'tags' in post:
        frontmatter += 'tags:\n'
        tags = post['tags'].split(',')
        for tag in tags:
            frontmatter += '- ' + tag + '\n'
            if tag == 'mental health':
                category = 'Mental Work Health'
    if category:
        frontmatter += 'category: ' + category + '\n'
    if '<!--more-->' in text:
        frontmatter += 'excerpt_separator: "<!--more-->"\n'
    frontmatter += '---\n\n'

    text = frontmatter + text

    if 'dir' in config:
        dir = config['dir'] + "/"
        if 'title' in post:
            dir += "posts/"
        else:
            dir += "microposts/"
        filename = dir + filename

    file = open(filename,'w')
    file.write(text)
    file.close

    return filename

def main():
    # postTypes: post, micro, all
    config = {
        'postType':'all', 
        'category':'General', 
        'requireTag': False, 
        'dir': 'bennorris', 
        'excludeTags': 'books,movies',
        'removeTags': 'articles'
        }
    posts = parseXML('bennorris_wordpress.xml',  config)
    filenames = createPostFiles(posts,  config)
    for filename in filenames:
        print('created file=' + filename)
    print('\ncreated ' + str(len(filenames)) + ' files')

main()