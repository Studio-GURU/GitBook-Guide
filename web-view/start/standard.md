---
description: 보물섬 서비스 연동을 위한 방법을 안내합니다.
icon: user
---

# 보물섬

{% hint style="info" %}
보물섬 연동

***

:heavy\_check\_mark: 파트너사의 회원 정보를 사용하지 않습니다.

:heavy\_check\_mark: 보물섬의 별도 회원 정책을 사용합니다.

:heavy\_check\_mark: 카카오톡 로그인을 사용하며, 관련 설정이 필요합니다.
{% endhint %}

## 메인화면 진 경로

:heavy\_check\_mark: **사용하려는 웹뷰(인앱 브라우져)에 아래의 주소를 호출 합니다.**

`https://{env}.treasurecomics.com/`

***

## 메인화면 진입시 안내 메시지 노출

{% hint style="danger" %}
메인 화면 진입시 아래와 같이 보물섬 서비스 접속에 대한 안내 메시지가 노출 되어야 합니다.

***

:heavy\_check\_mark: message : "**웹툰 사이트로 이동했어요.**"
{% endhint %}

<figure><img src="../../.gitbook/assets/Simulator Screenshot - iPhone 16 Pro - 2024-10-25 at 14.08.11.png" alt=""><figcaption><p>안내 메시지 노출 예시 화면</p></figcaption></figure>

***

## 카카오톡 로그인을 위한 웹뷰 설정

웹뷰에서 카카오톡 Javascript SDK가 올바르게 동작하기 위해서는 아래의 설정이 필요합니다.

### ANDROID

Android 11 이상에서 JavaScript SDK을 이용하여 카카오 로그인과 카카오톡 공유를 사용할 경우, 반드시 **AndroidManifest.xml**에 카카오톡의 패키지명을 명시해야 합니다. 카카오톡 패키지명 미등록 시, Android Framework에서 호출을 차단하여 해당 기능을 사용할 수 없습니다.

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

#### 카카오톡 실행

