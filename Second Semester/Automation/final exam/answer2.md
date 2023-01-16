# Step 1 : Crwal the web and get information

we need two library: 1. requests 2. from bs4 import Beautifulsoap
from the link https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc we can get the information that we want.

with BeautifulSoup and method find_all we can extract the div html tag from page. Every div element with class "lister-item mode-advanced" is one of the movies.

inside of every div that we found before we can see title of movie inside of h3 tag.
"inline-block ratings-imdb-rating" = this class refer to the rating.
"text-muted" = this class refer to the description

we can save those information in dictionary varible.

for save the data into a csv file we can use pandas dataframe.after we import the data into pandas dataframe we can save it as CSV by call df.to_csv().

# Step 2 : Create a presentation in cloud

- first of all you need to install these google libraries.

  1. google-api-python-client
  2. google-auth-httplib2
  3. oauth2client

- you need to create a project in google cloud and get credential information and place the credential in your project folder.

- now you have access to google account and you can create presentation with the command service.presentations().batchUpdate

# Step 3 : Send Email

Google also have a api for sending email.

by using service.users().drafts().create command you can send email to a predefined email address.

# Step 4 : Delete old presentation once a week

when we create presentation in google cloud we get an id and we have to save in a file.
after we can remove presentation file by command : service.files().delete(fileId=file_id)

# Step 5 : Run Every Sunday

we have two python files. one for create presentation and the other for delete presentation.

we can set new schedule by this command : crontab -e

0 0 \* \* SUN "Create file python code"

and also set another crontab for deleting file from google cloud.

0 0 \* \* MON "Delete file python code"
