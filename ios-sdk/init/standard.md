---
description: トレジャーアイランドiOS SDKを使用してトレジャーアイランドのメイン画面を起動する方法についてご案内します。
icon: user
---
# トレジャーアイランド
{% hint style="success" %}
パートナー企業の会員が存在しない場合、またはトレジャーアイランドが提供する独自アカウントを使用する場合
***
✔ **トレジャーアイランドの独自アカウントはパートナー企業で使用中のアカウントとは連携されません。**
{% endhint %}
<figure><img src="../../.gitbook/assets/スクリーンショット 2024-08-22 午後 2.05.51.png" alt=""><figcaption></figcaption></figure>

***

## 準備事項
トレジャーアイランドサービスを利用するためには、[start.md](../start.md "mention") -> [.](./ "mention")の基本設定を完了する必要があります。

***

## 連携手順
1. `Launcher.StandardBuilder` -> `Builder`インスタンスを生成します。
2. `Launcher.StandardBuilder Option`情報を設定します。
3. `Launcher.StandardBuilder build()`関数を呼び出してインスタンスを生成します。
4. 生成された`Launcher`インスタンスを通じて`launch(completionHandler: (_ success: Bool) -> Void)`関数を呼び出します。

***

## Launcher.StandardBuilder
{% code lineNumbers="true" %}
```swift
// Builder オプションと共にLaunchKitインスタンスを生成します。
let launchKit = LauncherKit.StandardBuilder()
    // Option: 広告識別子を設定します。
    .withAdvertisingId(advertisingId: "0000-0000-0000-0000-0000")
    .build()
// トレジャーアイランドを起動します。
launchKit.launch { completed in
    // completed(bool) 成功可否
}
```
{% endcode %}

***

### Options
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
