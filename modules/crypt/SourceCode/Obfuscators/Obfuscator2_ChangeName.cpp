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
#include <map>

using namespace std;

vector<string> vs;
map<string, int> methodnames;
map<string, int> obmethodnames;


void findAllDirectMethod(char* filepath2)
{
    string str;
    string OriginalString;
    int i;

    ifstream in(filepath2);
    ifstream in2(filepath2);

    getline(in2,str);
    istringstream istr(str);
    string tmp1;
    while(istr>>tmp1);

//    cout<<tmp1<<endl;


    while(getline(in,str))
    {

//	If this line of string is a method and it is not a constructor method or system methods, then change the method name and record the method name. 
        if (
            str[0]=='.'&&
            str.find("method")!=str.npos&&
            str.find("end")==str.npos&&
            str.find("constructor")==str.npos
            &&str.find("init")==str.npos
            &&str.find("$")==str.npos
            )
            {
                istringstream istr(str);
                string tmp;
		string newstr;
                while(istr>>tmp);

		string tmp2;
		for (i=0;i<tmp.length();i++)
		{	
			if (tmp[i]=='(')
			break;
			tmp2+=tmp[i];
		}

		if (methodnames[tmp2]!=1)
			{
				string tmp3=tmp1;
				tmp3+="->";
				tmp3+=tmp2;
//				cout<<tmp3<<endl;
				obmethodnames[tmp3]=1;
				
				newstr="";
                		bool changeflag=true;
                		for (i=0;i<str.length();i++)
               			{
                		if (changeflag==true&&str[i]=='(')
                    			{
					//add an arbitary string after each method.
                        		newstr+="abc123";
                        		changeflag=false;
                  			 }
                		newstr+=str[i];
               		 	}

//			       	cout<<newstr<<endl;
				OriginalString+=(newstr+'\n');
				continue;
			}
		}

    OriginalString+=(str+'\n');
    }
  in.close();

// Rewrite the original .smali file.
  ofstream out(filepath2);
  out<<OriginalString;
  out.close();
}

void changeAllDirectMethod(char* filepath2)
{
    ifstream in(filepath2);
    string str;
    int i;
    string OriginalString;

//Search for the invoking string code of the .smali file.
    while(getline(in,str))
    {
        if (
            str.find("invoke-")!=str.npos
            &&str.find("init")==str.npos
            &&str.find("$")==str.npos
            &&str.find("}, Landroid")==str.npos
            &&str.find("}, Ljava")==str.npos
            &&str.find("invoke-interface")==str.npos
            )
            {

            string fullmethod;
            bool flagstart=false;
//            cout<<str<<endl;
            for (i=0;i<str.length();i++)
            {
                if (str[i]=='L')
                {
                    flagstart=true;
//                  continue;
                }

                if (flagstart!=true)
                  continue;

                if (str[i]=='(')
                   break;

                fullmethod+=str[i];
            }

	    cout<<fullmethod<<endl;
	
	    //If the method is an obfuscated method in the record, then modify this invoking string code.

            if (obmethodnames[fullmethod]!=1)
            {
                OriginalString+=(str+'\n');
                continue;
            }

            string newstr;
            bool changeflag=false;
            for (i=0;i<str.length();i++)
            {
                if (str[i]=='>')
                    changeflag=true;
                if (changeflag==true&&str[i]=='(')
                    {
                        newstr+="abc123";
                    }
                newstr+=str[i];
            }

            cout<<newstr<<endl;
            OriginalString+=(newstr+'\n');
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

int traverse_dir(char *path,int type)
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
 		
		//If type == 0, then get the methods name, else change the invoking methods name.
			if (type==0)
	                        findAllDirectMethod(temp);
                        else
	                        changeAllDirectMethod(temp);

		}
		if (lstat(temp, &st) >= 0 && S_ISDIR(st.st_mode) )
		{
			traverse_dir(temp,type);
		}
	}
	closedir(dir);
	return 0;
}

bool cmp(string a,string b)
{
    return a.length()>b.length();
}

void getmethodnames(char* filepath)
{
    ifstream in(filepath);
    string str;

    // Read library methods from the file.
    while(getline(in,str))
    {
        methodnames[str]=1;
    }
}

int main(int argc,char* argv[])
{

    // Read library methods from the file.
    getmethodnames("./Rebuild/apktool/androidmethod2.txt");

    //Traverse the directory to get the methods name.
    traverse_dir(argv[1], 0);

//    Traverse the directory to change the invoking methods name.
    traverse_dir(argv[1],1);

    return 0;
}
