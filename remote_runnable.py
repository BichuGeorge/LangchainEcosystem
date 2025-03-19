from langserve import RemoteRunnable
chain_remote = RemoteRunnable(
    "http://localhost:5001/chain/c/N4XyA"
)
print(chain_remote.invoke(
    {
        "language": "hindi",
        "text": "What is GenerativeAI"
    }
))