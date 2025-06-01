# Notes

## Real-Time Data Issue
One of the main challenges right now is getting real-time data fed into AmiBorker.

### AmiBroker Reference Docs:
1. [How to work with Real-Time data plugins](https://www.amibroker.com/guide/h_rtsource.html)
2. [Working with real time quote window](https://www.amibroker.com/guide/w_rtquote.html)
3. [How to get quotes from various markets](https://www.amibroker.com/guide/h_quotes.html)

### Solutions
[Polygon.io](https://polygon.io/pricing) may be a good option. They are $200/mo for real-time data. Their API is attractive but they are not officially Amibroker supported (we would need to develop our own integration... much work work)
Per Ref 1 above [see also Ref 3], "In order to use AmiBroker with any real-time data source you have to set up the database with appropriate data plug-in first. This is required only once at the database creation time. Instructions for setting up are available here: eSignal, myTrack, IQFeed, QuoteTracker."
- eSignal: Has official AmiBroker integration

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTgwNTUzNjU2LC0xNDkzNzU0MDcsMTc3MD
I1NTYwMV19
-->