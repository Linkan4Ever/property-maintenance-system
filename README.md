# property-maintenance-system

## Kravspecifikation
*   Hålla reda på husunderhåll under tiden som vi bor där
*   Skapa klasser och metoder
*   Skissa på hur det kan se ut.
*   Mest skriver i Python eller C#.
*   Körs på egen server
*   Finns en hemsida att surfa till
*   För att hålla reda på och husunderhåll

## Metod

## Klassrelationer

*   Underhåll
    *   location
    *   starttime
    *   endtime
    *   cost
    *   description
    *   estimated technical servicetime
    *   name
    *   id
    *   attached documents
    *   attached file
    *   End time for maintenance, proposal
        *   Tapet, 1 år
        *   Köksrenovering, 10 år
        *   Badrummsmatta, 20 år
        *   Tak, 50 år
    *   Create maintenance post
    *   Edit maintenance post

*   Cost
    *   int value
    *   string "valuta"
    *   int "avskrivningsperiod"
    *   bol has "avskrivningsperiod"

*   attached file
        *   image
        *   pdf
        *   id
        *   added time
        *   date of upload
        *   date of creation
*   Paper manuals or equal
* "Kvitto"
    *   Amount
    *   Location of purchase
    *   time of purchase
    *   date of purchase