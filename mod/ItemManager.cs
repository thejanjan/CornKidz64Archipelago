using Archipelago.MultiClient.Net.Enums;
using CornKidz64Archipelago.Structures;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CornKidz64Archipelago
{
    public static class ItemManager
    {
        public static void Receive(APItem item)
        {
            // TODO - queue items so they get processed once we are in-game
        }
        public static ItemFlags GetTypeFromName(string name)
        {
            return ItemFlags.None;
        }
    }
}
}
