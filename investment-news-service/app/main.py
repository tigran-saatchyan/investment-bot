from fastapi import FastAPI, HTTPException
from app.strategy import NewsStrategy
from app.example_news_strategy import ExampleNewsStrategy

app = FastAPI()
news_strategy: NewsStrategy = ExampleNewsStrategy()

# Strategy Pattern: Delegates the news fetching to the strategy (ExampleNewsStrategy)
@app.get("/news")
async def get_news():
    try:
        data = news_strategy.get_news()
        return {"news": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8003)
