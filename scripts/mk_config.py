# mk_config.py
#
# Translate default FF.CFG into a C header.
# 
# Written & released by Keir Fraser <keir.xen@gmail.com>
# 
# This is free and unencumbered software released into the public domain.
# See the file COPYING for more details, or visit <http://unlicense.org>.

import re, sys

def main(argv):
    in_f = open(argv[1], "r")
    out_f = open(argv[2], "w")
    out_f.write("/* Autogenerated by " + argv[0] + " */\n")
    for line in in_f:
        match = re.match("[ \t]*([A-Za-z0-9-]+)[ \t]*=[ \t]*"
                         "([A-Za-z0-9-]+|\".*\")", line)
        if match:
            opt = match.group(1)            
            val = match.group(2)
            if opt == "interface":
                val = "FINTF_" + val.upper()
            elif opt == "oled-font":
                val = "FONT_" + val
            elif opt == "image-on-startup":
                val = "IMGS_" + val
            elif opt == "twobutton-action":
                val = "TWOBUTTON_" + val
            else:
                val = {
                    'no': 'FALSE',
                    'yes': 'TRUE'
                }.get(val,val)
            out_f.write("x(%s, %s, %s)\n" % (opt, re.sub('-','_',opt), val))

if __name__ == "__main__":
    main(sys.argv)
