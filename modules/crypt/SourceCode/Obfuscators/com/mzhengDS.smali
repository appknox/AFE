.class public Lcom/mzhengDS;
.super Ljava/lang/Object;
.source "mzhengDS.java"


# direct methods
.method public constructor <init>()V
    .locals 0

    .prologue
    .line 3
    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method

.method public static DecryptString(Ljava/lang/String;)Ljava/lang/String;
    .locals 4
    .parameter "b"

    .prologue
    .line 7
    invoke-virtual {p0}, Ljava/lang/String;->toCharArray()[C

    move-result-object v0

    .line 9
    .local v0, c:[C
    const/4 v1, 0x0

    .local v1, i:I
    :goto_0
    invoke-virtual {p0}, Ljava/lang/String;->length()I

    move-result v2

    if-lt v1, v2, :cond_0

    .line 25
    invoke-static {v0}, Ljava/lang/String;->valueOf([C)Ljava/lang/String;

    move-result-object v2

    return-object v2

    .line 11
    :cond_0
    aget-char v2, v0, v1

    const/16 v3, 0x5a

    if-gt v2, v3, :cond_2

    aget-char v2, v0, v1

    const/16 v3, 0x41

    if-lt v2, v3, :cond_2

    .line 13
    aget-char v2, v0, v1

    add-int/lit8 v2, v2, -0x41

    int-to-char v2, v2

    aput-char v2, v0, v1

    .line 14
    aget-char v2, v0, v1

    add-int/lit8 v2, v2, 0x1a

    add-int/lit8 v2, v2, -0xa

    rem-int/lit8 v2, v2, 0x1a

    int-to-char v2, v2

    aput-char v2, v0, v1

    .line 15
    aget-char v2, v0, v1

    add-int/lit8 v2, v2, 0x41

    int-to-char v2, v2

    aput-char v2, v0, v1

    .line 9
    :cond_1
    :goto_1
    add-int/lit8 v1, v1, 0x1

    goto :goto_0

    .line 17
    :cond_2
    aget-char v2, v0, v1

    const/16 v3, 0x7a

    if-gt v2, v3, :cond_1

    aget-char v2, v0, v1

    const/16 v3, 0x61

    if-lt v2, v3, :cond_1

    .line 19
    aget-char v2, v0, v1

    add-int/lit8 v2, v2, -0x61

    int-to-char v2, v2

    aput-char v2, v0, v1

    .line 20
    aget-char v2, v0, v1

    add-int/lit8 v2, v2, 0x1a

    add-int/lit8 v2, v2, -0xa

    rem-int/lit8 v2, v2, 0x1a

    int-to-char v2, v2

    aput-char v2, v0, v1

    .line 21
    aget-char v2, v0, v1

    add-int/lit8 v2, v2, 0x61

    int-to-char v2, v2

    aput-char v2, v0, v1

    goto :goto_1
.end method
