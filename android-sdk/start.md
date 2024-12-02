---
description: トレジャーアイランドANDROID SDKが提供するサービスを連携する前に完了すべき設定について説明します。
icon: star-shooting
---
# はじめに
## 要件
{% hint style="success" %}
**要件仕様はトレジャーアイランドSDKの最新状態を基準として記載されています。**
OSとの互換性のため、最新バージョンへのアップデートを推奨します。
{% endhint %}
:heavy\_check\_mark: Android 5.0（API Level 21）以上を推奨します。
:heavy\_check\_mark: Android Studio -> 3.2以上（最新バージョンのIDEの使用を推奨します）
:heavy\_check\_mark: Android gradle plugin -> 4.0.1以上
:heavy\_check\_mark: Google PlayターゲットAPIレベル -> Compile SDK Version 34（:link:[Google PlayのターゲットAPIレベル要件を満たす](https://developer.android.com/google/play/requirements/target-sdk?hl=ja)）
:heavy\_check\_mark: Kotlin version 1.8.X以上のバージョンを推奨（開発設定1.9.0）
:heavy\_check\_mark: Support AndroidX

***

## 連携キーの発行
{% hint style="info" %}
トレジャーアイランド**ANDROID SDK**を連携するには、連携するアプリの固有識別子（AppId/AppSecret）が必要で、営業担当者を通じて発行されます。
{% endhint %}
| AppID     |   | アプリ固有識別子     |
| --------- | - | -------------- |
| AppSecret |   | アプリ固有識別子検証キー |

***

## リモートリポジトリの設定
**トレジャーアイランドは**:link:[**Cloud-Smith**](https://cloudsmith.com/company/about)**サービスを利用してANDROID SDKを提供しており、該当サービスのリポジトリ設定が必要です。**

{% tabs %}
{% tab title="setting.gradle" %}
**AGP 7.1.0以上またはAndroid Studio Bumblebee以上使用時**
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
**プロジェクトレベルの"build.gradle"ファイルに以下の項目を追加します。**
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
