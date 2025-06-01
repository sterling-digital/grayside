# Indicators and Elements

```
// AmiBroker Exploration Setup
filter = 1; /* all symbols and quotes accepted */

isGain = IIf(C > O, TRUE, FALSE);
```

## Get Name
```
// Display Name
AddTextColumn(FullName(),"Name",0,IIf( isGain, colorBrightGreen, colorPink ), colorDefault,72);
```

## Get Category
```
// Display Categories
//AddTextColumn(MarketID(1),"Market",0,colorBlueGrey,colorDefault,90); 
AddTextColumn(SectorID(1),"Sector",0,colorBlueGrey,colorDefault,90); 
AddTextColumn(IndustryID(1),"Industry",0,colorBlueGrey,colorDefault,90);
//AddTextColumn(GicsID(1),"GICS",0,colorBlueGrey,colorDefault,90); 
//AddTextColumn(IcbID(1),"ICB",0,colorBlueGrey,colorDefault,90); 
```

## MA Stack
```
MA8 = Ref(MA(C,8),0);
MA13 = Ref(MA(C,13),0);
MA21 = Ref(MA(C,21),0);
MA34 = Ref(MA(C,34),0);
MA55 = Ref(MA(C,55),0);

MA_STACK_BULLISH = IIf(MA8 > MA13 AND MA13 > MA21 AND MA21 > MA34 AND MA34 > MA55,True,False);
MA_STACK_BEARISH = IIf(MA8 < MA13 AND MA13 < MA21 AND MA21 < MA34 AND MA34 < MA55,True,False);

AddTextColumn(WriteIf(MA_STACK_BULLISH,"BULL",WriteIf(MA_STACK_BEARISH,"BEAR","----")),"Stack",1,IIf(MA_STACK_BULLISH,colorGreen,IIf(MA_STACK_BEARISH,colorRed,colorGrey50)),IIf(MA_STACK_BULLISH,colorDarkGreen,IIf(MA_STACK_BEARISH,colorDarkRed,colorDefault)));
```

## (21)EMA
```
// Display EMA 21: Show the value of C relative to EMA
// if C = 100, EMA = 105, then show -5
AddColumn(((EMA(C,21))-C),"(21)EMA");
```

## Close
```
// Display Close
AddColumn(C,"Close",1.2,IIf( isGain, colorBrightGreen, colorPink ), colorDefault,56);
```

## %Chg
```
// Display % change
AddColumn(((C/O)-1)*100,"%Chg",1.2,IIf( isGain, colorBrightGreen, colorPink), colorDefault, 48);
```

## Avg Vol
```
// Display Average Volume 21
AvgVolume = (MA(V,21));
AddColumn(V,"Volume",1,colorDefault, ColorRGB(50,0,77), 72);
AddColumn(((V/AvgVolume))*100,"%AvgVol",1,colorDefault, ColorRGB(50,0,77),72);
```

## Chande Momentum Oscillator
```
_SECTION_BEGIN("CHANDE MOMENTUM OSCILLATOR");

function funcCMO(periods) {
 
cmo_1=Sum( IIf( C > Ref( C, -1 ) , ( C - Ref( C ,-1 ) ) ,0 ) , periods ) ;
cmo_2=Sum( IIf( C < Ref( C ,-1 ) , ( Ref( C ,-1 ) - C ) ,0 ) , periods );
cmo=100 * (( cmo_1 -cmo_2) /( cmo_1+cmo_2));
return cmo;
}
 
cmo = funcCMO(21);

/* //FOR CHARTING
Plot(cmo,"cmo",IIf(cmo>Ref(cmo,-1),5,4),2|styleThick);
Plot(MA(cmo,9),"Trigger",colorYellow);
Plot(50,"",15);
Plot(-50,"",15);
 
Title="cmo"+WriteVal(cmo)+" Trigger"+WriteVal(MA(cmo,9));
*/

// FOR EXPLORING
AddColumn(cmo,"CMO",1,colorDefault,colorDefault,48);

_SECTION_END();
```

## ATR
```
// Display ATR
AddColumn(ATR(21),"ATR");
```

## Python
```
/*// DO PYTHON STUFF!
PyLoadFromFile("amipyscript","C:\\Program Files\\AmiBroker\\Formulas\\AmiPy\\AmiPy.py");

BBPy = BBandBot(C,5,2);

HiPi = PyEvalFunction("amipyscript","HelloWorld",FullName(),"AmiBroker is sending data.",BBPy);
//AddTextColumn(HiPi,"Python");
AddTextColumn(HiPi,"Python");

//Plot(BBPy,"BBPy",colorPink,styleLine,);
*/
```
