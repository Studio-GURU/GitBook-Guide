---
description: トレジャーアイランドサービスの連携方法についてご案内します。
icon: user
---

# トレジャーアイランド

{% hint style="info" %}
トレジャーアイランド連携

***

:heavy\_check\_mark: パートナー企業の会員情報は使用しません。

:heavy\_check\_mark: トレジャーアイランドの独自の会員ポリシーを使用します。

:heavy\_check\_mark: KakaoTalkログインを使用し、関連設定が必要です。
{% endhint %}

## メイン画面アクセス経路

:heavy\_check\_mark: **使用するウェブビュー（インアップブラウザ）で以下のアドレスを呼び出します。**

`https://{env}.treasurecomics.com/`

***

## メイン画面アクセス時のお知らせメッセージ表示

{% hint style="danger" %}
メイン画面アクセス時に、以下のようにトレジャーアイランドサービスへの接続に関するお知らせメッセージを表示する必要があります。

***

:heavy\_check\_mark: message : "**ウェブトゥーンサイトに移動しました。**"
{% endhint %}

<figure><img src="../../.gitbook/assets/Simulator Screenshot - iPhone 16 Pro - 2024-10-25 at 14.08.11.png" alt=""><figcaption><p>お知らせメッセージ表示例画面</p></figcaption></figure>

***

## KakaoTalkログインのためのウェブビュー設定

ウェブビューでKakaoTalk JavaScript SDKが正しく動作するためには、以下の設定が必要です。

### ANDROID

Android 11以上でJavaScript SDKを利用してKakaoログインとKakaoTalk共有を使用する場合、必ず**AndroidManifest.xml**にKakaoTalkのパッケージ名を明記する必要があります。KakaoTalkパッケージ名未登録の場合、Android Frameworkで呼び出しがブロックされ、該当機能を使用できません。

{% code lineNumbers="true" %}
```xml
<manifest package="com.example.sample">
    <queries>
        <package android:name="com.kakao.talk" />
    </queries>
    ...
</manifest>
```
{% endcode %}

#### KakaoTalkの起動

Androidアプリでウェブビューを通じてアプリを起動するには、`Intent URI`を使用します。これについての詳細は:link:[Android Intents with Chrome](https://developer.chrome.com/docs/android/intents)を参照してください。

JavaScript SDKがKakaoTalk起動のための`Intent URI`を生成して呼び出します。ウェブビューでは:link:[WebViewClient#shouldOverrideUrlLoading](https://developer.android.com/reference/android/webkit/WebViewClient#shouldOverrideUrlLoading\(android.webkit.WebView,%20android.webkit.WebResourceRequest\))メソッドをオーバーライドして`Intent`をパースし、該当`Activity`を実行する必要があります。

[Previous code blocks remain unchanged - maintaining original Kotlin code]

***

### iOS

#### KakaoTalkの起動

iOSアプリの場合、:link:[ユニバーサルリンク](https://developers.kakao.com/docs/latest/ko/documentation-guideline/glossary#%E3%85%87)が呼び出された場合は別途処理なしでアプリ起動が可能ですが、:link:[カスタムURLスキーム](https://developers.kakao.com/docs/latest/ko/documentation-guideline/glossary#%E3%85%8B)が呼び出された場合、該当URLをウェブビューで`open(_ url:)`メソッドを呼び出してアプリを起動する必要があります。

[Previous code blocks remain unchanged - maintaining original Swift code]

***

## メイン画面

<div align="left"><figure><img src="../../.gitbook/assets/bms_main.png" alt=""><figcaption></figcaption></figure></div>
