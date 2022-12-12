#!/bin/sh

cat article_content.txt | ./mapper.py | ./reducer.py | sudo cat > keyword_count.txt 
