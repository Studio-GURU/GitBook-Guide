---
description: トレジャーアイランドが提供するサービスをインアップブラウザで連携する際に必要な設定について説明します。
icon: star-shooting
---

# はじめに

## 要件

{% hint style="info" %}
要件はトレジャーアイランドAPIの最新状態を基準として記載されています。
***
OSとの互換性のため、指定されたプラットフォームの要件を確認してください。
{% endhint %}

### ANDROID
:heavy\_check\_mark: Android 5.0（API Level 21）以上を推奨します。
:heavy\_check\_mark: Android Studio -> 3.2以上（最新バージョンのIDEの使用を推奨します）
:heavy\_check\_mark: Android gradle plugin -> 4.0.1以上
:heavy\_check\_mark:️ Google PlayターゲットAPIレベル -> Compile SDK Version 34（:link:[Google PlayのターゲットAPIレベル要件を満たす](https://developer.android.com/google/play/requirements/target-sdk?hl=ja)）
:heavy\_check\_mark:️ Kotlin version 1.8.X以上を推奨（開発設定1.9.0）
:heavy\_check\_mark:️ Support AndroidX

***

### iOS
:heavy\_check\_mark: iOS 15以上のバージョンを推奨します。
:heavy\_check\_mark: Swift 5以上のバージョンを推奨します。
:heavy\_check\_mark: 最新バージョンのXCodeの使用を推奨します（開発基準15.4使用）

***

## 始め方
各OSで使用するインアップウェブビュー（WebView、WKWebView）を使用して、必要なAPIを呼び出して生成されたURLをロードします。ウェブビューの追加構成コードはオプションとして提供されているガイドを確認してください。

### 実行手順
* :link:[recommendation.md](channeling/recommendation.md "mention")
* :link:[recently.md](channeling/recently.md "mention")

***

### ウェブビュー実装ガイド（Optional）
グルーカンパニーではSDKで使用されているウェブビュー実装コードを提供しており、ウェブビュー実装時の参考用として確認してください。
* :link:[webview-option](../webview-option/ "mention")
  * :link:[android-webview.md](../webview-option/webview/android-webview.md "mention")
  * :link:[ios-wkwebview.md](../webview-option/webview/ios-wkwebview.md "mention")
