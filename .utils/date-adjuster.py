from datetime import datetime
import os
import re
import pytz

def adjustFiles(directory):
    for file in os.scandir(directory):
        if file.is_file():
            print(file.path)

def adjustFile(filename):
    file_read = open(filename, 'r')
    lines = file_read.readlines()
    file_name = file_read.name
    file_read.close()
    adjusted_date = datetime.now()
    is_adjusting_date = False
    date_regex = re.compile('(?P<year_month>\d{4}-\d{2}-)(?P<day>\d{2})\s(?P<hour>\d{2})(?P<minute_second>:\d{2}:\d{2})-0000')

    file_write = open(filename, 'w')
    for line in lines:
        if line.__contains__('date:'):
            search = date_regex.search(line)
            if search:
                if int(search.group('hour')) < 7:
                    is_adjusting_date = True
                    gmt_date = datetime.strptime(search.group(0), '%Y-%m-%d %H:%M:%S%z')
                    mtn = pytz.timezone('US/Mountain')
                    adjusted_date = gmt_date.astimezone(mtn)
                    new_date_string = adjusted_date.strftime('%Y-%m-%d %H:%M:%S%z')
                    adjusted_line = line.replace(search.group(0), new_date_string)
                    file_write.write(adjusted_line)
            if not is_adjusting_date:
                file_write.write(line)
        else:
            file_write.write(line)

    file_write.close()
    
    if is_adjusting_date:
        new_filename_date_string = adjusted_date.strftime('%Y-%m-%d')
        new_filename = re.sub('\d{4}-\d{2}-\d{2}', new_filename_date_string, file_name)
        os.rename(file_name, new_filename)

def main():
    directory = "_posts"
    adjustFiles(directory)
    # adjustFile('_posts/2020-05-05-star-wars-day.md')

main()
