---
description: 보물섬 기다리면 무료 컨텐츠의 모바일 알림을 위한 설정 방법을 안내 합니다.
icon: bell-ring
---

# 보물섬 알림 서비스@PLUG

***

{% hint style="info" %}
**보물섬의 기다무 서비스 사용시 유저에게 푸시 알림을 보내는 기능입니다.**

***

보물섬 알림 서비스는 **로컬 푸시**로 별도의 서버 연동 작업이 필요하지 않습니다.
{% endhint %}

<div><figure><img src="../.gitbook/assets/apple_notify_setting_01.png" alt=""><figcaption><p>기다무 설정 화면</p></figcaption></figure> <figure><img src="../.gitbook/assets/apple_notify_setting_02.png" alt=""><figcaption></figcaption></figure> <figure><img src="../.gitbook/assets/apple_nofity_setting_03.png" alt=""><figcaption></figcaption></figure></div>

***

## 연동 순서

1. **TreasureIslandPlugNotificationKit** 모듈 설치하기&#x20;
2. **TreasureIslandPlugNotificationKit** 모듈 연동하기

***

## 모듈 설 하기

### ![](../.gitbook/assets/cocoapods.png) COCOA PODS

보물섬 SDK를 설치하고자 하는 프로젝트의 Podfile에 다음 항목을 추가 합니다.

{% hint style="success" %}
**모듈 정보**

***

:heavy\_check\_mark: pod 'TreasureIslandFoundationKit', '{SDK-VERSION}'

:heavy\_check\_mark: pod 'TreasureIslandSceneKit', '{SDK-VERSION}'

:heavy\_check\_mark: pod '**TreasureIslandPlugNotificationKit**', '{SDK-VERSION}'
{% endhint %}

{% code lineNumbers="true" %}
```sh
# pod respository url
source 'https://github.com/CocoaPods/Specs.git'
# target project
target '{TARGET-PROJECT}' do
  use_frameworks!
  # 보물섬 필수 SDK
  pod 'TreasureIslandFoundationKit', '{SDK-VERSION}'
  pod 'TreasureIslandSceneKit', '{SDK-VERSION}''
  # 보물섬 알림 서비스 SDK(Notififatioin PLUG)
  pod 'TreasureIslandPlugNotificationKit', '{SDK-VERSION}''
end
```
{% endcode %}

pod install 명령어를 통해 보물섬 SDK를 설치합니다.

```sh
$ pod install
```

### ![](../.gitbook/assets/swiftpackage.png) SWIFT PACKAGE

{% hint style="success" %}
**기본 모듈 적용**

***

:heavy\_check\_mark: [https://github.com/Studio-GURU/TreasureIsland-iOS-Plug-NotificationKit.git](https://github.com/Studio-GURU/TreasureIsland-iOS-Plug-NotificationKit.git)
{% endhint %}

#### Package Dependency 설정

**⬇ Xcode -> File -> Add Package Dependencies...**&#x20;

<figure><img src="../.gitbook/assets/apple_swift_package_01.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/apple_plug_notify.png" alt=""><figcaption></figcaption></figure>

***

## 모듈 연동 하기

보물섬 초기화 부분에 다음 코드를 추가합니다.

{% code lineNumbers="true" %}
```swift
import TreasureIslandFoundationKit
import TreasureIslandSceneKit
// import!!
import TreasureIslandPlugNotificationKit

// SceneKit
let sceneKit = SceneKit.Builder(
    appId: "{APP-ID}", 
    appSecret: "{APP-SECRET}"
)
// option: 로그 출력 여부를 설정
.withAllowLog(allow: true)
// PlugNotificationKit을 추가 합니다.
.withContractorNotification(builder: PlugNotificationKit.builder())
// TreasureKit 인스턴스 생성
.build()
// 보물섬 SDK 초기화
sceneKit.initialize()
```
{% endcode %}