Android 앱에서 웹뷰를 통해 앱을 실행하려면 `Intent URI`를 이용합니다. 이에 대한 자세한 정보는 :link:[Android Intents with Chrome](https://developer.chrome.com/docs/android/intents)을 참고합니다.

JavaScript SDK가 카카오톡 실행을 위한 `Intent URI`를 생성해 호출합니다. 웹뷰에서는 :link:[WebViewClient#shouldOverrideUrlLoading](https://developer.android.com/reference/android/webkit/WebViewClient#shouldOverrideUrlLoading\(android.webkit.WebView,%20android.webkit.WebResourceRequest\)) 메서드를 오버라이딩(Override)하여 `Intent`를 파싱(Parsing)하고, 해당 `Activity`를 실행해야 합니다.

{% code lineNumbers="true" %}
```kotlin
webView = // 메인 웹뷰

// 공통 설정
webView.settings.run {
    javaScriptEnabled = true
    javaScriptCanOpenWindowsAutomatically = true
    setSupportMultipleWindows(true)
}

webView.webViewClient = object: WebViewClient() {
    override fun shouldOverrideUrlLoading(
        view: WebView,
        request: WebResourceRequest
    ): Boolean {
        Log.d(TAG, request.url.toString())
        if (request.url.scheme == "intent") {
            try {
                // Intent 생성
                val intent = Intent.parseUri(
                    request.url.toString(), 
                    Intent.URI_INTENT_SCHEME
                )
                // 실행 가능한 앱이 있으면 앱 실행
                if (intent.resolveActivity(packageManager) != null) {
                    startActivity(intent)
                    Log.d(TAG, "ACTIVITY: ${intent.`package`}")
                    return true
                }
                // Fallback URL이 있으면 현재 웹뷰에 로딩
                val fallbackUrl = intent.getStringExtra("browser_fallback_url")
                if (fallbackUrl != null) {
                    view.loadUrl(fallbackUrl)
                    Log.d(TAG, "FALLBACK: $fallbackUrl")
                    return true
                }
                Log.e(TAG, "Could not parse anythings")
            } catch (e: URISyntaxException) {
                Log.e(TAG, "Invalid intent request", e)
            }
        }
        // 나머지 서비스 로직 구현
        // ....
        // ....
        // ....
        return false
    }
}
```
{% endcode %}

#### 팝업 웹뷰 처리 { window.open()  window.close() }

{% code lineNumbers="true" %}
```kotlin
webView = // 메인 웹뷰
webViewLayout = // 웹뷰가 속한 레이아웃

// 공통 설정
webView.settings.run {
    javaScriptEnabled = true
    javaScriptCanOpenWindowsAutomatically = true
    setSupportMultipleWindows(true)
}

webView.webChromeClient = object: WebChromeClient() {
    /// ---------- 팝업 열기 ----------
    /// - 카카오 JavaScript SDK의 로그인 기능은 popup을 이용합니다.
    /// - window.open() 호출 시 별도 팝업 webview가 생성되어야 합니다.
    ///
    override fun onCreateWindow(
        view: WebView,
        isDialog: Boolean,
        isUserGesture: Boolean,
        resultMsg: Message
    ): Boolean {
        // 웹뷰 만들기
        var childWebView = WebView(view.context)
        // 부모 웹뷰와 동일하게 웹뷰 설정
        childWebView.run {
            settings.run {
                javaScriptEnabled = true
                javaScriptCanOpenWindowsAutomatically = true
                setSupportMultipleWindows(true)
            }
            layoutParams = view.layoutParams
            webViewClient = view.webViewClient
            webChromeClient = view.webChromeClient
        }
        // 화면에 추가하기
        webViewLayout.addView(childWebView)
        // TODO: 화면 추가 이외에 onBackPressed() 와 같이
        //       사용자의 내비게이션 액션 처리를 위해
        //       별도 웹뷰 관리를 권장함
        //   ex) childWebViewList.add(childWebView)

        // 웹뷰 간 연동
        val transport = resultMsg.obj as WebView.WebViewTransport
        transport.webView = childWebView
        resultMsg.sendToTarget()
        return true
    }
    /// ---------- 팝업 닫기 ----------
    /// - window.close()가 호출되면 앞에서 생성한 팝업 webview를 닫아야 합니다.
    ///
    override fun onCloseWindow(window: WebView) {
        super.onCloseWindow(window)
        // 화면에서 제거하기
        webViewLayout.removeView(window)
        // TODO: 화면 제거 이외에 onBackPressed() 와 같이
        //       사용자의 내비게이션 액션 처리를 위해
        //       별도 웹뷰 array 관리를 권장함
        //   ex) childWebViewList.remove(childWebView)
    }
}
```
{% endcode %}

***

### iOS

#### 카카오톡 실행

iOS 앱의 경우, :link:[유니버설 링크](https://developers.kakao.com/docs/latest/ko/documentation-guideline/glossary#%E3%85%87)가 호출되었을 때는 별도 처리 없이 앱 실행이 가능하지만, :link:[커스텀 URL 스킴](https://developers.kakao.com/docs/latest/ko/documentation-guideline/glossary#%E3%85%8B)이 호출된 경우 해당 URL을 웹뷰에서 `open(_ url:)` 메서드를 호출하여 앱을 실행해야 합니다.

{% code lineNumbers="true" %}
```swift
func webView(
    _ webView: WKWebView, 
    decidePolicyFor navigationAction: WKNavigationAction, 
    decisionHandler: @escaping (WKNavigationActionPolicy) -> Void
    ) { 
    print(navigationAction.request.url?.absoluteString ?? "") 
    // 카카오 SDK가 호출하는 커스텀 URL 스킴인 경우 open(_ url:) 메서드를 호출합니다. 
    if let url = navigationAction.request.url , ["kakaolink"].contains(url.scheme) {
        // 카카오톡 실행 가능 여부 확인 후 실행
        if UIApplication.shared.canOpenURL(url) {
            UIApplication.shared.open(url, options: [:], completionHandler: nil)
        }
        decisionHandler(.cancel) return 
    } 
    // 서비스에 필요한 나머지 로직을 구현합니다. 
    decisionHandler(.allow) 
}
```
{% endcode %}

#### 팝업 웹뷰 처리

{% code lineNumbers="true" %}
```swift
class ViewController: UIViewController, WKUIDelegate, WKNavigationDelegate {
    // 웹뷰 목록 관리
    var webViews = [WKWebView]()
    ...
    /// ---------- 팝업 열기 ----------
    /// - 카카오 JavaScript SDK의 로그인 기능은 popup을 이용합니다.
    /// - window.open() 호출 시 별도 팝업 webview가 생성되어야 합니다.
    ///
    func webView(
        _ webView: WKWebView,
        createWebViewWith configuration: WKWebViewConfiguration,
        for navigationAction: WKNavigationAction,
        windowFeatures: WKWindowFeatures
    ) -> WKWebView? {
        guard let frame = self.webViews.last?.frame else {
            return nil
        }
        // 웹뷰를 생성하여 리턴하면 현재 웹뷰와 parent 관계가 형성됩니다.
        return createWebView(frame: frame, configuration: configuration)
    }

    /// ---------- 팝업 닫기 ----------
    /// - window.close()가 호출되면 앞에서 생성한 팝업 webview를 닫아야 합니다.
    ///
    func webViewDidClose(_ webView: WKWebView) {
        destroyCurrentWebView()
    }

    // 웹뷰 생성 메서드 예제
    func createWebView(
        frame: CGRect, 
        configuration: WKWebViewConfiguration
    ) -> WKWebView {
        let webView = WKWebView(frame: frame, configuration: configuration)       
        // set delegate
        webView.uiDelegate = self
        webView.navigationDelegate = self                
        // 화면에 추가
        self.view.addSubview(webView)
        // 웹뷰 목록에 추가
        self.webViews.append(webView)
        // 그 외 서비스 환경에 최적화된 뷰 설정하기
        // ...
        // ...
        // ...
        return webView
    }

    // 웹뷰 삭제 메서드 예제
    func destroyCurrentWebView() {
        // 웹뷰 목록과 화면에서 제거하기
        self.webViews.popLast()?.removeFromSuperview()
    }
}
```
{% endcode %}

***

## 메인화면

<div align="left"><figure><img src="../../.gitbook/assets/bms_main.png" alt=""><figcaption></figcaption></figure></div>









