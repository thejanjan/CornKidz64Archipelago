using Archipelago.MultiClient.Net;
using Archipelago.MultiClient.Net.Enums;
using Archipelago.MultiClient.Net.Packets;
using Archipelago.MultiClient.Net.Helpers;
using Archipelago.MultiClient.Net.BounceFeatures.DeathLink;
using System;
using System.Collections.Generic;
using UnityEngine;
using Newtonsoft.Json.Linq;
using UnityEngine.UI;
using Newtonsoft.Json;
using CornKidz64Archipelago.Structures;
using Archipelago.MultiClient.Net.Models;

namespace CornKidz64Archipelago
{
    public static class Multiworld
    {
        public static int[] AP_VERSION = new int[] { 0, 4, 4 };
        public static DeathLinkService DeathLinkService = null;
        public static bool DeathLinkKilling = false;

        public static bool Authenticated;
        public static ArchipelagoSession Session;
        public static List<string> messages = new List<string>();

        // This flag tells the game to load from a dedicated Archipelago save file.
        public static bool UsingArchiSave = false;

        public static bool Connect()
        {
            if (Authenticated)
            {
                return true;
            }

            Session = ArchipelagoSessionFactory.CreateSession(Core.data.host_name);
            Session.Socket.SocketClosed += SocketClosed;
            Session.Socket.ErrorReceived += ErrorReceived;
            Session.Socket.PacketReceived += PacketReceived;
            Session.Items.ItemReceived += ItemReceived;

            LoginResult loginResult = Session.TryConnectAndLogin(
                "Corn Kidz 64",
                Core.data.slot_name,
                ItemsHandlingFlags.AllItems,
                new Version(AP_VERSION[0], AP_VERSION[1], AP_VERSION[2]),
                null,
                null,
                Core.data.password == "" ? null : Core.data.password,
                true
            );

            if (loginResult is LoginSuccessful success)
            {
                Authenticated = true;

                ArchipelagoData data = Core.data;
                data.LoadSlotData(success.SlotData);

                if (Core.data.death_link) EnableDeathLink();

                Core.Logger.LogInfo("Successfully connected to server as player \"" + Core.data.slot_name + "\".");
            }
            else if (loginResult is LoginFailure failure)
            {
                Authenticated = false;
                Core.Logger.LogWarning(String.Join("\n", failure.Errors));
                Session.Socket.DisconnectAsync();
                Session = null;
            }
            return loginResult.Successful;
        }

        public static void Disconnect()
        {
            if (Session != null && Session.Socket != null) Session.Socket.DisconnectAsync();
            Core.Logger.LogWarning("Disconnected from Archipelago server.");
            UIManager.log.GetComponent<Text>().text = "";
            DisableDeathLink();
            messages.Clear();
            Session = null;
            DeathLinkService = null;
            Authenticated = false;
        }

        public static void SocketClosed(string reason)
        {
            Core.Logger.LogError("Lost connection to Archipelago server. " + reason);
            Disconnect();
        }

        public static void ErrorReceived(Exception e, string message)
        {
            Core.Logger.LogError(message);
            if (e != null) Core.Logger.LogError(e.ToString());
            Disconnect();
        }

