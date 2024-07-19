from fastapi import FastAPI, HTTPException
from app.strategy import TickerStrategy
from app.yfinance_strategy import YFinanceStrategy

app = FastAPI()
ticker_strategy: TickerStrategy = YFinanceStrategy()

# Strategy Pattern: Delegates the data fetching to the strategy (YFinanceStrategy)
@app.get("/ticker/{symbol}")
async def get_ticker(symbol: str):
    try:
        data = ticker_strategy.get_ticker_data(symbol)
        return {"ticker": symbol, "price": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)
