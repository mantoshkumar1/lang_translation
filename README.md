# lang_translation

## Still in Progress:
Status Update: April 2, 2018.

Creating a web server with a RESTful API to translate a text from any language to any language. For the actual translation I plan to use an external service like Google Translate or Bing Translations. The source and target language would be definable via the API. In addition, I have decided to not only translate a text but also cache translations. So that if the same text should be translated again the application does not have to make the heavy request to the external service again but can just pick it up from our cache. The cache is supposed to be persistent.

I am going to follow DNR principle (Do Not Repeat), that's why  structure and architecture of the server will be designed in such a way that it can easily grow into a bigger project and would be easy to maintain. E.g. we want to change our caching strategy or switch out our translation service.
