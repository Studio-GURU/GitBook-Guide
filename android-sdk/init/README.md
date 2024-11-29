---
description: 보물섬 ANDROID SDK 초기화 방법에 대해 안내합니다.
icon: laptop-code
---

# 보물섬 서비스

{% hint style="warning" %}
**Application의 “onCreate()"에서 보물섬 ANDROID SDK 초기화가 진행 됩니다.**
{% endhint %}

사용중인 ":link:[Application Class](https://developer.android.com/reference/android/app/Application)"가 없다면, 신규로 생성후 초기화를 진행하시면 됩니다.

***

## 기본 모듈 적용 하기

기본 블록을 **앱(모듈) 수준의 "build.gradle"** 파일에 설정하세요.

{% hint style="info" %}
최신 버전(:white\_check\_mark: 24.10.4.9) 사용을 권장하며, :link:[release.md](../release.md "mention")를 통해 최신 버전을 확인 하세요.

***

:heavy\_check\_mark: 추가 기능 사용을 위해 보물섬 PLUG 모듈의 추가될 수 있습니다.
{% endhint %}

{% code lineNumbers="true" %}
```gradle
dependencies {
  implementation 'kr.co.studioguru.sdk:treasureisland-scene:{SDK-VERSION}'
}
```
{% endcode %}

***

## SDK 초기화 하기

보물섬 SDK 사용을 위해 초기화를 진행 합니다.

`Application`의 `onCreate()`에서 S`ceneConfig.Builder`를 통해 SDK를 초기화하세요.

### **TreasureConfig.Builder**

| Name        | Value           |
| ----------- | --------------- |
| `context`   | Android Context |
| `appId`     | 연동앱의 고유 식별자     |
| `appSecret` | 연동앱의 공유 식별자 검증키 |

:heavy\_check\_mark: **생성된 Builder 인스턴스를 통해 옵션과 SDK 초기화를 진행합니다.**

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
        // option 로그 출력 여부를 설정합니다.
        .withAllowLog(allowLog = true)
        // option 상태창의 색상을 설정 합니다.
        .withStatusBarOption(
            config = SceneConfig.StatusBarOption(
                allow = true,
                statusBarColor = Color.parseColor("#FF6103"),
                isWindowLight = false
            )
        )
        // option 푸시 알림 설정
        .withNotificationOption(
            config = SceneConfig.NotificationOption(
                allow = true,
                channelName = "알림 채널명",
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
            "보물섬",
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

SDK 로그 출력 여부를 설정 합니다.

:heavy\_check\_mark: 기본값 -> 로그가 출력되지 않습니다.

| Name       | Type    | Description            |
| ---------- | ------- | ---------------------- |
| `allowLog` | boolean | 로그 출력 여부 (`기본값 false`) |

#### 🎈withStatusBarColor(config: TreasureConfig.StatusBarOption)

화면의 상단 상태창의 색상을 설정합니다.

:heavy\_check\_mark: 기본값 -> 안드로이드 기본 설정이 적용됩니다.

⬇ TreasureConfig.StatusBarOption

| Name             | Type                        | Description                                                                                                         |
| ---------------- | --------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `allow`          | boolean                     | 상태창 색상 적용 여부                                                                                                        |
| `statusBarColor` | **'@'ColorInt**(`nullable`) | <p>상태창 배경 색상<br><code>기본값: Color.WHITE</code></p>                                                                   |
| `isWindowLight`  | boolean(`nullable`)         | <p>상태창 텍스트 색상 설정<br><code>기본값: false</code><br><code>true: 어두운 색상의 텍스트</code><br><code>false: 밝은 색상의 텍스트</code></p> |

#### 🎈withNotificationOption(config: TreasureConfig.NotificationOption)

{% hint style="info" %}
해당 옵션을 사용하기 위해서는 하다무 알림 서비스 SDK 적용이 필요합니다.

-> 하다무 알림 SDK 적용이 되어있지 않은 경우 정상 동작하지 않습니다.

***

알림 서비스 SDK 적용 방법에 대해서는 "[plug-notification.md](../plug-notification.md "mention")" 가이드를 참고 바랍니다.
{% endhint %}

기다무 푸시 알림을 설정합니다.

:heavy\_check\_mark: 기본값 -> 푸시 알림을 사용하지 않습니다.

⬇ TreasureConfig.NotificationOption

<table><thead><tr><th width="242">Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>allow</code></td><td>boolean</td><td>푸시 알림 사용 여부<br><code>기본값: false</code></td></tr><tr><td><code>channelName</code></td><td>string(<code>nullable</code>)</td><td>푸시 알림 채널명<br><code>기본값: '보물섬'</code></td></tr><tr><td><code>smallIconResourceId</code></td><td><strong>'@'DrawableRes</strong>(<code>nullable</code>)</td><td>푸시 알림 아이콘 리소스<br><code>기본값: 보물섬 아이콘</code></td></tr></tbody></table>



***

