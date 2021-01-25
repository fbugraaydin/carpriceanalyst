#### Heroku Commands

heroku run python manage.py shell

heroku logs --app=$app_name -t

#### Learn server ip

import http.client

connection = http.client.HTTPSConnection("httpbin.org")
connection.request("GET", "/ip")
response = connection.getresponse()
print("Status: {} and response: {}".format(response.status, response.read().decode()))

connection.close()

#### Restart Dynos

https://devcenter.heroku.com/articles/platform-api-reference#dyno-restart-all

heroku authorizations:create -d "getting started token"

curl -n -X DELETE https://api.heroku.com/apps/$APP_ID_OR_NAME/dynos -H "Content-Type: application/json" -H "Accept: application/vnd.heroku+json; version=3" -H "Authorization: Bearer a0c3b35b-3f57-4b34-8aaf-963481c632e9"

