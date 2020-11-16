import re
from weather import Weather


# 都道府県別のメソッド
def tokyo():
    city_tokyo = Weather()
    city_tokyo.name = "東京都"
    city_tokyo.kisyotyo_url = "https://www.jma.go.jp/jp/week/319.html"
    city_tokyo.user_select = 463
    city_tokyo.weather()


def hokkaido():
    city_hokkaido = Weather()
    city_hokkaido.name = "札幌"
    city_hokkaido.kisyotyo_url = "https://www.jma.go.jp/jp/week/306.html"
    city_hokkaido.user_select = 65
    city_hokkaido.weather()


def kyoto():
    city_kyoto = Weather()
    city_kyoto.name = "京都"
    city_kyoto.kisyotyo_url = "https://www.jma.go.jp/jp/week/333.html"
    city_kyoto.user_select = 716
    city_kyoto.weather()


def aomori():
    city_aomori = Weather()
    city_aomori.name = "青森"
    city_aomori.kisyotyo_url = "https://www.jma.go.jp/jp/week/308.html"
    city_aomori.user_select = 238
    city_aomori.weather()


def akita():
    city_akita = Weather()
    city_akita.name = "秋田"
    city_akita.kisyotyo_url = "https://www.jma.go.jp/jp/week/309.html"
    city_akita.user_select = 266
    city_akita.weather()


def iwate():
    city_iwate = Weather()
    city_iwate.name = "岩手"
    city_iwate.kisyotyo_url = "https://www.jma.go.jp/jp/week/310.html"
    city_iwate.user_select = 297
    city_iwate.weather()


def miyagi():
    city_miyagi = Weather()
    city_miyagi.name = "宮城"
    city_miyagi.kisyotyo_url = "https://www.jma.go.jp/jp/week/312.html"
    city_miyagi.user_select = 327
    city_miyagi.weather()


def yamagata():
    city_yamagata = Weather()
    city_yamagata.name = "山形"
    city_yamagata.kisyotyo_url = "https://www.jma.go.jp/jp/week/311.html"
    city_yamagata.user_select = 340
    city_yamagata.weather()


def hukushima():
    city_hukushima = Weather()
    city_hukushima.name = "福島"
    city_hukushima.kisyotyo_url = "https://www.jma.go.jp/jp/week/313.html"
    city_hukushima.user_select = 392
    city_hukushima.weather()


def ibaraki():
    city_ibaraki = Weather()
    city_ibaraki.name = "茨城"
    city_ibaraki.kisyotyo_url = "https://www.jma.go.jp/jp/week/314.html"
    city_ibaraki.user_select = 407
    city_ibaraki.weather()


def totigi():
    city_totigi = Weather()
    city_totigi.name = "栃木"
    city_totigi.kisyotyo_url = "https://www.jma.go.jp/jp/week/316.html"
    city_totigi.user_select = 424
    city_totigi.weather()


def gunma():
    city_gunma = Weather()
    city_gunma.name = "群馬"
    city_gunma.kisyotyo_url = "https://www.jma.go.jp/jp/week/315.html"
    city_gunma.user_select = 443
    city_gunma.weather()


def saitama():
    city_saitama = Weather()
    city_saitama.name = "埼玉"
    city_saitama.kisyotyo_url = "https://www.jma.go.jp/jp/week/317.html"
    city_saitama.user_select = 452
    city_saitama.weather()


def chiba():
    city_chiba = Weather()
    city_chiba.name = "千葉"
    city_chiba.kisyotyo_url = "https://www.jma.go.jp/jp/week/318.html"
    city_chiba.user_select = 490
    city_chiba.weather()


def kanagawa():
    city_kanagawa = Weather()
    city_kanagawa.name = "神奈川"
    city_kanagawa.kisyotyo_url = "https://www.jma.go.jp/jp/week/320.html"
    city_kanagawa.user_select = 500
    city_kanagawa.weather()


def nagano():
    city_nagano = Weather()
    city_nagano.name = "長野"
    city_nagano.kisyotyo_url = "https://www.jma.go.jp/jp/week/322.html"
    city_nagano.user_select = 530
    city_nagano.weather()


def yamanashi():
    city_yamanashi = Weather()
    city_yamanashi.name = "山梨"
    city_yamanashi.kisyotyo_url = "https://www.jma.go.jp/jp/week/321.html"
    city_yamanashi.user_select = 545
    city_yamanashi.weather()


def shizuoka():
    city_shizuoka = Weather()
    city_shizuoka.name = "静岡"
    city_shizuoka.kisyotyo_url = "https://www.jma.go.jp/jp/week/327.html"
    city_shizuoka.user_select = 560
    city_shizuoka.weather()


def aichi():
    city_aichi = Weather()
    city_aichi.name = "愛知"
    city_aichi.kisyotyo_url = "https://www.jma.go.jp/jp/week/329.html"
    city_aichi.user_select = 576
    city_aichi.weather()


def gifu():
    city_gifu = Weather()
    city_gifu.name = "岐阜"
    city_gifu.kisyotyo_url = "https://www.jma.go.jp/jp/week/328.html"
    city_gifu.user_select = 607

    city_gifu.weather()


