import requests

def test_get_req():
     response = requests.get("https://restful-booker.herokuapp.com/booking")
     #print(response.text)
     print(response.status_code)
     #print(response.json())
     assert response.status_code == 200
     assert len(response.json()) > 0

def test_get_post_create_token():
     payload = {
          "username": "admin",
          "password": "password123"
     }
     headers = {
          "Content-type": "application/json"
     }
     response = requests.post("https://restful-booker.herokuapp.com/auth", headers = headers, json = payload)
     print(response.text)
     print(response.status_code)
     print(response.json()["token"])
     assert response.status_code == 200

def test_post_create_booking():
     payload_create_booking = {
          "firstname" : "Hema",
          "lastname" : "Brown",
          "totalprice" : 250,
          "depositpaid" : True,
          "bookingdates" : {
               "checkin" : "2023-01-01",
               "checkout" : "2023-02-02"
          },
          "additionalneeds" : "Breakfast"
     }
     headers = {
          "Content-type": "application/json"
     }
     response = requests.post("https://restful-booker.herokuapp.com/booking", headers = headers,json = payload_create_booking)
     print(response.json())
     print(response.status_code)
     Booking_Id = response.json()["bookingid"]
     print(Booking_Id)
     assert response.status_code == 200


# def test_patch_req():
#      response = requests.get("https://restful-booker.herokuapp.com/booking")
#      print(response.text)
#      print(response.status_code)
#      assert response.status_code == 200

# def test_Delete_Booking():
#      headers = {
#           "Content-type": "application/json"
#      }
#      response = requests.delete("https://restful-booker.herokuapp.com/booking/233", headers=headers)
#      print(response.text)
#      print(response.status_code)
#      assert response.status_code == 201