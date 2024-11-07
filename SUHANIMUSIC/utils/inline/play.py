import math
from pyrogram.types import InlineKeyboardButton
from SUHANIMUSIC import app
import config
from SUHANIMUSIC.utils.formatters import time_to_seconds

def track_markup(_, videoid, user_id, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            )
        ],
    ]
    return buttons

def stream_markup_timer(_, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 200
    umm = math.floor(percentage)
    if 0 < umm <= 15:
        bar = "🅟︎——————————————"
    elif 15 < umm < 30:
        bar = "🅟︎🅡︎—————————————"
    elif 30 <= umm < 45:
        bar = "🅟︎🅡︎🅐︎————————————"
    elif 45 <= umm < 60:
        bar = "🅟︎🅡︎🅐︎🅣︎———————————"
    elif 60 <= umm < 75:
        bar = "🅟︎🅡︎🅐︎🅣︎🅐︎——————————"
    elif 75 <= umm < 90:
        bar = "🅟︎🅡︎🅐︎🅣︎🅐︎🅟︎—————————"
    elif 90 <= umm < 105:
        bar = "🅟︎🅡︎🅐︎🅣︎🅐︎🅟︎—————————"
    elif 105 <= umm < 120:
        bar = "🅟︎🅡︎🅐︎🅣︎🅐︎🅟︎—❤️———————"
    elif 120 <= umm < 135:
        bar = "🅟︎🅡︎🅐︎🅣︎🅐︎🅟︎—❤️—🅢︎—————"
    elif 135 <= umm < 150:
        bar = "🅟︎🅡︎🅐︎🅣︎🅐︎🅟︎—❤️—🅢︎🅤︎————"
    elif 150 <= umm < 165:
        bar = "🅟︎🅡︎🅐︎🅣︎🅐︎🅟︎—❤️—🅢︎🅤︎🅗︎———"
    elif 165 <= umm < 180:    
        bar = "🅟︎🅡︎🅐︎🅣︎🅐︎🅟︎—❤️—🅢︎🅤︎🅗︎🅐︎——"
    elif 180 <= umm < 195:
        bar = "🅟︎🅡︎🅐︎🅣︎🅐︎🅟︎—❤️—🅢︎🅤︎🅗︎🅐︎🅝︎—"
        else:    
        bar = "🅟︎🅡︎🅐︎🅣︎🅐︎🅟︎—❤️—🅢︎🅤︎🅗︎🅐︎🅝︎🅘︎"
    
    buttons = [
    buttons = [
         [
            InlineKeyboardButton(text="▷", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="II", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="↻", callback_data=f"ADMIN Replay|{chat_id}"),
            InlineKeyboardButton(text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"),
            InlineKeyboardButton(text="▢", callback_data=f"ADMIN Stop|{chat_id}"),
        ],
        [
            InlineKeyboardButton(
                text=f"{played} {bar} {dur}",
                callback_data="GetTimer",
            )
        ],
          [
            InlineKeyboardButton(
                text="✰ 𝖡ᴧ፝֠֩ʙꭎ ✰", url="https://t.me/VENOM_PRATAP",
            ),
            InlineKeyboardButton(
                text="✰ 𝛅ᴏ፝֠֩𝛈ᴧ ✰", url="https://t.me/VENOM_SUHANI",
            )
        ],
         [InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close")],
        ]

    return buttons

def stream_markup(_, chat_id):
    buttons = [
        [
            InlineKeyboardButton(text="▷", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="II", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="↻", callback_data=f"ADMIN Replay|{chat_id}"),
            InlineKeyboardButton(text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"),
            InlineKeyboardButton(text="▢", callback_data=f"ADMIN Stop|{chat_id}"),
         ],
         [
            InlineKeyboardButton(
                text="✰ 𝖡ᴧ፝֠֩ʙꭎ ✰", url="https://t.me/VENOM_PRATAP",
            ),
            InlineKeyboardButton(
                text="✰ 𝛅ᴏ፝֠֩𝛈ᴧ ✰", url="https://t.me/VENOM_SUHANI",
            )
        ],
         [InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close")],
        ]

    return buttons

def playlist_markup(_, videoid, user_id, ptype, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"SUHANIPlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"SUHANIPlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons

def livestream_markup(_, videoid, user_id, mode, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_3"],
                callback_data=f"LiveStream {videoid}|{user_id}|{mode}|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons

def slider_markup(_, videoid, user_id, query, query_type, channel, fplay):
    query = f"{query[:20]}"
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="◁",
                callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {query}|{user_id}",
            ),
            InlineKeyboardButton(
                text="▷",
                callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
        ],
    ]
    return buttons
