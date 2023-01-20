# Brawl Stars checker
#### Video Demo:  https://youtu.be/S7AwuDgdwX8
#### Description:
Get quick info about Brawl Stars with Brawl Stars checker! Rankings, Events and more.

[Brawl Stars](https://supercell.com/en/games/brawlstars/) is a multiplayer online battle arena and third-person hero shooter video game developed and published by the Finnish video game company Supercell. The game features various game modes, each with a different objective. Players can choose from a selection of Brawlers, which are characters that can be controlled with on-screen joysticks in a game [match](https://en.wikipedia.org/wiki/Brawl_Stars).

All data used in the app is obtained from supercell's Brawl Stars API. This content is not affiliated with, endorsed, sponsored, or specifically approved by Supercell and Supercell is not responsible for it. For more information see Supercell’s Fan Content Policy: www.supercell.com/fan-content-policy.

In the program, classes are used to prompt the user with the available options. In functions, the API is accessed, after validating the data provided by the user. A CSV file is used to validate the country code.

## Download required libraries

```commandline
pip install -r requirements.txt
```

## Add / Change required information

- Token from Brawl Stars API
- Player ID

## Access general brawler information:
- Get list of available brawlers.
- Get information about a brawler.
## Get list of recent battle results for a player
(NOTE: It may take up to 30 minutes for a new battle to appear in the battlelog.)
## Get event rotation for ongoing events
## Access global and local rankings:
- Get player rankings for a country or global rankings.
- Get brawler rankings for a country or global rankings.
- Get club rankings for a country or global rankings.
- Get list of power play seasons for a country or global rankings.