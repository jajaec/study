import streamlit as st

def samsung_finance():    
    import pandas_datareader as pdr
    from datetime import datetime

    st.write('''
    # 삼성전자 주식 데이터
    마감 가격과 거래량을 차트로 보여줍니다!
    ''');

    start = datetime(2022,1,1)
    end = datetime(2022,8,31)

    # https://finance.yahoo.com/quote/005930.KS?p=005930.KS
    df = pdr.get_data_yahoo('005930.KS', start, end)

    if st.checkbox("data show/hide"):
        st.write(df)

    st.line_chart(df.Close)     # 마감가격
    st.line_chart(df.Volume)    # 거래량

def btc_dinance():
    from cryptocmd import CmcScraper
    import plotly.express as px
    from datetime import datetime    

    st.sidebar.header('Menu')

    name = st.sidebar.selectbox('Name', ['BTC', 'ETH', 'USDT'])

    start_date = st.sidebar.date_input('Start date', datetime(2022, 1, 1))
    end_date = st.sidebar.date_input('End date', datetime(2022, 8, 31))

    st.write('# Cryptocurrency Web App ['+name+']')

    # https://coinmarketcap.com
    scraper = CmcScraper(name, start_date.strftime('%d-%m-%Y'), end_date.strftime('%d-%m-%Y'))

    df = scraper.get_dataframe()

    fig_close = px.line(df, x='Date', y=['Open', 'High', 'Low', 'Close'], title='가격')
    fig_Volume = px.line(df, x='Date', y=['Volume'], title='거래량')

    st.plotly_chart(fig_close)
    st.plotly_chart(fig_Volume)

if __name__ == '__main__':
    #samsung_finance()
    btc_dinance()