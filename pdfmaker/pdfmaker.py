#!/usr/bin/python3

import sys
import jinja2
import os
from jinja2 import Template
import json
import subprocess

templateDir = "/home/melvyn/Desktop/MathTestMakerLibrary/pdfmaker"
OUTPUT_DIR="/tmp"
JOB_NAME=sys.argv[1]

latex_jinja_env = jinja2.Environment(
	block_start_string = '\BLOCK{',
	block_end_string = '}',
	variable_start_string = '\VAR{',
	variable_end_string = '}',
	comment_start_string = '\#{',
	comment_end_string = '}',
	line_statement_prefix = '%%',
	line_comment_prefix = '%#',
	trim_blocks = True,
	autoescape = False,
	loader = jinja2.FileSystemLoader(templateDir)
)
template = latex_jinja_env.get_template('test-template001.tex')
test_data = json.loads(sys.stdin.read())
tex_data = template.render(test_data)
with open(JOB_NAME+".tex", "w") as fout:
	fout.write(tex_data)
subprocess.run(["pdflatex", "-output-directory=" + OUTPUT_DIR, JOB_NAME + ".tex"])
