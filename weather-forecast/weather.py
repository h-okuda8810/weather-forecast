import requests
from bs4 import BeautifulSoup
import datetime
import locale
import re

locale.setlocale(locale.LC_ALL, '')


class Weather:
    name = None
    kisyotyo_url = None  # 東京の週間天気予報(気象庁)
    user_select = None

    def weather(self):

        res = requests.get(self.kisyotyo_url)
        soup = BeautifulSoup(res.text, "lxml")
        # 現在の気温はsoup変数を使ったとことのタイムラグを無くすため、ここに記述
        now_url = "https://www.data.jma.go.jp/obd/stats/data/mdrr/tem_rct/alltable/mntemareaext00.html#a44"
        now_res = requests.get(now_url)
        now_soup = BeautifulSoup(now_res.text, "lxml")
        now_soup_select = now_soup.select(".mtx")
        now_text = now_soup_select[self.user_select].find_all("td")[4].text
        now_temp = re.sub(r"[\s|\]]", "", now_text)

        print("\n")
        print("                         " + "<" + self.name + "の天気をお知らせします>")
        print("")

        # 日付を代入
        dt_hour = datetime.datetime.now().hour  # 現在の時間が何時か
        dt_today = datetime.datetime.today().strftime("%Y年%m月%d日(%a)")
        dt_tomorrow = datetime.datetime.today() + datetime.timedelta(days=1)
        day_after_tomorrow = datetime.datetime.today() + datetime.timedelta(days=2)

        if dt_hour < 17:  # 17時からは次の日の天気が表示される
            print(dt_today, end="                                    ")
            print(dt_tomorrow.strftime("%Y年%m月%d日(%a)"))
        else:
            print(dt_tomorrow.strftime("%Y年%m月%d日(%a)"), end="                                    ")
            print(day_after_tomorrow.strftime("%Y年%m月%d日(%a)"))

            # 天気を代入
        sunny = "晴れ"
        sunny_cloudy = ["晴れ後曇り", "晴れ後時々曇り", "晴れ時々曇り", "晴れ後一時曇り"]
        cloudy = "曇り"
        cloudy_sunny = ["曇り後晴れ", "曇り後時々晴れ", "曇り後一時晴れ", "曇り時々晴れ"]
        rainy = "雨"
        rainy_cloudy = ["雨後曇り", "雨後時々曇り", "雨一時曇り", "雨後一時曇り", "雨時々曇り", "雨時々止む"]
        cloudy_rainy = ["曇り後雨", "曇り後時々雨", "曇り時々雨", "曇り一時雨", "曇り後一時雨", "曇り一時雨か雪"]
        cloudy_snowy = ["曇り後雪", "曇り後時々雪", "曇り時々雪", "曇り一時雪", "曇り後一時雪"]
        snowy = "雪"
        snowy_sunny = ["雪後晴れ", "雪後時々晴れ", "雪後一時晴れ", "雪時々晴れ"]

        weather = soup.select(".for")  # 天気はclass = forの中にあるimgタグのtitle、alt属性に書いてある
        # 今日
        if weather[0].img["alt"] in sunny:
            print(weather[0].img["alt"] + "☀", end="                                                 ")
        elif weather[0].img["alt"] in sunny_cloudy:
            print(weather[0].img["alt"] + "☀🌥", end="                                           ")
        elif weather[0].img["alt"] in cloudy:
            print(weather[0].img["alt"] + "🌥", end="                                                 ")
        elif weather[0].img["alt"] in cloudy_sunny:
            print(weather[0].img["alt"] + "🌥☀", end="                                          ")
        elif weather[0].img["alt"] in rainy:
            print(weather[0].img["alt"] + "☂", end="                                                 ")
        elif weather[0].img["alt"] in rainy_cloudy:
            print(weather[0].img["alt"] + "☂🌥", end="                                        ")
        elif weather[0].img["alt"] in cloudy_rainy:
            print(weather[0].img["alt"] + "🌥☂", end="                                          ")
        elif weather[0].img["alt"] in cloudy_snowy:
            print(weather[0].img["alt"] + "🌥❄", end="                                        ")
        elif weather[0].img["alt"] in snowy:
            print(weather[0].img["alt"] + "❄", end="                                                 ")
        elif weather[0].img["alt"] in snowy_sunny:
            print(weather[0].img["alt"] + "❄☀", end="                                        ")
        else:
            print(weather[0].img["alt"] + "❄☀", end="                                           ")
        # 明日
        if weather[1].img["alt"] in sunny:
            print(weather[1].img["alt"] + "☀")
        elif weather[1].img["alt"] in sunny_cloudy:
            print(weather[1].img["alt"] + "☀🌥")
        elif weather[1].img["alt"] in cloudy:
            print(weather[1].img["alt"] + "🌥")
        elif weather[1].img["alt"] in cloudy_sunny:
            print(weather[1].img["alt"] + "🌥☀")
        elif weather[1].img["alt"] in rainy:
            print(weather[1].img["alt"] + "☂")
        elif weather[1].img["alt"] in rainy_cloudy:
            print(weather[1].img["alt"] + "☂🌥")
        elif weather[1].img["alt"] in cloudy_rainy:
            print(weather[1].img["alt"] + "🌥☂")
        elif weather[0].img["alt"] in cloudy_snowy:
            print(weather[0].img["alt"] + "🌥❄")
        elif weather[1].img["alt"] in snowy:
            print(weather[1].img["alt"] + "❄")
        elif weather[0].img["alt"] in snowy_sunny:
            print(weather[0].img["alt"] + "❄☀")
        else:
            print(weather[0].img["alt"] + "❄☀")
        # 最高気温
        max_temp_select = soup.select(".maxtemp")
        max_text = max_temp_select[0].text
        max_temp = re.sub(r"[\n\t]", "", max_text)
        max_text2 = max_temp_select[1].text
        max_temp2 = re.sub(r"[\n\t]", "", max_text2)

        print("最高気温：" + max_temp + "℃", end="                                          ")
        print("最高気温：" + max_temp2 + "℃")

        # 最低気温
        min_temp_select = soup.select(".mintemp")
        min_text = min_temp_select[0].text
        min_temp = re.sub(r"[\n\t]", "", min_text)
        min_text2 = min_temp_select[1].text
        min_temp2 = re.sub(r"[\n\t]", "", min_text2)
        dt_hour = datetime.datetime.now().hour

        if 5 <= dt_hour < 17:  # 気象庁の最低気温は時間によって/で表示されるため、if分を使う
            print("現在の気温:" + now_temp + "℃", end="                                        ")
            print("最低気温：" + min_temp + "℃")

        else:
            print("最低気温：" + min_temp + "℃", end="                                           ")
            print("最低気温：" + min_temp2 + "℃")

        # 気温によってどんな服装にすればいいか教える
        # 今日
        dt_very_hot = re.search(r"3[0-9]|4[0-9]", max_temp)
        dt_hot = re.search(r"2[5-9]", max_temp)
        dt_warm = re.search(r"2[1-4]", max_temp)
        dt_cool = re.search(r"1[6-9]|20", max_temp)
        dt_chilly = re.search(r"1[2-5]", max_temp)
        dt_cold = re.search(r"1[0-1]|[6-9]", max_temp)
        dt_freezing = re.search(r"[0-5]|-[0-9]|1[0-9]", max_temp)

        if dt_very_hot:
            print("服装：半袖短パンがベストです", end="                          ")
        elif dt_hot:
            print("服装：半袖に長ズボンがベストです", end="  　　                       ")
        elif dt_warm:
            print("服装：長袖に長ズボンがベストです", end="                            ")
        elif dt_cool:
            print("服装：パーカーや薄手の羽織れる服がベストです", end="                  ")
        elif dt_chilly:
            print("服装：ニットやセーターにアウターがベストです", end="                  ")
        elif dt_cold:
            print("服装：ヒートテックにダウンジャケットがベストです", end="               ")
        elif dt_freezing:
            print("服装：マフラーなどをして温かいアウターがベストです", end="            ")

        # 明日
        tomorrow_very_hot = re.search(r"3[0-9]|4[0-9]", max_temp2)
        tomorrow_hot = re.search(r"2[5-9]", max_temp2)
        tomorrow_warm = re.search(r"2[1-4]", max_temp2)
        tomorrow_cool = re.search(r"1[6-9]|20", max_temp2)
        tomorrow_chilliy = re.search(r"1[2-5]", max_temp2)
        tomorrow_cold = re.search(r"1[0-1]|[6-9]", max_temp2)
        tomorrow_freezing = re.search(r"[0-5]|-[0-9]|1[0-9]", max_temp2)

        if tomorrow_very_hot:
            print("服装：半袖短パンがベストです")
        elif tomorrow_hot:
            print("服装：半袖に長ズボンがベストです")
        elif tomorrow_warm:
            print("服装：長袖に長ズボンがベストです")
        elif tomorrow_cool:
            print("服装：パーカーや薄手の羽織れる服がベストです")
        elif tomorrow_chilliy:
            print("服装：ニットやセーターにアウターがベストです")
        elif tomorrow_cold:
            print("服装：ヒートテックにダウンジャケットがベストです")
        elif tomorrow_freezing:
            print("服装：マフラーなどの防寒対策をして温かいアウターがベストです")
