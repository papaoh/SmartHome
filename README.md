# SmartHome

Smart Home 프로젝트

- 3/4 한이음 프로젝트에 참여
- 서로 비슷한 생각을 가진 팀원들이 모여 프로젝트 주제를 정하고 제작
- 3명이서 시작해서 음성인식이 가능한 IoT 환경 구축을 해보자.

Web 구축 + 디바이스 제어 부분을 담당

프로젝트를 진행하면서 만들었지만 실제 프로젝트에는 사용되지 않은 코드들은
테스트 코드로 올릴 예정: 날씨 Api 활용하기, json 데이터 가져오기


# 작품 개요

라즈베리 파이안에 사용자의 명령을 처리해주는 딥러닝 기반의 NLP 어시스턴트 서버와, java기반의 웹 프레임워크인 Spring boot 서버를 만들고, 
핸드폰 어플리케이션을 firebase DB와 연동하여 실내에서는 스마트 미러로 장치를 제어할 수 있고, 
실외에서는 스마트폰으로 집안의 장치들을 제어할 수 있다.


# 주요 기능 및 기술

-	음성인식을 통해 LED, 창문, 블라인드 제어 가능 및 날씨 정보 출력
-	안드로이드 앱 및 웹 서버에서 회원가입을 통해 회원 별 장치제어 가능
-	웹 서버에서 채팅지원 시스템 지원
-	데이터베이스에 연결 장치의 상태 저장
-	사용자 가정 내 연결된 디바이스들의 정보를 웹, 앱 안에서 볼 수 있음.
-	스마트 미러를 통해 화면이 꺼져 있으면 거울 켜져 있으면 모니터로 활용 가능 

# 개발 환경

음성인식
- 개발언어 : python,java
- DB : Firebase
- 사용 라이브러리: pytorch,kocrawl,kochat,Gtts,flask
- 사용된 보드: raspberryPi4 8G

웹UI
- 개발언어: JS,HTML5
- 개발환경: Eclipse
- DB: Firebase
- 사용된 보드: raspberryPi4 8G

앱UI
- 개발언어: JAVA
- 개발환경: Android Studio
- DB: Firebase

IoT장치
- 개발언어: C
- 개발환경: Arduino IDE
- 사용된 보드:esp-8266
- 연결된 센서: LED, 기어모터, PDLC 필름, 릴레이/ 추가예정: 빗물감지 센서, 조도 센서
- DB: Firebase

# 시스템 구성도
![image](https://user-images.githubusercontent.com/116075431/197699175-081d967e-5c20-48cf-b5bc-ebbdf4bbb7f9.png)

# 모니터 UI
![image](https://user-images.githubusercontent.com/116075431/197977836-7c1fe859-79cd-4c2b-8e29-953bea8c1886.png)

# 어플리케이션 UI
![image](https://user-images.githubusercontent.com/116075431/197977967-385f5280-6526-4c6f-8beb-cb8fed4a3a5f.png)

# 창문 하드웨어
![image](https://user-images.githubusercontent.com/116075431/197978036-5e7e19f9-9e10-4902-bc27-30867630b952.png)
 현재 하드웨어 제작중에 있으며 제작이 완료되면 전체적인 사직 업로드 예정

해당 프로젝트는 hyunwoongko님이 올리신 kochat-master와 kocrawl API를 사용하여 자연어처리를 개발하였습니다. 
URL: https://github.com/hyunwoongko/kochat
