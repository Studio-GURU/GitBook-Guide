---
description: 보물섬 iOS SDK를 사용하여 보물섬 메인화면을 실행 방법에 대해 안내합니다.
icon: user
---

# 보물섬

{% hint style="success" %}
파트너사의 회원이 존재하지 않거나, 보물섬에서 제공하는 자체 계정을 사용하고자 하는 경우

***

✔ **보물섬 자체 계정의 경우 파트너사에서 사용중인 계정과 연동되지 않습니다.**
{% endhint %}

<figure><img src="../../.gitbook/assets/스크린샷 2024-08-22 오후 2.05.51.png" alt=""><figcaption></figcaption></figure>

***

## 준비 사항

보물섬 서비스 이용을 위해서는 [start.md](../start.md "mention") -> [.](./ "mention")의 기본 설정이 완료 되어야 합니다.

***

## 연동 순서

1. `Launcher.StandardBuilder` ->`Builder` 인스턴스를 생성합니다.
2. `Launcher.StandardBuilder Option` 정보를 설정합니다.
3. `Launcher.StandardBuilder build()` 함수를 호출하여 인스턴스를 생성합니다.
4. 생성된 `Launcher` 인스턴스를 통해 `launch(completionHandler: (_ success: Bool) -> Void)` 함수를 호출 합니다.

***

## Launcher.StandardBuilder

{% code lineNumbers="true" %}
```swift
// Builder 옵션과 함께 LaunchKit 인스턴스를 생성합니다.
let launchKit = LauncherKit.StandardBuilder()
    // Option: 광고 식별자를 설정합니다.
    .withAdvertisingId(advertisingId: "0000-0000-0000-0000-0000")
    .build()

// 보물섬을 시작합니다.
launchKit.launch { completed in
    // completed(bool) 성공여부
}
```
{% endcode %}

***

### Options

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







