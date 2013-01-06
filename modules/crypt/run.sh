#!/bin/bash

cnt=1
fis=`ls ./Input/`

for i in $fis
do
	echo "$i"
	echo $cnt
	cp ./Input/"$i" ./Output/"$cnt".apk

	cp ./Output/"$cnt".apk ./Output/"$cnt"-resigned.apk
	java -classpath ./modules/crypt/Signapk/testsign.jar testsign ./Output/"$cnt"-resigned.apk

	cp ./Output/"$cnt".apk ./modules/crypt/Rebuild/apktool/"$cnt".apk

	./modules/crypt/Rebuild/apktool/apktool d ./modules/crypt/Rebuild/apktool/"$cnt".apk ./modules/crypt/Rebuild/apktool/"$cnt"
	./modules/crypt/Rebuild/apktool/apktool b ./modules/crypt/Rebuild/apktool/"$cnt" ./Output/"$cnt"-rebuilt.apk 
	rm -rf ./modules/crypt/Rebuild/apktool/"$cnt" 

	./modules/crypt/Rebuild/apktool/apktool d ./modules/crypt/Rebuild/apktool/"$cnt".apk ./modules/crypt/Rebuild/apktool/"$cnt"
	./modules/crypt/Rebuild/apktool/Obfuscator1_insert ./modules/crypt/Rebuild/apktool/"$cnt"
	./modules/crypt/Rebuild/apktool/apktool b ./modules/crypt/Rebuild/apktool/"$cnt" ./Output/"$cnt"-insert.apk 
	rm -rf ./modules/crypt/Rebuild/apktool/"$cnt" 

	./modules/crypt/Rebuild/apktool/apktool d ./modules/crypt/Rebuild/apktool/"$cnt".apk ./modules/crypt/Rebuild/apktool/"$cnt"
	./modules/crypt/Rebuild/apktool/Obfuscator2_ChangeName ./modules/crypt/Rebuild/apktool/"$cnt"
	./modules/crypt/Rebuild/apktool/apktool b ./modules/crypt/Rebuild/apktool/"$cnt" ./Output/"$cnt"-changename.apk 
	rm -rf ./modules/crypt/Rebuild/apktool/"$cnt" 

	./modules/crypt/Rebuild/apktool/apktool d ./modules/crypt/Rebuild/apktool/"$cnt".apk ./modules/crypt/Rebuild/apktool/"$cnt"
	./modules/crypt/Rebuild/apktool/Obfuscator3_ChangeCFG ./modules/crypt/Rebuild/apktool/"$cnt"
	./modules/crypt/Rebuild/apktool/apktool b ./modules/crypt/Rebuild/apktool/"$cnt" ./Output/"$cnt"-changecfg.apk 
	rm -rf ./modules/crypt/Rebuild/apktool/"$cnt" 

	./modules/crypt/Rebuild/apktool/apktool d ./modules/crypt/Rebuild/apktool/"$cnt".apk ./modules/crypt/Rebuild/apktool/"$cnt"
	./modules/crypt/Rebuild/apktool/Obfuscator4_StringEncrypt ./modules/crypt/Rebuild/apktool/"$cnt"
	./modules/crypt/Rebuild/apktool/apktool b ./modules/crypt/Rebuild/apktool/"$cnt" ./Output/"$cnt"-stringcrypt.apk 
	rm -rf ./modules/crypt/Rebuild/apktool/"$cnt" 

################################ Add Your Extension Obfuscator Here ######################################







################################ Add Your Extension Obfuscator Here ######################################

	java -classpath ./modules/crypt/Signapk/testsign.jar testsign ./Output/"$cnt"-rebuilt.apk
	java -classpath ./modules/crypt/Signapk/testsign.jar testsign ./Output/"$cnt"-insert.apk
	java -classpath ./modules/crypt/Signapk/testsign.jar testsign ./Output/"$cnt"-changename.apk
	java -classpath ./modules/crypt/Signapk/testsign.jar testsign ./Output/"$cnt"-changecfg.apk
	java -classpath ./modules/crypt/Signapk/testsign.jar testsign ./Output/"$cnt"-stringcrypt.apk

	rm -f ./modules/crypt/Rebuild/apktool/"$cnt".apk
	
	((cnt++))
done

