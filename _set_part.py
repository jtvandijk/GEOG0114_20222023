# libraries
# conda env: html
import pandas as pd
import os
import glob

# placeholder
html_files = []

# get html files
files = glob.glob('docs/*')
for f in files:
    if os.path.basename(f).endswith('.html'):
        html_files.append(f)

# loop html files
for htmlf in html_files:

    # initialise template
    with open(htmlf) as file :
      html_content = file.read()

    # update TOC
    html_content = html_content.replace('<li class="chapter" data-level="" data-path="index.html"><a href="index.html"><i class="fa fa-check"></i>Module Overview</a></li>', \
                                        '<li class="part"><span><b>Module Overview</b></span></li>')

    # update back and forth buttons

    # write
    with open(htmlf, 'w') as file:
        file.write(html_content)
