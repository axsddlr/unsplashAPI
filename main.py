import uvicorn
from fastapi import FastAPI

from api.unsplash import unslph
from ratelimit import limits

app = FastAPI(
    title="Unsplash API",
    description="An Unofficial REST API for Unsplash, Made by [Andre Saddler]("
                "https://github.com/axsddlr)",
    version="1.0.0",
    docs_url="/",
    redoc_url=None,
)

# import class from scrape file
unsplash = unslph()
TWO_MINUTES = 150


@limits(calls=250, period=TWO_MINUTES)
@app.get("/unsplash/s", tags=["Images"])
def unsplash_search(search):
    return unsplash.unsplash_search(search)


@limits(calls=250, period=TWO_MINUTES)
@app.get("/unsplash/t", tags=["Images"])
def unsplash_topics(topics):
    """[topics]\n\n
    food-drink\n
    wallpapers\n
    nature\n
    experimental\n
    people\n
    architecture\n
    current-events\n
    business-work\n
    fashion\n
    film\n
    health-wellness\n
    interiors\n
    street-photography\n
    technology\n
    textures-patterns\n
    travel\n
    covid-19\n
    animals\n
    athletics\n
    spirituality\n
    arts-culture\n
    history\n
    family\n
    friends\n
    relationships\n
    work\n
    bokeh\n
    fill_the_frame\n
    liquid_macro_abstract\n

    """
    return unsplash.unsplash_topics(topics)


@limits(calls=250, period=TWO_MINUTES)
@app.get("/unsplash", tags=["Images"])
def unsplash_main():
    return unsplash.unsplash_main()


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=3000)
