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
                allTags[child.text] = True
                if tags:
                    tags += ',' + child.text.lower()
                else:
                    tags = child.text.lower()
        
        if postType != 'all':
            if 'title' in post:
                if postType != 'post':
                    shouldInclude = False
            elif postType != 'micro':
                shouldInclude = False

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
    for post in posts:
        createPostFile(post, config)
        
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
        filename = config['dir'] + "/" + filename

    print(filename)
    file = open(filename,'w')
    file.write(text)
    file.close

def main():
    # postTypes: post, micro, all
    config = {'postType':'post', 'category':'General', 'requireTag': False, 'dir': 'posts'}
    posts = parseXML('bennorris_wordpress.xml',  config)
    createPostFiles(posts,  config)

main()