        public static void PacketReceived(ArchipelagoPacketBase packet)
        {
            switch (packet.PacketType)
            {
                case ArchipelagoPacketType.PrintJSON:
                    {
                        if (messages.Count >= UIManager.lines) messages.RemoveAt(0);

                        var p = packet as PrintJsonPacket;

                        string richText = "";
                        string plainText = "";
                        string color = "<color=#" + ColorUtility.ToHtmlStringRGB(Colors.White) + "FF>";

                        foreach (var messagePart in p.Data)
                        {
                            switch (messagePart.Type)
                            {
                                case JsonMessagePartType.PlayerId:
                                    if (Session.Players.GetPlayerName(int.Parse(messagePart.Text)) == Core.data.slot_name) color = "<color=#" + ColorUtility.ToHtmlStringRGB(Colors.PlayerSelf) + "FF>";
                                    else color = "<color=#" + ColorUtility.ToHtmlStringRGB(Colors.PlayerOther) + "FF>";
                                    if (int.TryParse(messagePart.Text, out int playerSlot))
                                    {
                                        string playerName = Session.Players.GetPlayerAlias(playerSlot) ?? $"Slot: {playerSlot}";
                                        richText += color + playerName + "</color>";
                                        plainText += playerName;
                                    }
                                    else
                                    {
                                        richText += $"{color}{messagePart.Text}</color>";
                                        plainText += messagePart.Text;
                                    }
                                    break;
                                case JsonMessagePartType.ItemId:
                                    switch (messagePart.Flags)
                                    {
                                        case ItemFlags.Advancement:
                                            color = "<color=#" + ColorUtility.ToHtmlStringRGB(Colors.ItemAdvancement) + "FF>";
                                            break;
                                        case ItemFlags.NeverExclude:
                                            color = "<color=#" + ColorUtility.ToHtmlStringRGB(Colors.ItemNeverExclude) + "FF>";
                                            break;
                                        case ItemFlags.Trap:
                                            color = "<color=#" + ColorUtility.ToHtmlStringRGB(Colors.ItemTrap) + "FF>";
                                            break;
                                        default:
                                            color = "<color=#" + ColorUtility.ToHtmlStringRGB(Colors.ItemFiller) + "FF>";
                                            break;
                                    }
                                    if (int.TryParse(messagePart.Text, out int itemId))
                                    {
                                        string itemName = Session.Items.GetItemName(itemId) ?? $"Item: {itemId}";
                                        richText += color + itemName + "</color>";
                                        plainText += itemName;
                                    }
                                    else
                                    {
                                        richText += $"{color}{messagePart.Text}</color>";
                                        plainText += messagePart.Text;
                                    }
                                    break;
                                case JsonMessagePartType.LocationId:
                                    color = "<color=#" + ColorUtility.ToHtmlStringRGB(Colors.Location) + "FF>";
                                    if (int.TryParse(messagePart.Text, out int locationId))
                                    {
                                        string locationName = Session.Locations.GetLocationNameFromId(locationId) ?? $"Location: {locationId}";
                                        richText += color + locationName + "</color>";
                                        plainText += locationName;
                                    }
                                    else
                                    {
                                        richText += $"{color}{messagePart.Text}</color>";
                                        plainText += messagePart.Text;
                                    }
                                    break;
                                default: 
                                    richText += messagePart.Text;
                                    plainText += messagePart.Text;
                                    break;
                            }
                        }
                        messages.Add(richText);
                        UIManager.log.GetComponent<Text>().text = string.Join("\n", messages.ToArray());
                        break;
                    }
            }
        }

        public static void ItemReceived(ReceivedItemsHelper helper)
        {
            if (helper.Index > Core.data.index)
            {
                int player = helper.PeekItem().Player;
                String player_name = Session.Players.GetPlayerAlias(player);
                String item_name = helper.PeekItemName();

                if (player == Session.ConnectionInfo.Slot)
                {
                    Core.Logger.LogInfo("Name: \"" + item_name + "\" | Type: " + ItemManager.GetTypeFromName(item_name) + " | Player: \"" + player_name + "\"");

                    APItem item = new APItem()
                    {
                        itemName = helper.PeekItemName(),
                        type = ItemManager.GetTypeFromName(item_name),
                        playerName = Core.data.slot_name
                    };

                    ItemManager.Receive(item);
                }

                helper.DequeueItem();
                Core.data.index++;
            }
        }

        public static void EnableDeathLink()
        {
            if (DeathLinkService == null)
            {
                DeathLinkService = Session.CreateDeathLinkService();
                DeathLinkService.OnDeathLinkReceived += DeathLinkReceived;
            }
            DeathLinkService.EnableDeathLink();
        }

        public static void DisableDeathLink()
        {
            if (DeathLinkService == null) return;
            else DeathLinkService.DisableDeathLink();
        }

        public static void DeathLinkReceived(DeathLink deathLink)
        {
            if (Core.InGame)
            {
                DeathLinkKilling = true;
                string cause = "{0} has died.";
                if (deathLink.Cause != "") cause = deathLink.Cause;
                else cause = string.Format(cause, deathLink.Source);

                messages.Add($"[DeathLink] {cause}");

                // TODO - Kill this damn got
            }
            else Core.Logger.LogWarning("Received DeathLink, but player cannot be killed right now.");
        }

        public static void SendCompletion()
        {
            var packet = new StatusUpdatePacket() { Status = ArchipelagoClientState.ClientGoal };
            Session.Socket.SendPacket(packet);
        }
    }
}
