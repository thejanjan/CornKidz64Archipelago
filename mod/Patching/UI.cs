using HarmonyLib;
using System.IO;
using System.Runtime.Serialization.Formatters.Binary;
using UnityEngine;
using UnityEngine.UI;

namespace CornKidz64Archipelago.Patches
{
	/*
	 * Set the quest to something Archipelago adjacent.
	 */
	/*
	[HarmonyPatch(typeof(UI), nameof(UI.RunMenu))]
	class UI_RunMenu_Patch
    {
		public static void Postfix(UI __instance)
		{
			__instance.quest.text = "Test";
		}
	}
	*/
}