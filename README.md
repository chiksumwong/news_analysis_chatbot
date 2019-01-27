[![CircleCI](https://circleci.com/gh/chiksumwong/news_analysis_chatbot.svg?style=svg)](https://circleci.com/gh/chiksumwong/news_analysis_chatbot)
# news-analysis-chatbot

# Start Server
```sh
$ python manage.py runserver
```


# url
### Chatbot
| Method | Urls |
| ------ | ------ |
| POST | http://127.0.0.1:8000/chatbot/webhook/ |

### News
| Method | Urls |
| ------ | ------ |
| GET | http://127.0.0.1:8000/api/news/ |
| POST | http://127.0.0.1:8000/api/news/ |
| POST | http://127.0.0.1:8000/api/info/ |
| POST | http://127.0.0.1:8000/api/checknews/ |
| POST | http://127.0.0.1:8000/api/checknewsbyurl/ |

# requirements
```sh
$ pip freeze > requirements.txt
```

# All functions of data preprocessing 
```sh
$ python train_model/DataPreprocessFunctions.py
```