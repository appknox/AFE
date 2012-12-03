#!/bin/env python

import sys, os
from optparse import OptionParser

#ApkToolPath = os.path.dirname(os.path.abspath(__file__))
ApkToolPath = 'c:\\\\android\\\\apkjet'


def sign_apk(fn, fn_new):
    if not fn_new:
        file_path, ext = os.path.splitext(fn)
        fn_new = r'%s_signed%s' %(file_path, ext)
    cmd = '''java -Xmx80m -jar %s/signapk.jar -w %s/testkey.x509.pem %s/testkey.pk8 %s %s''' % (
        ApkToolPath, ApkToolPath, ApkToolPath, fn, fn_new)
    print cmd
    os.system(cmd)
    print 'done!!! ... %s' % fn_new

def dec_apk(fn, path_new):
    if not path_new: 
        file_path, ext = os.path.splitext(fn)
        path_new = file_path.split('/')[-1] 
    cmd = '''java -Xmx80m -jar %s/apktool.jar d %s %s''' %(ApkToolPath, fn, path_new )
    print cmd
    os.system(cmd)
    print 'done!!! ... dir %s' %(path_new)

def bld_apk(file_path, fn_new):
    if not fn_new:
        fn_new = file_path.split('/')[-1]  + '.apk'
    cmd = '''java -Xmx80m -jar %s/apktool.jar b %s %s''' % (ApkToolPath, file_path, fn_new)
    os.system(cmd)
    print 'done!!! ... new apk file %s' %(fn_new)

def bsign_apk(file_path, fn_sign):
    if not fn_sign:
        path_new = file_path.split('/')[-1]
        fn_nosign = path_new  + '.apk'
        fn_sign = path_new + '_sign.apk'
    else:
        file_path, ext = os.path.splitext(fn)
        fn_nosign = file_path + '_nosign.apk'
    bld_apk(file_path, fn_nosign)
    print 'done!!! ... new apk before sign file %s' %(fn_nosign)
    sign_apk(fn_nosign, fn_sign)
    print 'done!!! ... new apk signed file %s' %(fn_sign)


def main():
    usage = "usage: %prog [options] args"
    parser = OptionParser(usage=usage)
    parser.add_option("-d", "--decompress", dest="dpath",
                  help="decompress apk file", metavar="decode")
    parser.add_option("-b", "--build", dest="bpath",
                  help="build apk file", metavar="build")
    parser.add_option("-s", "--sign", dest="sign",
                  help="sign apk file", metavar="sign")
    parser.add_option("-r", "--bulid_sign", dest="bsign",
                  help="build and sign apk file", metavar="bsign")

    (opts, args) = parser.parse_args()
    if opts.dpath:
        if len(args) > 0:
            new_path = args[0]
        else:
            new_path = None
        if os.path.isfile(opts.dpath):
            dec_apk(opts.dpath, new_path)
        else:
            parser.error("original apk file not exist")
    if opts.bpath:
        if len(args) > 0:
            new_apk = args[0]
        else:
            new_apk = None
        if opts.bpath and os.path.isdir(opts.bpath):
            bld_apk(opts.bpath, new_apk)
        else:
            parser.error("building dir not exist")
    if opts.sign:
        if len(args) > 0:
            new_apk = args[0]
        else:
            new_apk = None
        if opts.sign and os.path.isfile(opts.sign):
            sign_apk(opts.sign, new_apk)
        else:
            parser.error("apk file not exist")
    if opts.bsign:
        if len(args) > 0:
            new_apk = args[0]
        else:
            new_apk = None
        if os.path.isdir(opts.bsign):
            bsign_apk(opts.bsign, new_apk)
        else:
            parser.error("building dir not exist")
        
if __name__ == '__main__':
    main()
