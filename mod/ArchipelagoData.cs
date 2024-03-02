using System.Collections.Generic;

namespace CornKidz64Archipelago
{
    public class ArchipelagoData
    {
        public long index;
        public string host_name;
        public string slot_name;
        public string password;
        public HashSet<string> @checked = new HashSet<string>();

        // Received Slot Data
        public string goal = "owlloh";
        public int goat_color = 0;
        public int xp_count = 72;
        public int max_hp = 8;
        public bool cranksanity = true;
        public bool ratsanity = true;
        public bool achievements = true;
        public bool can_jump = true;
        public bool can_punch = true;
        public bool can_climb = true;
        public bool can_ground_pound = true;
        public bool can_headbutt = true;
        public bool can_wall_jump = true;
        public bool can_swim = true;
        public bool can_crouch = true;
        public bool can_drill = true;
        public bool can_fall_warp = true;

        public bool death_link = false;

        public void LoadSlotData(Dictionary<string, object> slotData)
        {
            // Load goal.
            LoadGoal(slotData);

            // Load options.
            LoadSlotDataValue(slotData, ref goat_color,     "goat_color");
            LoadSlotDataValue(slotData, ref xp_count,       "xp_count");
            LoadSlotDataValue(slotData, ref max_hp,         "max_hp");
            LoadSlotDataValue(slotData, ref cranksanity,    "cranksanity");
            LoadSlotDataValue(slotData, ref ratsanity,      "ratsanity");
            LoadSlotDataValue(slotData, ref achievements,   "achievements");

            // Load movement options.
            LoadSlotDataValue(slotData, ref can_jump,           "can_jump");
            LoadSlotDataValue(slotData, ref can_punch,          "can_punch");
            LoadSlotDataValue(slotData, ref can_climb,          "can_climb");
            LoadSlotDataValue(slotData, ref can_ground_pound,   "can_ground_pound");
            LoadSlotDataValue(slotData, ref can_headbutt,       "can_headbutt");
            LoadSlotDataValue(slotData, ref can_wall_jump,      "can_wall_jump");
            LoadSlotDataValue(slotData, ref can_swim,           "can_swim");
            LoadSlotDataValue(slotData, ref can_crouch,         "can_crouch");
            LoadSlotDataValue(slotData, ref can_drill,          "can_drill");
            LoadSlotDataValue(slotData, ref can_fall_warp,      "can_fall_warp");

            // Load misc options.
            LoadSlotDataValue(slotData, ref death_link, "death_link");
        }

        private void LoadGoal(Dictionary<string, object> slotData)
        {
            switch (int.Parse(slotData["goal"].ToString()))
            {
                case 0:
                    goal = "tower";
                    break;
                case 1:
                    goal = "anxiety";
                    break;
                case 2:
                    goal = "god";
                    break;
                default:
                    goal = "tower";
                    break;
            }
        }

        private void LoadSlotDataValue(Dictionary<string, object> slotData, ref int option, string key)
        {
            try { option = int.Parse(slotData[key].ToString()); }
            catch (KeyNotFoundException)
            {
                Core.Logger.LogWarning($"No key found for option \"{key}\". Using default value ({option})");
            }
        }

        private void LoadSlotDataValue(Dictionary<string, object> slotData, ref bool option, string key)
        {
            try { option = bool.Parse(slotData[key].ToString()); }
            catch (KeyNotFoundException)
            {
                Core.Logger.LogWarning($"No key found for option \"{key}\". Using default value ({option})");
            }
        }

    }
}
