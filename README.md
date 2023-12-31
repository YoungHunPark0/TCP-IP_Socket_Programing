# TCP-IP_Socket_Programing
TCP/IP 소켓 프로그래밍

## 1일차
- TCP/IP 소켓 프로그래밍 학습
	- PuTTY 설치
	- 소켓의 생성과정
		- 1. 소켓 생성 - socket 함수호출
			- int socket(int domain, int type, int protocol);
				- domain : 소켓이 사용할 프로토콜 체계 정보 전달
				- type : 소켓의 데이터 전송방식에 대한 정보 전달
				- protocol : 두 컴퓨터간 통신에 사용되는 프로토콜 정보 전달
		- 2. IP주소와 Port번호 할당 - bind 함수호출
		- 3. 연결요청 가능상태로 변경 - listen 함수호출
		- 4. 연결요청에 대한 수락 - accept 함수호출
	- 리눅스에서 알아야 할 기본명령어(필수)
		- 폴더 생성 " mkdir
		- 폴더 및 파일 삭제 : rm -fr[삭제할 폴더명/파일]
		- 현재 폴더 확인 : ls
			- -l : 구체적 파일 출력 
			- -a : 숨겨진 파일도 출력
		- 현재 위치 확인 : pwd
		- 기본 편집기 열기 : nano
		- 폴더 이동 : cd[이동할 폴더명]
					  ./ : 현재폴더 ../ : 바로 위 폴더로 이동
		- 기본 폴더 : /home/pi
		- 컴파일 : gcc 파일명.c -o 실행파일명  (실행파일명에는 확장자(c) 안와도됨)
	- 프로토콜 체계 : 생성된 소켓이 사용할 프로토콜의 부류정보
		- PF_INET : IPv4 인터넷 프로토콜 체계 - 4바이트
		- PF_INET6 : IPv6 인터넷 프로토콜 체계 - 16바이트
	- 소켓의 타입
		- 연결지향형 소켓(SOCK_STREAM) : TCP
		- 비 연결지향형 소켓(SOCK_DGRAM) : UDP
	- 클래스 별 네트워크 주소와 호스트 주소의 경계
		- 클래스 A : 0 ~ 127   0~0111 1111   항상 첫비트 0으로 시작 
		- 클래스 B : 128 ~ 191 128~1011 1111 첫두비트는 항상 10으로 시작
		- 클래스 C : 192 ~ 223 192~1101 1111 첫세비트는 항상 110으로 시작
	- 특수한 목적으로 개발되는 컴퓨터를 임베디드라고 한다
	  클라인트에 접속할려면 내가 접속하려는 서버의 주소 필요하다 = > 포트번호 + ip
	- 포트(번호) = 지금 실행되고있는 응용프로그램을      찾아가는 길
	- IP = 내 컴퓨터까지 찾아오는 길
	- 구조체 : 사용자 정의한 기본 자료형(디폴트). 사용자가 하나의 타입을 만든것을 묶어서 만듬.
	구조체를 만들려면 struct 키워드가 반드시 입력.
	- 열거형 : 사용자가 정의한 기본 자료형(정수, 문자, string 등)

## 2일차
- TCP/IP 소켓 프로그래밍 학습
	- 구조체 
		- 멤버 sin_family
			- 주소체계 AF_INET : IPv4 인터넷 프로토콜 적용 주소체계
		- 멤버 sin_port : 16비트 port번호 저장. 단, 네트워크 바이트 순서로 저장
		- 멤버 sin_addr : 32비트 IP주소정보 저장. 단, 네트워크 바이트 순서로 저장. 정확히 파악하기 위해 구조체 in_addr도 함께 봐야함. 32비트 정수자료형으로 인식해도 괜찮음.
		- 멤버 sin_zero : 특별한 의미x. 반드시 0으로 채워야함. 하지못하면 원하는 결과 얻지못함.
	- 주소체계와 데이터 정렬
		- 바이트 순서(Order)와 네트워크 바이트 순서
			- 빅 엔디안(Big Endian)
				- 상위 바이트값을 작은 번지수에 저장
			- 리틀 엔디안(Little Endian)
				- 상위 바위트값을 큰 번지수에 저장
		- 인터넷 주소 초기화
			- memset : 동일한 값으로 byte단위 초기화 할 때 호출 함수
		- 클라이언트의 주소정보 초기화
			- INADDR_ANY - 상수 통해 서버IP주소 할당
	- TCP와 UDP
		- TCP
			- 인터넷 기반 데이터 송수신을 목적으로 설계된 스택(stack)
			- IP기반으로 신뢰성 있는 데이터의 송수신을 위해 "흐름제어(Flow Control)"
			- 큰문제를 작게 나눠서 계층화한 결과
			- 데이터 송수신 과정을 4개의 영역으로 계층화한 결과.
			- 각 스택별 영역을 전문화하고 표준화함.
			- 7계층으로 세분화, 4계층으로도 표현함.
			- TCP 서버 함수호출 순서
				- socket() 소켓 생성
				- bind() 소켓 주소할당
				- listen() 연결요청 대기상태
				- accept() 연결허용
				- read()/write() 데이터 송수신
				- close() 연결종료
			- TCP 클라이언트 함수호출 순서
				- socket() 소켓 생성과정
				- connect() 연결요청에
				- read()/write() 데이터 송수신
				- close() 연결종료

