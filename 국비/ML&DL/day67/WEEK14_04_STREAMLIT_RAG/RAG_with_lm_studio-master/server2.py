from langchain_core.messages import ChatMessage, HumanMessage, AIMessage, SystemMessage
from langchain_core.embeddings import Embeddings
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_community.vectorstores.utils import DistanceStrategy

from langchain_openai import ChatOpenAI

from langchain.text_splitter import RecursiveCharacterTextSplitter

from openai import OpenAI
from typing import List

import os

RAG_PROMPT_TEMPLATE = "You always answer into Korean. You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question. If you don't know the answer, just say that you don't know. Use three sentences maximum and keep the answer concise.\nQuestion: {question} \nContext: {context} \nAnswer:"

SYS_PROMPT_TEMPLATE = "You are a helpful, smart, kind, and efficient AI assistant. You always fulfill the user's requests to the best of your ability. You always answer succinctly. You must always answer in Korean."

class MyEmbeddings(Embeddings):
    def __init__(self, base_url, api_key="lm-studio"):
        self.client = OpenAI(base_url=base_url, api_key=api_key)

    def embed_documents(self, texts: List[str], model="nomic-ai/nomic-embed-text-v1.5-GGUF") -> List[List[float]]:
        texts = list(map(lambda text:text.replace("\n", " "), texts))
        datas = self.client.embeddings.create(input=texts, model=model).data
        return list(map(lambda data:data.embedding, datas))
        
    def embed_query(self, text: str) -> List[float]:
        return self.embed_documents([text])[0]

# 언어모델
llm = ChatOpenAI(
    base_url="http://localhost:1234/v1",
    api_key="lm-studio",
    model="lmstudio-community/Meta-Llama-3-8B-Instruct-GGUF",
    temperature=0.1,
    )

# 임베딩 모델
emb = MyEmbeddings(base_url="http://localhost:1234/v1")

# 문서 분할
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=200, chunk_overlap=50,
    separators=["\n\n", "\n", "(?<=\. )", " ", ""], length_function=len,
)

# RAG 체인
rag_prompt = ChatPromptTemplate.from_messages([
    ("system", "You always answer into Korean."),
    ("user", RAG_PROMPT_TEMPLATE),
])
rag_chain = rag_prompt | llm | StrOutputParser()

# 일반 채팅 체인
chat_prompt = ChatPromptTemplate.from_messages([
    ("system", SYS_PROMPT_TEMPLATE),
    MessagesPlaceholder(variable_name='messsages1'),
])
chat_chain = chat_prompt | llm | StrOutputParser()

# 파일 -> 벡터저장소
def embed_file(file_path):
    # 문서 불러오고 분할
    file_extension = file_path.split('.')[-1].lower()
    Loader = {'txt': TextLoader, 'pdf': PyPDFLoader}[file_extension]
    docs = Loader(file_path).load_and_split(text_splitter=text_splitter)
    # 벡터화
    vectorstore = FAISS.from_documents(docs, embedding=emb, distance_strategy=DistanceStrategy.COSINE)
    retriever = vectorstore.as_retriever(search_kwargs={'k':10})
    return retriever

# 메인 실행 부분
messages = [
    ChatMessage(role="assistant", content="앞에 '!'(느낌표)를 붙이면 문서검색 후 답변합니다."),
]

# 파일 임베딩 (예: 'sample.txt' 파일을 사용)
file_path = 'd:/sample.txt'  # 실제 파일 경로로 변경해주세요

if os.path.exists(file_path):
    retriever = embed_file(file_path)
    print(f"File '{file_path}' has been embedded.")
else:
    print(f"File '{file_path}' not found. Proceeding without document retrieval.")
    retriever = None

while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit':
        break

    messages.append(ChatMessage(role='user', content=user_input))
    retrieve_flag = user_input[0] == '!'
    if retrieve_flag:
        user_input = user_input[1:]

    if retriever and retrieve_flag:
        format_docs = lambda docs: "\n\n".join(doc.page_content for doc in docs)
        chain = (
            {"context": retriever | format_docs, "question": RunnablePassthrough()}
            | rag_chain
        )
        response = chain.invoke(user_input)
    else:
        response = chat_chain.invoke(messages)

    print("Assistant:", response)
    messages.append(ChatMessage(role='assistant', content=response))

