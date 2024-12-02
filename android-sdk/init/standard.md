---
description: トレジャーアイランドANDROID SDKを使用してトレジャーアイランドのメイン画面を起動する方法についてご案内します。
icon: user
---
# トレジャーアイランド
{% hint style="success" %}
パートナー企業の会員が存在しない場合、またはトレジャーアイランドが提供する独自アカウントを使用する場合
***
:heavy\_check\_mark: **トレジャーアイランドの独自アカウントはパートナー企業で使用中のアカウントとは連携されません。**
{% endhint %}
<figure><img src="../../.gitbook/assets/スクリーンショット 2024-08-22 午後 2.05.51.png" alt=""><figcaption><p>トレジャーアイランド会員フロー</p></figcaption></figure>

***

## 準備事項
トレジャーアイランドサービスを利用するためには、:link:[start.md](../start.md "mention") -> :link:[.](./ "mention")の基本設定を完了する必要があります。

***

## 連携手順
1. `Launcher.StandardBuilder` -> `Builder`インスタンスを生成します。
2. `Launcher.StandardBuilder Option`情報を設定します。
3. `Launcher.StandardBuilder build()`関数を呼び出してインスタンスを生成します。
4. 生成された`Launcher`インスタンスを通じて`launch(activity)`関数を呼び出します。

***

## Launcher.StandardBuilder
{% tabs %}
{% tab title="KOTLIN" %}
{% code lineNumbers="true" %}
```kotlin
// ビルダーインスタンスを生成します。
val builder = Launcher.StandardBuilder()
// ADID値を設定します
builder.withAdvertisingId(advertisingId = "00000000-0000-0000-0000-000000000000")
// ヘッダースタイルを設定します。
val headerModel = SceneHeaderModel.Builder()
    // ヘッダータイトル
    .withHeaderTitle(title = "トレジャーアイランド")
    // ヘッダーバックボタン
    .withUseBackButton(use = true)
    // ヘッダークローズボタン
    .withUseCloseButton(use = true)
    .build()
builder.withHeader(headerModel = headerModel)
    
// Launcherインスタンスを生成します。
val launcher = builder.build()
// トレジャーアイランドを起動します。
launcher.launch(
    // アクティビティ
    ownerActivity = {ACTIVITY}, 
    // 結果リスナー
    listener = object : Launcher.Listener {
        override fun onLaunched(success: Boolean) {
            // success: 成功可否            
       }
    }
)
```
{% endcode %}
{% endtab %}

{% tab title="JAVA" %}
{% code lineNumbers="true" %}
```java
// ビルダーインスタンスを生成します。
Launcher.StandardBuilder builder = new Launcher.StandardBuilder();
// ADID値を設定します
builder.withAdvertisingId("00000000-0000-0000-0000-000000000000");
// ヘッダースタイルを設定します。
SceneHeaderModel.Builder headerBuilder = new SceneHeaderModel.Builder();
// ヘッダータイトル（空値の場合タイトル表示されません）
headerBuilder.withHeaderTitle("トレジャーアイランド");
// ヘッダーバックボタン使用
headerBuilder.withUseBackButton(true);
// ヘッダークローズボタン使用
headerBuilder.withUseCloseButton(true);
SceneHeaderModel headerModel = headerBuilder.build();
builder.withHeader(headerModel);
// Launcherインスタンスを生成します。
Launcher launcher = builder.build();
// トレジャーアイランドを起動します。
launcher.launch(
    // アクティビティ
    this, 
    // 結果リスナー
    new Launcher.Listener() {
        @Override
        public void onLaunched(boolean success) {
            // success: 成功可否
        }
    }
);
```
{% endcode %}
{% endtab %}
{% endtabs %}

***

### Options
#### 🎈withAdvertisingId(advertisingId: String)
ANDROID ADIDを設定します。
:heavy\_check\_mark: 設定がない場合、SDKで別途抽出して使用します。
| Name            | Type   | Description    |
| --------------- | ------ | -------------- |
| `advertisingId` | string | Android広告識別子 |

***

#### 🎈withHeader(headerModel: SceneHeaderModel)
:heavy\_check\_mark: None、Back、Close、Custom設定を通じて希望するヘッダーを設定できます。
| Name          | Type               | Description          |
| ------------- | ------------------ | -------------------- |
| `headerModel` | `SceneHeaderModel` | ヘッダー設定データクラス |

{% hint style="success" %}
**設定についての詳細は**[#undefined](options.md#undefined "mention")**ガイドを確認してください。**
{% endhint %}

***

## Launcher.launch
トレジャーアイランドを起動します。状況に応じてトレジャーアイランドのメイン画面または利用規約同意画面が表示されます。
#### 🎈launch(ownerActivity: Activity, listener: Launcher.Listener)
| Name            | Type              | Description        |
| --------------- | ----------------- | ------------------ |
| `ownerActivity` | activity          | Androidアクティビティ  |
| `listener`      | Launcher.Listener | 実行結果リスナー       |

⬇ Launcher.Listener
| Name                           | Description                  |
| ------------------------------ | ---------------------------- |
| `onLaunched(success: Boolean)` | 実行可否が'success'値として伝達されます。 |
