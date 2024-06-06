from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Manage(models.Model):
    ユーザー名 = models.ForeignKey(User, on_delete=models.SET_DEFAULT, null=True, blank=True, default=1)
    案件名 = models.CharField(max_length=100)
    
    PLAN_CHOICES = [
        ("plan01", "アドバンスドプラン"),
        ("plan02", "レギュラープラン"),
        ("plan03", "スマートプラン"),
        ("plan04", "For採用"),
        ("plan05", "ダイレクトセールス"),
        ("plan06", "社内案件"),
        ("plan07", "有償メンテナンス"),
        ("plan08", "LP"),
        ("plan09", "直案件"),
        ("plan10", "名刺"),
        ("plan11", "封筒"),
        ("plan12", "ロゴ"),
        ("plan13", "WEBサイト"),
        ("plan14", "チラシ"),
        ("plan99", "その他"),
    ]
    プラン名 = models.CharField(
        max_length=100,
        choices=PLAN_CHOICES,
        default='plan01',
    )

    DESIGNER_CHOICES = [
        ("designer01", "菊田"),
        ("designer02", "魚戸"),
        ("designer03", "後"),
        ("designer04", "和田"),
        ("designer05", "福原"),
        ("designer99", "その他"),
    ]
    デザイナー名 = models.CharField(
        max_length=100,
        choices=DESIGNER_CHOICES,
        default='designer01',
    )

    CODER_CHOICES = [
        ("coder01", "ラジ"),
        ("coder02", "久保木"),
        ("coder03", "菅野"),
        ("coder04", "小濱"),
        ("coder05", "稲野"),
        ("coder06", "青木"),
        ("coder99", "その他"),
    ]
    コーダー名 = models.CharField(
        max_length=100,
        choices=CODER_CHOICES,
        default='coder01',
    )

    DIRECTOR_CHOICES = [
        ("director01", "木下"),
        ("director02", "永見"),
        ("director03", "春木"),
        ("director04", "野本"),
        ("director05", "中吉"),
        ("director98", "営業"),
        ("director99", "その他"),
    ]
    ディレクター名 = models.CharField(
        max_length=100,
        choices=DIRECTOR_CHOICES,
        default='director01',
    )

    納品月 = models.CharField(max_length=7, default='', help_text='例: 2023-06')
    開始日 = models.DateField(default=timezone.now)
    終了日 = models.DateField(default=timezone.now)
    備考 = models.TextField(max_length=999, default='', null=True, blank=True)
    
    def __str__(self):
        return self.案件名
