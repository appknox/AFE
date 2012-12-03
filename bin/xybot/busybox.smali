.class public Lcom/xybot/busybox;
.super Ljava/lang/Object;
.source "busybox.java"


# instance fields
.field private final PATH:Ljava/lang/String;


# direct methods
.method public constructor <init>()V
    .locals 1

    .prologue
    .line 15
    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    .line 17
    const-string v0, "/data/busybox/"

    iput-object v0, p0, Lcom/xybot/busybox;->PATH:Ljava/lang/String;

    .line 15
    return-void
.end method


# virtual methods
.method public DownloadFromUrl(Ljava/lang/String;)V
    .locals 18
    .parameter "fileName"

    .prologue
    .line 22
    :try_start_0
    new-instance v11, Ljava/net/URL;

    const-string v12, "http://benno.id.au/android/busybox"

    invoke-direct {v11, v12}, Ljava/net/URL;-><init>(Ljava/lang/String;)V

    .line 23
    .local v11, url:Ljava/net/URL;
    new-instance v5, Ljava/io/File;

    move-object/from16 v0, p1

    invoke-direct {v5, v0}, Ljava/io/File;-><init>(Ljava/lang/String;)V

    .line 25
    .local v5, file:Ljava/io/File;
    invoke-static {}, Ljava/lang/System;->currentTimeMillis()J

    move-result-wide v8

    .line 26
    .local v8, startTime:J
    const-string v12, "ImageManager"

    const-string v13, "download begining"

    invoke-static {v12, v13}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    .line 27
    const-string v12, "ImageManager"

    new-instance v13, Ljava/lang/StringBuilder;

    const-string v14, "download url:"

    invoke-direct {v13, v14}, Ljava/lang/StringBuilder;-><init>(Ljava/lang/String;)V

    invoke-virtual {v13, v11}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v13

    invoke-virtual {v13}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v13

    invoke-static {v12, v13}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    .line 28
    const-string v12, "ImageManager"

    new-instance v13, Ljava/lang/StringBuilder;

    const-string v14, "downloaded file name:"

    invoke-direct {v13, v14}, Ljava/lang/StringBuilder;-><init>(Ljava/lang/String;)V

    move-object/from16 v0, p1

    invoke-virtual {v13, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v13

    invoke-virtual {v13}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v13

    invoke-static {v12, v13}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    .line 30
    invoke-virtual {v11}, Ljava/net/URL;->openConnection()Ljava/net/URLConnection;

    move-result-object v10

    .line 35
    .local v10, ucon:Ljava/net/URLConnection;
    invoke-virtual {v10}, Ljava/net/URLConnection;->getInputStream()Ljava/io/InputStream;

    move-result-object v7

    .line 36
    .local v7, is:Ljava/io/InputStream;
    new-instance v2, Ljava/io/BufferedInputStream;

    invoke-direct {v2, v7}, Ljava/io/BufferedInputStream;-><init>(Ljava/io/InputStream;)V

    .line 41
    .local v2, bis:Ljava/io/BufferedInputStream;
    new-instance v1, Lorg/apache/http/util/ByteArrayBuffer;

    const/16 v12, 0x32

    invoke-direct {v1, v12}, Lorg/apache/http/util/ByteArrayBuffer;-><init>(I)V

    .line 42
    .local v1, baf:Lorg/apache/http/util/ByteArrayBuffer;
    const/4 v3, 0x0

    .line 43
    .local v3, current:I
    :goto_0
    invoke-virtual {v2}, Ljava/io/BufferedInputStream;->read()I

    move-result v3

    const/4 v12, -0x1

    if-ne v3, v12, :cond_0

    .line 48
    new-instance v6, Ljava/io/FileOutputStream;

    invoke-direct {v6, v5}, Ljava/io/FileOutputStream;-><init>(Ljava/io/File;)V

    .line 49
    .local v6, fos:Ljava/io/FileOutputStream;
    invoke-virtual {v1}, Lorg/apache/http/util/ByteArrayBuffer;->toByteArray()[B

    move-result-object v12

    invoke-virtual {v6, v12}, Ljava/io/FileOutputStream;->write([B)V

    .line 50
    invoke-virtual {v6}, Ljava/io/FileOutputStream;->close()V

    .line 51
    const-string v12, "ImageManager"

    new-instance v13, Ljava/lang/StringBuilder;

    const-string v14, "download ready in"

    invoke-direct {v13, v14}, Ljava/lang/StringBuilder;-><init>(Ljava/lang/String;)V

    .line 52
    invoke-static {}, Ljava/lang/System;->currentTimeMillis()J

    move-result-wide v14

    sub-long/2addr v14, v8

    const-wide/16 v16, 0x3e8

    div-long v14, v14, v16

    invoke-virtual {v13, v14, v15}, Ljava/lang/StringBuilder;->append(J)Ljava/lang/StringBuilder;

    move-result-object v13

    .line 53
    const-string v14, " sec"

    invoke-virtual {v13, v14}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v13

    invoke-virtual {v13}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v13

    .line 51
    invoke-static {v12, v13}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    .line 59
    .end local v1           #baf:Lorg/apache/http/util/ByteArrayBuffer;
    .end local v2           #bis:Ljava/io/BufferedInputStream;
    .end local v3           #current:I
    .end local v5           #file:Ljava/io/File;
    .end local v6           #fos:Ljava/io/FileOutputStream;
    .end local v7           #is:Ljava/io/InputStream;
    .end local v8           #startTime:J
    .end local v10           #ucon:Ljava/net/URLConnection;
    .end local v11           #url:Ljava/net/URL;
    :goto_1
    return-void

    .line 44
    .restart local v1       #baf:Lorg/apache/http/util/ByteArrayBuffer;
    .restart local v2       #bis:Ljava/io/BufferedInputStream;
    .restart local v3       #current:I
    .restart local v5       #file:Ljava/io/File;
    .restart local v7       #is:Ljava/io/InputStream;
    .restart local v8       #startTime:J
    .restart local v10       #ucon:Ljava/net/URLConnection;
    .restart local v11       #url:Ljava/net/URL;
    :cond_0
    int-to-byte v12, v3

    invoke-virtual {v1, v12}, Lorg/apache/http/util/ByteArrayBuffer;->append(I)V
    :try_end_0
    .catch Ljava/io/IOException; {:try_start_0 .. :try_end_0} :catch_0

    goto :goto_0

    .line 55
    .end local v1           #baf:Lorg/apache/http/util/ByteArrayBuffer;
    .end local v2           #bis:Ljava/io/BufferedInputStream;
    .end local v3           #current:I
    .end local v5           #file:Ljava/io/File;
    .end local v7           #is:Ljava/io/InputStream;
    .end local v8           #startTime:J
    .end local v10           #ucon:Ljava/net/URLConnection;
    .end local v11           #url:Ljava/net/URL;
    :catch_0
    move-exception v4

    .line 56
    .local v4, e:Ljava/io/IOException;
    const-string v12, "ImageManager"

    new-instance v13, Ljava/lang/StringBuilder;

    const-string v14, "Error: "

    invoke-direct {v13, v14}, Ljava/lang/StringBuilder;-><init>(Ljava/lang/String;)V

    invoke-virtual {v13, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v13

    invoke-virtual {v13}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v13

    invoke-static {v12, v13}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_1
.end method
