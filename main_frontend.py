import streamlit as st # importing streamlit package
import Trilio_Blockchain_Main as tbm # importing Trilio_Blockchain_Main.py
from datetime import datetime

st. set_page_config(layout="wide") # full screen width for streamlit

st.markdown("<h1 style='text-align: center; color: red;'>Trilio Blockchain</h1>", unsafe_allow_html=True)

# importing variables from main
blockchain = tbm.blockchain 
all_wallets = tbm.all_wallets 
total_wallets = len(all_wallets)
st.subheader("Actions:")

# Wallet creation
st.title('Create a Wallet')
if st.button("Generate a wallet"): # button to run the wallet creating code
    create_wallet = blockchain.Wallet.create_wallet()
    all_wallets.append(create_wallet) # appending every wallet created to a list
    address = create_wallet['address']
    st.text('Your private key is:')
    st.success(address['pve'])

# Wallet Top up
st.title('Top up your wallet')
if total_wallets > 0:
    public_key = st.text_input('Your public key') # taking public key from user input
    credit_amount = st.number_input('Enter the amount') # taking amount of coins from user input to credit
    if st.button('credit your wallet'):
        blockchain.Wallet.credit_wallet(public_key=str(public_key), amount=credit_amount) # crediting the wallet 
else:
    st.text('No wallets available')
st.text(all_wallets)

# Trransfer Coins
st.title('Transfer Funds')
sender_key = st.text_input('Enter your private key') # taking sender's pve 
receiver_address = st.text_input('Enter the receivers public address') # taking receiever's pbc
transfer_amount = st.number_input('Amount to send')
if st.button('Transfer'):
    blockchain.create_transaction(
    datetime.now(),
    data = {
        "type":"token-transfer",
        "data":{
            "to":receiver_address,
            "from":sender_key,
            "amount":transfer_amount
        }
    }
)
    total_transactions = 0
    total_transactions = total_transactions + 1
    st.success('Transaction successfull')

st.text(total_transactions)