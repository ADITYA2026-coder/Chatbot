# import streamlit as st

# with st.chat_message('user'):
#      st.text('Hi')

# with st.chat_message('assistant'):
#      st.text('How can i help you?')

# with st.chat_message('user'):
#      st.text('Aditya')

# user_input=st.chat_input('Type here') # Creating the component where user can interact with chatbot

# if user_input:            
#      with st.chat_message('user'):
#         st.text(user_input)           $ this will print whatever user has written in text box on screen



# Now in this part our aim is that if user writes "CR7" then assistant should reply "CR7" Bascially same output as input

# import streamlit as st
# message_history = []

# for message in message_history:
#      with st.chat_message(message['role']):
#           st.text(message['content'])

# user_input=st.chat_input('Type here')

# if user_input:
#     # first add the message to message_history
#     message_history.append('role':'user','content':user_input)
#     with st.chat_message('user'):
#         st.text(user_input)
#     # now chatbot will reply whatever user has written
#     message_history.append{'role':'user','content':user_input}
#     with st.chat_message('assistent'):
#             st.text(user_input)

# The problem with this code is that when we 'message_history = []' then everything gets reset . So we use concept of session state in streamlit

import streamlit as st
from langraph_backend import chatbot 
from langchain_core.messages import HumanMessage

CONFIG={'configurable':{'thread_id':'thread-1'}}

if 'message_history' not in st.session_state:
     st.session_state['message_history']=[]
# Loading conversation history
for message in  st.session_state['message_history']:
     with st.chat_message(message['role']):
          st.text(message['content'])

user_input=st.chat_input('Type here')

if user_input:
    # first add the user message to message_history, and then display to ui
    st.session_state['message_history'].append({'role':'user','content':user_input})
    with st.chat_message('user'):
        st.text(user_input)

    response = chatbot.invoke({'messages':[HumanMessage(content=user_input)]},config=CONFIG)
    ai_message=response['messages'][-1].content
    # now chatbot will reply whatever user has written
    st.session_state['message_history'].append({'role':'assistant','content':ai_message})
    with st.chat_message('assistant'):
            st.text(ai_message)   