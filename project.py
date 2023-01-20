import requests
import os
import csv
from tabulate import tabulate
from time import sleep


TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjQ1YWVkNTA3LTAyMDItNGI3Yy1iYjJiLTY2NTdmNDU5MjIzNCIsImlhdCI6MTY2MjUyNzI0MCwic3ViIjoiZGV2ZWxvcGVyLzljNzIzZWQ2LWFlNTMtYjQxNS1kZjZlLTdkNWNiNzZiMWUxMSIsInNjb3BlcyI6WyJicmF3bHN0YXJzIl0sImxpbWl0cyI6W3sidGllciI6ImRldmVsb3Blci9zaWx2ZXIiLCJ0eXBlIjoidGhyb3R0bGluZyJ9LHsiY2lkcnMiOlsiNTIuMTQ5LjIyMC42OCJdLCJ0eXBlIjoiY2xpZW50In1dfQ.KaSkKF8AWZp4ImGlLWuPVaALUZrSzwBSeg4MWfvnTYSYYOagNDGenPPyrnPK3dEv2NE_KxliX0aIUBWvZ9v6KA"
id = "YG898Q9GP"

class Menu:
    def menu(self, option):
        default = "Invalid option!!"
        print(getattr(self, 'case_' + str(option), lambda: default)())
    def case_1(self):
        while True:
            print("\t1 - Get list of available brawlers.")
            print("\t2 - Get information about a brawler.")
            op2 = input().strip()
            my_switch2 = SUBMenu1()
            my_switch2.menu(op2)
            if op2 == '1' or op2 == '2':
                break
        return "Continue?"
    def case_2(self):
        print("NOTE: It may take up to 30 minutes for a new battle to appear in the battlelog.")
        battlelog(input("Player ID: "))
        return "Continue?"
    def case_3(self):
        events()
        return "Continue?"
    def case_4(self):
        valid_options = ["1", "2", "3", "4"]
        while True:
            print("\t1 - Get player rankings for a country or global rankings.")
            print("\t2 - Get brawler rankings for a country or global rankings.")
            print("\t3 - Get club rankings for a country or global rankings.")
            print("\t4 - Get list of power play seasons for a country or global rankings.")
            op2 = input().strip()
            my_switch2 = SUBMenu2()
            my_switch2.menu(op2)
            if op2 in valid_options:
                break
        return "Continue?"


class SUBMenu1:
    def menu(self, option):
        default = "Invalid option!!"
        print(getattr(self, 'case_' + str(option), lambda: default)())
    def case_1(self):
        geral_lista()
        return ' '
    def case_2(self):
        printar(brawlers(input("Which brawler do you want more information about? ")))
        return ' '


class SUBMenu2:
    def menu(self, option):
        default = "Invalid option!!"
        print(getattr(self, 'case_' + str(option), lambda: default)())
    def case_1(self):
        rankings_players(input("Two letter country code, or 'global' for global rankings: "))
        return ' '
    def case_2(self):
        braw = input("Brawler name: ")
        pais = input("Two letter country code, or 'global' for global rankings: ")
        rankings_braws(braw, pais)
        return ' '
    def case_3(self):
        ranking_clubs(input("Two letter country code, or 'global' for global rankings: "), "clubs")
        return ' '
    def case_4(self):
        ranking_modo(input("Two letter country code, or 'global' for global rankings: "), "powerplay/seasons")
        return ' '

def main():
    while True:
        print("==================================== Brawl Stars checker ====================================\n")
        print("\t 1 - Access general brawler information")
        print("\t 2 - Get list of recent battle results for a player")
        print("\t 3 - Get event rotation for ongoing events")
        print("\t 4 - Access global and local rankings")
        print("\t 5 - Exit")
        op = input().strip()
        if op == '5':
            limpa_tela()
            break
        my_switch = Menu()
        my_switch.menu(op)


def brawlers(brawler):
    brawler = brawler.strip().upper()
    try:
        res = requests.get(
        f"https://api.brawlstars.com/v1/brawlers",
        headers={'Authorization': f'Bearer {TOKEN}'}
        )
        output = res.json()
        #print(output)
        for nome in output["items"]:
            if nome["name"] == brawler:
                return(nome)
    except Exception:
        return 'Brawler not found!'
    return 'Brawler not found!'

