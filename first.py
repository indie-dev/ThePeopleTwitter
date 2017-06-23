import tweepy

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main():
  # Fill values asked for in get_api
  cfg = { 
    "consumer_key"        : "MnQKUU7vjFRUJU6gOQ8QYxNQO",
    "consumer_secret"     : "GqFOz9gmxorLq5AnLzHpgQ6IyB41NYvmUVSROmWZQhgVSnNbZ6",
    "access_token"        : "878143562705063937-ZnkVgSHcpLieHIHUsa3upa2FQQMJ4jj",
    "access_token_secret" : "sNE2ktIgYn2LXEvaa6YnceqsIRMTy5jzyyOb2YztO8n8E" 
    }

  api = get_api(cfg)
  tweet = raw_input("Tweet: ")
  status = api.update_status(status=tweet) 
  print("Tweet sent successfully.");
if __name__ == "__main__":
  main()
