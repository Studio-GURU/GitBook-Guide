---
description: 宝島 ANDROID SDKを使用して宝島のメイン画面を実行する方法についてご案内します。
icon: user-group
---

# 宝島チャネリング

{% hint style="success" %}
パートナー企業の会員を宝島アカウントと連携して使用する場合

***

パートナー企業から提供された会員情報を使用して宝島アカウントを作成します。&#x20;

:heavy_check_mark: **パートナー企業のアプリの運用方式によって、ログイン状態の確認が可能な機能の実装が必要になる場合があります。**
{% endhint %}

<figure><img src="../../.gitbook/assets/image (3).png" alt=""><figcaption><p>チャネリングサービスのフロー</p></figcaption></figure>

***

## 準備事項

宝島チャネリングサービスを利用するためには、:link:[start.md](../start.md "mention") -> :link:[.](./ "mention")の基本設定が完了している必要があります。

***

## 連携手順

1. `Launcher.ChannelingBuilder` -> Builderインスタンスを作成します。
2. `Launcher.ChannelingBuilder Option` 会員情報および必要なオプションを設定します。
3. `Launcher.ChannelingBuilder build()` 関数を呼び出してインスタンスを生成します。
4. 生成された`Launcher`インスタンスを通じて`launch(activity)`関数を呼び出します。

***

## Launcher.ChannelingBuilder

{% tabs %}
{% tab title="KOTLIN" %}
{% code lineNumbers="true" %}
```kotlin
// ビルダーインスタンスを生成します。
val builder = Launcher.ChannelingBuilder()

// ユーザー情報を設定します（会員固有キー、性別）
// ユーザーがログイン状態の場合のみ、該当値を設定します。
builder.withUserId(userId = "{会員固有キー}")
builder.withGender(gender = Launcher.Gender.MALE)

// ADID値を設定します
builder.withAdvertisingId(advertisingId = "00000000-0000-0000-0000-000000000000")

// ヘッダースタイルを設定します。
val headerModel = SceneHeaderModel.Builder()
    .withHeaderTitle(title = "宝島")
    .withHeaderStyle(style = SceneHeaderModel.HeaderStyle.CLOSE)
    .build()    
builder.withHeader(headerModel = headerModel)

// Launcherインスタンスを生成します。
val launcher = builder.build()

// 宝島を実行します。
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
Launcher.ChannelingBuilder builder = new Launcher.ChannelingBuilder();

// ユーザー情報を設定します（会員固有キー、性別）
// ユーザーがログイン状態の場合のみ、該当値を設定します。
builder.withUserId("{会員固有キー}");
builder.withGender(Launcher.Gender.FEMALE);

// ADID値を設定します
builder.withAdvertisingId("00000000-0000-0000-0000-000000000000");

// ヘッダースタイルを設定します。
SceneHeaderModel.Builder headerBuilder = new SceneHeaderModel.Builder();
// ヘッダータイトル（空値の場合タイトルは表示されません）
headerBuilder.withHeaderTitle("宝島");
// ヘッダーバックボタンの使用
headerBuilder.withUseBackButton(true);
// ヘッダークローズボタンの使用
headerBuilder.withUseCloseButton(true);
SceneHeaderModel headerModel = headerBuilder.build();
builder.withHeader(headerModel);

// Launcherインスタンスを生成します。
Launcher launcher = builder.build();

// 宝島を実行します。
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

#### 🎈withUserId(userId: String)

{% hint style="info" %}
**ユーザーのログイン状態に応じて設定します。**

***

* ログインを必須とするアプリの場合
  * ユーザーの固有識別子を設定します。
* ログインを必須としないアプリの場合
  * 別途値を設定しませんが、SDKでログイン要求に対するコールバック処理が必要です。
  * アプリのポリシーに応じて、ログインユーザーのみアクセスを許可する方法などを柔軟に適用できます。
{% endhint %}

| Name     | Type   | Description |
| -------- | ------ | ----------- |
| `userId` | string | パートナー企業会員固有キー |

***

#### 🎈withGender(gender: Launcher.Gender)

会員の性別を設定します。

:heavy_check_mark: 性別情報の提供が可能な場合、値を設定します。

⬇ Launcher.Gender

| Name     | Type                     | Description   |
| -------- | ------------------------ | ------------- |
| `gender` | enum { `.MALE .FEMALE` } | パートナー企業会員の性別情報 |

***

#### 🎈withAdvertisingId(advertisingId: String)

ANDROID ADIDを設定します。

:heavy_check_mark: 設定がない場合、SDKで別途抽出して使用します。

| Name            | Type   | Description  |
| --------------- | ------ | ------------ |
| `advertisingId` | string | Android広告識別子 |

***

#### 🎈withHeader(headerModel: SceneHeaderModel)

:heavy_check_mark: None、Back、Close、Customの設定を通じて希望するヘッダーを設定できます。

| Name          | Type               | Description   |
| ------------- | ------------------ | ------------- |
| `headerModel` | `SceneHeaderModel` | ヘッダー設定データクラス |

{% hint style="success" %}
**設定に関する詳細は** [#undefined](options.md#undefined "mention") **ガイドをご確認ください。**
{% endhint %}

***

## Launcher.launch

宝島を実行します。状況に応じて宝島のメイン画面または利用規約同意画面が表示されます。

#### 🎈launch(ownerActivity: Activity, listener: Launcher.Listener)

| Name            | Type              | Description |
| --------------- | ----------------- | ----------- |
| `ownerActivity` | activity          | Androidアクティビティ |
| `listener`      | Launcher.Listener | 実行結果リスナー |

⬇ Launcher.Listener

| Name                           | Description                  |
| ------------------------------ | ---------------------------- |
| `onLaunched(success: Boolean)` | 実行可否が'success'値として渡されます。 |
