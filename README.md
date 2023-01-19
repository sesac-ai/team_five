# team_five

# 1️⃣ 알고리즘 트레이딩

## 알고리즘 트레이딩
    
### 컴퓨터 프로그램을 이용하여 일정한 알고리즘이나 논리구조, 특정 매매기법에 따라 증권, 외환, 파생상품 등의 자산을 자동으로 거래하는 매매 방식이다. 이러한 알고리즘 트레이딩을 하는 사람을 [퀀트 트레이더](http://wiki.hash.kr/index.php?title=%ED%80%80%ED%8A%B8_%ED%8A%B8%EB%A0%88%EC%9D%B4%EB%8D%94&action=edit&redlink=1)(Quantitative Trader)라고 부른다.


#2️⃣ 알고리즘 트레이딩 작동 원리

## 1)API(**Application Programming Interface)**

### **API 의미**

API는 Application Programming Interface(애플리케이션 프로그램 인터페이스)의 줄임말입니다. API의 맥락에서 애플리케이션이라는 단어는 고유한 기능을 가진 모든 소프트웨어를 나타냅니다. 인터페이스는 두 애플리케이션 간의 서비스 계약이라고 할 수 있습니다. 이 계약은 요청과 응답을 사용하여 두 애플리케이션이 서로 통신하는 방법을 정의합니다. API 문서에는 개발자가 이러한 요청과 응답을 구성하는 방법에 대한 정보가 들어 있습니다.

def Future_Hisorical_data(self,stocks,time,start):
        client=self.client
        # client.futures_historical_klines(stocks, time,  start)
        Price_data=pd.DataFrame(client.futures_historical_klines(stocks, time,  start))
        # print(Price_data)
        Price_data[0]=Price_data[0].apply(lambda x : datetime.fromtimestamp(x//1000))
        Price_data=Price_data.iloc[:, :6]
        Price_data.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']
        Price_data=Price_data.set_index('Date')
        return Price_data

## 2) Websockets

WebSocket은  클라이언트와 서버 사이에 지속적인 완전 양방향 연결 스트림을 만들어 주는 기술입니다.

- 상태를 유지하는 프롤토콜(Stateful protocol)이기 때문에  차트 데이터를 빠르게 업데이트 할 수 있습니다.




