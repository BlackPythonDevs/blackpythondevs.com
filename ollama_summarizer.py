from rich.progress import track
import pathlib
import frontmatter
from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM
from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders.text import TextLoader
from langchain_text_splitters.character import RecursiveCharacterTextSplitter


llm = OllamaLLM(model="llama3.2")
prompt_template = """Write a subtle description to encourage the reader to read the blog post. 

{text}

---

Instructions:
These are professional updates from Black Python Devs.
Use no more than 200 characters about the content.
Avoid clickbait phrases
Only return the response, no confirmation.
"""
prompt = PromptTemplate(template=prompt_template, input_variables=["text"])
chain = load_summarize_chain(llm=llm, prompt=prompt)

splitter = RecursiveCharacterTextSplitter(
    separators=["\n", ".", "?"],
    keep_separator="end",
    chunk_size=1000,
    chunk_overlap=200,
)

for file in track(pathlib.Path("_posts").glob("*.md"), description="running"):
    fm_file = frontmatter.loads(file.read_text())
    doc = TextLoader(file.absolute()).load()[0]

    if "description" in fm_file.keys():
        continue
    summary = chain.invoke(input=splitter.split_documents([doc]))
    fm_file["description"] = summary["output_text"].strip('"')
    file.write_text(frontmatter.dumps(fm_file))
