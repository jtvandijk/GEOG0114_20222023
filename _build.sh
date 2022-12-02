#!/bin/sh

# option
set -ev

# render gitbook
Rscript -e "bookdown::render_book('index.Rmd', 'bookdown::gitbook')"

# pretty fix HTML
source activate html
python _set_part.py
