---
description: 보물섬 iOS SDK 초기화 방법에 대해 안내합니다.
icon: laptop-code
---

# 보물섬 서비스

{% hint style="warning" %}
프로젝트의 AppDelegate에서 **보물섬 iOS SDK 초기화가 진행 됩니다.**

***

초기화가 진행되지 않을경우 보물섬 서비스가 정상 동작하지 않습니다.

:heavy\_check\_mark: [https://developer.apple.com/documentation/uikit/uiapplicationdelegate](https://developer.apple.com/documentation/uikit/uiapplicationdelegate)
{% endhint %}

***

## SDK 초기화 하기

보물섬 SDK 사용을 위한 초기화를 진행합니다.

`AppDelegate`(StoryBoardUI), `App`(SwiftUI) 클래스에서 `SceneKit.Builder`를 통해 SDK를 초기화 하세요.

### SceneKit.Builder

| Name      | Type   | Value           |
| --------- | ------ | --------------- |
| appId     | string | 연동앱의 고유 식별자     |
| appSecret | string | 연동앱의 고유 식별자 검증키 |

:heavy\_check\_mark: **SceneKit.Builder 인스터스를 통해 옵션과 보물섬 SDK 초기화를 진행합니다.**

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
        // option: 로그 출력 여부를 설정
<strong>        .withAllowLog(allow: true)
</strong>        // TreasureKit 인스턴스 생성
        .build()
        // 보물섬 SDK 초기화
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

{% tab title="StoryBoar(App Delegate)" %}
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
        // option: 로그 출력 여부를 설정
        .withAllowLog(allow: true)
        // TreasureKit 인스턴스 생성
        .build()
        // 보물섬 SDK 초기화
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

SDK 로그 출력 여부를 설정 합니다.

✔️ 기본값 -> 로그가 출력되지 않습니다.

| Name       | Type    | Description            |
| ---------- | ------- | ---------------------- |
| `allowLog` | boolean | 로그 출력 여부 (`기본값 false`) |

















