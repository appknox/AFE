.class Lcom/xybot/toastmaker$1;
.super Ljava/lang/Thread;
.source "toastmaker.java"


# annotations
.annotation system Ldalvik/annotation/EnclosingClass;
    value = Lcom/xybot/toastmaker;
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0x0
    name = null
.end annotation


# instance fields
.field final synthetic this$0:Lcom/xybot/toastmaker;


# direct methods
.method constructor <init>(Lcom/xybot/toastmaker;)V
    .locals 0
    .parameter

    .prologue
    .line 1
    iput-object p1, p0, Lcom/xybot/toastmaker$1;->this$0:Lcom/xybot/toastmaker;

    .line 15
    invoke-direct {p0}, Ljava/lang/Thread;-><init>()V

    return-void
.end method


# virtual methods
.method public run()V
    .locals 4

    .prologue
    .line 19
    new-instance v0, Landroid/os/Message;

    invoke-direct {v0}, Landroid/os/Message;-><init>()V

    .line 20
    .local v0, myMessage:Landroid/os/Message;
    new-instance v1, Landroid/os/Bundle;

    invoke-direct {v1}, Landroid/os/Bundle;-><init>()V

    .line 21
    .local v1, resBundle:Landroid/os/Bundle;
    const-string v2, "status"

    const-string v3, "SUCCESS"

    invoke-virtual {v1, v2, v3}, Landroid/os/Bundle;->putString(Ljava/lang/String;Ljava/lang/String;)V

    .line 22
    iput-object v1, v0, Landroid/os/Message;->obj:Ljava/lang/Object;

    .line 23
    iget-object v2, p0, Lcom/xybot/toastmaker$1;->this$0:Lcom/xybot/toastmaker;

    #getter for: Lcom/xybot/toastmaker;->handler:Landroid/os/Handler;
    invoke-static {v2}, Lcom/xybot/toastmaker;->access$0(Lcom/xybot/toastmaker;)Landroid/os/Handler;

    move-result-object v2

    invoke-virtual {v2, v0}, Landroid/os/Handler;->sendMessage(Landroid/os/Message;)Z

    .line 24
    return-void
.end method
