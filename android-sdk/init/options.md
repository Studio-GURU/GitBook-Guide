---
description: 보물섬의 추가 기능에 대해 안내 합니다.
icon: flask-gear
---

# Options

## Header Style

Launcher Builder Option -> withHeader(headerModel: SceneHeaderModel) 설정을 통해 구성

:heavy\_check\_mark: <mark style="color:red;">**설정을 하지 않을 경우 해더는 노출되지 않습니다.**</mark>

### Preset

기본 설정된 값을 사용하여 Header를 구성합니다.

| View Height | Title            | Title Size | Title Style | Title Color |
| ----------- | ---------------- | ---------- | ----------- | ----------- |
| 48.5dp      | option(nullable) | 14dp       | bold        | #212121     |

<figure><img src="../../.gitbook/assets/bmskit_header_preset (1).png" alt=""><figcaption><p>PRESET</p></figcaption></figure>

Back, Close, Title 노출 유무 설정이 가능 하며  "Back & Close" 는 창을 닫는 동일한 동작을 수행합니다.

{% tabs %}
{% tab title="KOTLIN" %}
{% code lineNumbers="true" %}
```kotlin
val headerModel = SceneHeaderModel.Builder()
    // Header Title(빈값 타이틀 노출 되지 않음)
    .withHeaderTitle(title = "보물섬")
    // Header Use Back Button 
    .withUseBackButton(use = true)
    // Header Use Close Button
    .withUseCloseButton(use = true)
    .build()
//...
//...
// Launcher Builder
//...
launcherBuilder.withHeader(headerModel = headerModel)
```
{% endcode %}
{% endtab %}

{% tab title="JAVA" %}
{% code lineNumbers="true" %}
```java
SceneHeaderModel.Builder headerBuilder = new SceneHeaderModel.Builder();
// Header Title(빈값 타이틀 노출 되지 않음)
headerBuilder.withHeaderTitle("보물섬");
// Header Use Back Button
headerBuilder.withUseBackButton(true);
// Header Use Close Button
headerBuilder.withUseCloseButton(true);
SceneHeaderModel headerModel = headerBuilder.build();
//...
// Launcher Builder
//...
launcherBuilder.withHeader(headerModel);
```
{% endcode %}
{% endtab %}
{% endtabs %}

***

### Custom

앱 스타일에 맞는 별도의 헤더를 구성할 수 있습니다.

:heavy\_check\_mark: Header Layout을 구성 합니다.

:heavy\_check\_mark: Header Layout에서 액션을 처리할 R.id 값을 정의 합니다.

<figure><img src="../../.gitbook/assets/bmskit_custom_header.png" alt=""><figcaption><p>CUSTOM HEADER</p></figcaption></figure>

{% tabs %}
{% tab title="KOTLIN" %}
{% code lineNumbers="true" %}
```kotlin
val customHeaderModel = SceneHeaderModel.CustomBuilder()
    // Custom Header Layout-ID
    .withHeaderLayoutId(layoutId = R.layout.custom_header_view)
    // Custom Header Layout Action View Id & Action(Click)
    .addHeaderAction(actionViewId = R.id.button_custom_header_back, action = object: SceneHeaderModel.IHeaderAction {
        override fun onAction(activity: Activity, webView: WebView?) {
            activity.finish()
        }
    })
    .build()
//...
//...
// Launcher Builder
//...
launcherBuilder.withHeader(headerModel = customHeaderModel)
```
{% endcode %}
{% endtab %}

{% tab title="JAVA" %}
{% code lineNumbers="true" %}
```java
SceneHeaderModel.CustomBuilder customBuilder = new SceneHeaderModel.CustomBuilder();
customBuilder.withHeaderLayoutId(R.layout.custom_header_view);
customBuilder.addHeaderAction(R.id.button_custom_header_back, new SceneHeaderModel.IHeaderAction() {
    @Override
    public void onAction(@NonNull Activity activity, @Nullable WebView webView)
        activity.finish();
    }
});
SceneHeaderModel.CustomBuilder customModel = customBuilder.build();
//...
//...
// Launcher Builder
//...
launcherBuilder.withHeader(customModel);
```
{% endcode %}
{% endtab %}
{% endtabs %}





***

