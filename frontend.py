import streamlit as st
import Trilio_Blockchain_Main as tb

st.title('Trilio BlockChain FrontEnd')
if st.button('Show Wallet'):
    store_wallet = tb.wallet
    st.text(tb.create_wallet(store_wallet))
    st.text(tb.wallet_balance)
