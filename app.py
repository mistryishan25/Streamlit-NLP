
import streamlit as st
import time
import pandas as pd
# import convokit

# add session state variables
# if "node_list" not in st.session_state:
#     st.session_state["node_list"] = []

# if "edge_list" not in st.session_state:
#     st.session_state["edge_list"] = []

# to track the no of utterances left in the conversation.
if "index_rows" not in st.session_state:
    #Index to keep track of the rows in the datafrme
    st.session_state["index_rows"] = 0

    # Index yto keep track of the rows in a conversation
    st.session_state["index_utterances"] = 0

# Functional Requirements
st.write(
    '''
'''
)

# Uploading the file
st.write('''# Upload the file here''')
file = st.file_uploader("Upload file", type=['csv'])
if file is not None:
    file_df = pd.read_csv(file)
    file_df[["node_label", "edge_label", "remove"]] = None
    st.write(file_df)

st.write('''# Resource section''')
with st.expander("Click to expand info about the sentence categories"):
    st.write(
        """
        #### Agreement :
            - Agreeing to the point made before
            - Positive example/experience or confirming or acknowledging the made point
        #### Answer : 
            - Any general response to a Question
            - Many comments underneath a question can be Answers,unless they look more like other options
        #### Appreciation
            - Just praise, appreciation or excitement
            - Has less intent of educating others.

        #### Disagreement
            - comment that is correcting, criticizing, contradicting, or objecting. 
            - can also be an experience or story that expresses disagreement 
        #### Elaboration
            - Adding extra relevant information to the previous comment
            - A good test would be if I just add this to the previous comment, the flow of the idea remains intact.
        #### Humour
            - A joke, piece of SaRcAsM or just silly puns
            - Could be a fun story
            - Intent here is just to have fun, for example if that joke supports then it might belong in other category
        #### Negative Reaction
            - attacking or mocking the commenter, or expressing emotions like disgust, derision, or anger
            - Has no intent of adding value or justification or correction
        #### Question
            - Is it a question or a request seeking forfeedback, help, or other kinds of responses.
            - Remember not every comment that ends with a "?" is a question
            - If it ends with a "?" does not mean it is a question
        
        """
    )
with st.expander("Click to expand the relations between the sentences"):
    st.write(
        '''
        #### Asking
            - Ask questions of the other person in a conversation to discover information about them, their situation and what they do or do not know.
        #### Informing
            - Providing information to others helps them understand what you understand and enables them to make informed, sensible decisions.
        #### Asserting
            - Asserting is stating something as if it were true.
            -When a person asserts something, they are also sending a message that they do not want to have an argument whether it is true or not.
        #### Proposing
        #### Summarizing
        #### Checking
        #### Building
        #### Including
        #### Excluding
        #### Self-promotion
        #### Supporting
        #### Disagreeing
        #### Avoiding
        #### Challenging
        #### Attacking
        #### Defendin    
        '''
    )

node_list = []
edge_list = []

if file:
    st.write('''# Labelling section''')
    # What to do when this is the first utterance here
    st.warning(' The title of the conversation')

    with st.form('Node1_input'):
        # st.write(st.session_state["index_utterances"])
        # st.info(file_df.iloc[st.session_state["index_utterances"]][2])
        node = st.selectbox('Node_1', ['Agreement',
                                       'Announcement',
                                       'Answer',
                                       'Appreciation',
                                       'Disagreement',
                                       'Elaboration',
                                       'Humour',
                                       'Negative Reaction',
                                       'Question'], key=1)
        sub1 = st.form_submit_button('Submit 1')
        file_df["node_label"][st.session_state["index_utterances"]] = node
        keep_node1 = st.checkbox('Should we exclude this one?', key=2)
        st.write(keep_node1)
        file_df["remove"][st.session_state]

    # Sanity check
    st.write(file_df)
    with st.form('Node2_input'):
        st.info(""" Utterance 2 """)
        node = st.selectbox('Node_2', ['Agreement',
                                       'Announcement',
                                       'Answer',
                                       'Appreciation',
                                       'Disagreement',
                                       'Elaboration',
                                       'Humour',
                                       'Negative Reaction',
                                       'Question'], key=1)
        sub1 = st.form_submit_button('Submit 2')
        keep_node1 = st.checkbox('Should we excluse this one?', key=2)

    # only show it when the count of the utterances is more than one.
    edge = st.selectbox("What kind of realtionship exists between these sentenes", ['Asking',
                                                                                    'Informing',
                                                                                    'Asserting',
                                                                                    'Proposing',
                                                                                    'Summarizing',
                                                                                    'Checking',
                                                                                    'Building',
                                                                                    'Including',
                                                                                    'Excluding',
                                                                                    'Self-promotion',
                                                                                    'Supporting',
                                                                                    'Disagreeing',
                                                                                    'Avoiding',
                                                                                    'Challenging',
                                                                                    'Attacking',
                                                                                    'Defending'], key=3)

    next = st.button("Next")
    if next:
        st.write("Clicked")
        # if index_utterances + 1 > last_page:
        #     index_utterances = 0
        # else:
        #     index_utterances += 1

    # Stuff to do when it is continous

    # stuff when you reach the end of the file.
