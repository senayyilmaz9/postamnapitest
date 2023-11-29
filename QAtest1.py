import unittest
import requests
import json

class TestAPI(unittest.TestCase):

    def test_api_get(self):
        cevap = requests.get("https://api.github.com/events")
        print(cevap.text)

    def test_api_post(self):
        payload = {"key1": "value1"}
        gonder = requests.post("https://api.github.com/events", data=payload)
        print(gonder.elapsed.total_seconds())

    def test_api_get_2(self):
        cevap = requests.get("https://automationexercise.com/api/productsList")
        print(cevap.text)
        print(cevap.status_code)

    def test_api_post_2(self):
        payload = {"birth_date": "Miss"}
        gonder = requests.post("https://automationexercise.com/api/createAccount", data=payload)
        icerik = json.loads(gonder.text)
        print(gonder.text)
        self.assertEqual("Miss", icerik["birth_date"])
        self.assertEqual("birth_year" in icerik, True)

    def test_api_get_3(self):
        cevap = requests.get("https://automationexercise.com/api/brandsList")
        icerik = json.loads(cevap.text)
        item_id = icerik["brands"[10]["id"]]
        self.assertEqual(12,"item_id")

    def test_api_delete(self):
        cevap = requests.delete("https://automationexercise.com/api/deleteAccount")
        print(cevap.text)
        print(cevap.status_code)

    def test_api_post_3(self):
        payload={"key1":"value1"}
        gonder=requests.post("https://automationexercise.com/api/verifyLogin", data=payload)
        print(gonder.text)

    def test_api_get_4(self):
        cevap= requests.get(" https://automationexercise.com/api/getUserDetailByEmail")
        print(cevap.text)
        print(cevap.status_code)

    def test_api_post_4(self):
        payload={"key1":"value1"}
        gonder=requests.post(" https://automationexercise.com/api/productsList",data=payload)
        print(gonder.text)
        print(gonder.status_code)

    def test_api_post_5(self):
        payload = {"search_product": "jean"}
        gonder = requests.post("https://automationexercise.com/api/searchProduct", data=payload)
        icerik = json.loads(gonder.text)
        self.assertEqual("Jeans", icerik["products"][2]["category"]["category"])

    def test_api_post_6(self):
        gonder = requests.get("https://automationexercise.com/api/searchProduct")
        print(gonder.text)
        icerik = json.loads(gonder.text)
        self.assertEqual(405, icerik["responseCode"])

    def test_api_post_7(self):
        payload={"key1":"value1"}
        gonder=requests.post(" https://automationexercise.com/api/verifyLogin",data=payload)
        print(gonder.text)
        print(gonder.status_code)

    def test_api_delete_2(self):
        cevap = requests.delete(" https://automationexercise.com/api/verifyLogin")
        print(cevap.text)
        print(cevap.status_code)

    def test_api_put(self):

        cevap = requests.put("https://automationexercise.com/api/brandsList")
        print(cevap.text)


if __name__ == '__main__':
    unittest.main()