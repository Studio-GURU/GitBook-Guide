---
description: トレジャーアイランドiOS SDKを使用してトレジャーアイランドのメイン画面を起動する方法についてご案内します。
icon: user-group
---

# トレジャーアイランドチャネリング

{% hint style="success" %}
パートナー企業の会員をトレジャーアイランドアカウントと連携して使用する場合
***
提供されたパートナー企業の会員情報を通じてトレジャーアイランドアカウントを作成します。
:heavy\_check\_mark: **パートナー企業のアプリの運用方式に応じて、ログイン状態確認が可能な機能の実装が必要になる場合があります。**
{% endhint %}

<figure><img src="../../.gitbook/assets/image (3).png" alt=""><figcaption><p>チャネリングサービスフロー</p></figcaption></figure>

***

## 準備事項
トレジャーアイランドチャネリングサービスを利用するためには、[start.md](../start.md "mention") -> [.](./ "mention")の基本設定を完了する必要があります。

***

## 連携手順
1. `Launcher.ChannelingBuilder` -> Builderインスタンスを生成します。
2. `Launcher.ChannelingBuilder Option` 会員情報および必要なオプションを設定します。
3. `Launcher.ChannelingBuilder build()`関数を呼び出してインスタンスを生成します。
4. 生成された`Launcher`インスタンスを通じて`launch(completionHandler: (_ success: Bool) -> Void)`関数を呼び出します。

***

## Launcher.ChannelingBuilder
{% code lineNumbers="true" %}
```swift
// BuilderオプションとともにLaunchKitインスタンスを生成します。
let launchKit = LauncherKit.ChannelingBuilder()
    // ユーザー情報を設定します（会員固有キー、性別）
    // ユーザーがログイン状態の場合のみ該当値を設定します。
    .withUserId(userId: "{会員固有キー}")
    .withGender(gender: .male)
    // Option: 広告識別子を設定します。
    .withAdvertisingId(advertisingId: "0000-0000-0000-0000-0000")
    // Launcherインスタンスを生成します。
    .build()
    
// トレジャーアイランドを起動します。
launchKit.launch { completed in
    // completed(bool) 成功可否
}
```
{% endcode %}

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
  * アプリのポリシーに応じてログインユーザーのみアクセスを許可する方法などを柔軟に適用できます。
{% endhint %}

| Name     | Type   | Description        |
| -------- | ------ | ------------------ |
| `userId` | string | パートナー企業会員固有キー |

***

#### 🎈withGender(gender: LauncherKit.Gender)
会員の性別を設定します。
:heavy\_check\_mark: 性別情報の提供が可能な場合、値を設定します。
⬇ LauncherKit.Gender
| Name     | Type                     | Description          |
| -------- | ------------------------ | -------------------- |
| `gender` | enum { `.MALE .FEMALE` } | パートナー企業会員性別情報 |

***

#### 🎈withAdvertisingId(advertisingId: String)
ANDROID ADIDを設定します。
:heavy\_check\_mark: 設定がない場合、SDKで別途抽出して使用します。
| Name            | Type   | Description    |
| --------------- | ------ | -------------- |
| `advertisingId` | string | Android広告識別子 |

***

## Launcher.launch
トレジャーアイランドを起動します。状況に応じてトレジャーアイランドのメイン画面または利用規約同意画面が表示されます。
#### 🎈launch(completionHandler: (\_ success: Bool) -> Void)
:heavy\_check\_mark: completionHandlerのsuccess値はlaunch実行結果を伝達します。
<table><thead><tr><th width="325">Name</th><th width="129">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>success</code></td><td>bool</td><td>実行結果<br><code>true: 成功 / false: 失敗</code></td></tr></tbody></table>

***
