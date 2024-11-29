---
description: 보물섬 ANDROID SDK를 사용하여 보물섬 메인화면을 실행 방법에 대해 안내합니다.
icon: user
---

# 보물섬

{% hint style="success" %}
파트너사의 회원이 존재하지 않거나, 보물섬에서 제공하는 자체 계정을 사용하고자 하는 경우

***

:heavy\_check\_mark: **보물섬 자체 계정의 경우 파트너사에서 사용중인 계정과 연동되지 않습니다.**
{% endhint %}

<figure><img src="../../.gitbook/assets/스크린샷 2024-08-22 오후 2.05.51.png" alt=""><figcaption><p>보물섬 회원 플로우</p></figcaption></figure>

***

## 준비 사항

보물섬 서비스 이용을 위해서는 :link:[start.md](../start.md "mention") -> :link:[.](./ "mention")의 기본 설정이 완료 되어야 합니다.

***

## 연동 순서

1. `Launcher.StandardBuilder` ->`Builder` 인스턴스를 생성합니다.
2. `Launcher.StandardBuilder Option` 정보를 설정합니다.
3. `Launcher.StandardBuilder build()` 함수를 호출하여 인스턴스를 생성합니다.
4. 생성된 `Launcher` 인스턴스를 통해 `launch(activity)` 함수를 호출 합니다.

***

## Launcher.StandardBuilder

{% tabs %}
{% tab title="KOTLIN" %}
{% code lineNumbers="true" %}
```kotlin
// 빌더 인스턴스를 생성합니다.
val builder = Launcher.StandardBuilder()

// ADID값을 설정합니다
builder.withAdvertisingId(advertisingId = "00000000-0000-0000-0000-000000000000")

// Header 스타일을 설정합니다.
val headerModel = SceneHeaderModel.Builder()
    // Header Title
    .withHeaderTitle(title = "보물섬")
    // Header Back Button
    .withUseBackButton(use = true)
    // Header Close Button
    .withUseCloseButton(use = true)
    .build()
builder.withHeader(headerModel = headerModel)
    
// Launcher 인스턴스를 생성합니다.
val launcher = builder.build()

// 보물섬을 실행 합니다.
launcher.launch(
    // 액티비티
    ownerActivity = {ACTIVITY}, 
    // 결과 리스너
    listener = object : Launcher.Listener {
        override fun onLaunched(success: Boolean) {
            // success: 성공 여부            
       }
    }
)
```
{% endcode %}
{% endtab %}

{% tab title="JAVA" %}
{% code lineNumbers="true" %}
```java
// 빌더 인스턴스를 생성합니다.
Launcher.StandardBuilder builder = new Launcher.StandardBuilder();

// ADID값을 설정합니다
builder.withAdvertisingId("00000000-0000-0000-0000-000000000000");

// Header 스타일을 설정합니다.
SceneHeaderModel.Builder headerBuilder = new SceneHeaderModel.Builder();
// Header Title(빈값 타이틀 노출 되지 않음)
headerBuilder.withHeaderTitle("보물섬");
// Header Use Back Button
headerBuilder.withUseBackButton(true);
// Header Use Close Button
headerBuilder.withUseCloseButton(true);
SceneHeaderModel headerModel = headerBuilder.build();
builder.withHeader(headerModel);

// Launcher 인스턴스를 생성합니다.
Launcher launcher = builder.build();

// 보물섬을 실행 합니다.
launcher.launch(
    // 액티비티
    this, 
    // 결과 리스너
    new Launcher.Listener() {
        @Override
        public void onLaunched(boolean success) {
            // success: 성공 여부
        }
    }
);
```
{% endcode %}
{% endtab %}
{% endtabs %}

***

### Options

#### 🎈withAdvertisingId(advertisingId: String)

&#x20;ANDROID ADID를 설정합니다.

:heavy\_check\_mark: 설정이 없을 경우 SDK에서 별도 추출하여 사용합니다.

| Name            | Type   | Description  |
| --------------- | ------ | ------------ |
| `advertisingId` | string | 안드로이드 광고 식별자 |

***

#### 🎈withHeader(headerModel: SceneHeaderModel)

:heavy\_check\_mark: None, Back, Close, Custom 설정을 통해 원하는 해더를 설정 할 수 있습니다.

| Name          | Type               | Description   |
| ------------- | ------------------ | ------------- |
| `headerModel` | `SceneHeaderModel` | 해덩 설정 데이타 클래스 |

{% hint style="success" %}
**설정에 대한 자세한 내용은** [#undefined](options.md#undefined "mention") **가이드를 확인 바랍니다.**
{% endhint %}

***

## Launcher.launch

보물섬을 실행합니다. 상황에 따라 보물섬 메인 화면 또는 약관 동의 화면이 노출 됩니다.

#### 🎈launch(ownerActivity: Activity, listener: Launcher.Listener)

| Name            | Type              | Description |
| --------------- | ----------------- | ----------- |
| `ownerActivity` | activity          | 안드로이드 액티비티  |
| `listener`      | Launcher.Listener | 실행 결과 리스너   |

⬇ Launcher.Listener

| Name                           | Description                  |
| ------------------------------ | ---------------------------- |
| `onLaunched(success: Boolean)` | 실행 여부가 'success' 값으로 전달 됩니다. |

