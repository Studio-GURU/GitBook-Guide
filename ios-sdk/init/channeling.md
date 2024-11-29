---
description: 보물섬 iOS SDK를 사용하여 보물섬 메인화면을 실행 방법에 대해 안내합니다.
icon: user-group
---

# 보물섬 채널링

{% hint style="success" %}
파트너사의 회원을 보물섬 계정과 연동하여 사용하고자 하는 경우

***

전달된 파트너사의 회원정보를 통해 보물섬 계정을 생성합니다.&#x20;

:heavy\_check\_mark: **파트너사의 앱의 운영 방식에 따라 로그인 여부 확인이 가능한 기능 구현이 필요 할 수 있습니다.**
{% endhint %}

<figure><img src="../../.gitbook/assets/image (3).png" alt=""><figcaption><p>채널링 서비스 플로우</p></figcaption></figure>

***

## 준비 사항

보물섬 채널링 서비스 이용을 위해서는 [start.md](../start.md "mention") -> [.](./ "mention")의 기본 설정이 완료 되어야 합니다.

***

## 연동 순서

1. `Launcher.ChannelingBuilder` -> Builder 인스턴스를 생성합니다.
2. `Launcher.ChannelingBuilder Option` 회원정보 및 필요한 옵션을 설정합니다.
3. `Launcher.ChannelingBuilder build()` 함수를 호출하여 인스턴스를 생성합니다.
4. 생성된 `Launcher` 인스턴스를 통해 `launch(completionHandler: (_ success: Bool) -> Void)` 함수를 호출 합니다.

***

## Launcher.ChannelingBuilder

{% code lineNumbers="true" %}
```swift
// Builder 옵션과 함께 LaunchKit 인스턴스를 생성합니다.
let launchKit = LauncherKit.ChannelingBuilder()
    // 사용자 정보를 설정합니다 (회원고유키, 성별)
    // 사용자 로그인 상태의 경우만 해당 값을 설정 합니다.
    .withUserId(userId: "{회원고유키}")
    .withGender(gender: .male)
    // Option: 광고 식별자를 설정합니다.
    .withAdvertisingId(advertisingId: "0000-0000-0000-0000-0000")
    // Launcher 인스턴스를 생성합니다.
    .build()
    
// 보물섬을 시작합니다.
launchKit.launch { completed in
    // completed(bool) 성공여부
}
```
{% endcode %}

***

### Options

#### 🎈withUserId(userId: String)

{% hint style="info" %}
**유저의 로그인 상태에 따라 설정합니다.**

***

* 로그인을 필수로 사용하는 앱의 경우
  * 유저의 고유 식별자를 설정합니다.
* 로그인을 필수로 사용하지 않는 앱
  * 별도 값을 설정하지 않으나, SDK에서 로그인 요구에 대한 콜백 처리가 필요합니다.
  * 앱의 정책에 따라 로그인 유저에게만 접근을 허용 하는 방법등을 유연하게 적용 가능합니다.
{% endhint %}

| Name     | Type   | Description |
| -------- | ------ | ----------- |
| `userId` | string | 파트너사 회원 고유키 |

***

#### 🎈withGender(gender: LauncherKit.Gender)

회원의 성별을 설정합니다.

:heavy\_check\_mark: 성별 정보 제공이 가능 할 경우 값을 설정합니다.

⬇ LauncherKit.Gender

| Name     | Type                     | Description   |
| -------- | ------------------------ | ------------- |
| `gender` | enum { `.MALE .FEMALE` } | 파트너사 회원 성별 정보 |

***

#### 🎈withAdvertisingId(advertisingId: String)

&#x20;ANDROID ADID를 설정합니다.

:heavy\_check\_mark: 설정이 없을 경우 SDK에서 별도 추출하여 사용합니다.

| Name            | Type   | Description  |
| --------------- | ------ | ------------ |
| `advertisingId` | string | 안드로이드 광고 식별자 |

***

## Launcher.launch

보물섬을 실행합니다. 상황에 따라 보물섬 메인 화면 또는 약관 동의 화면이 노출 됩니다.

#### 🎈launch(completionHandler: (\_ success: Bool) -> Void)

:heavy\_check\_mark: completionHandler의 success 값은 launch 실행 결과를 전달합니다.

<table><thead><tr><th width="325">Name</th><th width="129">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>success</code></td><td>bool</td><td>success 실행 결과<br><code>true: 성공 / false: 실패</code></td></tr></tbody></table>

***

