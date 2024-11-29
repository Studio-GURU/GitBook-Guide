---
description: 보물섬 ANDROID SDK에서 제공하는 서비스를 연동하기 전 완료해야 하는 설정에 대해 알아 보세요.
icon: star-shooting
---

# 시작하기

## 요구사항

{% hint style="success" %}
**요구 사양은 보물섬 SDK의 최신 상태를 기준으로 명시됩니다.**

OS와의 호환성을 위해 최신 버전으로 업데이트하는 것을 권장합니다.
{% endhint %}

:heavy\_check\_mark: Android 5.0(API Level 21) 이상을 권장합니다.

:heavy\_check\_mark: Android Studio -> 3.2 이상 (최신 버전의 IDE 사용을 권장합니다.)

:heavy\_check\_mark: Android gradle plugin -> 4.0.1 이상

:heavy\_check\_mark: Google Play 타겟 API 수준 -> Compile SDK Version 34(:link:[Google Play의 대상 API 수준 요구사항 충족](https://developer.android.com/google/play/requirements/target-sdk?hl=ko))

:heavy\_check\_mark: Kotlin version 1.8.X 이상의 버전 권장 (개발 설정 1.9.0)

:heavy\_check\_mark: Support AndroidX

***

## 연동키 발급

{% hint style="info" %}
보물섬 **ANDROID SDK**를 연동하려면 연동하려는 앱의 고유 식별자가(AppId/AppSecret) 필요하며 영업  담당자를 통해 발급 전달 됩니다.
{% endhint %}

| AppID     |   | 앱 고유 식별자     |
| --------- | - | ------------ |
| AppSecret |   | 앱 고유 식별자 검증키 |

***

## 원격 저장소 설정

**보물섬은** :link:[**Cloud-Smith**](https://cloudsmith.com/company/about) **서비스를 이용하여 ANDROID SDK를 제공하며, 해당 서비스의 저장소 설정이 필요합니다.**

{% tabs %}
{% tab title="setting.gradle" %}
**AGP 7.1.0 이상 또는 Android Studio Bumblebee 이상 사용시**

{% code title="settings.gradle" lineNumbers="true" %}
```gradle
pluginManagement {
  repositories {
    google()
    mavenCentral()
    gradlePluginPortal()
  }
}
dependencyResolutionManagement {
  repositoriesMode.set(RepositoriesMode.FAIL_ON_PROJECT_REPOS)
  repositories {
    google()
    mavenCentral()
    maven {
      url "https://dl.cloudsmith.io/public/studio-guru/treasureisland-android/maven/"
    }
  }
}
```
{% endcode %}

{% code title="settings.gradle.kts" lineNumbers="true" %}
```gradle
pluginManagement {
  repositories {
    google()
    mavenCentral()
    gradlePluginPortal()
  }
}
dependencyResolutionManagement {
  repositoriesMode.set(RepositoriesMode.FAIL_ON_PROJECT_REPOS)
  repositories {
    google()
    mavenCentral()
    maven {
      url = uri("https://dl.cloudsmith.io/public/studio-guru/treasureisland-android/maven/")
    }
  }
}
```
{% endcode %}
{% endtab %}

{% tab title="build.gralde" %}
**프로젝트 수준의 "build.gradle" 파일에 다음 항목을 추가 합니다.**

{% code lineNumbers="true" %}
```gradle
// build.gradle(project)
allprojects {
  repositories {
    google()
    mavenCentral()
    maven {
      url "https://dl.cloudsmith.io/public/studio-guru/treasureisland-android/maven/"
    }
  }
}
```
{% endcode %}
{% endtab %}
{% endtabs %}
