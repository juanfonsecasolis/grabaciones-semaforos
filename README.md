# Accessible pedestrian signal recordings

Recordings used on the studies [ARAPSUAA: Automatic recognition of accessible pedestrian signals using an adaptive approach](https://github.com/juanfonsecasolis/ARAPSUAA) and [Automatic recognition of accessible pedestrian signals](https://doi.org/10.1121/2.0000675). 

The major part of these recordings were originally compiled by Mario Monge Ordonez<sup>1</sup> and Sharon Corrales Montero<sup>1</sup> on 2013 using a _Samsung ACE and Galaxy_, later on, LG recordings were gathered by Juan Manuel Fonseca-Solís<sup>1,2</sup> on 2017.  

## Affiliations    
<sup>1</sup> Research Center in Information and Communication Technologies ([CITIC](http://www.citic.ucr.ac.cr/)) at [UCR](https://www.ucr.ac.cr/).  
<sup>2</sup> Electronics School ([IE](http://www.ie.tec.ac.cr)) at [TEC](http://www.tec.ac.cr).  

## Filename format
The filenames follow the format `TDsemNSyyyy_MM_dd_hh_mm_ss.wav`, where:
* T is the type of sound (`n`for noise and `s` for accessible pedestrian signal (APS) sound)
* D is the device (`a` for _Samsung Galaxy Ace, `d` for _Samsung Duos_, `l` for LG G2 mini)
* N is the APS identifier of the semaphores (see location1.png and location2.png)
* S is the side of the street where the recording was taken (`or` for otherside of the APS unit, `s` for next to the APS unit)
* `yyyy_MM_dd_hh_mm_ss` stands for the date format (24h format) when the recording was taken
					
So,`slsem5o2016_10_22_15_39_10.wav`, for instance, would mean that the recording contains an APS sound, taken by the LG device, on semaphore 5 (Central avenue, Alfredo street), on the opposite side of the street, on October 22th 2016 at 15:39:10. 

# Resampling
The file `resample.py` contains a python script to standardize the recordings to the desired frequency. The usage is the following:

```
python resample.py <base directory> <new sample rate>,
```

where:
* `base directory` is the directory where the recording file structure can be found
* `new sample rate` is the new desired sample rate (in Hertz)
