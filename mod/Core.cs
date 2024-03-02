using HarmonyLib;
using System.Collections.Generic;
using System.Text;
using BepInEx;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;
using System.IO;
using Newtonsoft.Json;
using BepInEx.Logging;
using System.Reflection;

namespace CornKidz64Archipelago
{
    [BepInPlugin(PluginGUID, PluginName, PluginVersion)]
    public class Core : BaseUnityPlugin
    {
        public const string PluginGUID = "mica.goatkidz64archipelago";
        public const string PluginName = "Archipelago";
        public const string PluginVersion = "1.0.0";

        public static string workingPath;
        public static string workingDir;
        public static new ManualLogSource Logger { get; } = BepInEx.Logging.Logger.CreateLogSource("Archipelago");

        public static GameObject obj;
        public static UIManager uim;

        public static ArchipelagoData data = new ArchipelagoData();

        public static bool InPregame = false;
        public static bool InGame = false;

        public void Awake()
        {
            Harmony harmony = new Harmony("archipelago");
            harmony.PatchAll();

            workingPath = Assembly.GetExecutingAssembly().Location;
            workingDir = Path.GetDirectoryName(workingPath);
            //logger.LogInfo($"Working Path: {workingPath}, Working Dir: {workingDir}");

            obj = gameObject;
            obj.transform.localPosition = new Vector3(960, 540, 0);

            uim = obj.AddComponent<UIManager>();

            SceneManager.sceneLoaded += OnSceneLoaded;
        }

        public void OnSceneLoaded(Scene scene, LoadSceneMode mode)
        {
            Logger.LogInfo(scene.name);

            // some fake FSM logic
            if (scene.name == "launcher" && !InPregame) EnterPregame();
            if (scene.name != "launcher" &&  InPregame) ExitPregame();
            if (scene.name == "PizzaOut" && !InGame) EnterGame();
            if (scene.name != "PizzaOut" && InGame)  ExitGame();
        }

        /*
         * Pre-Game State
         */

        public void EnterPregame()
        {
            // TODO - Add Archipelago UI to the top right
            Logger.LogInfo("EnterPregame");
            Multiworld.UsingArchiSave = true;
        }

        public void ExitPregame()
        {
            // Clean up Archipelago UI
            Logger.LogInfo("ExitPregame");
        }

        /*
         * In Game State
         */

        public void EnterGame()
        {
            Logger.LogInfo("EnterGame");
        }

        public void ExitGame()
        {
            Logger.LogInfo("ExitGame");
        }
    }
}
