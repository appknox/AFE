#include <iostream>
#include <stdio.h>
#include <string.h>
#include <fstream>
#include <string>
#include <sys/types.h>
#include <dirent.h>
#include <sys/stat.h>
#include <sstream>

using namespace std;

void ChangeCFG(char* filepath2)
{
    static int counter=0;

    ifstream in(filepath2);
    string str;
    int i;
    string OriginalString;
    string classname;

    bool caninsert = false;


    getline(in,str);

    OriginalString+=(str+'\n');

    istringstream istr(str);

    while(getline(in,str))
    {
	//If this line of string has ".prologue", then it means this is the beginning of the method.
        if (str.find(".prologue")!=str.npos)
        {
            caninsert = true;
            OriginalString+=(str+'\n');
            OriginalString+=('\n');

	    //Insert goto obfuscation code at the beginning of the method.
            string newstr = "    goto :CFGGoto2";
            OriginalString+=(newstr+'\n');
            OriginalString+=('\n');

            newstr = "    :CFGGoto1";
            OriginalString+=(newstr+'\n');
            OriginalString+=('\n');
            continue;
        }

	//If this line of string has ".end method", then it means this is the end of the method.
        if (str.find(".end method")!=str.npos&&caninsert==true)
        {
            caninsert = false;

            OriginalString+=('\n');

	    //Insert goto obfuscation code at the end of the method.
            string newstr = "    :CFGGoto2";
            OriginalString+=(newstr+'\n');
            OriginalString+=('\n');

            newstr = "    goto :CFGGoto1";
            OriginalString+=(newstr+'\n');
            OriginalString+=('\n');

            OriginalString+=(str+'\n');

            continue;
        }

    OriginalString+=(str+'\n');
    }

  in.close();

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
			ChangeCFG(temp);
		}
		if (lstat(temp, &st) >= 0 && S_ISDIR(st.st_mode) )
		{
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
