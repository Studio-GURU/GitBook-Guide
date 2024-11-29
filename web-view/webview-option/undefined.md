---
description: 스크린 캡처 방지를 통해 콘텐츠를 보호하는 방법을 안내합니다.
icon: camera-slash
---

# 컨텐츠 보호

## ANDROID

보물섬을 감싸고 있는 Activity에 FLAG\_SECURE 적용을 통해 쉽게 스크린 캡춰 방지를 할 수 있습니다.

{% tabs %}
{% tab title="KOTLIN" %}
<pre class="language-kotlin" data-line-numbers><code class="lang-kotlin">override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
<strong>    window.addFlags(WindowManager.LayoutParams.FLAG_SECURE)
</strong>    //..
    // code
    //..
}
</code></pre>
{% endtab %}

{% tab title="JAVA" %}
<pre class="language-java" data-line-numbers><code class="lang-java">@Override
protected void onCreate(@Nullable Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
<strong>    getWindow().addFlags(WindowManager.LayoutParams.FLAG_SECURE);
</strong>    //..
    // code
    //..
}
</code></pre>
{% endtab %}
{% endtabs %}

***

## iOS

ANDROID 플랫폼과 달리 시스템에서 별도 지원은 되지 않아, `UITextField`의 isSecureTextEntry 속성을 통해 사용자가 스크린 캡춰를 할 수 없도록 우회 처리해야 합니다.

<pre class="language-swift" data-line-numbers><code class="lang-swift"><strong>private let preventedView = UITextField()
</strong>
func applySecureContent() {
    self.addSubview(self.preventedView)
<strong>    self.preventedView.backgroundColor = .clear
</strong><strong>    self.preventedView.isSecureTextEntry = true
</strong><strong>    self.preventedView.isUserInteractionEnabled = false
</strong>    self.preventedView.translatesAutoresizingMaskIntoConstraints = false
    self.preventedView.centerYAnchor.constraint(equalTo: self.centerYAnchor).isActive = true
    self.preventedView.centerXAnchor.constraint(equalTo: self.centerXAnchor).isActive = true
    self.preventedView.leftView = UIView(frame: CGRect(x: 0, y: 0, width: self.preventedView.frame.self.width, height: self.preventedView.frame.self.height))
    self.preventedView.leftViewMode = .always
<strong>    self.layer.superlayer?.addSublayer(self.preventedView.layer)
</strong><strong>    self.preventedView.layer.sublayers?.last?.addSublayer(self.layer)
</strong>}

//..
//..
<strong>override func viewDidAppear(_ animated: Bool) {
</strong>    DispatchQueue.main.async {
        applySecureContent()
    }
}
</code></pre>

