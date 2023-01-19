# team_five_visualization

## streamlit 라이브러리를 사용한 시각화를 진행.




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

![주가 데이터](https://user-images.githubusercontent.com/111418464/213383014-9b83edf5-dc73-4e21-9c5e-f0757610cc42.PNG)

![전략별 PNL](https://user-images.githubusercontent.com/111418464/213382805-a0c2d919-ac9d-480e-8734-97173ad3daaf.PNG)
