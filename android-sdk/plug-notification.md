---
description: 보물섬의 기다리면 무료 모바일 알림을 위한 설정 방법을 안내 합니다.
icon: bell-ring
---

# 보물섬 알림 서비스@PLUG

***

{% hint style="info" %}
**보물섬의 기다무 서비스 사용시 유저에게 푸시 알림을 보내는 기능입니다.**

***

보물섬 알림 서비스는 로컬 푸시로 별도의 서버 연동 작업이 필요하지 않습니다.
{% endhint %}

<figure><img src="../.gitbook/assets/push_setting.png" alt=""><figcaption><p>기다무 알림 설정 예시 화면</p></figcaption></figure>

<figure><img src="../.gitbook/assets/push_notification.png" alt=""><figcaption><p>기다무 알림 예시 화면</p></figcaption></figure>

***

## 기본 모듈 적용 하기

기본 블록을 **앱(모듈) 수준의 "build.gradle"** 파일에 설정하세요.

{% hint style="info" %}
최신 버전 사용을 권장하며, :link:[release.md](release.md "mention")를 통해 최신 버전을 확인 하세요.

***

알림서비스(treasureisland-plug-notify) 버전은 **보물섬 기본 모듈의 버전과 동일합니다**.
{% endhint %}

{% code lineNumbers="true" %}
```gradle
dependencies {
  implementation 'kr.co.studioguru.sdk:treasureisland-plug-notify:{SDK-VERSION}'
}
```
{% endcode %}

***

## SDK 초기화 하기

보물섬 SDK 초기화시 withNotificationOption() 설정을 진행합니다.

<mark style="color:red;">생성된 Builder 인스턴스를 통해 옵션과 SDK 초기화를 진행합니다.</mark>

{% tabs %}
{% tab title="KOTLIN" %}
{% code lineNumbers="true" %}
```kotlin
class AppApplication : Application() {
    override fun onCreate() {
        super.onCreate()
        SceneConfig.Builder(...)
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
        TreasureConfig.Builder builder = new TreasureConfig.Builder(...);
        // option 푸시 알림 설정
        builder.withNotificationOption(new TreasureConfig.NotificationOption(
            true,
            "보물섬",
            R.drawable.ic_notify
        ));
        TreasureConfig treasureConfig = builder.build();
        if (treasureConfig != null) {
            treasureConfig.initialize();
        }
    }
}
```
{% endcode %}
{% endtab %}
{% endtabs %}

#### 🎈withNotificationOption(config: SceneConfig.NotificationOption)

기다무 푸시 알림을 설정합니다.

:heavy\_check\_mark: 기본값 -> 푸시 알림을 사용하지 않습니다.

⬇ SceneConfig.NotificationOption

<table><thead><tr><th width="242">Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>allow</code></td><td>boolean</td><td>푸시 알림 사용 여부<br><code>기본값: false</code></td></tr><tr><td><code>channelName</code></td><td>string(<code>nullable</code>)</td><td>푸시 알림 채널명<br><code>기본값: '보물섬'</code></td></tr><tr><td><code>smallIconResourceId</code></td><td><strong>'@'DrawableRes</strong>(<code>nullable</code>)</td><td>푸시 알림 아이콘 리소스<br><code>기본값: 보물섬 아이콘</code></td></tr></tbody></table>