def geral_lista():
    limpa_tela()
    try:
        res = requests.get(
        f"https://api.brawlstars.com/v1/brawlers",
        headers={'Authorization': f'Bearer {TOKEN}'}
        )
        output = res.json()
        #print(output)
        for i, nome in enumerate(output["items"]):
            print(i + 1, nome["name"].capitalize())
    except Exception as e:
        print(e)

def printar(info) -> None:
    limpa_tela()
    try:
        print(tabulate([["Brawler ID".upper(), str(info["id"])],["Name".upper(), info["name"].capitalize()]],
                        tablefmt="fancy_grid"))
        print("==================================== Star Powers ====================================")
        for i in range(len(info["starPowers"])):
            print(tabulate([["star Power ID".upper(), str(info["starPowers"][i]["id"])],
                            ["star Power Name".upper(), info["starPowers"][i]["name"].capitalize()]], tablefmt="fancy_grid"))
        print("==================================== Gadgets ====================================")
        for i in range(len(info["gadgets"])):
            print(tabulate([["gadget ID".upper(), str(info["gadgets"][i]["id"])],
                            ["gadget Name".upper(), info["gadgets"][i]["name"].capitalize()]], tablefmt="fancy_grid"))
    except Exception:
        print('Brawler not found!')


def battlelog(user_id):
    limpa_tela()
    user_id = user_id.strip()
    res = requests.get(
        f"https://api.brawlstars.com/v1/players/%23{id}/battlelog",
        headers={'Authorization': f'Bearer {TOKEN}'}
    )
    output = res.json()
    output = output["items"]
    ranks = [1, 2, 3]
    for k in range(len(output)):
        print()
        print(f'==================================== BattleTime: {output[k]["battleTime"]} ====================================')
        try:
            print(f'Mode played: {output[k]["event"]["mode"].capitalize()}, on {output[k]["event"]["map"]} map!')
        except Exception:
            print(f'{output[k]["battle"]["mode"].capitalize()}, on map maker!')
        try:
            if output[k]["battle"]["result"] == "victory":
                print(f'{output[k]["battle"]["result"].capitalize()} 😀😁')
            else:
                print(f'{output[k]["battle"]["result"].capitalize()} 😢😢')
            print(f'Duration: {output[k]["battle"]["duration"]} seconds.')
        except Exception:
            print()
        try:
            if int(output[k]["battle"]["rank"]) in ranks:
                print(f'Rank: {output[k]["battle"]["rank"]}!!!! 😀😁')
            else:
                print(f'Rank: {output[k]["battle"]["rank"]}... 😢😢')
        except Exception:
            print()
        try:
            print(f'Star Player: {output[k]["battle"]["starPlayer"]["name"]}, playing with Brawler {output[k]["battle"]["starPlayer"]["brawler"]["name"].capitalize()}, power {output[k]["battle"]["starPlayer"]["brawler"]["power"]}.')
            print("\nRed team:\n")
            for i in range(3):
                print(f'\t{output[k]["battle"]["teams"][0][i]["name"]}, playing with {output[k]["battle"]["teams"][0][i]["brawler"]["name"].capitalize()}, power {output[k]["battle"]["teams"][0][i]["brawler"]["power"]}.')  # Grupo RED
            print("\nBlue team:\n")
            for i in range (3):
                print(f'\t{output[k]["battle"]["teams"][1][i]["name"]}, playing with {output[k]["battle"]["teams"][1][i]["brawler"]["name"].capitalize()}, power {output[k]["battle"]["teams"][1][i]["brawler"]["power"]}.')  # Grupo BÇUE5
            print()
            print(f'===================================================================================================\n')
        except Exception:
            print()
        return 'OK'


def limpa_tela() -> None:
    sleep(.1)
    os.system('clear')


def events() -> None:
    limpa_tela()
    try:
        res = requests.get(
        f"https://api.brawlstars.com/v1/events/rotation",
        headers={'Authorization': f'Bearer {TOKEN}'}
        )
        output = res.json()
        print(f'==================================== Current Events in the game ====================================\n')
        for item in output:
            evento = seprar_palavras(item['event']['mode'])
            print(f" ➡ {evento}, on {item['event']['map']} map.\n")
    except Exception as e:
        print(e)


def seprar_palavras(palavra):
    trans = []
    for i in range(len(palavra)):
        if palavra[i].isupper():
            trans.append(' ')
            trans.append(palavra[i])
        else:
            trans.append(palavra[i])
    try:
        trans[0] = trans[0].upper()
    except Exception:
        return
    return ''.join(trans)


