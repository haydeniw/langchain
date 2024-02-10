
# nvidia-riva

This template performs LLM response generation with streamed audio input using automatic speech recognition (ASR) and streamed output (TTS). NVIDIA Riva is used for ASR and TTS and an NVIDIA chat model is used to generate an LLM response. 

## Environment Setup

You should export your NVIDIA API Key as an environment variable.
If you do not have an NVIDIA API Key, you can create one by following these steps:
1. Create a free account with the [NVIDIA GPU Cloud](https://catalog.ngc.nvidia.com/) service, which hosts AI solution catalogs, containers, models, etc.
2. Navigate to `Catalog > AI Foundation Models > (Model with API endpoint)`.
3. Select the `API` option and click `Generate Key`.
4. Save the generated key as `NVIDIA_API_KEY`. From there, you should have access to the endpoints.

```shell
export NVIDIA_API_KEY=...
```

For instructions on setting up Riva, refer to the section at the bottom.

## Usage

To use this package, you should first have the LangChain CLI installed:

```shell
pip install -U langchain-cli
```

To use the NVIDIA models, install the Langchain NVIDIA AI Endpoints package:
```shell
pip install -U langchain_nvidia_aiplay
```

To create a new LangChain project and install this as the only package, you can do:

```shell
langchain app new my-app --package nvidia-rag-canonical
```

If you want to add this to an existing project, you can just run:

```shell
langchain app add nvidia-rag-canonical
```

And add the following code to your `server.py` file:
```python
from nvidia_riva import chain as nvidia_riva

add_routes(app, nvidia_riva, path="/nvidia-riva")
```

If you want to set up an ingestion pipeline, you can add the following code to your `server.py` file:
```python
from nvidia_rag_canonical import ingest as nvidia_rag_ingest

add_routes(app, nvidia_rag_ingest, path="/nvidia-rag-ingest")
```
Note that for files ingested by the ingestion API, the server will need to be restarted for the newly ingested files to be accessible by the retriever.

(Optional) Let's now configure LangSmith.
LangSmith will help us trace, monitor and debug LangChain applications.
LangSmith is currently in private beta, you can sign up [here](https://smith.langchain.com/).
If you don't have access, you can skip this section


```shell
export LANGCHAIN_TRACING_V2=true
export LANGCHAIN_API_KEY=<your-api-key>
export LANGCHAIN_PROJECT=<your-project>  # if not specified, defaults to "default"
```

If you DO NOT already have a Milvus Vector Store you want to connect to, see `Milvus Setup` section below before proceeding.

If you DO have a Milvus Vector Store you want to connect to, edit the connection details in `nvidia_rag_canonical/chain.py`

If you are inside this directory, then you can spin up a LangServe instance directly by:

```shell
langchain serve
```

This will start the FastAPI app with a server is running locally at
[http://localhost:8000](http://localhost:8000)

We can see all templates at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
We can access the playground at [http://127.0.0.1:8000/nvidia-riva/playground](http://127.0.0.1:8000/nvidia-riva/playground)

We can access the template from code with:

```python
from langserve.client import RemoteRunnable

runnable = RemoteRunnable("http://localhost:8000/nvidia-riva")
```


## Riva Setup

Use this step if you need to create a Riva speech server. 
TODO: finish docs. 
We will first follow the setup instructions (link to riva)

1. 
