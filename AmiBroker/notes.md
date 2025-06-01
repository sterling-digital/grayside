# Notes

## Real-Time Data Issue
One of the main challenges right now is getting real-time data fed into AmiBorker. Most are 15-min delayed.

### AmiBroker Reference Docs:
1. [How to work with Real-Time data plugins](https://www.amibroker.com/guide/h_rtsource.html)
2. [Working with real time quote window](https://www.amibroker.com/guide/w_rtquote.html)
3. [How to get quotes from various markets](https://www.amibroker.com/guide/h_quotes.html)

### Solutions
1. [Polygon.io](https://polygon.io/pricing) may be a good option. They are $200/mo for real-time data. Their API is attractive but they are not officially Amibroker supported (we would need to develop our own integration... much work work).
2. Per Ref 1 above [see also Ref 3], "In order to use AmiBroker with any real-time data source you have to set up the database with appropriate data plug-in first. This is required only once at the database creation time. Instructions for setting up are available here: eSignal, ~~myTrack(defunct)~~, IQFeed, ~~QuoteTracker(limited )~~."
 - **eSignal**:
	 - Has official AmiBroker [integration](https://www.amibroker.com/guide/h_esignal.html) 
	 - Costs $228/month (Exchange Fees Not Included!) for streaming real-time data
-  **IQFeed**:
	- Has official AmiBroker [integration](https://www.amibroker.com/iqfeed.html)
	- [Cool features](https://www.iqfeed.net/Amibroker/index.cfm?displayaction=data&section=services)
	- Has a free-ish trial (may incur exchange fees, see below) [More info](https://www.iqfeed.net/Amibroker/index.cfm?displayaction=start)
	- [Pricing](https://www.iqfeed.net/Amibroker/index.cfm?displayaction=data&section=fees) is a little harder to pinpoint.
		- Starts at $105/mo 
		- Then each exchange is an add-on (NASDAQ = $7.50/mo)
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTczNzAyNDA5NSwxODMzNjQzMzE2LC0xND
kzNzU0MDcsMTc3MDI1NTYwMV19
-->