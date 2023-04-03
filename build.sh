#!/bin/bash

cd /home/pi/Documents/PythonScripts/UniNotes/
source ./envvars
./notionToMarkdown.py >> /tmp/notion_log 2>&1
