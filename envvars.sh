#!/bin/bash
export SENDER_EMAIL='lucasrpi144@gmail.com'
export SENDER_PASSWORD='rwucmkcgdcdbxhgg'
export RECEIVER_EMAIL='lucagough7@gmail.com'
export NOTION_TOKEN='secret_BpkQqHT6LLgTWSmTTrOa7slrkScBR6xo13pCEEJsHjp'
export DATABASE_ID='5723db6fec26453e9ba04f9858845f6d'

cd /home/pi/Documents/PythonScripts/UniNotes/
./notionToMarkdown.py >> /tmp/notion_log 2>&1
