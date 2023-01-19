# anacond prompt 에서 실행하는 명령어 : streamlit run [파일이름].py
# 사전 준비 파일 : requirement.txt 파일 생성 후 import 모듈 앞이름 적어야함.

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from cryptocmd import CmcScraper
import plotly.express as px
import numpy as np
import cufflinks as cf

tab1, tab2, tab3, tab4, tab5 = st.tabs(['모델 1', '모델 2', '모델 3', '모델 4', '통계']) # tab 사전 설정.

name = st.sidebar.selectbox('Name', ['BTC'])

sevendayago = datetime.today() - timedelta(7)
start_date = st.sidebar.date_input('Start date', sevendayago)
end_date = st.sidebar.date_input('End date', datetime.today())

 
with tab1: # 비트코인 주가데이터랑 PnL 데이터 라인 차트.
        st.write('# 비트코인 주가 데이터')
        scraper = CmcScraper(name, start_date.strftime('%d-%m-%Y'), end_date.strftime('%d-%m-%Y'))
        data = scraper.get_dataframe()
        fig_close = px.line(data, x='Date', y=['Close'], title='가격')
        st.plotly_chart(fig_close)
        st.markdown('### 초기 전략 PnL : 27%, 최종 전략 : 301%')
        df = pd.read_csv('./seo_add.csv').drop(columns='Unnamed: 0') #.set_index('EntryTime')
        # df.Yong=round(df.Yong,2).cumsum()
        # df.Yunseo=round(df.Yunseo,2).cumsum()
        df.Seoho=round(df.Seoho,2).cumsum()
        df.Seoho_proto=round(df.Seoho_proto,2).cumsum()
        # df.Moon= round(df.Moon,2).cumsum()
        # st.write(df.head())
        df=df.iloc[:,0:]
        st.line_chart(df, x= 'EntryTime', y= ['Seoho', 'Seoho_proto'], use_container_width=True)
        

with tab2: 
        st.write('# 비트코인 주가 데이터')
        scraper = CmcScraper(name, start_date.strftime('%d-%m-%Y'), end_date.strftime('%d-%m-%Y'))
        data = scraper.get_dataframe()
        fig_close = px.line(data, x='Date', y=['Close'], title='가격')
        st.plotly_chart(fig_close)
        st.markdown('### 초기 전략 PnL : 20%, 최종 전략 : 1300%')
        df = pd.read_csv('./Yong_add.csv').drop(columns='Unnamed: 0')
        df.Yong=round(df.Yong,2).cumsum()
        df.Yong_proto=round(df.Yong_proto,2).cumsum()
        df=df.iloc[:,0:]
        st.line_chart(df, x= 'EntryTime', y= ['Yong', 'Yong_proto'], use_container_width=True)

        for i in range(1):
                new_rows = np.random.randn(10, 2)
                st.snow()

        

with tab3: 
        st.write('# 비트코인 주가 데이터')
        scraper = CmcScraper(name, start_date.strftime('%d-%m-%Y'), end_date.strftime('%d-%m-%Y'))
        data = scraper.get_dataframe()
        fig_close = px.line(data, x='Date', y=['Close'], title='가격')
        st.plotly_chart(fig_close)
        st.markdown('### 초기 전략 PnL: 1%, 최종 전략 : 1200%')
        df = pd.read_csv('./Yun_add.csv').drop(columns='Unnamed: 0')
        df.Yunseo=round(df.Yunseo,2).cumsum()
        df.Yunseo_proto=round(df.Yunseo_proto,2).cumsum()
        df=df.iloc[:,0:]
        st.line_chart(df, x= 'EntryTime', y= ['Yunseo', 'Yunseo_proto'], use_container_width=True)
        for i in range(1):
                new_rows = np.random.randn(10, 2)
                st.balloons()
                st.snow()

        

with tab4: # 비트코인 주가데이터랑 PnL 데이터 라인 차트.
        st.write('# 비트코인 주가 데이터')
        scraper = CmcScraper(name, start_date.strftime('%d-%m-%Y'), end_date.strftime('%d-%m-%Y'))
        data = scraper.get_dataframe()
        fig_close = px.line(data, x='Date', y=['Close'], title='가격')
        st.plotly_chart(fig_close)
        st.markdown('### 초기 전략 PnL: 26%, 최종 전략 : 705%')
        df = pd.read_csv('./Moon_add.csv').drop(columns='Unnamed: 0') #.set_index('EntryTime')
        # df.Yong=round(df.Yong,2).cumsum()
        # df.Yunseo=round(df.Yunseo,2).cumsum()
        df.Moon=round(df.Moon,2).cumsum()
        df.Moon_proto=round(df.Moon_proto,2).cumsum()
        # df.Moon= round(df.Moon,2).cumsum()
        # st.write(df.head())
        df=df.iloc[:,0:]
        st.line_chart(df, x= 'EntryTime', y= ['Moon', 'Moon_proto'], use_container_width=True)
        # progress_bar = st.progress(0)
        status_text = st.empty()
        for i in range(1):
                new_rows = np.random.randn(10, 2)
                st.balloons()
        
        

with tab5:
        import pandas as pd 

        st.write('# 비트코인 주가 데이터')
        scraper = CmcScraper(name, start_date.strftime('%d-%m-%Y'), end_date.strftime('%d-%m-%Y'))
        data = scraper.get_dataframe()
        fig_close = px.line(data, x='Date', y=['Close'], title='가격')
        st.plotly_chart(fig_close)
        df = pd.read_csv('./real_final.csv').drop(columns='Unnamed: 0') #.set_index('EntryTime')
        df.Yong=round(df.Yong,2).cumsum()
        df.Yunseo=round(df.Yunseo,2).cumsum()
        df.Seoho=round(df.Seoho,2).cumsum()
        df.Moon= round(df.Moon,2).cumsum()
        # st.write(df.head())
        df=df.iloc[:,0:]
        st.markdown('# 전략별 PnL')
        st.line_chart(df, x= 'EntryTime', y= ['Yong', 'Yunseo', 'Seoho', 'Moon'], use_container_width=True)     

        cf.go_offline()
        cf.set_config_file(offline=False, world_readable=True)
        st.markdown('# 전략별 승률')
        st.markdown('## 43%,  38%,   29%,   54%')
        win_df = pd.read_csv('./win_rate.csv').set_index('model')
        bar_fig =win_df[["win_rate", "defeat_rate"]].iplot(kind="bar",
                        barmode="stack",
                        xTitle="model",
                        title="win rate",
                        asFigure=True,
                        opacity=1.0
                        )

        bar_fig
        


#  yong 38 moon 54 yun 29 seo 43