def mie():
    city_mie = Weather()
    city_mie.name = "三重"
    city_mie.kisyotyo_url = "https://www.jma.go.jp/jp/week/330.html"
    city_mie.user_select = 621
    city_mie.weather()


def niigata():
    city_niigata = Weather()
    city_niigata.name = "新潟"
    city_niigata.kisyotyo_url = "https://www.jma.go.jp/jp/week/323.html"
    city_niigata.user_select = 646
    city_niigata.weather()


def toyama():
    city_toyama = Weather()
    city_toyama.name = "富山"
    city_toyama.kisyotyo_url = "https://www.jma.go.jp/jp/week/324.html"
    city_toyama.user_select = 666
    city_toyama.weather()


def ishikawa():
    city_totigi = Weather()
    city_totigi.name = "石川"
    city_totigi.kisyotyo_url = "https://www.jma.go.jp/jp/week/325.html"
    city_totigi.user_select = 682
    city_totigi.weather()


def fukui():
    city_fukui = Weather()
    city_fukui.name = "福井"
    city_fukui.kisyotyo_url = "https://www.jma.go.jp/jp/week/326.html"
    city_fukui.user_select = 691
    city_fukui.weather()


def shiga():
    city_totigi = Weather()
    city_totigi.name = "滋賀"
    city_totigi.kisyotyo_url = "https://www.jma.go.jp/jp/week/334.html"
    city_totigi.user_select = 705
    city_totigi.weather()


def osaka():
    city_oasaka = Weather()
    city_oasaka.name = "大阪"
    city_oasaka.kisyotyo_url = "https://www.jma.go.jp/jp/week/331.html"
    city_oasaka.user_select = 728
    city_oasaka.weather()


def hyogo():
    city_hyogo = Weather()
    city_hyogo.name = "兵庫"
    city_hyogo.kisyotyo_url = "https://www.jma.go.jp/jp/week/332.html"
    city_hyogo.user_select = 751
    city_hyogo.weather()


def nara():
    city_nara = Weather()
    city_nara.name = "奈良"
    city_nara.kisyotyo_url = "https://www.jma.go.jp/jp/week/335.html"
    city_nara.user_select = 761
    city_nara.weather()


def wakayama():
    city_wakayama = Weather()
    city_wakayama.name = "和歌山"
    city_wakayama.kisyotyo_url = "https://www.jma.go.jp/jp/week/336.html"
    city_wakayama.user_select = 772
    city_wakayama.weather()


def okayama():
    city_okayama = Weather()
    city_okayama.name = "岡山"
    city_okayama.kisyotyo_url = "https://www.jma.go.jp/jp/week/340.html"
    city_okayama.user_select = 792
    city_okayama.weather()


def hiroshima():
    city_hiroshima = Weather()
    city_hiroshima.name = "広島"
    city_hiroshima.kisyotyo_url = "https://www.jma.go.jp/jp/week/338.html"
    city_hiroshima.user_select = 814
    city_hiroshima.weather()


def shimane():
    city_shimane = Weather()
    city_shimane.name = "島根"
    city_shimane.kisyotyo_url = "https://www.jma.go.jp/jp/week/337.html"
    city_shimane.user_select = 833
    city_shimane.weather()


def tottori():
    city_tottori = Weather()
    city_tottori.name = "鳥取"
    city_tottori.kisyotyo_url = "https://www.jma.go.jp/jp/week/339.html"
    city_tottori.user_select = 848
    city_tottori.weather()


def tokushima():
    city_tokushima = Weather()
    city_tokushima.name = "徳島"
    city_tokushima.kisyotyo_url = "https://www.jma.go.jp/jp/week/343.html"
    city_tokushima.user_select = 861
    city_tokushima.weather()


def kagawa():
    city_kagawa = Weather()
    city_kagawa.name = "香川"
    city_kagawa.kisyotyo_url = "https://www.jma.go.jp/jp/week/341.html"
    city_kagawa.user_select = 871
    city_kagawa.weather()


def ehime():
    city_ehime = Weather()
    city_ehime.name = "愛媛"
    city_ehime.kisyotyo_url = "https://www.jma.go.jp/jp/week/342.html"
    city_ehime.user_select = 889
    city_ehime.weather()


def kouchi():
    city_kouchi = Weather()
    city_kouchi.name = "高知"
    city_kouchi.kisyotyo_url = "https://www.jma.go.jp/jp/week/344.html"
    city_kouchi.user_select = 904
    city_kouchi.weather()


def yamaguchi():
    city_yamaguchi = Weather()
    city_yamaguchi.name = "山口"
    city_yamaguchi.kisyotyo_url = "https://www.jma.go.jp/jp/week/345.html"
    city_yamaguchi.user_select = 920
    city_yamaguchi.weather()


def fukuoka():
    city_fukuoka = Weather()
    city_fukuoka.name = "福岡"
    city_fukuoka.kisyotyo_url = "https://www.jma.go.jp/jp/week/346.html"
    city_fukuoka.user_select = 944
    city_fukuoka.weather()


