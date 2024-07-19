from fastapi import FastAPI, Request
import httpx

app = FastAPI()


# Gateway Aggregation Pattern: routes requests to appropriate services based on URL prefix
@app.api_route("/{path:path}", methods=["GET", "POST", "PUT", "DELETE"])
async def proxy(request: Request, path: str):
    url_map = {
        "bot": "http://telegram-bot",
        "ticker": "http://ticker-service",
        "news": "http://investment-news-service",
    }
    service = path.split("/")[0]
    url = f"{url_map.get(service, 'http://default-service')}/{path}"

    async with httpx.AsyncClient() as client:
        response = await client.request(
            method=request.method,
            url=url,
            headers=request.headers,
            data=await request.body()
        )
    return response.text


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
