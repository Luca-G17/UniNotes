from notion2md.exporter.block import MarkdownExporter
from grip import export
from notion_client import Client
import os
import time
import pypandoc
from anyascii import anyascii
from git import Repo
from datetime import datetime

# First get all block ids for pages inside the table
# Next export them all to ./{page_id}/ unzipped
# Then rename each one to its Title
# Export each one to to html

def linePrepender(filename, line):
    with open(filename, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(line.rstrip('\r\n') + '\n' + content)

def removeOldFiles(dir):
    if os.path.exists(dir):
        files = os.listdir(dir)
        for file in files:
            os.remove(os.path.join(dir, file))

def removeUnicodeChars(string):
    string = string.replace('≠', '!=')
    string = string.replace('≥', '>=') 
    string = string.replace('≤', '<=')
    return string

def downloadFile(page_id, output_path, module, title):
    print("Downloading " + module + "/" + title)
    markdown_exported = False
    while not markdown_exported:
        try:
            MarkdownExporter(block_id=page_id, output_path=output_path, download=True, unzipped=True).export()
            markdown_exported = True
        except:
            time.sleep(3)
    curr_filename = output_path + "/" + page_id + '.md'
    new_filename = output_path + "/" + title + '.md'
    os.rename(curr_filename, new_filename)
    return new_filename

def convertToPDF(output_filename, output_path, new_filename):
    pandoc_options = [
        "-t", "latex",
        "-f", "markdown-raw_tex",
        "-o", output_filename,
        "--resource-path=" + output_path,
        "--pdf-engine=pdflatex",
    ]
    try:
        pypandoc.convert_file(new_filename, "pdf", outputfile=output_filename, extra_args=pandoc_options)
    except Exception as e:
        print(e)
        print("Failed to convert " + new_filename)

def copyMarkdownFileAndWriteREADME(file):
    with open(file, "r") as f:
        s = f.read()
    split = file.split('/')
    split[len(split) - 1] = 'README.md'
    with open('/'.join(split), "w") as f:
        f.write(s)

def pushAllNotes():
    repo = Repo('./')
    repo.git.add('--all')
    now = datetime.now
    repo.index.commit('Automated Update - {}'.format(now))
    origin = repo.remotes[0]
    origin.push()

def downloadAndConvertAllNotes(database_id):
    notion = Client(auth=os.getenv("NOTION_TOKEN"))
    allPages = notion.databases.query(database_id)
    for result in allPages['results']:
        # Get page_id, module name and page title
        page_id = result['id']
        module = result['properties']['Class']['select']['name']
        title = result['properties']['Name']['title'][0]['plain_text']
        title = title.replace("/", "+")
        output_path = "./notes/" + module + "/" + title

        removeOldFiles(output_path)
        new_filename = downloadFile(page_id, output_path, module, title)
        linePrepender(new_filename, "# " + title)

        copyMarkdownFileAndWriteREADME(new_filename)
        with open(new_filename, "r") as f:
            s = f.read()

        with open(new_filename, 'w+') as f:
            f.write(removeUnicodeChars(s))

        output_filename = new_filename.replace(".md", ".pdf")
        convertToPDF(output_filename, output_path, new_filename)
        os.remove(new_filename)
        time.sleep(3)
    pushAllNotes()

database_id = "5723db6fec26453e9ba04f9858845f6d"
downloadAndConvertAllNotes(database_id)


