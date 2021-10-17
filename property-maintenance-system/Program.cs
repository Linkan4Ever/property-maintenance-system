using System;

namespace property_maintenance_system
{
    class Program
    {
        static void Main(string[] args)
        {
            MaintenanceItem bytaTak = MaintenanceItem.Add("Vardagsrum", 79.9);



            //bytaTak.Location = "Vardagrummet";
            //bytaTak.StartTime = DateTime.Now;
            //bytaTak.Description = "Nu har vi bytt tak i vardagsrummet.";
            Console.WriteLine(bytaTak.ToString());
        }
    }
}
