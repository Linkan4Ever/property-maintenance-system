using System;
using System.Collections.Generic;
using System.Text;

namespace property_maintenance_system
{
    class MainenancePost
    {
        //Plats
        //Starttid
        //Sluttid
        //Kostnad
        //Beskrivning
        //Uppskattad teknisk livslängd
        //Namn
        //id
        //bifogat kvitton etc.
        //Bifogad_fil(består av)

        // Metoder:
        // Skapa ett underhållItem
        // (Redigera underhåll)

        public string Location { get; set; }
        public DateTime StartTime { get; set; }
        public DateTime EndTime { get; set; }
        public double Amount { get; set; }
        public string Description { get; set; }
        public string TechnicalServiceLife { get; set; }
        public string Name { get; set; }
        public int MaintenanceId { get; set; }

        public MainenancePost()
        {
            
        }
        public override string ToString()
        {
            string temp = "Location: " + Location + "\nAmount: " + Amount + "\nDescription: " + Description + "\nStarttid: " + StartTime;
            return temp;
        }

        public static MainenancePost Add(string location, double amount)
        {
         MainenancePost item = new MainenancePost();
            item.Location = location;
            item.Amount = amount;
            item.StartTime = DateTime.Now;
            return item;
        }
    }
}