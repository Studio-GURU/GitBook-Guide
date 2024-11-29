---
icon: bell-on
---

# 애플 앱스토어 실시간 알림 설정

## 참고 자료

{% embed url="https://developer.apple.com/kr/help/app-store-connect/configure-in-app-purchase-settings/enter-server-urls-for-app-store-server-notifications/" %}

***

## 시작하기

1. **App Store Connect → 나의 앱 → 앱 선택 → 일반 정보 → 앱 정보 → App Store 서버 알림**
2. **프로덕션 서버 URL** 또는 **Sandbox 서버 URL(테스트)** → **URL 설정** 선택
3. 알림 URL 입력

### App Store 서버 알림 접근

App Store Connect → 나의 앱 → 앱 선택 → 일반 정보 → 앱 정보 → App Store 서버 알림 → 프로덕션 서버 URL 또는 Sandbox 서버 URL(테스트) → URL 설정 선택

<figure><img src="../../.gitbook/assets/apple_realtime_01.png" alt=""><figcaption></figcaption></figure>

### 서버 URL 입력

<figure><img src="../../.gitbook/assets/apple_realtime_02.png" alt=""><figcaption></figcaption></figure>

{% hint style="success" %}
알림 URL 정보

***

:heavy\_check\_mark:`https://api-iap.cloud.toast.com/callback/subscription/{APP_BUNDLE_ID}/AS/v2`
{% endhint %}

### 서버 URL 확인

<figure><img src="../../.gitbook/assets/apple_realtime_03.png" alt=""><figcaption></figcaption></figure>
