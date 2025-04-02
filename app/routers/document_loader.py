from dependencies import chroma, record_manager
from fastapi import APIRouter, Body
from langchain.indexes import aindex
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from schemas.document_upload import DocumentUpload

router = APIRouter()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,  # кол-во символов
    chunk_overlap=20,  # наложение между чанками
    length_function=len,
    is_separator_regex=False,
    separators=["\n", "\n\n", "."],
)


@router.post(
    "/load/chroma", description="Простая загрузка содержимого документа в Chroma"
)
async def upload_document(document: DocumentUpload = Body()):
    document: Document = text_splitter.create_documents(
        [document.content], metadatas=[document.metadata]
    )
    ## только добавление в хранилище
    # await chroma.aadd_documents([document])

    # добавление с индексацией
    out = await aindex(document, record_manager=record_manager, vector_store=chroma)

    return out
