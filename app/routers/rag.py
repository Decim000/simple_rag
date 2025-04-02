from dependencies import chroma, llm
from fastapi import APIRouter, Body
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain
from langchain_core.prompts import ChatPromptTemplate
from prompts.rag_prompt import template
from schemas.search_query import SearchQuery

router = APIRouter()


@router.post("/search/rag")
async def rag(search_query: SearchQuery = Body()):
    if search_query.query:
        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", template),
                ("human", "{input}"),
            ]
        )

        retriever = chroma.as_retriever()
        combine_docs_chain = create_stuff_documents_chain(llm, prompt)
        retrieval_chain = create_retrieval_chain(retriever, combine_docs_chain)

        output = await retrieval_chain.ainvoke({"input": search_query.query})

        return output


@router.post("/search/rag/with_meta")
async def rag_with_meta(search_query: SearchQuery = Body()):
    if search_query.metadata:
        filters = []
        for k, v in search_query.metadata.items():
            filters.append({k: v})
        if len(filters) > 0:
            retriever = chroma.as_retriever(search_kwargs={"filter": {"$and": filters}})
        else:
            retriever = chroma.as_retriever()

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", template),
            ("human", "{input}"),
        ]
    )

    combine_docs_chain = create_stuff_documents_chain(llm, prompt)
    retrieval_chain = create_retrieval_chain(retriever, combine_docs_chain)

    output = await retrieval_chain.ainvoke({"input": search_query.query})

    return output
