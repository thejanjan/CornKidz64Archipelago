using HarmonyLib;

namespace CornKidz64Archipelago.Patches
{
	[HarmonyPatch(typeof(SaveInt), nameof(SaveInt.SetData))]
	class SaveInt_SetData_Patch
	{
		public static void Prefix(int intSet, SaveInt __instance)
		{
			Core.Logger.LogInfo("SaveInt set to " + intSet.ToString() + " with id " + __instance.id.ToString());
		}
	}

    [HarmonyPatch(typeof(SaveItem), nameof(SaveItem.Collect))]
    class SaveItem_Collect_Patch
    {
        public static void Prefix(SaveItem __instance)
        {
            Core.Logger.LogInfo("[items] SaveItem collected with id " + __instance.id.ToString());
        }
    }

    [HarmonyPatch(typeof(SaveTrigger), nameof(SaveTrigger.SetData))]
    class SaveTrigger_SetData_Patch
    {
        public static void Prefix(bool bSet, SaveTrigger __instance)
        {
            Core.Logger.LogInfo("[switches] SaveTrigger with id " + __instance.id.ToString() + " set to " + bSet.ToString());
        }
    }

    [HarmonyPatch(typeof(UpgradeItem), nameof(UpgradeItem.Collect))]
    class UpgradeItem_Collect_Patch
    {
        public static void Prefix(UpgradeItem __instance)
        {
            Core.Logger.LogInfo("[upgrades] UpgradeItem collected with id " + __instance.id.ToString());
        }
    }
}