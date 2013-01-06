import os, fnmatch, string, random, re
newpkg = ""
oldpkg = ""

def checkfilename(name):
	"check if file name matches with the given pattern"

	m = re.search('(\D*).xml$', name)
	#print 'checking filename', name
	if m is None:
		return False
	else:
		#print 'returning true for filename', name
		return True

def extract(raw_string, start_marker, end_marker):
    start = raw_string.index(start_marker) + len(start_marker)
    end = raw_string.index(end_marker, start)
    return raw_string[start:end]

def findReplace(directory, find, replace, filePattern):
    for path, dirs, files in os.walk(os.path.abspath(directory)):
        for filename in fnmatch.filter(files, filePattern):
            filepath = os.path.join(path, filename)
            with open(filepath) as f:
                linelist = []
                for line in f:
                    line = line.replace(find, replace)
                    linelist.append(line)
            with open(filepath, "w") as f:
                for item in linelist:
                    f.write("%s\n" % item)

#findReplace("/Users/subho_halder/Hacking/Android/AFE/test/malware", "com/link/uranai", "wam/ama/gama", "*.smali")
def id_generator(size=3, chars=string.ascii_lowercase):
    return ''.join(random.choice(chars) for x in range(size))

#print id_generator(3)

def package_change_manifest(path):
    global newpkg, oldpkg
    with open(path) as f:
        linelist = []
        for line in f:
            if "package" in line:
                oldpkg = extract(line[line.index("package"):len(line)],"\"","\"")
                num = oldpkg.count('.')
                newpkg = "com"
                for x in range(0,num):
                    newpkg = newpkg + "." + id_generator(3)
                print newpkg
                line = line.replace(oldpkg,newpkg)
            linelist.append(line)
        with open(path, "w") as f:
                for item in linelist:
                    f.write(item)

def rewrite_com_dir(path_to_smali_com):
    oldsplitted= re.split('\.',oldpkg)
    #print len(oldsplitted)
    iterdir = iter(oldsplitted)
    next(iterdir)
    for cdir in iterdir:
        if (os.path.isdir(path_to_smali_com + "/" + cdir)):
            print "exist !"
        else:
            g


package_change_manifest("/Users/subho_halder/Hacking/Android/AFE/test/malware/AndroidManifest.xml")

rewrite_com_dir("/Users/subho_halder/Hacking/Android/AFE/test/malware/smali")

print newpkg
print oldpkg