---
description: トレジャーアイランドiOS SDKの初期化方法についてご案内します。
icon: laptop-code
---

# トレジャーアイランドサービス

{% hint style="warning" %}
プロジェクトのAppDelegateで**トレジャーアイランドiOS SDKの初期化が行われます。**
***
初期化が行われない場合、トレジャーアイランドサービスが正常に動作しません。
:heavy\_check\_mark: [https://developer.apple.com/documentation/uikit/uiapplicationdelegate](https://developer.apple.com/documentation/uikit/uiapplicationdelegate)
{% endhint %}

***

## SDKの初期化
トレジャーアイランドSDK使用のための初期化を行います。
`AppDelegate`(StoryBoardUI)、`App`(SwiftUI)クラスで`SceneKit.Builder`を通じてSDKを初期化してください。

### SceneKit.Builder
| Name      | Type   | Value              |
| --------- | ------ | ------------------ |
| appId     | string | 連携アプリの固有識別子      |
| appSecret | string | 連携アプリの固有識別子検証キー |
:heavy\_check\_mark: **SceneKit.Builderインスタンスを通じてオプションとトレジャーアイランドSDKの初期化を行います。**

{% tabs %}
{% tab title="Swift UI(App)" %}
<pre class="language-swift" data-line-numbers><code class="lang-swift">import SwiftUI
import TreasureIslandFoundationKit
import TreasureIslandSceneKit
@main
struct PartnerApp: App {
    init() {
        // SceneKit
        let sceneKit = SceneKit.Builder(
            appId: "{APP-ID}", 
            appSecret: "{APP-SECRET}"
        )
        // option: ログ出力の有無を設定
<strong>        .withAllowLog(allow: true)
</strong>        // TreasureKitインスタンスの生成
        .build()
        // トレジャーアイランドSDKの初期化
        treasureKit.initialize()
    }
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
    }
}
</code></pre>
{% endtab %}

{% tab title="StoryBoard(App Delegate)" %}
{% code lineNumbers="true" %}
```swift
import TreasureIslandFoundationKit
import TreasureIslandSceneKit
@main
class AppDelegate: UIResponder, UIApplicationDelegate {
    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
         // SceneKit
        let sceneKit = SceneKit.Builder(
            appId: "{APP-ID}", 
            appSecret: "{APP-SECRET}"
        )
        // option: ログ出力の有無を設定
        .withAllowLog(allow: true)
        // TreasureKitインスタンスの生成
        .build()
        // トレジャーアイランドSDKの初期化
        treasureKit.initialize()        
        return true
    }
}
```
{% endcode %}
{% endtab %}
{% endtabs %}

#### Options <a href="#options" id="options"></a>
**🎈withAllowLog(allowLog: boolean)**
SDKのログ出力有無を設定します。
✔️ デフォルト値 -> ログは出力されません。
| Name       | Type    | Description                |
| ---------- | ------- | -------------------------- |
| `allowLog` | boolean | ログ出力の有無 (`デフォルト値 false`) |

<userStyle>Normal</userStyle>
