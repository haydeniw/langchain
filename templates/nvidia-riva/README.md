
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
langchain app new my-app --package nvidia-riva
```

If you want to add this to an existing project, you can just run:

```shell
langchain app add nvidia-riva
```

And add the following code to your `server.py` file:
```python
from nvidia_riva import chain as nvidia_riva

add_routes(app, nvidia_riva, path="/nvidia-riva")
```

**TODO: ask ryan about env variables**

If you DO NOT already have a Riva Speech Server you want to connect to, see [`Riva Speech Server Setup`](##riva-speech-server-setup) section below before proceeding.

If you DO have a Riva Speech Server you want to connect to, edit the connection details in `nvidia_riva/chain.py` by modifying the variable `RIVA_SPEECH_URL="your-host"`

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


## Riva Speech Server Setup

Use this step if you need to create a Riva Speech Server. 

1. Follow the Riva Quick Start setup instructions for [Local Deployment Using Quick Start Scripts](https://docs.nvidia.com/deeplearning/riva/user-guide/docs/quick-start-guide.html#local-deployment-using-quick-start-scripts).

