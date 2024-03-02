using HarmonyLib;
using System.IO;
using System.Runtime.Serialization.Formatters.Binary;
using UnityEngine;

namespace CornKidz64Archipelago.Patches
{
	/*
	 * Game Save/Load patching
	 */
	[HarmonyPatch(typeof(GameCtrl), nameof(GameCtrl.SaveGame))]
	class GameCtrl_SaveGame_Patch
    {
		public static bool Prefix(GameCtrl __instance)
		{
			if (Multiworld.UsingArchiSave)
			{
                // Use new save file.
                BinaryFormatter binaryFormatter = new BinaryFormatter();
                FileStream fileStream = File.Create(Application.persistentDataPath + "/save_archi.cow");
                binaryFormatter.Serialize(fileStream, __instance.data);
                fileStream.Close();
                Debug.Log("SAVED");
				return false;
            }
			else
			{
                return true;
            }
		}
	}

    [HarmonyPatch(typeof(GameCtrl), nameof(GameCtrl.LoadGame))]
    class GameCtrl_LoadGame_Patch
    {
        public static bool Prefix(GameCtrl __instance)
        {
            if (Multiworld.UsingArchiSave)
            {
                // Use our archi save.
                if (File.Exists(Application.persistentDataPath + "/save_archi.cow"))
                {
                    BinaryFormatter binaryFormatter = new BinaryFormatter();
                    FileStream fileStream = File.Open(Application.persistentDataPath + "/save_archi.cow", FileMode.Open);
                    __instance.data = (binaryFormatter.Deserialize(fileStream) as Data);
                    fileStream.Close();
                }

                // Then, load the config from our old save on top.
                /*
                if (File.Exists(Application.persistentDataPath + "/save1.cow"))
                {
                    BinaryFormatter binaryFormatter = new BinaryFormatter();
                    FileStream fileStream = File.Open(Application.persistentDataPath + "/save1.cow", FileMode.Open);
                    Data data = (binaryFormatter.Deserialize(fileStream) as Data);
                    fileStream.Close();

                    __instance.data.currentCamMode = data.currentCamMode;
                    __instance.data.ctrlType = data.ctrlType;
                    __instance.data.camInvertOff = data.camInvertOff;
                    __instance.data.bRumble = data.bRumble;
                    __instance.data.bFullscreen = data.bFullscreen;
                    __instance.data.bWidescreen = data.bWidescreen;
                    __instance.data.bVsync = data.bVsync;
                    __instance.data.bRAnalogDpad = data.bRAnalogDpad;
                    __instance.data.bAnalogX2 = data.bAnalogX2;
                    __instance.data.b1080 = data.b1080;
                    __instance.data.bIgnoreDpadX = data.bIgnoreDpadX;
                    __instance.data.bP1only = data.bP1only;
                    __instance.data.volume = data.volume;
                    __instance.data.antialias = data.antialias;
                    __instance.data.bMusic = data.bMusic;
                    __instance.data.bAchDisable = data.bAchDisable;
                    __instance.data.b60fps = data.b60fps;
                    __instance.data.bForce60hz = data.bForce60hz;
                }
                */

                // Ensure we don't skip launcher.
                __instance.data.bSkipLauncher = false;
                return false;
            }

            // Otherwise, just use real save.
            return true;
        }
    }
}