## 3일차
- TCP/IP 소켓 프로그래밍 학습
	- TCP와 UDP
		- UDP
			- 신뢰할 수 없는 전송방법 제공
			- TCP보다 간결한 구조로 설계된
			- 따라서 신뢰성<성능 중요시한 상황에 좋은선택
			- 흐름제어 x
	- TCP 기반 Half-close
		- 리눅스 close 함수호출, 윈도우 closesocket 함수호출
			- 완전종료를 의마함
				- 데이터 전송, 수신하는것 조차 불가능한 상황
		- Stream : 소켓을 통해 두 호스트가 연결되면, 상호간 데이터 송수신이 가능한 상태
			- 양방향 통신을 위해서는 두개의 스트림이 필요
	- Half-close 사용되는 함수
		- shotdown 함수 : 스트림을 일부 종료하는데 사용
			- SHUT_RD   입력 스트림 종료
			- SHUT_WR   출력 스트림 종료
			- SHUT_RDWR 입출력 스트림 종료

## 4일차
- TCP/IP 소켓 프로그래밍 학습
	- 도메인 : IP를 대신하는 접속 주소
		ex) 222.222.222.2 == www.naver.com
		- gethostbyname 함수의 인자로 도메인 이름정보를 전달하면, 해당 도메인의 서버정보가 hostent 구조체 변수에 채워지고, 그 변수의 주소값이 반환된다.
			- 서버의 IP가 변경될 때마다 컴파일을 다시해야 하는 번거로운 상황이 발생
			- 도메인 이름을 이용해서 서버가 실행될 때마다 IP를 얻어오게 구현
			- h_name 공식 도메인 이름
			- h_aliases 별칭의 도메인 이름
			- h_addrtype 반환된 IP의 정보가 IPv4, IPv6 지원
			- h_length IP주소 크기정보. IPv4=4byte=4저장, IPv6=16byte=16저장
			- h_addr_list 가장 중요한 멤버. 멤버를 통해서 도메인 이름에 대한 IP주소가 정수형태로 반환됨.
	- 프로세스 : 실행되고 있는 프로그램(운영체제 관점에서 실행흐름 구성하는 단위)
		- 프로세스 ID : 운영체제로 부터 ID부여 받음. 2이상 정수형태
		- fock 함수 : 호출한 프로세스 복사본 생성
		- 좀비프로세스
		- 시그널
	- 스레드 : 프로세스 관점에서 실행흐름을 구성하는 단위
		- 멀티스레드
			- 뮤텍스(Mutex) 쓰레드 동시접근 허용하지 않음

웹서버 구현

<img
src="https://raw.githubusercontent.com/YoungHunPark0/TCP-IP_Socket_Programing/main/images/rasptest.png" width="700">

## 5일차
- Python-라즈베리파이
	- python -m venv env 가상환경 설치
	- deactivate 빠져나오기
	- 전역설치 apt get -
	- 가상환경에서 설치 pip install
	- GPIO.PUD_DOWN ON = 1, OFF = 0
	- 0V = ground(GND)
	- PULL UP, PULL DOWN
	
7-Segment 회로도
<img
src="https://raw.githubusercontent.com/YoungHunPark0/TCP-IP_Socket_Programing/main/images/7-segment.jpg" width="700">

## 6일차
- Python-라즈베리파이
	- RPi.GPIO Interrupt
		- 1. 핀설정
			- GPIO.add_event_detect(channel, GPIO.Mode)
			- channel : Pin number
			- GPIO.Mode : RISING or FALLING or BOTH
		- 2. 콜백함수 설정
			- GPIO.add_event_callback(channel, function)
				- channel : Pin number
				- function : call back function
		- 3. 하나의 인터럽트 사용시
			GPIO.add_event_detect(channel, GPIO.Mode, callback=my_callback, (선택 사항) 바운스 시간(밀리초))
			
## 7일차
- Python-라즈베리파이
	- Python3 PyQt5 설치
		- sudo apt-get install python3-pyqt5
		- sudo apt-get install qttools5-dev-tools