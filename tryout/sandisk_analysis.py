import yfinance as yf

# ============================================================
# SETTINGS
# ============================================================

TICKER = "BABA"
TARGET_DATE = "2026-09-24"


# ============================================================
# CREATE STOCK OBJECT
# ============================================================

stock = yf.Ticker(TICKER)


# ============================================================
# 1. GET LATEST 3 NEWS ARTICLES
# ============================================================

print("\n" + "=" * 70)
print(f"LATEST NEWS FOR {TICKER}")
print("=" * 70)

try:
    news = stock.get_news(count=3)

    if not news:
        print("No news found.")

    else:
        for i, article in enumerate(news, start=1):
            content = article.get("content", {})

            title = content.get("title", "No title")

            publisher = content.get(
                "provider", {}
            ).get("displayName", "Unknown publisher")

            published = content.get(
                "pubDate",
                "Unknown date"
            )

            summary = content.get(
                "summary",
                "No summary available"
            )

            print(f"\nNEWS {i}")
            print("-" * 70)
            print(f"Title:     {title}")
            print(f"Publisher: {publisher}")
            print(f"Published: {published}")
            print(f"Summary:   {summary}")

except Exception as e:
    print("Error retrieving news:")
    print(e)


# ============================================================
# 2. GET PRICE DATA FOR 23 AND 24 SEP 2026
# ============================================================

print("\n" + "=" * 70)
print("SANDISK PRICE ACTIVITY - 24 SEP 2026")
print("=" * 70)

try:
    data = stock.history(
        start="2026-09-23",
        end="2026-09-25",
        interval="1d",
        auto_adjust=False
    )

    if len(data) < 2:
        print("Not enough stock data found.")

    else:
        previous_day = data.iloc[-2]
        current_day = data.iloc[-1]

        previous_close = previous_day["Close"]

        open_price = current_day["Open"]
        high_price = current_day["High"]
        low_price = current_day["Low"]
        close_price = current_day["Close"]
        volume = current_day["Volume"]

        # Standard daily % change:
        # previous close -> current close
        daily_change = (
            (close_price - previous_close)
            / previous_close
        ) * 100

        # Intraday movement:
        # open -> close
        intraday_change = (
            (close_price - open_price)
            / open_price
        ) * 100

        # Trading range
        trading_range = high_price - low_price

        trading_range_percent = (
            trading_range
            / low_price
        ) * 100

        print(f"Previous Close: ${previous_close:.2f}")
        print(f"Open:           ${open_price:.2f}")
        print(f"High:           ${high_price:.2f}")
        print(f"Low:            ${low_price:.2f}")
        print(f"Close:          ${close_price:.2f}")
        print(f"Volume:         {volume:,.0f}")

        print("\n" + "-" * 70)
        print("PRICE MOVEMENT")
        print("-" * 70)

        print(f"Daily Change:       {daily_change:+.2f}%")
        print(f"Open -> Close:      {intraday_change:+.2f}%")
        print(f"Trading Range:      ${trading_range:.2f}")
        print(f"Trading Range %:    {trading_range_percent:.2f}%")

        if daily_change > 0:
            print("Direction:           UP")

        elif daily_change < 0:
            print("Direction:           DOWN")

        else:
            print("Direction:           UNCHANGED")


        # ====================================================
        # 3. SIMPLE AUTOMATIC INTERPRETATION
        # ====================================================

        print("\n" + "=" * 70)
        print("SIMPLE ANALYSIS")
        print("=" * 70)

        if daily_change >= 5:
            momentum = "Very Strong Positive"

        elif daily_change >= 2:
            momentum = "Strong Positive"

        elif daily_change > 0:
            momentum = "Slightly Positive"

        elif daily_change <= -5:
            momentum = "Very Strong Negative"

        elif daily_change <= -2:
            momentum = "Strong Negative"

        elif daily_change < 0:
            momentum = "Slightly Negative"

        else:
            momentum = "Neutral"

        print(f"Momentum: {momentum}")

        if intraday_change < 0:
            print(
                "Intraday behaviour: Stock closed below its opening price."
            )

        elif intraday_change > 0:
            print(
                "Intraday behaviour: Stock closed above its opening price."
            )

        else:
            print(
                "Intraday behaviour: Stock closed near its opening price."
            )

        if trading_range_percent >= 5:
            print(
                "Volatility: High intraday volatility."
            )

        elif trading_range_percent >= 2:
            print(
                "Volatility: Moderate intraday volatility."
            )

        else:
            print(
                "Volatility: Relatively low intraday volatility."
            )


except Exception as e:
    print("Error retrieving stock price data:")
    print(e)


print("\n" + "=" * 70)
print("ANALYSIS COMPLETE")
print("=" * 70)