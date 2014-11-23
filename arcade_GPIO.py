from twython import Twython, TwythonError
import time
import datetime
import csv
import RPi.GPIO as GPIO

# Twitter application authentication
app_key = "REEMPLAZAR"
app_secret = "REEMPLAZAR"
oauth_token = "REEMPLAZAR"
oauth_token_secret = "REEMPLAZAR"

twitter = Twython(app_key,app_secret,oauth_token,oauth_token_secret)

datestamp = datetime.datetime.now().strftime("%d-%m-%Y")

hashtag = raw_input("Hashtag a buscar: ")

usuarios = []
tuits = []
fecha = []

reset = 50

usuarios.insert(0,"Usuarios")
tuits.insert(0,"Tuits")
fecha.insert(0,"Fecha")

def busqueda():

        while (reset == 50):
                
                search_results = twitter.search(q=hashtag, count=reset)

                for tweet in search_results['statuses']:
                    print 'Tweet from @%s Date: %s' % (tweet['user']['screen_name'].encode('utf-8'),tweet['created_at'])
                    print tweet['text'].encode('utf-8'), '\n'

            # GPIO pin number of LED
            LED = 22

            # Setup GPIO as output
            GPIO.setmode(GPIO.BOARD)
            GPIO.setup(LED, GPIO.OUT)
            GPIO.output(LED, GPIO.LOW)
                     
                    GPIO.output(LED, GPIO.HIGH)
                    time.sleep(0.5)
                    GPIO.output(LED, GPIO.LOW)

                    tuits.append(tweet['text'].encode('utf-8'))
                    usuarios.append(tweet['user']['screen_name'].encode('utf-8'))
                    fecha.append(tweet['created_at'])

                    open_csv = open(hashtag+"-"+datestamp+".csv","wb")
                    busqueda_csv = csv.writer(open_csv)

                    #Merge all the lists together so that they line up
                    rows = zip(usuarios,tuits,fecha)

                    #Write each row one-by-one to our spreadsheet
                    for row in rows:
                            busqueda_csv.writerow(row)

                    #Save and close the csv spreadsheet
                    open_csv.close()

                    time.sleep(10)

                    if KeyboardInterrupt: GPIO.cleanup()

busqueda()
