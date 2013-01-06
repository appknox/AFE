Sdir=./SourceCode/Obfuscators
Ddir=./Rebuild/apktool

all : $(Ddir)/Obfuscator1_insert $(Ddir)/Obfuscator2_ChangeName $(Ddir)/Obfuscator3_ChangeCFG $(Ddir)/Obfuscator4_StringEncrypt ./ResultAnalyze
./Rebuild/apktool/Obfuscator1_insert:$(Sdir)/Obfuscator1_insert.cpp
	g++ $< -o $@
./Rebuild/apktool/Obfuscator2_ChangeName:$(Sdir)/Obfuscator2_ChangeName.cpp
	g++ $< -o $@
./Rebuild/apktool/Obfuscator3_ChangeCFG:$(Sdir)/Obfuscator3_ChangeCFG.cpp
	g++ $< -o $@
./Rebuild/apktool/Obfuscator4_StringEncrypt:$(Sdir)/Obfuscator4_StringEncrypt.cpp
	g++ $< -o $@

clean :
	rm ./Rebuild/apktool/Obfuscator1_insert
	rm ./Rebuild/apktool/Obfuscator2_ChangeName
	rm ./Rebuild/apktool/Obfuscator3_ChangeCFG
	rm ./Rebuild/apktool/Obfuscator4_StringEncrypt

