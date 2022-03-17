from src.utils.settings import RIOT_TOKEN

REGIONS = {
    'AMERICAS': 'americas.api.riotgames.com',
    'ASIA': 'asia.api.riotgames.com',
    'EUROPE': 'europe.api.riotgames.com'
}
PLATFORM = {
    'BR1': 'br1.api.riotgames.com',
    'EUN1': 'eun1.api.riotgames.com',
    'EUW1': 'euw1.api.riotgames.com',
    'JP1': 'jp1.api.riotgames.com',
    'KR': 'kr.api.riotgames.com',
    'LA1': 'la1.api.riotgames.com',
    'LA2': 'la2.api.riotgames.com',
    'NA1': 'na1.api.riotgames.com',
    'OC1': 'oc1.api.riotgames.com',
    'TR1': 'tr1.api.riotgames.com',
    'RU': 'ru.api.riotgames.com',
}
QUEUE = ['RANKED_SOLO_5x5', 'RANKED_TFT', 'RANKED_FLEX_SR', 'RANKED_FLEX_IT']
TIER = [
    'CHALLENGER',
    'GRANDMASTER',
    'MASTER',
    'DIAMOND',
    'PLATINUM',
    'GOLD',
    'SILVER',
    'BRONZE',
    'IRON',
]
DIVISION = ['I', 'II', 'III', 'IV']
LANGUAGES = [
    'en_US','cs_CZ','de_DE','el_GR','en_AU','en_GB','en_PH','en_SG','es_AR',
    'es_ES','es_MX','fr_FR','hu_HU','id_ID','it_IT','ja_JP','ko_KR','pl_PL',
    'pt_BR','ro_RO','ru_RU','th_TH','tr_TR','vn_VN','zh_CN','zh_MY','zh_TW'
]
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36', # noqa
    'Accept-Language': 'en-AU,en;q=0.9,pt-BR;q=0.8,pt;q=0.7,en-GB;q=0.6,en-US;q=0.5',
    'Accept-Charset': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://developer.riotgames.com',
    'X-Riot-Token': RIOT_TOKEN
}
ENDPOINTS = {
    'ACCOUNT-V1': [
        '/riot/account/v1/accounts/by-puuid/{puuid}',
        '/riot/account/v1/accounts/by-riot-id/{game_name}/{tag_line}',
        '/riot/account/v1/active-shards/by-game/{game}/by-puuid/{puuid}'
        '/riot/account/v1/accounts/me',
    ],
    'CHAMPION-MASTERY-V4': [
        '/lol/champion-mastery/v4/champion-masteries/by-summoner/{encrypted_summoner_id}', # noqa
        '/lol/champion-mastery/v4/champion-masteries/by-summoner/{encrypted_summoner_id}/by-champion/{champion_id}', # noqa
        '/lol/champion-mastery/v4/scores/by-summoner/{encrypted_summoner_id}',
    ],
    'CHAMPION-V3': [
        '/lol/platform/v3/champion-rotations'
    ],
    'LEAGUE-EXP-V4': [
        '/lol/league-exp/v4/entries/{queue}/{tier}/{division}',
    ],
    'LEAGUE-V4': [
        '/lol/league/v4/challengerleagues/by-queue/{queue}',
        '/lol/league/v4/entries/by-summoner/{encrypted_summoner_id}',
        '/lol/league/v4/entries/{queue}/{tier}/{division}',
        '/lol/league/v4/grandmasterleagues/by-queue/{queue}',
        '/lol/league/v4/leagues/{league_id}',
        '/lol/league/v4/masterleagues/by-queue/{queue}',
    ],
    'LOL-STATUS-V4': [
        '/lol/status/v4/platform-data',
    ],
    'MATCH-V5': [
        '/lol/match/v5/matches/by-puuid/{puuid}/ids',
        '/lol/match/v5/matches/{match_id}',
        '/lol/match/v5/matches/{match_id}/timeline',
    ],
    'SPECTATOR-V4': [
        '/lol/spectator/v4/active-games/by-summoner/{encrypted_summoner_id}',
        '/lol/spectator/v4/featured-games',
    ],
    'SUMMONER-V4': [
        '/lol/summoner/v4/summoners/by-account/{encrypted_account_id}',
        '/lol/summoner/v4/summoners/by-name/{summoner_name}',
        '/lol/summoner/v4/summoners/by-puuid/{encrypted_puuid}',
        '/lol/summoner/v4/summoners/{encryptedSummoner_id}',
        '/lol/summoner/v4/summoners/me',
    ],
}