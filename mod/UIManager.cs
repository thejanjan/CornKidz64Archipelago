using CornKidz64Archipelago.Structures;
using HarmonyLib;
using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
// using TMPro;

namespace CornKidz64Archipelago
{
    public class UIManager : MonoBehaviour
    {
        public static Font font;
        public static GameObject log;
        public static int lines = 5;

        public static GameObject canvas;
        public static GameObject chapterSelect;
        public static Text actStats;
        public static Dictionary<string, GameObject> chapters = new Dictionary<string, GameObject>();
        public static Dictionary<string, GameObject> layers = new Dictionary<string, GameObject>();
        public static Dictionary<string, GameObject> levels = new Dictionary<string, GameObject>();
        public static Dictionary<string, GameObject> secrets = new Dictionary<string, GameObject>();

        public static GameObject menuText;
        public static GameObject menuIcon;
        public static GameObject goalCount;

        public static List<GameObject> skullIcons = new List<GameObject>();

        public static GameObject hud;
        public static GameObject popupCanvas;
        public static GameObject popupText;
        public static GameObject popupImage;
        public static bool displayingMessage = false;

        public static void CreateLogObject()
        {
            log = new GameObject();
            log.name = "Archipelago Log";
            log.transform.parent = Core.obj.transform;
            log.transform.localPosition = new Vector3(0, 0, 0);

            Core.obj.AddComponent<Canvas>().renderMode = RenderMode.ScreenSpaceOverlay;
            Core.obj.GetComponent<Canvas>().sortingOrder = 256;

            log.AddComponent<Text>().font = font;
            log.GetComponent<Text>().fontSize = 12;
            log.GetComponent<Text>().alignment = TextAnchor.LowerCenter;
            log.GetComponent<Text>().alignByGeometry = true;
            log.GetComponent<RectTransform>().sizeDelta = new Vector2(Screen.width - 10, Screen.height - 10);
        }

        public static void AdjustLogBounds()
        {
            log.GetComponent<RectTransform>().sizeDelta = new Vector2(Screen.width - 10, Screen.height - 10);
        }
    }
}