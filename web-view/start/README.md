---
description: 보물섬에서 제공하는 서비스를 인앱 브라우저를 통해 연동시 필요한 설정에 대해 알아 보세요.
icon: star-shooting
---

# 시작하기

## 요구사항

{% hint style="info" %}
요구 사항은 보물섬 API의 최신 상태를 기준으로 명시됩니다.

***

OS와의 호환성을 위하여 명시된 플랫폼의 요구사항을 확인 바랍니다.
{% endhint %}

### ANDROID

:heavy\_check\_mark: Android 5.0(API Level 21) 이상을 권장합니다.

:heavy\_check\_mark:Android Studio -> 3.2 이상 (최신 버전의 IDE 사용을 권장합니다.)

:heavy\_check\_mark: Android gradle plugin -> 4.0.1 이상

:heavy\_check\_mark:️ Google Play 타겟 API 수준 -> Compile SDK Version 34(:link:[Google Play의 대상 API 수준 요구사항 충족](https://developer.android.com/google/play/requirements/target-sdk?hl=ko))

:heavy\_check\_mark:️ Kotlin version 1.8.X 이상의 버전 권장 (개발 설정 1.9.0)

:heavy\_check\_mark:️ Support AndroidX

***

### iOS

:heavy\_check\_mark: iOS 15 이상의 버전을 권장합니다.

:heavy\_check\_mark: Swift 5 이상의 버전을 권장합니다.

:heavy\_check\_mark: 최신 버전의 XCode 사용을 권장 합니다. { 개발 기준 15.4 사용)

***

## 시작하기

각 OS에서 사용하는 인앱웹뷰{WebView, WKWebView}를 사용하여, 필요한 API를 호출하여 생성된 URL을 로드 합니다. 웹뷰의 추가 구성 코드는 옵션으로 제공되고 있는 가이드를 확인 바랍니다.

### 실행하기

* :link:[recommendation.md](channeling/recommendation.md "mention")
* :link:[recently.md](channeling/recently.md "mention")

***

### 웹뷰 구현 가이드(Optional)

구루 컴퍼니에서 SDK에서 사용된 웹뷰 구현 코드를 제공하고 있으며, 웹뷰 구현시 참고용으로 확인 바랍니다.

* :link:[webview-option](../webview-option/ "mention")
  * :link:[android-webview.md](../webview-option/webview/android-webview.md "mention")
  * :link:[ios-wkwebview.md](../webview-option/webview/ios-wkwebview.md "mention")









