---
description: 보물섬 ANDROID SDK를 사용하여 보물섬 메인화면을 실행 방법에 대해 안내합니다.
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

보물섬 채널링 서비스 이용을 위해서는 :link:[start.md](../start.md "mention") -> :link:[.](./ "mention")의 기본 설정이 완료 되어야 합니다.

***

## 연동 순서

1. `Launcher.ChannelingBuilder` -> Builder 인스턴스를 생성합니다.
2. `Launcher.ChannelingBuilder Option` 회원정보 및 필요한 옵션을 설정합니다.
3. `Launcher.ChannelingBuilder build()` 함수를 호출하여 인스턴스를 생성합니다.
4. 생성된 `Launcher` 인스턴스를 통해 `launch(activity)` 함수를 호출 합니다.

***

## Launcher.ChannelingBuilder

{% tabs %}
{% tab title="KOTLIN" %}
{% code lineNumbers="true" %}
```kotlin
// 빌더 인스턴스를 생성합니다.
val builder = Launcher.ChannelingBuilder()

// 사용자 정보를 설정합니다 (회원고유키, 성별)
// 사용자 로그인 상태의 경우만 해당 값을 설정 합니다.
builder.withUserId(userId = "{회원고유키}")
builder.withGender(gender = Launcher.Gender.MALE)

// ADID값을 설정합니다
builder.withAdvertisingId(advertisingId = "00000000-0000-0000-0000-000000000000")

// Header 스타일을 설정합니다.
val headerModel = SceneHeaderModel.Builder()
    .withHeaderTitle(title = "보물섬")
    .withHeaderStyle(style = SceneHeaderModel.HeaderStyle.CLOSE)
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
Launcher.ChannelingBuilder builder = new Launcher.ChannelingBuilder();

// 사용자 정보를 설정합니다 (회원고유키, 성별)
// 사용자 로그인 상태의 경우만 해당 값을 설정 합니다.
builder.withUserId("{회원고유키}");
builder.withGender(Launcher.Gender.FEMALE);

// ADID값을 설정합니다
builder.withAdvertisingId("00000000-0000-0000-0000-000000000000");

// Header 스타일을 설정합니다.
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

#### 🎈withGender(gender: Launcher.Gender)

회원의 성별을 설정합니다.

:heavy\_check\_mark: 성별 정보 제공이 가능 할 경우 값을 설정합니다.

⬇ Launcher.Gender

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

