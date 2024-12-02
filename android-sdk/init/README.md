---
description: 宝島 ANDROID SDKの初期化方法についてご案内します。
icon: laptop-code
---

# 宝島サービス

{% hint style="warning" %}
**Applicationの"onCreate()"で宝島 ANDROID SDKの初期化が行われます。**
{% endhint %}

":link:[Application Class](https://developer.android.com/reference/android/app/Application)"を使用していない場合は、新規作成後に初期化を行ってください。

***

## 基本モジュールの適用

基本ブロックを**アプリ（モジュール）レベルの"build.gradle"**ファイルに設定してください。

{% hint style="info" %}
最新バージョン（:white_check_mark: 24.10.4.9）の使用を推奨します。:link:[release.md](../release.md "mention")で最新バージョンを確認してください。

***

:heavy_check_mark: 追加機能の使用のために宝島PLUGモジュールが追加される場合があります。
{% endhint %}

{% code lineNumbers="true" %}
```gradle
dependencies {
  implementation 'kr.co.studioguru.sdk:treasureisland-scene:{SDK-VERSION}'
}
```
{% endcode %}

***

## SDKの初期化

宝島SDKを使用するために初期化を行います。

`Application`の`onCreate()`で`SceneConfig.Builder`を通じてSDKを初期化してください。

### **TreasureConfig.Builder**

| Name        | Value           |
| ----------- | --------------- |
| `context`   | Android Context |
| `appId`     | 連携アプリの固有識別子 |
| `appSecret` | 連携アプリの共有識別子検証キー |

:heavy_check_mark: **生成されたBuilderインスタンスを通じてオプションとSDKの初期化を行います。**

{% tabs %}
{% tab title="KOTLIN" %}
{% code lineNumbers="true" %}
```kotlin
class AppApplication : Application() {
    override fun onCreate() {
        super.onCreate()
        SceneConfig.Builder(
            context = this, 
            appId = "{APP-ID}", 
            appSecret = "{APP-SECRET}"
        )
        // オプション：ログ出力の可否を設定します。
        .withAllowLog(allowLog = true)
        // オプション：ステータスバーの色を設定します。
        .withStatusBarOption(
            config = SceneConfig.StatusBarOption(
                allow = true,
                statusBarColor = Color.parseColor("#FF6103"),
                isWindowLight = false
            )
        )
        // オプション：プッシュ通知設定
        .withNotificationOption(
            config = SceneConfig.NotificationOption(
                allow = true,
                channelName = "通知チャンネル名",
                iconResourceId = R.drawable.ic_notification
            )
        )
        .build()?.initialize()
    }
}
```
{% endcode %}
{% endtab %}

{% tab title="JAVA" %}
{% code lineNumbers="true" %}
```java
public class AppApplication extends Application {
    @Override
    public void onCreate() {
        super.onCreate();
        SceneConfig.Builder builder = new SceneConfig.Builder(
            this,
            "testAppID",
            "testSecret"
        );
        builder.withAllowLog(true);
        builder.withStatusBarOption(new SceneConfig.StatusBarOption(
            true,
            Color.parseColor("#FF6103"),
            false
        ));
        builder.withNotificationOption(new SceneConfig.NotificationOption(
            true,
            "宝島",
            R.drawable.ic_notify
        ));
        SceneConfig SceneConfig = builder.build();
        if (SceneConfig != null) {
            SceneConfig.initialize();
        }
    }
}
```
{% endcode %}
{% endtab %}
{% endtabs %}

### Options

#### 🎈withAllowLog(allowLog: boolean)

SDKのログ出力可否を設定します。

:heavy_check_mark: デフォルト値 -> ログは出力されません。

| Name       | Type    | Description            |
| ---------- | ------- | ---------------------- |
| `allowLog` | boolean | ログ出力可否（`デフォルト値 false`） |

#### 🎈withStatusBarColor(config: TreasureConfig.StatusBarOption)

画面上部のステータスバーの色を設定します。

:heavy_check_mark: デフォルト値 -> Androidのデフォルト設定が適用されます。

⬇ TreasureConfig.StatusBarOption

| Name             | Type                        | Description                                                                                                         |
| ---------------- | --------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `allow`          | boolean                     | ステータスバーの色適用可否                                                                                                     |
| `statusBarColor` | **'@'ColorInt**(`nullable`) | <p>ステータスバーの背景色<br><code>デフォルト値: Color.WHITE</code></p>                                                           |
| `isWindowLight`  | boolean(`nullable`)         | <p>ステータスバーのテキスト色設定<br><code>デフォルト値: false</code><br><code>true: 暗い色のテキスト</code><br><code>false: 明るい色のテキスト</code></p> |

#### 🎈withNotificationOption(config: TreasureConfig.NotificationOption)

{% hint style="info" %}
このオプションを使用するためには、宝島通知サービスSDKの適用が必要です。

-> 宝島通知SDKが適用されていない場合は正常に動作しません。

***

通知サービスSDKの適用方法については"[plug-notification.md](../plug-notification.md "mention")"ガイドをご参照ください。
{% endhint %}

宝島プッシュ通知を設定します。

:heavy_check_mark: デフォルト値 -> プッシュ通知を使用しません。

⬇ TreasureConfig.NotificationOption

<table><thead><tr><th width="242">Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>allow</code></td><td>boolean</td><td>プッシュ通知使用可否<br><code>デフォルト値: false</code></td></tr><tr><td><code>channelName</code></td><td>string(<code>nullable</code>)</td><td>プッシュ通知チャンネル名<br><code>デフォルト値: '宝島'</code></td></tr><tr><td><code>smallIconResourceId</code></td><td><strong>'@'DrawableRes</strong>(<code>nullable</code>)</td><td>プッシュ通知アイコンリソース<br><code>デフォルト値: 宝島アイコン</code></td></tr></tbody></table>

***
