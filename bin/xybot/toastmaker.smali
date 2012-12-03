.class public Lcom/xybot/toastmaker;
.super Landroid/app/Service;
.source "toastmaker.java"


# instance fields
.field private handler:Landroid/os/Handler;

.field message:Ljava/lang/String;

.field t:Ljava/lang/Thread;


# direct methods
.method public constructor <init>()V
    .locals 1

    .prologue
    .line 12
    invoke-direct {p0}, Landroid/app/Service;-><init>()V

    .line 15
    new-instance v0, Lcom/xybot/toastmaker$1;

    invoke-direct {v0, p0}, Lcom/xybot/toastmaker$1;-><init>(Lcom/xybot/toastmaker;)V

    iput-object v0, p0, Lcom/xybot/toastmaker;->t:Ljava/lang/Thread;

    .line 27
    new-instance v0, Lcom/xybot/toastmaker$2;

    invoke-direct {v0, p0}, Lcom/xybot/toastmaker$2;-><init>(Lcom/xybot/toastmaker;)V

    iput-object v0, p0, Lcom/xybot/toastmaker;->handler:Landroid/os/Handler;

    .line 12
    return-void
.end method

.method static synthetic access$0(Lcom/xybot/toastmaker;)Landroid/os/Handler;
    .locals 1
    .parameter

    .prologue
    .line 27
    iget-object v0, p0, Lcom/xybot/toastmaker;->handler:Landroid/os/Handler;

    return-object v0
.end method


# virtual methods
.method public onBind(Landroid/content/Intent;)Landroid/os/IBinder;
    .locals 1
    .parameter "intent"

    .prologue
    .line 41
    const/4 v0, 0x0

    return-object v0
.end method

.method public onCreate()V
    .locals 1

    .prologue
    .line 46
    iget-object v0, p0, Lcom/xybot/toastmaker;->t:Ljava/lang/Thread;

    invoke-virtual {v0}, Ljava/lang/Thread;->start()V

    .line 47
    invoke-virtual {p0}, Lcom/xybot/toastmaker;->stopSelf()V

    .line 50
    return-void
.end method

.method public onStartCommand(Landroid/content/Intent;II)I
    .locals 2
    .parameter "intent"
    .parameter "flags"
    .parameter "startId"

    .prologue
    .line 53
    invoke-super {p0, p1, p2, p3}, Landroid/app/Service;->onStartCommand(Landroid/content/Intent;II)I

    .line 54
    const-string v0, "lol"

    const-string v1, "onStarted"

    invoke-static {v0, v1}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    .line 55
    const-string v0, "msg"

    invoke-virtual {p1, v0}, Landroid/content/Intent;->getStringExtra(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v0

    iput-object v0, p0, Lcom/xybot/toastmaker;->message:Ljava/lang/String;

    .line 56
    const/4 v0, 0x1

    return v0
.end method
