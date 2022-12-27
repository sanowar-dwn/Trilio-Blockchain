import streamlit as st # importing streamlit package
import Trilio_Blockchain_Main as tbm # importing Trilio_Blockchain_Main.py

st. set_page_config(layout="wide") # full screen width for streamlit

st.markdown("<h1 style='text-align: center; color: red;'>Trilio Blockchain</h1>", unsafe_allow_html=True)

# importing variables from main
blockchain = tbm.blockchain 
all_wallets = tbm.all_wallets 
total_wallets = len(all_wallets)

st.subheader("Actions:")

if st.button("Generate a wallet"): # button to run the wallet creating code
    create_wallet = blockchain.Wallet.create_wallet()
    address = create_wallet['address']
    all_wallets.append(create_wallet) # appending every wallet created to a list


if total_wallets >= 1:
    public_key = st.text_input('Your public key')
    if st.button('credit your wallet'):
        blockchain.Wallet.credit_wallet(public_key=str(public_key), amount=1000)
        st.text(all_wallets)

st.text(all_wallets)