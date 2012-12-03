Summary
===
apkjet is a python wrap of the apktool to make it easier to do apk reverse engineering in a automated way.

usage
===
$ apkjet.py -h
Usage: apkjet.py [options] args

Options:
  -h, --help            show this help message and exit
  -d decode, --decompress=decode
                        decompress apk file
  -b build, --build=build
                        build apk file
  -s sign, --sign=sign  sign apk file
  -r bsign, --bulid_sign=bsign
                        build and sign apk file



Examples:
===
  python apkjet.py -d mitbbs.apk  # decompress apk file
  python apkjet.py -b mitbbs.apk  # build apk file
  python apkjet.py -s mitbbs.apk  # sign apk file


