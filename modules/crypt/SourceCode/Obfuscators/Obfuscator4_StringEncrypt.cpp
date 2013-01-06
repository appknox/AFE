#include <iostream>
#include <stdio.h>
#include <string.h>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>
#include <sys/types.h>
#include <dirent.h>
#include <sys/stat.h>

using namespace std;

//encrypt the character.
char encryptString(char t)
{
    if (t<='Z'&&t>='A')
    {
        t-='A';
        t=(t+10)%26;
        t+='A';
    }
    else if (t<='z'&&t>='a')
    {
        t-='a';
        t=(t+10)%26;
        t+='a';
    }
    return t;
}

void encryptConstString(char* filepath2)
{
    ifstream in(filepath2);
    string str;
    int i;
    string OriginalString;
    string classname;

    getline(in,str);
    OriginalString+=(str+'\n');
    istringstream istr(str);

    string tmp;
    while(istr>>tmp);
    classname=tmp;

    cout<<classname<<endl;

    int ccount=0;
    int notnewstr=0;

    while(getline(in,str))
    {
	//If this line of string has "const-string", then try to extract this const string.
        if (str.find("const-string")!=str.npos
	    &&str.find("\\u")==str.npos
	    &&str.find("\\n")==str.npos
	)
        {
            string teststr;
            teststr = str;
            string  vstr;
            string enstr;

            int flagv=0;
            bool flagenstr=false;

            ccount=0;
            notnewstr=0;

	    //extract the const string.
            for (i=0;i<teststr.length();i++)
            {
                if (teststr[i]=='v'||teststr[i]=='p')
                {
                    flagv++;
                }
                if (teststr[i]==',')
                    flagv++;

                if (teststr[i]=='"')
                {
                    flagenstr=true;
                    flagv++;
                }
                if (flagv==1)
                {
                    vstr+=teststr[i];
                }
		
		//If the string is a const string, then encryt this string.
                else if (flagenstr==true&&(i!=teststr.length()-1))
                {
                    enstr+=teststr[i];
                    if ((teststr[i]<='z'&&teststr[i]>='a')||(teststr[i]<='Z'&&teststr[i]>='A')||teststr[i]=='"')
                        {
                                    if (teststr[i]!='"')
                                        {
                                            teststr[i]=encryptString(teststr[i]);
                                        }
                        }
                    else
                    {
//                        notnewstr=1;
                    }
                }
            }

            string newstr;
            OriginalString+='\n';

            if (notnewstr==0&&vstr[0]!='p'&&vstr.length()<=2)
            {
                OriginalString+=(teststr+'\n');

		//Insert decrypt string function code after encryt string.
                OriginalString+='\n';
                newstr = "    invoke-static {"+vstr+"}, Lcom/mzhengDS;->DecryptString(Ljava/lang/String;)Ljava/lang/String;";
                OriginalString+=(newstr+'\n');
                OriginalString+='\n';
		
		//Insert moving decrypt string result code back to the const string after decrypt string function code.
                newstr = "    move-result-object "+vstr;
                cout<<str<<endl;
                cout<<newstr<<endl;
                OriginalString+=(newstr+'\n');
            }
            else
             {
                OriginalString+=(str+'\n');
             }

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


int counter=0;

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

		// If the file is a .smali file then obfuscate this file.
		if (strncmp(temp + strlen(temp) - 6, ".smali", 6) == 0)
		{
			printf("%s\n", temp);
			encryptConstString(temp);
		}
		if (lstat(temp, &st) >= 0 && S_ISDIR(st.st_mode) )
		{
			traverse_dir(temp);
		}
	}
	closedir(dir);
	return 0;
}


bool cmp(string a,string b)
{
    return a.length()>b.length();
}

int main(int argc,char* argv[])
{
    char str[100];
    char str2[100];

    sprintf(str,"%s",argv[1]);

    //Copy the .smali file of decrypt class to the directory.  
    sprintf(str2,"cp -R ./Rebuild/apktool/com %s/smali/",str);
    cout<<str2<<endl;
    system(str2);

    //Traverse the directory.
    traverse_dir(argv[1]);

    return 0;
}
