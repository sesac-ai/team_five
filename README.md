# team_five

# 1️⃣ 알고리즘 트레이딩

## 알고리즘 트레이딩
    
### 컴퓨터 프로그램을 이용하여 일정한 알고리즘이나 논리구조, 특정 매매기법에 따라 증권, 외환, 파생상품 등의 자산을 자동으로 거래하는 매매 방식이다. 이러한 알고리즘 트레이딩을 하는 사람을 [퀀트 트레이더](http://wiki.hash.kr/index.php?title=%ED%80%80%ED%8A%B8_%ED%8A%B8%EB%A0%88%EC%9D%B4%EB%8D%94&action=edit&redlink=1)(Quantitative Trader)라고 부른다.


# 2️⃣ 알고리즘 트레이딩 작동 원리

## 1)API(**Application Programming Interface)**

### **API 의미**

API는 Application Programming Interface(애플리케이션 프로그램 인터페이스)의 줄임말입니다. API의 맥락에서 애플리케이션이라는 단어는 고유한 기능을 가진 모든 소프트웨어를 나타냅니다. 인터페이스는 두 애플리케이션 간의 서비스 계약이라고 할 수 있습니다. 이 계약은 요청과 응답을 사용하여 두 애플리케이션이 서로 통신하는 방법을 정의합니다. API 문서에는 개발자가 이러한 요청과 응답을 구성하는 방법에 대한 정보가 들어 있습니다.


## 2) Websockets

WebSocket은  클라이언트와 서버 사이에 지속적인 완전 양방향 연결 스트림을 만들어 주는 기술입니다.

- 상태를 유지하는 프롤토콜(Stateful protocol)이기 때문에  차트 데이터를 빠르게 업데이트 할 수 있습니다.
- **HTTP**

HTTP는 클라이언트와 서버간 접속을 유지하지 않으며 요청과 응답 형태로 단방향 통신만 가능합니다.

따라서 서버에서 클라이언트로의 요청은 불가능합니다. 또한 요청-응답이 완료되면 수립했던 연결이 닫힙니다.

**WebSocket**

WebSocekt은 서버와 클라이언트 양방향 연결이 이루어지는 통신으로, 클라이언트도 서버로 요청을 보낼 수 도 있고 서버도 클라이언트로 요청을 보낼 수 있습니다.

주식데이터는 실시간으로 데이터를 주고받아야 하기 때문에 Connection을 자주 맺고 끊는 HTTP 통신보다 WebSocket방식이 더 적합하다.

    def on_open(self,ws): # 소켓이 시작하면 실행될 함수
            print('소켓 시작')
            self.bot.send_message(self.Group_ID, f'소켓 시작.')

# 3️⃣모델
### 1. Model A

RSI(상대강도지수)가 과매수구간에 돌입하면 진입,

 MA(이동평균선)의 dead cross에 도달하면 청산하는 조건.



	import pandas as pd
	import time
	from binance.client import Client
	import time
	from datetime import datetime
	from backtesting import Backtest, Strategy
	from backtesting.lib import crossover
	from backtesting.test import SMA
	import talib as ta

	class SmaCross(Strategy):
	    upper_bound = 70
	    lower_bound = 30
	    def init(self):
		self.rsi = self.I(ta.RSI, self.data.Close, 14)
		self.can_buy = False
		price = self.data.Close
		high_sma = 100
		low_sma = 20
		self.high = self.I(ta.SMA, price, high_sma)
		self.low = self.I(ta.SMA, price, low_sma)
	    # 포지션 사이즈 조절, 손절 라인 확정.
	    def next(self):
		if crossover(self.rsi, self.upper_bound):
		    self.buy(sl=.005*self.data.Close[-1],tp=self.data.Close[-1]*.05+self.data.Close[-1],size=100) 
		    self.can_buy = False
		elif crossover(self.lower_bound, self.rsi): 
		    self.position.close()
		    self.can_buy = True
		if crossover(self.low,self.high):
		    self.position.close()





