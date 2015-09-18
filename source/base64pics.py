"""
 * Base64 1.0.0
 * https://github.com/RobertoPrevato/Base64
 *
 * Copyright 2015, Roberto Prevato
 * http://ugrose.com
 *
 * Licensed under the MIT license:
 * http://www.opensource.org/licenses/MIT
"""
import argparse

separator = "******************************************************\n"

parser = argparse.ArgumentParser(description= 'Pictures to base64 encoded bulk converter.',
                                 epilog = "{}\n{}".format("author: Roberto Prevato roberto.prevato@gmail.com", separator))

parser.add_argument('-p', '--path', dest= 'path', required=True,
                    help='path to root folder from where to start the research of pictures files')

parser.add_argument('-m', '--mode', dest='mode', required=False, choices=['css', 'csv'],
                    help='whether to generate a csv file or a css file')

parser.add_argument('-f', '--filename', dest='filename', default="pics",
                    help='output file name and extension (default: "pics")')

args = parser.parse_args()

from lib import PicsHelper

def main(options):
    PicsHelper.generate_base64_file(options.path, options.filename, options.mode)

main(args)