def oita():
    city_oita = Weather()
    city_oita.name = "大分"
    city_oita.kisyotyo_url = "https://www.jma.go.jp/jp/week/350.html"
    city_oita.user_select = 962
    city_oita.weather()


def nagasaki():
    city_nagasaki = Weather()
    city_nagasaki.name = "長崎"
    city_nagasaki.kisyotyo_url = "https://www.jma.go.jp/jp/week/348.html"
    city_nagasaki.user_select = 980
    city_nagasaki.weather()


def saga():
    city_saga = Weather()
    city_saga.name = "佐賀"
    city_saga.kisyotyo_url = "https://www.jma.go.jp/jp/week/347.html"
    city_saga.user_select = 993
    city_saga.weather()


def kumamoto():
    city_kumamoto = Weather()
    city_kumamoto.name = "熊本"
    city_kumamoto.kisyotyo_url = "https://www.jma.go.jp/jp/week/349.html"
    city_kumamoto.user_select = 1010
    city_kumamoto.weather()


def miyazaki():
    city_miyazaki = Weather()
    city_miyazaki.name = "宮崎"
    city_miyazaki.kisyotyo_url = "https://www.jma.go.jp/jp/week/351.html"
    city_miyazaki.user_select = 1029
    city_miyazaki.weather()


def kagoshima():
    city_kagoshima = Weather()
    city_kagoshima.name = "鹿児島"
    city_kagoshima.kisyotyo_url = "https://www.jma.go.jp/jp/week/352.html"
    city_kagoshima.user_select = 1058
    city_kagoshima.weather()


def okinawa():
    city_okinawa = Weather()
    city_okinawa.name = "那覇"
    city_okinawa.kisyotyo_url = "https://www.jma.go.jp/jp/week/353.html"
    city_okinawa.user_select = 1084
    city_okinawa.weather()


# この県の時はこれ表示してってやつ
def city():
    city_weather = input("都道府県を県まで入れてください(空白のままだと東京都の天気になります)例 東京都：")
    if city_weather == "東京都":
        tokyo()

    elif city_weather == "北海道":
        hokkaido()
    elif city_weather == "京都府":
        kyoto()
    elif city_weather == "青森県":
        aomori()
    elif city_weather == "秋田県":
        akita()
    elif city_weather == "岩手県":
        iwate()
    elif city_weather == "宮城県":
        miyagi()
    elif city_weather == "山形県":
        yamagata()
    elif city_weather == "福島県":
        hukushima()
    elif city_weather == "茨城県":
        ibaraki()
    elif city_weather == "栃木県":
        totigi()
    elif city_weather == "群馬県":
        gunma()
    elif city_weather == "埼玉県":
        saitama()
    elif city_weather == "神奈川県":
        kanagawa()
    elif city_weather == "千葉県":
        chiba()
    elif city_weather == "長野県":
        nagano()
    elif city_weather == "山梨県":
        yamanashi()
    elif city_weather == "静岡県":
        shizuoka()
    elif city_weather == "愛知県":
        aichi()
    elif city_weather == "岐阜県":
        gifu()
    elif city_weather == "三重県":
        mie()
    elif city_weather == "富山県":
        toyama()
    elif city_weather == "新潟県":
        niigata()
    elif city_weather == "石川県":
        ishikawa()
    elif city_weather == "福井県":
        fukui()
    elif city_weather == "滋賀県":
        shiga()

    elif city_weather == "大阪府":
        osaka()
    elif city_weather == "兵庫県":
        hyogo()
    elif city_weather == "奈良県":
        nara()
    elif city_weather == "岡山県":
        okayama()
    elif city_weather == "和歌山県":
        wakayama()
    elif city_weather == "広島県":
        hiroshima()
    elif city_weather == "島根県":
        shimane()
    elif city_weather == "鳥取県":
        tottori()
    elif city_weather == "徳島県":
        tokushima()
    elif city_weather == "香川県":
        kagawa()
    elif city_weather == "愛媛県":
        ehime()
    elif city_weather == "高知県":
        kouchi()
    elif city_weather == "山口県":
        yamaguchi()
    elif city_weather == "福岡県":
        fukuoka()
    elif city_weather == "大分県":
        oita()
    elif city_weather == "長崎県":
        nagasaki()
    elif city_weather == "佐賀県":
        saga()
    elif city_weather == "熊本県":
        kumamoto()
    elif city_weather == "宮崎県":
        miyazaki()
    elif city_weather == "鹿児島県":
        kagoshima()
    elif city_weather == "沖縄県":
        okinawa()
    elif city_weather == "":
        tokyo()

    elif city_weather != re.search(r".*都|.*道|.*府|.*県|\s", city_weather):
        print("都道府県を入力してください")
        print("\n")
        city()


def other():
    other_cities = input("他に知りたい都市の天気はありますか？(ある or ない):")
    if other_cities == "ある":
        city()
        print("\n")
        other()
    elif other_cities == "ない":
        pass
    else:
        print("そのような都市はありませんので終了します")


city()
print("\n")
other()