def rankings_players(code):
    limpa_tela()
    code = code.strip().upper()
    if len(code) == 2 or code == "GLOBAL":
        if code == "GLOBAL":
            code = "global"
        else:
            pais = validar_pais(code)
            if pais == "invalido":
                return print('Invalid country code!')
        try:
            res = requests.get(
            f"https://api.brawlstars.com/v1/rankings/{code}/players",
            headers={'Authorization': f'Bearer {TOKEN}'}
            )
            output = res.json()
            items = output["items"]
            if len(code) > 2:
                print(f'==================================== {code.capitalize()} players Ranking ====================================\n')
            else:
                print(f'==================================== {pais} players Ranking ====================================\n')
            for i, item in enumerate(items):
                print(f"{i + 1}. {item['name']} ➡ {int(item['trophies']):,} trophies.\n")
            return " "
        except Exception as e:
            return print(e)
    return print('Invalid country code!')


def validar_pais(codigo):
    pais = "invalido"
    with open("countries.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if row[1] == codigo:
                pais = row[0]
                break
    return pais


def rankings_braws(braw, code):
    limpa_tela()
    code = code.strip().upper()
    if len(code) == 2 or code == "GLOBAL":
        if code == "GLOBAL":
            code = "global"
        else:
            pais = validar_pais(code)
            if pais == "invalido":
                return print('Invalid country code!')
        info_braw = brawlers(braw)
        if len(info_braw) != 4:
            return print("Invalid Brawler!")
        braw_code = info_braw["id"]
        try:
            res = requests.get(
            f"https://api.brawlstars.com/v1/rankings/{code}/brawlers/{braw_code}",
            headers={'Authorization': f'Bearer {TOKEN}'}
            )
            output = res.json()
            items = output["items"]
            if len(code) > 2:
                print(f'==================================== {code.capitalize()} {braw.capitalize()} Ranking ====================================\n')
            else:
                print(f'==================================== {pais} {braw.capitalize()} Ranking ====================================\n')
            for i, item in enumerate(items):
                print(f"{i + 1}. {item['name']} ➡ {int(item['trophies']):,} trophies.\n")
            return " "
        except Exception as e:
            return print(e)
    return print('Invalid country code!')


def ranking_clubs(code, tipo):
    limpa_tela()
    code = code.strip().upper()
    if len(code) == 2 or code == "GLOBAL":
        if code == "GLOBAL":
            code = "global"
        else:
            pais = validar_pais(code)
            if pais == "invalido":
                return print('Invalid country code!')
        try:
            res = requests.get(
            f"https://api.brawlstars.com/v1/rankings/{code}/{tipo}",
            headers={'Authorization': f'Bearer {TOKEN}'}
            )
            output = res.json()
            items = output["items"]
            if len(code) > 2:
                print(f'==================================== {code.capitalize()} {tipo.capitalize()} Ranking ====================================\n')
            else:
                print(f'==================================== {pais} {tipo.capitalize()} Ranking ====================================\n')
            for i, item in enumerate(items):
                print(f"{i + 1}. {item['name']} ➡ {int(item['trophies']):,} trophies.\n")
            return " "
        except Exception as e:
            return print(e)
    return print('Invalid country code!')


def ranking_modo(code, tipo):
    limpa_tela()
    code = code.strip().upper()
    if len(code) == 2 or code == "GLOBAL":
        if code == "GLOBAL":
            code = "global"
        else:
            pais = validar_pais(code)
            if pais == "invalido":
                return print('Invalid country code!')
        try:
            res = requests.get(
            f"https://api.brawlstars.com/v1/rankings/{code}/{tipo}",
            headers={'Authorization': f'Bearer {TOKEN}'}
            )
            output = res.json()
            items = output["items"]
            if len(code) > 2:
                print(f'==================================== {code.capitalize()} {tipo.capitalize()} Ranking ====================================\n')
            else:
                print(f'==================================== {pais} {tipo.capitalize()} Ranking ====================================\n')
            for i, item in enumerate(items):
                print(f"{i + 1}. Start Time: {item['startTime']}, End Time: {item['endTime']}.\n")
            return " "
        except Exception as e:
            return print(e)
    return print('Invalid country code!')


if __name__ == "__main__":
    main()