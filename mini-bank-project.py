kullanici_1 = {
    "ad": "Safa",
    "hesap_no": "46807540",
    "bakiye": 5500,
    "ek_hesap": 1000

}

kullanici_2 = {
    "ad": "Zeynep",
    "hesap_no": "99845380",
    "bakiye": 7904,
    "ek_hesap": 8890

}


def paraCek(hesap, miktar):
    print(f"Merhaba {hesap['ad']}")

    if (hesap["bakiye"] >= miktar):
        hesap["bakiye"] -= miktar
        print("paranzı alabilirsiniz")
    else:
        toplam = hesap["bakiye"] + hesap["ek_hesap"]

        if (toplam >= miktar):
            ek_hesap_kullanimi = input("ek hesap kullanılsı mı (e/h)")

            if ek_hesap_kullanimi == "e":
                ek_hesap_kullanilacak_miktar = miktar - hesap["bakiye"]
                hesap["bakiye"] = 0
                hesap["ek_hesap"] -= ek_hesap_kullanilacak_miktar
                print("parınız alabilirsiniz")
            else:
                print(
                    f"{hesap['hesap_no']} nolu hesabınızda {hesap['bakiye']} bulunmaktadır")

        else:
            print("Üzgünüz bakiye yetersiz")


def bakiye_sorgula(hesap):
    print(f"{hesap['hesap_no']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır. EK hesap limitiniz ise {hesap['ek_hesap']} TL bulunmaktadır")


paraCek(kullanici_1, 6000)
bakiye_sorgula(kullanici_1)

paraCek(kullanici_2, 2445)
bakiye_sorgula(kullanici_2)