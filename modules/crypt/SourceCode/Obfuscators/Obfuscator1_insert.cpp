#include <iostream>
#include <stdio.h>
#include <string.h>
#include <fstream>
#include <string>
#include <sys/types.h>
#include <dirent.h>
#include <sys/stat.h>

using namespace std;


void obfuscator(char* filepath2)
{
// Read the smali file.
    ifstream in(filepath2);

// Read Log.d debug method(defunct methods) from the file.
    ifstream in2("./Rebuild/apktool/methodOF1.txt");

    string str;
    string OFstring;
    string OriginalString;

    while(getline(in2,str))
    {
        OFstring+=(str+'\n');
    }

    while(getline(in,str))
    {
        OriginalString+=(str+'\n');

	//When the program finds the string“# direct methods" in the .smali file, the program insert the obfuscation method after this string.
        if (str.find("direct methods")!=str.npos)
        {
            OriginalString+=OFstring;
        }
    }

    in.close();
    in2.close();


// Rewrite the original .smali file.
  ofstream out(filepath2);
  out<<OriginalString;
  out.close();
}
int traverse_dir(char *path)
{
	DIR *dir;
	struct dirent *file;
	struct stat st;
	char temp[1024];

	if ( !(dir = opendir(path)) )
	{
		printf("error opendir %s!!!\n", path);
		return -1;
	}

	while ((file = readdir(dir)) != NULL)
	{
		if (strncmp(file->d_name, ".", 1) == 0)
			continue;
		sprintf(temp, "%s/%s", path, file->d_name);

		printf("%s\n", temp);

		// If the file is a .smali file then obfuscate this file.
		if (strncmp(temp + strlen(temp) - 6, ".smali", 6) == 0)
		{
			printf("%s\n", temp);
			obfuscator(temp);
		}
		if (lstat(temp, &st) >= 0 && S_ISDIR(st.st_mode) )
		{
		//Traverse the directory.
			traverse_dir(temp);
		}
	}
	closedir(dir);
	return 0;
}



int main(int argc,char* argv[])
{
    //Traverse the directory.
    traverse_dir(argv[1]);
    return 0;
}
