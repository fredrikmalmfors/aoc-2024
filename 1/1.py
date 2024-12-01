import polars as pl

with open("input", "r+") as file:
    lines = file.read().splitlines()


def get_col(i):
    return sorted(int(x.split("   ")[i]) for x in lines)


df = pl.DataFrame(
    {
        "a": get_col(0),
        "b": get_col(1),
    }
).with_columns(diff=(pl.col("a") - pl.col("b")).abs())

print("part 1:", df.sum().select("diff").item())

ans = (
    df.select("a")
    .join(df.select(a="b").group_by("a").len(), on="a", how="left")
    .fill_null(0)
    .select(res=pl.col("a").mul(pl.col("len")))
    .sum()
    .item()
)

print("part 2:", ans)
