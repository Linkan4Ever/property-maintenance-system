using System;

namespace property_maintenance_system
{
    class Program
    {
        static void Main(string[] args)
        {
            MaintenancePost golvbyteBadrum1 = MaintenancePost.Add("vardagsrum", 79.9, "golvbyte", "Byte av golv", 7); 

            // (string location, double amount, string description, string name, int technicalservicelife)
            Console.WriteLine(bytaTak.ToString());
        }
    }
}
