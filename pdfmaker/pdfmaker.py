#!/usr/bin/python3

from jinja2 import Template
import argparse
import jinja2
import json
import os
import subprocess
import sys

parser = argparse.ArgumentParser(description='Generate a pdf from json passed to stdin.')
parser.add_argument('posargs', metavar='posargs', type=str, nargs='+',
                    help='[job name, output directory]. job name will be the name of the generated pdf.')
parser.add_argument('infile', metavar='json stdin', nargs='?', type=argparse.FileType('r'),
					default=sys.stdin, help="json file passed to stdin via <")
args = parser.parse_args()

JOB_NAME=args.posargs[0]
OUTPUT_DIR=args.posargs[1]

TEMPLATE_DIR = "/home/melvyn/Desktop/MathTestMakerLibrary/pdfmaker"
TEMPLATE = "test-template001.tex"

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
	loader = jinja2.FileSystemLoader(TEMPLATE_DIR)
)

template = latex_jinja_env.get_template(TEMPLATE)
test_data = json.loads(sys.stdin.read())
tex_data = template.render(test_data)
with open(JOB_NAME+".tex", "w") as fout:
	fout.write(tex_data)

subprocess.run(["pdflatex", "-output-directory=" + OUTPUT_DIR, JOB_NAME + ".tex"])
