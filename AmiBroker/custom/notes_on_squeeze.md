```C
// Squeeze Duration Tracking
squeezeBars = 0;
for (i = 1; i < BarCount; i++) { // https://www.amibroker.com/guide/keyword/for.html, BarCount is a single number equal to the number of bars loaded in the current chart.
    if (isSqueeze[i]) {
        if (isSqueeze[i-1]) {
            squeezeBars[i] = squeezeBars[i-1] + 1;
        } else {
            squeezeBars[i] = 1;
        }
    } else {
        squeezeBars[i] = 0;
    }
}
```
This loop walks through each bar in your chart and builds an array, squeezeBars, that tells you how many consecutive bars the market has been “in squeeze” up to—and including—that bar:

Initialization
`squeezeBars = 0;`
This creates an array of the same length as your data, filled with zeros.

Loop over bars
`for (i = 1; i < BarCount; i++) {`
Starts at the second bar (index 1) and runs through the last bar (BarCount–1).

Check if current bar is in squeeze
`if ( isSqueeze[i] ) {`
If the squeeze condition is true here…

Continuing a squeeze
`if ( isSqueeze[i-1] )
    squeezeBars[i] = squeezeBars[i-1] + 1;`
…and the previous bar was also in squeeze, add 1 to the previous count.

Starting a new squeeze
`else
    squeezeBars[i] = 1;`
…if the previous bar was not squeezed, start a fresh count at 1.

Not in squeeze
`else
    squeezeBars[i] = 0;`
If the squeeze isn’t on at this bar, reset the count to 0.
