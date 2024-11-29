---
icon: google-play
---

# 구글 플레이 스토어

***

{% hint style="success" %}
**보물섬의 유료 재화(유료 이용권)를 인앱 구매(IAP) 기능 입니다.**

***

:heavy\_check\_mark: 기본 모듈 적용 후 별도 코드를 통한 연동 작업은 필요하지 않습니다.

:heavy\_check\_mark: 인앱 구매 기능은 스토어에 유료 결제 관련 설정 및 구글 클라우드 서비스의 계정 정보 설정이 필요합니다.

:heavy\_check\_mark: 보물섬 SDK는 Play 결제 라이브러리 7.0.0을 사용하고 있습니다.

:heavy\_check\_mark: 보물섬 SDK는 소비성 제품만 제공 됩니다.
{% endhint %}

***

## 기본 모듈 적용 하기

기본 블록을 **앱(모듈) 수준의 "build.gradle"** 파일에 설정하세요.

{% hint style="info" %}
최신 버전 사용을 권장하며, :link:[release.md](../../release.md "mention")를 통해 최신 버전을 확인 하세요.

***

인앱 구매(treasureisland-plug-purchase) 버전은 **보물섬 기본 모듈의 버전과 동일합니다**.
{% endhint %}

{% code lineNumbers="true" %}
```gradle
dependencies {
  implementation 'kr.co.studioguru.sdk:treasureisland-plug-purchase:{SDK-VERSION}'
}
```
{% endcode %}

***

## 구글 플레이 구매를 위한 설정 안내

구글 플레이 구매를 위해서는 아래와 같은 설정이 필요합니다.

* [console-config.md](console-config.md "mention")
  * 구글 플레이 스토어 결제 기능 활성화 및 판매 상품 등록
  * 구글 플레이 스토어 재무 데이터 접근 계정 전달
* [api-config.md](api-config.md "mention")
* [rtdn-config.md](rtdn-config.md "mention")
