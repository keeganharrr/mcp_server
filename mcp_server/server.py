from mcp.server.fastmcp import FastMCP
from nba_api.stats.endpoints import playercareerstats


mcp = FastMCP("my-server")

@mcp.tool()
def add(a: int, b: int):
    return a + b

@mcp.tool()
def booker_stats():
    career = playercareerstats.PlayerCareerStats(player_id="203932")
    df = career.get_data_frames()[0]
    season_2026 = df[df["SEASON_ID"] == "2025-26"].iloc[0]
    gp = season_2026['GP']
    return f"PPG: {round(season_2026['PTS']/gp, 1)}, APG: {round(season_2026['AST']/gp, 1)}, RPG: {round(season_2026['REB']/gp, 1)}"


mcp.run()
