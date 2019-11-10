# Gfycat Downloader
Given only a Gfycat URL, it is difficult to programatically get the URL for the GIF version of it.
Therefore repo has a few helper functions that interact with the Gfycat API in order to download the GIF version of any Gfycat. 

**Note: Before using this script, you need a `client_id` and `client_secret` from Gfycat that can be obtained [here](https://developers.gfycat.com/signup).**


## My incentive
The reason I created this is that the tools available to sort/filter your saved posts on Reddit are very limited.
You have to pay for Reddit premium to be able to sort by subreddit. 
Therefore, I figured I'd just store them locally so that I can sort however I want.
To do this I first use `https://redditmanager.com/`. 
This website requests you to login to your account and it finds and sorts all of your saved posts for you. 
You can then export this to an `html` file which you can then parse and download.
There are toosl for downloading Imgure images and albums, but nothing for Gfycat.
Although this requires dev access from Gfycat, it's free and very easy to get.

## How to Use It

Save these two parameters in a json file called `auth.json`.
```json
{
  "client_id": "<<client_id>>",
  "client_secret": "<<client_secret>>"
}
```

The first step to downloading is getting an `access_token` from Gfycat that you must have in the header of every request you make after obtaining it. Once you have the access token you can obtain the access token:

```python
>>> get_credentials(cliend_id, client_secret)
```

This token is what you'll use for the current session of API access to be able to use it. It usually expires in 3600s seconds (1 hour).
Once you have the `access_token` you're ready to start downloading GIFs!

As an example, say you want to download the Gfycat at the following URL:

```
https://gfycat.com/energeticequatorialcrane-nikki-blonsky-wheeleybarger-logging-on
```

The Gfycat ID for this link is `energeticequatorialcrane`.
Although the URL has more words in the string, this is the unique ID assigned to thie Gfy.
You'll use this ID to tell the API which Gfy you want to download.
For ease of programing there's a function that'll get the `gfyid` from a URL:

```python
>>> getgfyid('https://gfycat.com/energeticequatorialcrane-nikki-blonsky-wheeleybarger-logging-on')
'energeticequatorialcrane'
```

Now that you have the ID, you can call:

```python
>>> response = get_gfy(access_token, gfyid)
```

The function returns a json object that's the response body from the `GET` request.
This may seem no abstracted enough for a toolkit like this repo, but the raw response contains all of the URLs that may be of interest.

The only function available at the moment, just grabs the URL for the largest size from the response json object:

```python
>>> largest_gif_url(response)
https://thumbs.gfycat.com/EnergeticEquatorialCrane-size_restricted.gif
```

If you go to the above URL, you'll get what you want.
If you want to grab some other URL, there are a few options:
* `largeGif`: this is the one that's implemented right now, it grabs the largest size
* `max1mbGif`: as the name implies, maximum size of 1mb
* `max2mbGif`
* `max5mbGif`

## Contributing
If you want to change the code to download one of the other sizes, just make the following change to the `largest_gif_url` function.

```python
def largest_gif_url(response):
    return response['gfyItem']['content_urls']['largeGif']['url']
```
Just change `largeGif` to the one you want, or just create a new function (the better way to do it).

