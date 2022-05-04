faq = 'question: Google Sheets report not working\n' \
      'answer: Add Google account to document with "can edit" permissions. ' \
      'You can get the name of a Google account by determining the access rights to applications' \
      '\n' \
      '\n' \
      'question: Stop validation button is not active\n' \
      'answer: The Stop Validation button becomes active while the report is being generated' \
      '\n' \
      '\n' \
      'question: I want to access the source files of the application\n' \
      'answer: Follow the link in the bottom left corner of the app. You can see the source files on GitHub. ' \
      'You have the opportunity to make your suggestions and comments to improve the application'

user_manual = '"copy symbol" - copy the name of the google account, ' \
              'after which you need to add to the google sheet with the rights "can edit"\n' \
              '"Check Link" - allows you to check a small number of links and display the result in the application window\n' \
              '"Google Docs report" - allows you to generate a report in a Google spreadsheet. ' \
              'The list of links must be on the first sheet in the first column.' \
              'Be sure to first add a Google account with the rights "can edit"' \
              'Google account name: mom-s-seo@momsseo.iam.gserviceaccount.com\n' \
              '"Excel report" - allows you to create a report in an excel spreadsheet. ' \
              'The list of links should be on the first sheet in the first column. File must be closed\n' \
              '"Designed by Eugene" - link to the project repository in GitHub\n' \
              '"Stop validate" - the button is not active. Activated during report generation. ' \
              'When pressed, stops the report generation process\n' \
              'Monitors that display summary statistics and progress'

credentials = {
    "type": "service_account",
    "project_id": "momsseo",
    "private_key_id": "27d3c18400805fe9b1583519ce85674736a7884a",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQC4OngLqK92JENS\nh4KaH1R0S+QVvuv8+AYK4Rry+twpF0hJ9MW8zcWM7WY6b8ARwCaaNbvwLAb7hHc6\nF/v3e5pGWE48COZRoHcuIkfZX9nNntkCX49+IPf3uJwwTQbp7rwZPd6FbSNc/b7C\n+nzAgH/Oh85afrppkFjrnvvvZoUi/YCucQ6eY+dcpVBm+JmsdTus9bSL6WRlONR8\nw/flE1GFhn3Xv6RkuK2rVqX9E5CLcmHa6wpb3zJIS0BfZmSY4hXRmHFLWF9nj5It\nF3i3j+FALQSprrCJH/C41/ufW5A4vycEHLfa1nEhxHXlkiMriSVb8bivysDkQGDA\n1SmNwMKBAgMBAAECggEALaht+oO8sqSzm6dSdqSHn4f0d/A4l9oXU0htT6Vc/YET\n7SJRBGUiDfaDJL3v5eZPmt3w3UnoFBtFGjx5+aCkQEVf5FCXVkkU6HXeBTFUbzms\nUkKBM1Lz6azS5sScT0tXylCzTrGY91G63qNKWkIuiq7NNU/dns6DvyeIjFFF80Dg\n7YoBw31NlX9vHX/5s7tWOVP9uKQsa/+Co1EQSD/DoQiNyS2Iqjn62kL/kZMQHZuG\nc3R5dWGUUl1syEAk7orQW1GAiN2fOIfAziSP34+bTx68t3f8b2/ZabD41k1ijlSe\n4bzT0lb605/i8TkXKmumChWxH7y6Vsf2Efl/88CTLQKBgQDul0hQGRfAem7q74cU\n4cly16Rc0vqhkPJVNmRtmjlNWFHHiCghfmlmkomb7YCYKgNleYwgZckDDU5+9aJ6\nto3+Eo6H20b99ABU4MG7ifAclAVBlksaWq4uFPfOtwuWjAOWItym1Zf3Ghz/HTJk\ntkIyi+v9HlgX1uLSEFWqps5GRQKBgQDFq7sRZN0Mg5rIWrqOwOgAYbBiBjhclyVg\nX5+o6WsH2SXOBCsumIx4T9aIxOwaCEj489uomOSfpjM6eTFgmYTZItaEMVra1s4o\nT0PCSnS00SF4zAzFSBJh/qi08IE7Vk1uGMc3HfP/Z6Q1TelgvaoEZQfWZSYjQwEo\noriz5lH9DQKBgQC8cxlWyrsL+KhrQE39nGk1IEZeWvZDbu05iQDB4TKpeLz/UPgB\nnIs7zTqLwofzqBuOpvabEEo48uWxOerf6hk1OQsDG5tzMqqgX/YlXsociH2uVDt1\n0XIKS91/lOy+OFEM4PRPgh3JuwJ0LmeDTMH0krgO8Uy7Z6s4KFbBt4bt0QKBgQCj\n0HXvLE+kl0wmzkndFDEwX8T094Kt+PSYsaZ3LTnt/x89ZGcE7pc6/a8lGU0xJbyT\n1EQtrMeLJwk9ZEJvc8qMyDpOwzgwM+QVs9rLoTimwMmkejX7KIdTfuABU29F5Xe1\nzgMKwl/7QcDsC+1kpsnHapLcMmcwwc6sBm5baHx54QKBgAEfDOaej4BZlw97hvLW\nAVeyWBSeR3hWT4RvsFN6AGRzTJSUvFLvl0dhwumhOCMPgU1I+QxkGLsnVh9gS0/e\nHf579LAi9WO4Rfx3gFe+6xDaE7gxn3Yup6jIdrvemvFrMRbS5Ycwycc/kiUW8qOP\nQ5/iCXalObRomi5Gxlxflv2t\n-----END PRIVATE KEY-----\n",
    "client_email": "mom-s-seo@momsseo.iam.gserviceaccount.com",
    "client_id": "116336220736210729985",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/mom-s-seo%40momsseo.iam.gserviceaccount.com"
}
