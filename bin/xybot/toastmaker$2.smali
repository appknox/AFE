.class Lcom/xybot/toastmaker$2;
.super Landroid/os/Handler;
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
    iput-object p1, p0, Lcom/xybot/toastmaker$2;->this$0:Lcom/xybot/toastmaker;

    .line 27
    invoke-direct {p0}, Landroid/os/Handler;-><init>()V

    return-void
.end method


# virtual methods
.method public handleMessage(Landroid/os/Message;)V
    .locals 3
    .parameter "msg"

    .prologue
    .line 32
    iget-object v0, p0, Lcom/xybot/toastmaker$2;->this$0:Lcom/xybot/toastmaker;

    invoke-virtual {v0}, Lcom/xybot/toastmaker;->getApplicationContext()Landroid/content/Context;

    move-result-object v0

    iget-object v1, p0, Lcom/xybot/toastmaker$2;->this$0:Lcom/xybot/toastmaker;

    iget-object v1, v1, Lcom/xybot/toastmaker;->message:Ljava/lang/String;

    const/4 v2, 0x1

    invoke-static {v0, v1, v2}, Landroid/widget/Toast;->makeText(Landroid/content/Context;Ljava/lang/CharSequence;I)Landroid/widget/Toast;

    move-result-object v0

    invoke-virtual {v0}, Landroid/widget/Toast;->show()V

    .line 33
    const-string v0, "lol"

    const-string v1, "messaged"

    invoke-static {v0, v1}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    .line 35
    return-void
.end method
