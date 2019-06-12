# Accessible pedestrian signal recordings
===========================================================================================
To be used as a companion of [ARAPSUAA: Automatic recognition of accessible pedestrian signals using an adaptive approach](https://github.com/juanfonsecasolis/ARAPSUAA)    
Author
-------
Mario Monge Ordonez
<sup>1</sup>    
Sharon Corrales Montero
<sup>1</sup>    
Juan Manuel Fonseca-Solís<sup>1,2</sup>    
<sup>1</sup> Research Center in Information and Communication Technologies ([CITIC](http://www.citic.ucr.ac.cr/)) at [UCR](https://www.ucr.ac.cr/).  
<sup>2</sup> Electronics School ([IE](http://www.ie.tec.ac.cr)) at [TEC](http://www.tec.ac.cr).  

## Nomenclature

The names of the .wav files of the samples were coded as follows:

FIELD 1; 1 character, describes if it is noise or the sound of the traffic light:
* s: "sound" a file with the sound of the traffic light
* r: "noise" a file with environmental noise


FIELD 2; 1 character, describes which device took the sample:
* a: "ACE" sample taken with the galaxy ace cell phone
* d: "DUOS" shows taken with the cell duos
* l: "LG" shows taken with a LG-D618 cell phone


FIELD 3; 5 characters, describes the semaphore identifier:
* sem (##): "semaphore" ## sound taken near a traffic light. Number corresponds to a numeric value that uniquely identifies the traffic light. Ex: sem01, sem02, sem03

FIELD 4; 1 character, describes which side of the street is the recording, since it can be a pair of traffic lights or the other side of the street:
* or: "otherside (on the other side)" The recording was taken on the opposite side to the one that was the traffic light. Across the street.
* s: "side (next)" The recording was taken at a traffic light.

FIELD 5; 19 characters, date and time of the recording, is a value inserted by the application with which the recording was made, normally they do not agree between recordings, nevertheless the order in which they were taken defines the correspondence between the simultaneous recordings of the sounds.
* ano: year the recording was made
* month: month the recording was made
* day: day the recording was made
* time: time in 24-hour format from the start of the recording
* minutes: minute value of the cellular device at the beginning of the recording
* seconds: value of the secondary of the cellular device in seconds of the beginning of the recording.

## Compilation history
1. Samsung ACE and Galaxy recordings gathered by Mario Monge and Sharon Bejarano on 2013
1. LG recordings gathered by Juan Fonseca on 2017
						
